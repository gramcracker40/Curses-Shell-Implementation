import os
from cmd_pkg.cmd_helpers import check_for_help_flag

@check_for_help_flag()
def dir(*args, **kwargs):
    '''
    shows directories

    does not show hidden. use ls for that
    '''
    temp = os.listdir(os.getcwd())
    
    returner = ""
    for dir in temp:
        returner += f"{dir}   " if "." not in dir else ""

    return returner

