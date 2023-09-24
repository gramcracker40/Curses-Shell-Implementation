import os
from cmd_pkg.cmd_helpers import check_for_help_flag

@check_for_help_flag()
def rm(*args, **kwargs):
    '''
    removes a file given a valid file path
    \nrm file.txt
    \nrm path/to/file.txt
    '''

    try:
        file = kwargs['options']['args'][0]
        os.remove(file)
        return f"File '{file}' removed successfully."
    except FileNotFoundError:
        return f"Error: File '{file}' not found."
    except OSError as e:
        return f"Error: {e}"
    except IndexError as e:
        return f"Please pass valid arguments {e}"
    except TypeError as e:
        return f"rm received no arguments"