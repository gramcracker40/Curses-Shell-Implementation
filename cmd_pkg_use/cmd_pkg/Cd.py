import os, sys
from cmd_pkg.cmd_helpers import check_for_help_flag

@check_for_help_flag()
def cd(*args, **kwargs):
    '''
    changes the directory to the file path pass\n
    \n ex: cd "/valid_path" , cd validpath
    '''
    path = kwargs['options']['args'][0]
    user = os.getenv('USERNAME') or os.getenv('USER')


    if not path:
        return f"Please specify a valid path to change into..."
    
    try:
        if path == '~':
            os.chdir(f"/home/{user}")
        else:
            os.chdir(path)

    except FileNotFoundError as err:
        return f"file not found error\n{err}"
    except PermissionError as err:
        return f"You do not have the permissions needed to access this directory\n{err}"
    except NotADirectoryError as err:
        return f"Invalid directory: {err}"


    return f"Switching..."
