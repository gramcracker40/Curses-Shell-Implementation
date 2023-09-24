#
# Functional helper units of the main shell loop
#
#   mapper -> dictionary mapping all key strokes to the 
#               appropriate terminal action
#   

import sys
import os
import time
import curses
from socket import gethostname
from Execute import execute
from window_helpers import clear_line, set_the_shell, prompt, pad_pos, curses_colors

prev_cmds = []              # in memory list of all previous commands
arrow_counter = 0           # up and down arrow index position



def backspace_key(cmd: str, w, **kwargs):
    '''
    delete a character from terminal
    return new string for the command with the
    appropriate index being removed. 
    '''
    curs = w.getyx()

    temp = cmd[:curs[1] - 3] + cmd[curs[1] - 2:] if curs[1] > 2 else cmd

    if temp != cmd:
        clear_line(w)
        w.addstr(prompt, curses.color_pair(curses_colors["YELLOW"]))
        w.addstr(temp)
        w.move(curs[0], curs[1] - 1)

    return temp


##################################################################
# left and right arrows allow placing the cursor in user desired positioning
##################################################################

def right_arrow(cmd: str, w, **kwargs):
    '''
    implements the right arrow key
    '''
    curs = w.getyx()
    max = w.getmaxyx()

    w.move(curs[0], curs[1] + 1) if curs[1] + 1 < max[1] else None
    
    return cmd
        
def left_arrow(cmd: str, w, **kwargs):
    '''
    implements the left arrow key
    '''
    curs = w.getyx()

    w.move(curs[0], curs[1] - 1) if curs[1] - 1 >= 0 else None

    return cmd

##################################################################
# up and down arrows implement switching between previous commands
##################################################################

def up_arrow(cmd: str, w, **kwargs):
    '''
    implements the up arrow key
    '''
    global arrow_counter

    if arrow_counter == 0:
        prev_cmds.insert(0, cmd)

    arrow_counter += 1 if arrow_counter + 1 < len(prev_cmds) else 0
    clear_line(w)

    new_cmd = prev_cmds[arrow_counter]

    w.addstr(prompt, curses.color_pair(curses_colors["YELLOW"]))
    w.addstr(new_cmd)

    return new_cmd


def down_arrow(cmd: str, w, **kwargs):
    '''
    implements the down arrow key
    '''
    global arrow_counter
    arrow_counter -= 1 if arrow_counter - 1 >= 0 else 0
    clear_line(w)
    
    new_cmd = prev_cmds[arrow_counter]

    w.addstr(prompt, curses.color_pair(curses_colors["YELLOW"]))
    w.addstr(new_cmd)

    return new_cmd

##################################################################
# window scroll buttons side '+' and '-'
##################################################################

scroller = 0

def scroll_up(cmd:str, w, **kwargs):
    '''
    scrolls the window 'up', increments the y axis by one
    use the 'Page up' button to scroll up
    '''
    y, x = w.getyx()
    w_height, w_width = kwargs["curses_w"].getmaxyx()

    global scroller

    scroller += 1

    refresh_y = y - scroller if y - scroller > 0 else 0
    
    w.refresh(refresh_y, 0, 0, 0, w_height - 1, w_width - 1)
    
    return cmd

def scroll_down(cmd:str, w, **kwargs):
    '''
    scrolls the window 'down', decrements the y position by one
    use the 'Page Down' button to scroll down
    '''
    
    y, x = w.getyx()
    w_height, w_width = kwargs["curses_w"].getmaxyx()

    global scroller
    scroller -= 1

    refresh_y = y - scroller if y - scroller > 0 else 0
    
    w.refresh(refresh_y, 0, 0, 0, w_height - 1, w_width - 1)
    
    return cmd


##################################################################
# enter_key sends the currently typed command to execute for
# processing the command properly
##################################################################


def enter_key(cmd: str, w, **kwargs):
    '''
    executes the command
    '''
    #time.sleep(1)
    global prev_cmds
    prev_cmds.insert(0, cmd)
    result = execute(cmd, w) if cmd != "" else None
    
    temp = [x for x in prev_cmds if x != ""]
    prev_cmds = temp

    set_the_shell(w)

    return "" # reset the command in shell


def tab_button(cmd: str, w, **kwargs):
    '''
    TODO: implement auto complete
    '''

    directory = os.listdir(os.getcwd())

    # find the being typed file at the end of the command, reconstruct after
    temp = cmd.split()
    #print(temp[-1])
    file_name = temp[-1]
    return_cmd = cmd

    for path in directory:
        # print(f"path: ({path})")
        if file_name in path:
            return_cmd = cmd[:-len(file_name)] + path
            # print(f"return_cmd: {return_cmd}")
    
    clear_line(w)
    w.addstr(prompt, curses.color_pair(curses_colors["YELLOW"]))
    w.addstr(return_cmd)


    return return_cmd


nav_mapper = {
    curses.KEY_UP: up_arrow,        #259
    curses.KEY_DOWN: down_arrow,    #258
    curses.KEY_LEFT: left_arrow,    #260
    curses.KEY_RIGHT: right_arrow,  #261
    10: enter_key,
    8: backspace_key,               # windows
    263: backspace_key,             # ubuntu
    127: backspace_key,             # ubuntu server
    curses.KEY_PPAGE: scroll_up,
    curses.KEY_NPAGE: scroll_down,
    9: tab_button
}
