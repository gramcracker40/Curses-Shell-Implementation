import shutil

def mv(*args, **kwargs):
    '''
    move a file into a specified directory
    mv source, destination
    '''

    try:
        source, destination = kwargs['options']['args']

        shutil.move(source, destination)
    
    except FileNotFoundError as err:
        print(f"Error: '{err}'")
    except FileExistsError as err:
        print(f"Error: '{err}'")


