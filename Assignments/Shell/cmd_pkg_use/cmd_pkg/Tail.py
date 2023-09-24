

def tail(*args, **kwargs):
    '''
    \n given a file, display the last few lines
    \n tail file.txt
    \n    default: 10 lines
    \n flags:
    \n    -n int:num_lines: -n 30 //displays last 30 lines
    \n 
    '''
    try:
        args = kwargs['options']['args']
        display = []
        
        num_lines = 10 if "n" not in kwargs['options']['flags'] else int(args[1])
        temp = open(args[0], "r").readlines()
        num_lines = len(temp) if num_lines > len(temp) else num_lines

        for line in range(num_lines):
            display.append(temp[-(line + 1)])
        
        display.reverse()   # very last line is first in list. reverse the list

        return display

    except IndexError as err:
        return f"tail: please pass a file to display"
    
    except FileNotFoundError as err:
        return f"tail: file not found -> {err}"

    except TypeError as err:
        return f"tail: please ensure you have passed valid integer values for -n"

    except IsADirectoryError as err:
        return f"tail: displays text from a file, directories can not be passed to tail"