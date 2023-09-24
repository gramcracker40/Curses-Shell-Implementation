import os
import pwd
import grp

def get_username_from_uid(uid):
    '''
    only works on unix like machines
    '''
    try:
        user_info = pwd.getpwuid(uid)
        return user_info.pw_name
    except KeyError:
        return None  # User not found


def get_groupname_from_gid(gid):
    '''
    only works on unix like machines
    '''
    try:
        group_info = grp.getgrgid(gid)
        return group_info.gr_name
    except KeyError:
        return None  # Group not found
    

def check_for_help_flag():
    '''
    checks for an "h" in the flag string passed to the command
    if there is one it will simply return the functions docstring 
    else, run the function
    '''
    def decorator(func):
        def wrapper(*args, **kwargs):
            if "h" in kwargs['options']['flags']:
                return func.__doc__.split('\n')
            else:
                return func(*args, **kwargs)

        return wrapper

    return decorator