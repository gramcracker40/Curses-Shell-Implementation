from cmd_pkg.cmd_helpers import check_for_help_flag

check_for_help_flag()
def exclamation(*args, **kwargs): 
    '''
    goes back a number of commands specified using the exclamation point operator. 
    \n! 5 --> goes back 5 commands
    '''
    try:

        places = int(kwargs['options']['args'][0])

        prev_cmds = open(f"/home/bench/Shell/cmd_pkg_use/cmd_pkg/command_history.txt", "r").read()
        temp = prev_cmds.split(",")  # formats it nicely from the stringified list passed from the enter key to the file path
        temp[0] = temp[0][1:]
        temp[-1] = temp[-1][:-1]
        temp.reverse()

        return temp[-places] # do it like this so that if they say "! 2" it will go back two commands. 
    except ValueError as err:
        return f"!: An error occurred with one of the values"
    except TypeError as err:
        return f"!: Please pass an integer to !" if "-h" not in kwargs['options']['flags'] else exclamation.__doc__.split('\n')