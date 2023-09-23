#!/usr/bin/env python
"""
Main loop of shell implementation
"""
import curses

##################################################################################
##################################################################################

from loop_helpers import nav_mapper
from window_helpers import set_the_shell, pad_pos

##################################################################################
##################################################################################

og_w = ""

def main():
    curses.wrapper(curses_main)


def curses_main(w):
    '''
    Main curses window that will facilitate the shell's infinite loop

    Settings are at the beginning

    Main loop is abstracted dramatically, see loop_helpers.py for more
    details on the actual navigation buttons of the terminal. 

    w: the main curses window. everything stems from w

    window: pad object that allows for reserving extra space on the y axis of your 
              display. all text is displayed in the window so that we can allow for 
              scrolling up and down in the terminal. Without the window object we 
              could not have a scrollable terminal. the past commands would be
              overwritten by new ones and their results. 
    '''
    # Main curses window and our nested text pads configuration
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)

    w.idlok(True)
    w.scrollok(True)  # allows cursor to be reset after resize
    w_height, w_width = w.getmaxyx()
    global og_w       # makes the viewable windows dimensions available to sub modules
    og_w = (w_height, w_width)

    window = curses.newpad(20000, w_width) # reserving a lot of y space up front
    window.idlok(True)
    window.scrollok(True)
    win_height, win_width = window.getmaxyx()

    y, x = window.getyx()

    # display initial message
    window.addstr("---------------------------\n")
    window.addstr("| Shell Implementation    |\n")
    window.addstr("| type 'help' for details |\n")
    window.addstr("---------------------------\n\n")
    set_the_shell(window)
    
    window.refresh(y, x, 0, 0, w_height - 1, win_width - 1)
    w.refresh()
    
    cmd = ""

    while True:
        key = w.getch()

        if key in nav_mapper:
            cmd = nav_mapper[key](cmd, window, curses_w=w)
        else:
            window.addch(chr(key))
            cmd += chr(key)

        # grab the cursor again, need fresh value to refresh on (window_helpers), 
        # only refresh if they are not scrolling
        y, x = window.getyx()
        refresh_y = (y + 2) - w_height if y - w_height > 0 else 0

        window.refresh(refresh_y, 0, 0, 0, w_height - 1, w_width - 1) \
            if key != curses.KEY_PPAGE and key != curses.KEY_NPAGE else None


# starts the curses window
if __name__ == "__main__":
    main()
