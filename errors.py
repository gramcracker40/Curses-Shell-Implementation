from window_helpers import clear_line

class CommandDoesNotExist(Exception):
    def __init__(self, message):
        super().__init__(message)
        

class FlagDoesNotExist(Exception):
    def __init__(self, message):
        super().__init__(message)


class InvalidArgument(Exception):
    def __init__(self, message):
        super().__init__(message)


def display_error(w, err):
    clear_line(w)
    w.addstr(f"An error occurred\n{err}\n")