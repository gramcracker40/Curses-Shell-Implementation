import os
from cmd_pkg.cmd_helpers import check_for_help_flag

@check_for_help_flag()
def rm(*args, **kwargs):
    '''
    removes a file given a valid file path
    \nrm file.txt
    \nrm path/to/file.txt
    #TODO; implement wildcards fil*e *file etc
    '''

    try:
        args = kwargs['options']['args']
        flags = kwargs['options']['flags']

        return_list = []
        for file in args:
            if os.path.isfile(file):
                os.remove(file)
                return_list.append(f"Successfully deleted '{file}'")
            elif os.path.isdir(file) and 'r' in flags:
                for each in os.listdir(file):
                    os.remove(f"{file}/{each}")
                    return_list.append(f"Successfully deleted '{each}'")
            
            else:
                return_list.append(f"Could not take action on '{file}', \nremember to pass -r if deleting any directories recursively")

        return return_list
    

    # except FileNotFoundError:
    #     return f"Error: File '{file}' not found."
    except IsADirectoryError as err:
        return f"IsADirectoryError: {e}"
    except OSError as e:
        return f"Error: {e}"
    except IndexError as e:
        return f"Please pass valid arguments {e}"
    except TypeError as e:
        return f"rm received no arguments"