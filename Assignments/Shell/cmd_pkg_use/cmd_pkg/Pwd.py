#!/usr/bin/env python
import os
from cmd_pkg.cmd_helpers import check_for_help_flag

@check_for_help_flag()
def pwd(*args, **kwargs):
    '''
    Print Working Directory

    gives the current path the user is currently working
    within in that shell instance. 
    '''
    temp = os.getcwd()
    return temp