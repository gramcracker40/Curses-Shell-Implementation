from cmd_pkg.cmd_helpers import check_for_help_flag

@check_for_help_flag()
def head(*args, **kwargs):
    '''display the first few lines of a file \n
    \n
    \nUsage: head file.txt
    \n
    \ndefault: show 10 lines
    \nflags:
    \n    -n : number of lines to display
    \n    head file.txt -n 20'''

    try:
        args = kwargs['options']['args']
        file = args[0]
        display = [] # print as a list in Execute.py for the formatting to be on point

        num_lines = 10 if "n" not in kwargs['options']['flags'] else int(args[1])

        temp = open(file, "r").readlines()

        num_lines = len(temp) if num_lines > len(temp) else num_lines

        for line in range(num_lines):
            display.append(temp[line])

        return display

    except FileNotFoundError as err:
        return f"head: file not found -> {err}"
    
    except TypeError as err:
        return f"head: please ensure you have passed valid integer values for -n"

    except IsADirectoryError as err:
        return f"head: displays text from a file, directories can not be passed to head"
    
    except IndexError as err:
        return f"head: you need to pass an integer value to the -n flag, '-n 25'"
