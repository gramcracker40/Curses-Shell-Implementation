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
prev_cmds = []              # in memory list of all previous commands
arrow_counter = 0           # up and down arrow index position


def backspace_key(cmd: str, w):
    '''
    delete a character from terminal
    return new string for the command with the
    appropriate index being removed. 
    '''
    curs = w.getyx()

    temp = cmd[:curs[1] - 3] + cmd[curs[1] - 2:] if curs[1] > 2 else cmd

    if temp != cmd:
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

def up_arrow(cmd: str, w):
    '''
    implements the up arrow key
    '''
    global arrow_counter
    arrow_counter += 1 if arrow_counter + 1 < len(prev_cmds) else 0
    clear_line(w)
    
    if arrow_counter == 0:
        prev_cmds.insert(0, cmd)

    if arrow_counter != arrow_counter:
        arrow_counter = arrow_counter

    new_cmd = prev_cmds[arrow_counter]
    w.addstr(prompt + new_cmd)

    return new_cmd


def down_arrow(cmd: str, w):
    '''
    implements the down arrow key
    '''
    global arrow_counter
    arrow_counter -= 1 if arrow_counter - 1 >= 0 else 0
    clear_line(w)
    
    new_cmd = prev_cmds[arrow_counter]

    w.addstr(prompt + new_cmd)

    return new_cmd

    

##################################################################
# enter_key sends the currently typed command to execute for
# processing the command properly
##################################################################


def enter_key(cmd: str, w):
    '''
    executes the command
    '''
    time.sleep(1)
    prev_cmds.append(cmd)
    result = execute(cmd, w)
    w.addstr(prompt)

    # result contains the result of the previous command

    new_cmd = ""

    return new_cmd


nav_mapper = {
    259: up_arrow,
    258: down_arrow,
    260: left_arrow,
    261: right_arrow,
    10: enter_key,
    8: backspace_key
}
