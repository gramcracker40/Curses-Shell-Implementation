import os
from cmd_pkg.cmd_helpers import check_for_help_flag

@check_for_help_flag()
def mkdir(*args, **kwargs):
    '''
    makes a new directory in the current directory
    '''
    try:
        dir_name = kwargs['options']['args'][0] # grab first argument passed

        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
            temp = f"Directory '{dir_name}' created successfully.\n"
        else:
            temp = f"Directory '{dir_name}' already exists.\n"

    except TypeError:
        temp = f"Please pass arguments to mkdir\n"

    return temp

    

