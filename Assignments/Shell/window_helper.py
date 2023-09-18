import textwrap
import curses

curses_colors = {           # all useable colors. Background black on all
    "RED": 1,
    "GREEN": 2,
    "YELLOW": 3,
    "BLUE": 4,
    "MAGENTA": 5,
    "CYAN": 6
}


def clear_line(w):
    '''
    helper function to move cursor to beginning and 
    clear all text on the current line to be rerendered
    '''
    curs = w.getyx()
    w.move(curs[0], 0)
    w.clrtobot()
    w.refresh()


def print_long_string(w, string: str, color_options=[{}]):
    '''
    color_options ex: [{'delimeter': '.', 'color': 'RED'}]
        allows for you to specify a delimeter to search for in 
        a given string. If delimeter is found, color that string 
        that color, can specify multiple delimeters with different or same
        colors

    all useable colors are up top
    '''
    height, width = w.getmaxyx()

    # move to the next line
    curs = w.getyx()
    w.move(curs[0] + 1, 0)

    # chop the string into segments that will fit into the window
    chopped = textwrap.wrap(string, width - 2)

    # add the segments to the window, color them if options are passed
    for line in chopped:
        if len(color_options) > 0:
            for each in color_options:
                if each["delimeter"] in line:
                    w.addstr(f"{line}\n", curses.color_pair(color_options[each["color"]]))
        else:
            w.addstr(f"{line}\n")

    w.refresh


def print_list(w, list, color_options=[{}]):
    '''
    prints a long list 
    '''

    height, width = w.getmaxyx()

    # move to the next line
    curs = w.getyx()
    w.move(curs[0] + 1, 0)

    for e_string in list:
        # chop the string into segments that will fit into the window
        chopped = textwrap.wrap(e_string, width - 2)

        # add the segments to the window, color them if options are passed
        for line in chopped:
            if len(color_options) > 0:
                for each in color_options:
                    if each["delimeter"] in line:
                        w.addstr(f"{line}\n", curses.color_pair(color_options[each["color"]]))
            else:
                w.addstr(f"{line}\n")
