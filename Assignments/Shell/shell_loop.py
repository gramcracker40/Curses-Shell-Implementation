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
from loop_helpers import nav_mapper, prompt

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

    w.addstr(f"\n{prompt}")
    w.refresh()

    cmd = ""
    
    while True:    
        
        char = w.getch()
        
        #w.addstr(f"Char: {char}  Type: {type(char)}")

        if char in nav_mapper:
            action = nav_mapper[char](cmd, w)

            if char == 8:
                cmd = action  # set cmd to the freshly returned str
                print(f"cmd new value: {cmd}")
        else:
            w.addch(char)
            cmd += chr(char)
        

        w.refresh()
        

# starts the curses window
if __name__ == "__main__":
    main()
    
    

