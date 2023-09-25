from cmd_pkg.cmd_helpers import check_for_help_flag

@check_for_help_flag()
def history(*args, **kwargs):
    '''
    provides the history of commands
    need a script to determine history location, fixed for now
    '''
    
    prev_cmds = open(f"/home/bench/Shell/Assignments/Shell/cmd_pkg_use/cmd_pkg/command_history.txt", "r").read()
    return prev_cmds