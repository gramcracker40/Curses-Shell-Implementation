import textwrap

def clear_line(w):
    '''
    helper function to move cursor to beginning and 
    clear all text on the current line to be rerendered
    '''
    curs = w.getyx()
    w.move(curs[0], 0)
    w.clrtobot()
    w.refresh()


def print_long_string(w, string:str):
    height, width = w.getmaxyx()
    
    # move to the next line
    curs = w.getyx()
    w.move(curs[0] + 1, 0)

    # chop the string into segments that will fit into the window
    chopped = textwrap.wrap(string, width - 2)

    # add the segments to the window
    for line in chopped:
        w.addstr(line + "\n")

    w.refresh



