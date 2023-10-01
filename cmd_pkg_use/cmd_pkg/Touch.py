import os
from pathlib import Path

def touch(*args, **kwargs):
    '''touches a file path
    \n if the file path does not exist, create it
    \n if the file path exists, update modification date to now
    '''
    try:
        file_paths = kwargs['options']['args']

        return_list = []
        for file_path in file_paths:
            file = Path(file_path)
            file_exists = os.path.isfile(file)
            file.touch(exist_ok=True)
            
            if file_exists:
                return_list.append(f"Touched '{file_path}'")
            else:
                return_list.append(f"Created '{file_path}'")
        
        return return_list
        
    except PermissionError as err:
        return f"You do not have permissions to access the file"
    except IsADirectoryError:
        return "Error: Specified path is a directory."
    except OSError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"