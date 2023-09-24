#!/usr/bin/env python
from subprocess import call
from cmd_pkg.cmd_helpers import check_for_help_flag

@check_for_help_flag()
def cat(*args, **kwargs):
    """   
    NAME
        cat - concatenate files and print on the standard output
    SYNOPSIS
        cat file1 file2 fileN
        cat file1 > new_file1.txt
    DESCRIPTION
        Concatenate FILE(s) to standard output.

    """
    try:
        files = kwargs['options']['args']

        display = [] # print as a list in Execute.py for the formatting to be on point
        for file in files:
            temp = open(file, "r").readlines()
            for line in temp:
                display.append(line)

        return display

    except FileNotFoundError as err:
        return f"File not found -> {err}"

