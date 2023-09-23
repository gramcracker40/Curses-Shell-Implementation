import textwrap
import curses
import os
from socket import gethostname

prompt = "$ "               # set default prompt #TODO change to .env file
pad_pos = 0                 # tracks the desired displayed section, allows scroll up and down

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


def set_the_shell(w):
    # sets the shell
    global pad_pos
    username = os.getenv('USERNAME') or os.getenv('USER')
    hostname = gethostname()

    w.addstr(f"\n{username}@{hostname} ~ ", curses.color_pair(curses_colors["RED"]))
    w.addstr(f"{os.getcwd()}\n", curses.color_pair(curses_colors["CYAN"]))
    w.addstr(prompt)

    pad_pos += 3


def delimeter_coloring(w, chopped, color_options=[{}]):
    '''
    handles the logic behind color_options in 
    print_long_string and print_list 
    adds the strings to the window
    '''
    global pad_pos
    color_check = bool(color_options[0].get("delimeter")) \
        and color_options[0].get("color")
    
    for line in chopped:
        colored = False
        if color_check:
            for each in color_options:
                if each["delimeter"] in line:
                    w.addstr(f"\n{line}", 
                        curses.color_pair(curses_colors[each["color"]]))
                    colored = True
                    pad_pos += 1
        if not colored:
            w.addstr(f"\n{line}")
            pad_pos += 1


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

    # chop the string into segments that will fit into the window
    chopped = textwrap.wrap(string, width - 2)
    delimeter_coloring(w, chopped, color_options)


def print_list(w, list, color_options=[{}]):
    '''
    prints a long list, same options as print_long_string
    '''

    height, width = w.getmaxyx()

    curs = w.getyx()

    for e_string in list:
        chopped = textwrap.wrap(e_string, width - 2)
        delimeter_coloring(w, chopped, color_options)

