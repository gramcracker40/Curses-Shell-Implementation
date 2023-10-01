import sys
from cmd_pkg.cmd_helpers import check_for_help_flag

@check_for_help_flag()
def exit(*args, **kwargs):
    sys.exit()
