#!/usr/bin/env python
import os
import stat
import datetime
from cmd_pkg.cmd_helpers import get_username_from_uid, get_groupname_from_gid


def convert_readable_size(size_bytes):
    '''
    Converts bytes to human readable size
    '''
    # List of unit labels and their respective byte sizes
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    unit_index = 0

    while size_bytes >= 1024 and unit_index < len(units) - 1:
        size_bytes /= 1024.0
        unit_index += 1

    return f"{size_bytes:.1f} {units[unit_index]}"


def l_flag(file_paths=[], human_readable=False):

    l_flag_output = []
    
    for file_path in file_paths:
        file_stat = os.stat(file_path)

        size = file_stat.st_size
        if human_readable:
            size = convert_readable_size(file_stat.st_size)  # bytes

        owner = get_username_from_uid(file_stat.st_uid)   # user ID
        group = get_groupname_from_gid(file_stat.st_gid)  # group ID
        permissions = stat.filemode(file_stat.st_mode)    

        modification_time = datetime.datetime.fromtimestamp(file_stat.st_mtime)  # Modification timestamp

        l_flag_output.append("{:<11} {:<8} {:<8} {:<8} {:<20} {:<30}\n".format(
            permissions, owner, group, size, str(modification_time.strftime("%Y-%m-%d %H:%M:%S")), os.path.basename(file_path)
        ))

    return l_flag_output


def ls(*args, **kwargs):
    '''
    return the entire current working directory
    '''
    temp = os.listdir(os.getcwd())
    returner = temp
    
    flags = kwargs["options"]["flags"]

    if "l" in flags:
        returner = l_flag(temp)
    
    if "l" and "h" in flags:
        returner = l_flag(temp, human_readable=True)

    return returner
