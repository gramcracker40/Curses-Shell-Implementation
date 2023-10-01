#!/usr/bin/env python
"""
Main loop of shell implementation
"""
import os
import sys
import curses
from time import sleep


##################################################################################
##################################################################################

from loop_helpers import nav_mapper, prompt, set_the_shell
from window_helpers import curses_colors

##################################################################################
##################################################################################


def main():
    curses.wrapper(curses_main)


def curses_main(w):
    '''
    Main curses window that will facilitate the shell's infinite loop

    Settings are at the beginning

    Main loop is abstracted dramatically, see loop_helpers.py for more
    details on the actual navigation. 
    '''
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)

    w.scrollok(True)
    #curses.scrollok(w, False)  # allows cursor to be reset after resize

    w.addstr("---------------------------\n")
    w.addstr("| Shell Implementation    |\n")
    w.addstr("| type 'help' for details |\n")
    w.addstr("---------------------------\n\n")
    w.refresh()

    set_the_shell(w)

    cmd = ""

    while True:
        char = w.getch()

        if char in nav_mapper:
            cmd = nav_mapper[char](cmd, w)

        else:
            w.addch(char)
            cmd += chr(char)

        w.refresh()


# starts the curses window
if __name__ == "__main__":
    main()
