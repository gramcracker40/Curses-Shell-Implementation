from cmd_pkg.cmd_helpers import check_for_help_flag

@check_for_help_flag()
def history(*args, **kwargs):
    '''
    provides the history of commands
    TODO: need a script to determine history location, fixed for now
    '''
    prev_cmds = open(f"/home/bench/Shell/cmd_pkg_use/cmd_pkg/command_history.txt", "r").read()
    temp = prev_cmds.split(",")  # formats it nicely from the stringified list passed from the enter key to the file path
    temp[0] = temp[0][1:]
    temp[-1] = temp[-1][:-1]
    temp.reverse()

    return temp