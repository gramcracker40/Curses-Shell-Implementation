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

            if char == 8 or char == 10:
                cmd = action

        else:
            w.addch(char)
            cmd += chr(char)

        w.refresh()

# starts the curses window
if __name__ == "__main__":
    main()
