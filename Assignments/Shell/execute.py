import re
from errors import CommandDoesNotExist, FlagDoesNotExist, InvalidArgument, display_error
from cmd_pkg_use.cmd_pkg import CommandsHelper
from window_helper import clear_line


ex_cmds = [
    "ls -l",
    "ls -a",
    "ls",
    "pwd",
    "cd",
    "cd ~",
    "cd ..",
    "cp file1 file2",
    "mv file1 file2",
    "rm file.txt",
    "rm -r my_directory",
    "rm *file*",
    "rmdir empty_directory",
    "cat file.txt",
    "cat file1 file2 fileN",
    "less large_file.txt",
    "head -n 10 file.txt",
    "tail -n 20 file.txt",
    "grep keyword file.txt",
    "grep -l error data.txt | cat -n > error_summary.txt",
    "grep key < data.txt"
]


commands = CommandsHelper()

capture_flag_pattern = r'\s*(-\w+)\b'
strip_flag_pattern = r'\s*-\w+\b'

capture_redirect_pattern = r'([<>])\s+(\S+)'
strip_redirect_pattern = r'\s+[<>]\s+\S+'


def capture_redirects(cmd):
    # capture input/output redirects and the start/end index of where
    # they were found in the command, we then add this info to cmd_obj
    redirects = list(re.finditer(capture_redirect_pattern, cmd))

    cmd_obj = {}
    cmd_obj['file_info'] = []
    for match in redirects:
        symbol, file_name = match.groups()
        start_index = match.start()
        end_index = match.end()
        cmd_obj['file_info'].append(
            {'symbol': symbol, 'file_name': file_name,
                'start': start_index, 'end': end_index}
        )

    return cmd_obj



def parse_cmd(cmd_temp):
    '''
    parses the command into an object with the key as the cmd name and arguments
    stores redirects
    '''
    cmd_obj = {}
    
    cmds_redirects = capture_redirects(cmd_temp)                                              # get all of the file redirects
    cmd_no_redirects = re.sub(strip_redirect_pattern, '', cmd_temp).strip()                   # deletes all of the redirects from the command 
    cmds_flags = re.findall(capture_flag_pattern, cmd_no_redirects)                           # captures each flag for the cmd
    cmd_param_result = re.sub(strip_flag_pattern, '', cmd_no_redirects)                       # deletes all the flags from the cmd
    cmd_obj[cmd_param_result.strip()] = {"flags": cmds_flags, "redirects": cmds_redirects}    # package the object        
    
    return cmd_obj


def execute(cmd: str, w):
    """
    : Musts for a command to work.
    : Name : Must be a valid command name listed in help
    : Params : Must be a valid parameter listed in the help section of the specified command
                ex: grep keyword file.txt --- valid
                ex: grfsdc                --- not valid
    : Flags : -f -t -tl etc. does not matter on flag placement just ensure the order of your arguments
                            are placed properly
                ex: grep -l keyword -f file.txt
                proper: grep -l -f keyword file

    : Pipe  : "|" as much as you want. The below function can parse it
                ex. grep -l error app.log | cat -n > error_summary.txt 

    parses command/s and formulates correct output

    allows for unlimited input/output redirects, 1 each per command though

    allows for unlimited pipes and valid flags for each command listed in help()

    redirects will be passed around based on string positioning. If a redirects pops up, 
    it will simply take the output from the very last command ran and create/read whatever
    data it needs based off of '<' and '>'

    errors:
        CommandDoesNotExist:
        FlagDoesNotExist:
        InvalidArgument:
    """
    try:
        cmd_obj = {}

        # split the commands if pipe exists
        commands = cmd.split("|") if "|" in cmd else cmd

        # parse the commands and 
        if type(commands) == list:
            for cmd_temp in commands:
                temp_cmd_obj = parse_cmd(cmd_temp)
                cmd_obj.update(temp_cmd_obj)
                     
        elif type(commands) == str:
            temp_cmd_obj = parse_cmd(commands)
            cmd_obj = temp_cmd_obj



        # performs logic on the actual command name and parameters passed if any. 
        # checks to make sure the command is valid 
        # using cmd_index to track the redirects
        cmd_index = 0
        for cmd_name in cmd_obj:
            parsed = cmd_name.split()
            name = parsed[0]
            args = parsed[1:] if len(parsed) > 1 else None

            run_cmd = commands.exists(name)

            #TODO : check for redirects, if the cmd ends with an output redirect
                        # open the specific file and write to it.
            for redirect in cmd_obj[cmd_name]["redirects"]:
                if redirect["symbol"] == "<":                           # input file passed to command
                    input_data = open(redirect["file_name"], "r")       # try to open the file
                    cmd_obj[cmd_name]["input_data"] = input_data.read() # pass the file as a string
                    break                                               # ensures only one input redirect can be passed per command
            
            if run_cmd:
                cmd_result = commands.runner(name, args, options=cmd_obj[cmd_name])  #TODO make able to parse for flags as well


            cmd_obj[cmd_name]['result'] = cmd_result

        # current structure of cmd_obj - Pure example
        # {'grep keyword file_name': {"flags": [-f, -l], "result": string returned by the command run. 
        #   "redirects": [{'symbol': symbol, 'file_name': file_name, 'start': start_index, 'end': end_index, 
        #                   'original_string': grep -l keyword filename -f | cat -n > appearances.txt}]}
        #               
        # }
        

    except CommandDoesNotExist as err:
        display_error(w, err)

    except FlagDoesNotExist as err:
        display_error(w, err)

    except InvalidArgument as err:
        display_error(w, err)

    except FileNotFoundError as err:
        display_error(w, err)
    

    print(f"Command: {cmd}")
    print(f"Command object: {cmd_obj}")

    return cmd_obj


# print(commands)
