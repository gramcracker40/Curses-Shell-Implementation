import os
from cmd_pkg.cmd_helpers import check_for_help_flag

@check_for_help_flag()
def sort(*args, **kwargs):
    '''
    given a string with rows seperated by new lines. sort the lines
    and return the output
    '''
    input_data = kwargs["options"]["input_data"]
    lines = input_data.split('\n') if type(input_data) == str else None

    if type(input_data) == list:
        temp = ""
        for each in input_data:
            temp += f"{each}\n"
        
        lines = temp.split('\n')

    lines.sort()

    return lines

