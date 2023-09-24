import os
from cmd_pkg.cmd_helpers import check_for_help_flag

@check_for_help_flag()
def mkdir(*args, **kwargs):
    '''makes a new directory in the current directory
    \n   can also specify multiple directories to create. 
    \n mkdir file1
    \n mkdir folder1 folder2 folderN
    '''
    try:
        dir_name = kwargs['options']['args']

        temp = []
        for dir in dir_name:
            if not os.path.exists(dir):
                os.makedirs(dir)
                temp.append(f"Directory '{dir}' created successfully.\n")
            else:
                temp.append(f"Directory '{dir}' already exists.\n")

    except TypeError:
        temp.append(f"Please pass arguments to mkdir\n")

    return temp

    

