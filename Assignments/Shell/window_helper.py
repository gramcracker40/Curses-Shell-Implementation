def clear_line(w):
    '''
    helper function to move cursor to beginning and 
    clear all text on the current line to be rerendered
    '''
    curs = w.getyx()
    w.move(curs[0], 0)
    w.clrtobot()
    w.refresh()