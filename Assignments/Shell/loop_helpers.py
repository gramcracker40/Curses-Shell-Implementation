#
# Functional helper units of the main shell loop
#
#   mapper -> dictionary mapping all key strokes to the appropriate terminal action
#

import sys, os, time
import curses


prompt = "$ "                               # set default prompt
prev_cmds = []

def print_cmd(cmd:str, w):
    """ This function "cleans" off the command line, then prints
        whatever cmd that is passed to it to the bottom of the terminal.
    """
    padding = " " * 80
    sys.stdout.write("\r"+padding)
    sys.stdout.write("\r"+prompt+cmd)
    sys.stdout.flush()


def right_arrow(cmd:str, w):
    '''
    implements the right arrow key
    '''
    curs = w.getyx()
    w.move(curs[0], curs[1] + 1)


def left_arrow(cmd:str, w):
    '''
    implements the left arrow key
    '''
    curs = w.getyx()
    w.move(curs[0], curs[1] - 1)


def up_arrow(cmd:str, w):
    '''
    implements the up arrow key
    '''
    print_cmd(cmd)


def down_arrow(cmd:str, w):
    '''
    implements the down arrow key
    '''
    print_cmd(cmd)


def enter_key(cmd:str, w):
    '''
    executes the command
    '''
    w.addstr("Executing...\n")
    w.refresh()
    time.sleep(1)

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


