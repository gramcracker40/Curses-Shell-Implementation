import os
from cmd_pkg.cmd_helpers import check_for_help_flag

@check_for_help_flag()
def rmdir(*args, **kwargs):
    '''
    \nremoves a directory given a valid directory 
    \nrmdir /path/to/directory
    \nrmdir directory
    '''

    try:
        args = kwargs['options']['args']
        return_list = []
        
        for directory in args:
            try:
                os.rmdir(directory)
                return_list.append(f"Directory '{directory}' removed successfully.")
            except FileNotFoundError as err:
                return_list.append(f"Directory '{directory}' not found")
        
        return return_list
    
    except OSError as e:
        return f"Error: {e}"
    except IndexError as e:
        return f"Please pass a valid directory to rmdir\nrmdir dir"
    except TypeError as e:
        return f"rmdir received no arguments"