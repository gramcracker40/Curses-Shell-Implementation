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

from loop_helpers import nav_mapper, prompt

##################################################################################
##################################################################################


def main():
    curses.wrapper(curses_main)


def curses_main(w):
    '''
    Main curses window that will facilitate the shell's infinite loop
    '''
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)

    


    w.scrollok(True)

    w.addstr("---------------------------\n")
    w.addstr("| Shell Implementation    |\n")
    w.addstr("| type 'help' for details |\n")
    w.addstr("---------------------------\n")
    w.refresh()

    w.addstr(f"\n{prompt}")
    w.refresh()

    cmd = ""

    while True:
        char = w.getch()

        if char in nav_mapper:
            action = nav_mapper[char](cmd, w)
            cmd = action

        else:
            w.addch(char)
            cmd += chr(char)

        w.refresh()

# starts the curses window
if __name__ == "__main__":
    main()
