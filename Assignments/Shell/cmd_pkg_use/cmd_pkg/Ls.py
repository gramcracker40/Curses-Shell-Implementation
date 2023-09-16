#!/usr/bin/env python
import os

def ls(**kwargs):
    '''
    print out the entire current working directory
    '''

    curr_dir = os.listdir(os.getcwd())
    print(os.getcwd())
    print(curr_dir)

ls()


print("Helllllooooo")