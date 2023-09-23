import os, sys


def cd(*args, **kwargs):
    '''
    changes the directory to the file path pass
    '''
    path = kwargs['options']['args'][0]

    if not path:
        return f"Please specify a valid path to change into..."
    
    try:
        os.chdir(path)

    except FileNotFoundError as err:
        return f"file not found error\n{err}"
    except PermissionError as err:
        return f"You do not have the permissions needed to access this directory\n{err}"
    except NotADirectoryError as err:
        return f"Invalid directory: {err}"


    return f"Switching..."
