import os, shutil
from cmd_pkg.cmd_helpers import check_for_help_flag

@check_for_help_flag()
def cp(*args, **kwargs):
    '''-- Examples:\n
    \ncp file1 file2
    \ncp directory1 directory2
    \ncp file1 directory2
    \n -- DESCRIPTION: copy file1 and call it file2
    \n     NOTE: also works for directories.
    \n     NOTE: can also copy file into an existing directory'''
    
    args = kwargs['options']['args']

    # make sure they have two arguments
    if isinstance(args, (list, tuple)) and len(args) == 2:
        file1, file2 = args # set paths for file1 and file2
        base_file1, base_file2 = os.path.basename(file1), os.path.basename(file2)

        try:
            # if theyre both files, or first is file second is directory
            if (("." in base_file1 and "." in base_file2) or
                ("." in base_file1 and "." not in base_file2)):
                shutil.copy(file1, file2)

                return f"Copied {file1} into {file2}"
            # if theyre both directories
            elif "." not in base_file1 and "." not in base_file2:
                if not os.path.isdir(file2):
                    os.mkdir(file2)
                shutil.copytree(file1, file2)

                return f"Copied {file1} into {file2}"
       
            else: # directories passed are not valid
                return f"arg1 and arg2 must both either be VALID files or VALID directories"


        except FileNotFoundError as err:
            return f"File not found -> {err}"
        except FileExistsError as err:
            return f"Directory already exists - {err}\nif you would like to overwrite this directory please rmdir first"
        except PermissionError as err:
            return f"You do not have the appropriate permissions: {err}"
        except NotADirectoryError as err:
            return f"Invalid directory: {err}"
        except shutil.SameFileError as err:
            return f"The two directories passed are the same - {err}"


    else:
        return f"""cp requires two valid file/directory 
                arguments be given\n ex: cp file1 file2
                \ncp directory1 directory2\ncp file1 directory2"""
    