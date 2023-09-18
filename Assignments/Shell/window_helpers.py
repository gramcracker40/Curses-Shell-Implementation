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


def delimeter_coloring(w, chopped, color_options):
    '''
    handles the logic behind color_options in 
    print_long_string and print_list 
    adds the strings to the window
    '''
    color_check = bool(color_options[0].get("delimeter")) \
        and color_options.get("color") is not None

    for line in chopped:
        colored = False
        if color_check:
            for each in color_options:
                if each["delimeter"] in line:
                    w.addstr(f"{line}\n", 
                        curses.color_pair(curses_colors[each["color"]]))
                    colored = True
        if not colored:
            w.addstr(f"{line}\n")


def print_long_string(w, string: str, color_options=[]):
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
    delimeter_coloring(w, chopped, color_options)

    w.refresh


def print_list(w, list, color_options=[{}]):
    '''
    prints a long list 
    '''

    height, width = w.getmaxyx()

    curs = w.getyx()
    w.move(curs[0] + 1, 0)

    for e_string in list:
        chopped = textwrap.wrap(e_string, width - 2)
        delimeter_coloring(w, chopped, color_options)

