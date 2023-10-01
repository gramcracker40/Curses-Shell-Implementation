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