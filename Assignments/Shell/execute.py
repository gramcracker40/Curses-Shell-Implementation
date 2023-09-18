import re
from errors import CommandDoesNotExist, FlagDoesNotExist, InvalidArgument, display_error
from cmd_pkg_use.cmd_pkg import CommandsHelper
from window_helpers import clear_line, print_long_string, print_list


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


commands_helper = CommandsHelper()

capture_flag_pattern = r'\s*(-\w+)\b'
strip_flag_pattern = r'\s*-\w+\b'

capture_redirect_pattern = r'([<>])\s+(\S+)'
strip_redirect_pattern = r'\s+[<>]\s+\S+'


##################################################################################
##################################################################################
#   execute() -->  HELPERS
##################################################################################
##################################################################################

def capture_redirects(cmd):
    # capture input/output redirects and the start/end index of where
    # they were found in the command, we then add this info to cmd_obj
    redirects = list(re.finditer(capture_redirect_pattern, cmd))

    cmd_obj = []
    for match in redirects:
        symbol, file_name = match.groups()
        
        cmd_obj.append(
            {'symbol': symbol, 'file_name': file_name,
                'start': match.start(), 'end': match.end()}
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

##################################################################################
##################################################################################



def execute(cmd: str, w):
    """
    execute(cmd: str, w:curses_window) --> given a command string, run the command and
                form the appropriate response. 

    : Below explains the syntax for a command to work.
    : Name : Must be a valid command name listed in help
    : Params : Must be a valid parameter listed in the help section of the specified command
                ex: grep keyword file.txt --- valid   --> file.txt must exist
                ex: grfsdc                --- not valid
    : Flags : -f -t -tl etc. does not matter on flag placement just ensure the order of your arguments
                            are placed properly. Get passed to the function for proper output
                ex: grep -l keyword -f file.txt
                proper: grep -l -f keyword file
                again, does not matter.

    : Pipe  : "|" as much as you want. The below function can parse it
                NOTE: if you do a pipe, the previous cmd's output becomes the piped commands input.
                ex. grep -l error app.log | cat -n > error_summary.txt \
            

    : Redirects : input: '< file.txt' or  output:'> file.txt'
                    input  --> user can specify files they want sent to the function
                    output --> user can specify where they want the result of the cmd to be sent
                NOTE: can only do one input and one output redirect per command
    ex command: grep keyword input.txt > occurences.txt | cat -n > showcase.txt

    returns: The result of the inputted command

    errors:
        CommandDoesNotExist:
        FlagDoesNotExist:
        InvalidArgument:
        FileNotFoundError:   
    """
    try:
        # main working object
        cmd_obj = {}

        # split the commands if pipe exists
        commands = cmd.split("|") if "|" in cmd else cmd

        # parse the commands
        if type(commands) == str:
            temp_cmd_obj = parse_cmd(commands)
            cmd_obj = temp_cmd_obj
        
        elif type(commands) == list:
            for cmd_temp in commands:
                temp_cmd_obj = parse_cmd(cmd_temp)
                cmd_obj.update(temp_cmd_obj)
                     
        print(f"cmd_obj: after parsing --> ({cmd_obj})")

        
        # loop below performs logic on the actual command name and parameters passed if any. 
        # sets piped value if there are any
        # handles input/output redirects found in the command
        prev_cmd_result = None
        print_output = True
        for count, cmd_name in enumerate(cmd_obj):
            # with all redirects/flags parsed, all that remains is the string holding the name and args
            parsed = cmd_name.split()
            name = parsed[0]

            # grab and set the arguments
            args = parsed[1:] if len(parsed) > 1 else None
            cmd_obj[cmd_name]["args"] = args

            ### CHECKING FOR PIPED VALUES - if second cmd in piped cmd, use prev result as input
            cmd_obj[cmd_name]['piped_value'] = prev_cmd_result if count >= 1 else None

            ### INPUT REDIRECTS
            if len(cmd_obj[cmd_name]["redirects"]) > 0:
                for redirect in cmd_obj[cmd_name]["redirects"]:
                    if redirect["symbol"] == "<":                           # input file redirect passed to command
                        input_data = open(redirect["file_name"], "r")       # try to open the file
                        cmd_obj[cmd_name]["input_data"] = input_data.read() # pass the file as a string to cmd_obj
                        break                                               # ensures only one input redirect can be passed per command
            
            ### RUNNING CMD
            if commands_helper.exists(name):
                cmd_result = commands_helper.runner(name, w, options=cmd_obj[cmd_name])

                ### STORE RESULTS FROM CMD
                cmd_obj[cmd_name]['result'] = cmd_result
                prev_cmd_result = cmd_result

            ### OUTPUT REDIRECTS
            if len(cmd_obj[cmd_name]["redirects"]) > 0:
                for redirect in cmd_obj[cmd_name]["redirects"]:
                    if redirect["symbol"] == ">":                           # output file redirect passed to command
                        output_data = open(redirect["file_name"], "w")      # try to open the file
                        output_data.write(cmd_result)                       # pass the file as a string to cmd_obj
                        break                       
            
            
            ### CHECK TO SEE IF CMD ENDS IN REDIRECT, if it does, print nothing to the screen
            ###   if there is no redirect. take the last commands result and print to the window. 
            furthest_redirect = 0
            for redirect in cmd_obj[cmd_name]["redirects"]:
                furthest_redirect = redirect["end"] if redirect["end"] > furthest_redirect else furthest_redirect

            if furthest_redirect - len(cmd) < 2 and furthest_redirect != 0: # redirect happened at end of string
                print_output = False                                        # do not print it
            

        # determine how to print the returned value
        # color options are defined in commandsHelper
        if print_output and type(prev_cmd_result) == str:
            print_long_string(w, prev_cmd_result)
        elif print_output and type(prev_cmd_result) == list:
            print_list(w, prev_cmd_result, 
                        color_options=commands_helper.color_options[name])
        else:
            print_long_string(w, f"No output detected\n")
        
        
        return prev_cmd_result
        
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




# current structure of cmd_obj - Pure example
# {'grep keyword file_name': {"flags": [-f, -l], "result": "string returned by the command run."
#   "redirects": [{'symbol': symbol, 'file_name': file_name, 'start': start_index, 'end': end_index}
#   "piped_value": last_cmd_result or None]}
#               
# }