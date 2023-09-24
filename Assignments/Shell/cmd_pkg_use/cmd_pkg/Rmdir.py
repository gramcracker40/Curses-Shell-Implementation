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
        directory = kwargs['options']['args'][0]
        os.rmdir(directory)
        return f"Directory '{directory}' removed successfully."
    except FileNotFoundError:
        return f"Error: Directory '{directory}' not found."
    except OSError as e:
        return f"Error: {e}"
    except IndexError as e:
        return f"Please pass a valid directory to rmdir\nrmdir dir"
    except TypeError as e:
        return f"rmdir received no arguments"