import os, sys


def cd(*args, **kwargs):
    '''
    changes the directory to the file path pass
    '''

    sys.path.append(os.path.join(os.getcwd(), kwargs['options']['args'][0]))

    return f"Changed path to {os.getcwd()}"
