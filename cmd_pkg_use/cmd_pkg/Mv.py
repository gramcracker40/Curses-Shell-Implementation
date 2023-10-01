import shutil

def mv(*args, **kwargs):
    '''
    move a file into a specified directory
    mv source, destination
    '''

    try:
        source, destination = kwargs['options']['args']

        shutil.move(source, destination)
        return f"Successfully moved {source} into {destination}"
    
    except FileNotFoundError as err:
        return f"Error: '{err}'"
    except FileExistsError as err:
        return f"Error: '{err}'"


