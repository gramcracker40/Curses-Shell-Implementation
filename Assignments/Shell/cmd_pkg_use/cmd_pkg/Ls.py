#!/usr/bin/env python
import os
import stat
import datetime


def l_flag(file_paths=[]):

    l_flag_output = ""
    
    for file_path in file_paths:
        file_stat = os.stat(file_path)

        size = file_stat.st_size  # bytes
        owner = file_stat.st_uid  # user ID

        group = file_stat.st_gid  # group ID
        permissions = stat.filemode(file_stat.st_mode)

        modification_time = datetime.datetime.fromtimestamp(file_stat.st_mtime)  # Modification timestamp

        l_flag_output += "{:<11} {:<10} {:<10} {:>10} {:>12} {:<25}\n".format(
            permissions, owner, group, size, str(modification_time), os.path.basename(file_path)
        )

    return l_flag_output


# Replace 'file_path' with the path to the file or directory you want to get information about
file_path =  os.listdir(os.getcwd())
file_info = l_flag(file_path)

print(file_info)



def ls(*args, **kwargs):
    '''
    return the entire current working directory
    '''
    curr_dir_paths = os.listdir(os.getcwd())

    
    flags = kwargs["options"]["flags"]

    if "-l" in flags:
        pass

    print(f"ls: flags({flags})")
    return curr_dir_paths
