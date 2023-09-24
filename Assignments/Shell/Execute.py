import re
from errors import CommandDoesNotExist, FlagDoesNotExist, InvalidArgument, display_error
from cmd_pkg_use.cmd_pkg import CommandsHelper
from window_helpers import clear_line, print_long_string, print_list


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
        start_index = match.start()
        end_index = match.end()
        cmd_obj.append(
            {'symbol': symbol, 'file_name': file_name,
                'start': start_index, 'end': end_index}
        )

    return cmd_obj


def handle_output_redirects(redirects: [{}], result:list or str):
    '''
    handles writing the success message and parsing the result of cmd into a file
    '''
    ret_string = ""
    furthest_redirect = 0

    ### OUTPUT REDIRECTS
    for redirect in redirects:
        if redirect["symbol"] == ">":                           # output file redirect passed to command
            output_data = open(redirect["file_name"], "w")      # try to open the file
            
            if type(result) == list:
                for item in result:
                    output_data.write(f"{item}\n")

            if type(result) == str:
                output_data.write(item)

            ret_string += f"Successfully wrote output - {redirect['file_name']}\n"

    return ret_string


def parse_cmd(cmd_temp):
    '''
    parses the command into an object with the key as the cmd name and arguments
    stores redirects and flags captured using regex
    '''
    cmd_obj = {}
    
    # REDIRECTS
    cmds_redirects = capture_redirects(cmd_temp) # get all of the file redirects
    cmd_no_redirects = re.sub(strip_redirect_pattern, '', cmd_temp).strip() # deletes all of the redirects from the command 
    
    # FLAGS
    cmds_flags = re.findall(capture_flag_pattern, cmd_no_redirects) # captures each flag for the cmd
    flag_string = ""        
    for cmd in cmds_flags:  # build the flag string, easier to check in functions
        flag_string += cmd
    cmd_param_result = re.sub(strip_flag_pattern, '', cmd_no_redirects) # deletes all the flags from the cmd
    
    # PACKAGING
    cmd_obj[cmd_param_result.strip()] = {"flags": flag_string, "redirects": cmds_redirects} # package the object        
    
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

    errors:
        CommandDoesNotExist:
        FlagDoesNotExist:
        InvalidArgument:
        FileNotFoundError:   
    """
    try:
        # main working object
        cmd_obj = {}

        # split the commands if pipe exists, easier to pass around prev_values. 
        commands = cmd.split("|") if "|" in cmd else cmd

        # parse the command/s, build cmd_obj
        if type(commands) == str:
            cmd_obj = parse_cmd(commands)
        
        elif type(commands) == list:
            for cmd_temp in commands:
                cmd_obj.update(parse_cmd(cmd_temp))


        # loop below performs logic on the actual command name and parameters passed if any.
        # for piped commands, will loop through each and then pass the previous result as input
        # data for the following cmd. 
        prev_cmd_result = None
        for count, cmd_name in enumerate(cmd_obj):
            parsed = cmd_name.split() # cmd_name: "grep key file" or "NAME ARG ARG". 
            name = parsed[0]

            # grab and set the arguments
            args = parsed[1:] if len(parsed) > 1 else None
            cmd_obj[cmd_name]["args"] = args

            # DEFINING INPUT_DATA
            ### CHECKING FOR PIPED VALUES - if second or further cmd in piped cmd, use prev result as input
            cmd_obj[cmd_name]['input_data'] = prev_cmd_result if count >= 1 else None

            ### INPUT REDIRECTS - Truncates a pipe. don't pass input files on piped cmd's!
            ###                     specify the input file to work on in the first cmd!
            if len(cmd_obj[cmd_name]["redirects"]) > 0:
                for redirect in cmd_obj[cmd_name]["redirects"]:
                    if redirect["symbol"] == "<":                           # input file redirect passed to command
                        input_data = open(redirect["file_name"], "r")       # try to open the file
                        cmd_obj[cmd_name]["input_data"] = input_data.readlines() # pass the file as a string to cmd_obj
                        break                                               # ensures only one input redirect can be passed per command
            #######################################################################################################################

            ### RUNNING CMD - reset prev_cmd result after successful execution
            output_redirects = ""
            if commands_helper.exists(name):
                cmd_result = commands_helper.runner(name, w, options=cmd_obj[cmd_name])
                output_redirects = handle_output_redirects(cmd_obj[cmd_name]["redirects"], cmd_result)                

                ### STORE RESULTS FROM CMD
                cmd_obj[cmd_name]['result'] = cmd_result
                prev_cmd_result = cmd_result
            else:
                raise CommandDoesNotExist(f"\nCommand: {name} does not exist")

            #######################################################################################################################
            #    DETERMINE OUTPUT
            # 
            # if there are no output redirects, print prev cmd_result
            # and it must be the very last piped command. 
            if output_redirects == "" and count + 1 == len(cmd_obj): 
                if type(prev_cmd_result) == str:
                    print_long_string(w, prev_cmd_result)
                elif type(prev_cmd_result) == list:
                    print_list(w, prev_cmd_result)
                else:
                    print_long_string(w, f"No output detected\n")
            else:
                print_long_string(w, output_redirects)

        
        return prev_cmd_result
        
    except CommandDoesNotExist as err:
        display_error(w, err)

    except FlagDoesNotExist as err:
        display_error(w, err)

    except InvalidArgument as err:
        display_error(w, err)

    except FileNotFoundError as err:
        display_error(w, err)

    return cmd_obj


# print(commands)




# current structure of cmd_obj - Pure example
# {'grep keyword file_name': {"flags": [-f, -l], "result": "string returned by the command run."
#   "redirects": [{'symbol': symbol, 'file_name': file_name, 'start': start_index, 'end': end_index}
#   "piped_value": last_cmd_result or None]}
#               
# }