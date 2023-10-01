import os
from cmd_pkg.cmd_helpers import check_for_help_flag

@check_for_help_flag()
def sort(*args, **kwargs):
    '''
    given a string with rows seperated by new lines. sort the lines
    and return the output
    \n
    example:   sort file.txt > sorted_file.txt
    example:   ls | sort
    '''
    try:
        input_data = kwargs["options"]["input_data"]
        
        if not input_data:
            input_data = open(kwargs["options"]["args"][0], "r").readlines()
        
        if type(input_data) == list:
            temp = ""
            for each in input_data:
                temp += f"{each}\n"
            
            lines = temp.split('\n')
        elif type(input_data) == str:
            lines = input_data.split('\n')

        lines.sort()

        return lines
    
    except FileNotFoundError as err:
        return f"Error: {err}"
