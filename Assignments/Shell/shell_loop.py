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

from getch import Getch
from cmd_pkg_use.main import cmd
from loop_helpers import print_cmd, nav_mapper

##################################################################################
##################################################################################

getch = Getch()  # Grabs the char typed


def main():
    curses.wrapper(curses_main)


def curses_main(w):
    '''
    Main curses window that will facilitate the shell's infinite loop
    '''
    w.addstr("---------------------------\n")
    w.addstr("| Shell Implementation    |\n")
    w.addstr("| type 'help' for details |\n")
    w.addstr("---------------------------\n")
    w.refresh()

    w.addstr("\n$ ")
    w.refresh()

    cmd = ""
    
    while True:    
        
        char = w.getch()
        cmd += chr(char)
        #w.addstr(f"Char: {char}  Type: {type(char)}")

        if char in nav_mapper:
            action = nav_mapper[char](cmd, w)
        else:
            w.addch(char)
        

        w.refresh()
        

# starts the curses window
if __name__ == "__main__":
    main()
    
    

