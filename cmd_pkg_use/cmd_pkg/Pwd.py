#!/usr/bin/env python
import os

def pwd(*args, **kwargs):
    '''
    Print Working Directory

    gives the current path the user is currently working
    within in that shell instance. 
    '''
    temp = os.getcwd()
    return temp


test = pwd()

print(test)