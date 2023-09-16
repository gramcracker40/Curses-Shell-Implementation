#
# Functional helper units of the main shell loop
#
#   mapper -> dictionary mapping all key strokes to the appropriate terminal action
#

import sys
import os
import time
import curses
from Execute import execute
from window_helper import clear_line

prompt = "$ "               # set default prompt #TODO change to .env file
prev_cmds = []

def backspace_key(cmd: str, w):
    '''
    delete a character from terminal
    return new string for the command with the
    appropriate index being removed. 
    '''
    curs = w.getyx()

    temp = cmd[:curs[1] - 3] + cmd[curs[1] - 2:] if curs[1] > 1 else cmd

    clear_line(w)

    w.addstr(prompt + temp)
    w.move(curs[0], curs[1] - 1)

    return temp


##################################################################
# left and right arrows allow placing the cursor in user desired positioning
##################################################################

def right_arrow(cmd: str, w):
    '''
    implements the right arrow key
    '''
    curs = w.getyx()
    max = w.getmaxyx()

    if curs[1] + 1 < max[1]:
        w.move(curs[0], curs[1] + 1)


def left_arrow(cmd: str, w):
    '''
    implements the left arrow key
    '''
    curs = w.getyx()

    if curs[1] - 1 >= 0:
        w.move(curs[0], curs[1] - 1)


##################################################################
# up and down arrows implement switching between previous commands
##################################################################

arrow_counter = 0

def up_arrow(cmd: str, w):
    '''
    implements the up arrow key
    '''
    temp = arrow_counter + 1 if arrow_counter + 1 <= len(prev_cmds) else None
    clear_line(w)
    w.addstr(prev_cmds[temp])

    return cmd


def down_arrow(cmd: str, w):
    '''
    implements the down arrow key
    '''
    temp = arrow_counter - 1 if arrow_counter - 1 >= 0 else None
    clear_line(w)
    w.addstr(prev_cmds[temp])

    return cmd

    

##################################################################
# enter_key sends the currently typed command to execute for
# processing the command properly
##################################################################


def enter_key(cmd: str, w):
    '''
    executes the command
    '''
    # clear_line(w)
    curs = w.getyx()
    w.move(curs[0] + 1, 0)
    time.sleep(1)

    prev_cmds.append(cmd)
    result = execute(cmd)

    return result


nav_mapper = {
    258: down_arrow,
    259: up_arrow,
    260: left_arrow,
    261: right_arrow,
    10: enter_key,
    8: backspace_key
}
