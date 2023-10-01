import os
from cmd_pkg.cmd_helpers import check_for_help_flag

@check_for_help_flag()
def chmod(*args, **kwargs):
    '''
    \nchange the permission of a file
    \n
    \n pass a 3 digit integer for permissions
    \n     chmod 777 file.txt , give owner, group and others read, write, execute
    
    \nOwner: The user who created the file or directory.
    \nGroup: A group of users who share certain permissions.
    \nOthers: Everyone else on the system who is neither the owner nor in the group.
    '''
    try:
        args = kwargs['options']['args']
        permissions = args[0]
        file = args[1]

        os.chmod(file, int(permissions, 8)) # 8 passed to represent as octal notation
        return f"Permissions for '{file}' changed to {permissions}"
    except FileNotFoundError:
        return f"Error: File '{file}' not found."
    except PermissionError:
        return f"Error: You don't have permission to change permissions for '{file}'."
    except OSError as e:
        return f"Error: {e}"
    