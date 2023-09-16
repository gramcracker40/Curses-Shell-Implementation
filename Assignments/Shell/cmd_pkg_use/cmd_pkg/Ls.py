#!/usr/bin/env python
import os

def ls(**kwargs):
    '''
    return the entire current working directory
    '''
    curr_dir = os.listdir(os.getcwd())

    printable = ""
    for dirr in curr_dir:
        printable = printable + dirr + "   "

    return printable
