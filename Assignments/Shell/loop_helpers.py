#
# Functional helper units of the main shell loop
#
#   mapper -> dictionary mapping all key strokes to the appropriate terminal action
#

import sys, os, time
import curses
from execute import execute


prompt = "$ "                               # set default prompt
prev_cmds = []


def right_arrow(cmd:str, w):
    '''
    implements the right arrow key
    '''
    curs = w.getyx()
    max = w.getmaxyx()
    
    if curs[1] + 1 < max[1]:
        w.move(curs[0], curs[1] + 1)


def left_arrow(cmd:str, w):
    '''
    implements the left arrow key
    '''
    curs = w.getyx()

    if curs[1] - 1 >= 0:
        w.move(curs[0], curs[1] - 1)


def up_arrow(cmd:str, w):
    '''
    implements the up arrow key
    '''
    pass


def down_arrow(cmd:str, w):
    '''
    implements the down arrow key
    '''
    


def enter_key(cmd:str, w):
    '''
    executes the command
    '''
    curs = w.getyx()
    w.move(curs[0], curs[1] - curs[1])
    w.clrtobot()
    w.refresh()
    w.addstr("Executing...\n")
    w.refresh()
    time.sleep(1)

    prev_cmds.append(cmd)
    result = execute(cmd)


    cmd_parts = cmd.split()



    
    pass


def backspace_key(cmd:str, w):
    '''
    delete a character from terminal
    '''
    new = cmd[:-1]
    return new



nav_mapper = {
    258: down_arrow,
    259: up_arrow,
    260: left_arrow,
    261: right_arrow,
    10: enter_key,
    8: backspace_key
}


