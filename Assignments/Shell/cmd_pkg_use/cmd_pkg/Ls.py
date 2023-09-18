#!/usr/bin/env python
import os

def ls(*args, **kwargs):
    '''
    return the entire current working directory
    '''
    curr_dir = os.listdir(os.getcwd())

    
    flags = kwargs["options"]["flags"]

    printable = ""
    for dirr in curr_dir:
        printable = printable + dirr + "   "

    return printable
