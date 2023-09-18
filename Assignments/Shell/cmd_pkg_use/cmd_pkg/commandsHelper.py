#!/usr/bin/env python
# from cmd_pkg.__init__ import ls, pwd, cat

from cmd_pkg import grep, cat, exit, ls, pwd, help, mkdir

class CommandsHelper(object):
    """

        A helper class that abstracts the general usage of the various commands

        Methods:
            __init__(self)  : initializes the helper class
            __repr__(string): returns a doc string for (help)
            exists (string) : checks if a command existse
            runner (cmd)    : returns a pointer to the correct function
    """
    def __init__(self):
        self.invoke = {}
        self.help = {}
        self.color_options = {}

        self.invoke["grep"] = grep
        self.invoke["cat"] = cat
        self.invoke["ls"] = ls
        self.invoke["exit"] = exit
        self.invoke["pwd"] = pwd
        self.invoke['help'] = help
        self.invoke['mkdir'] = mkdir


        self.color_options["grep"] = [{}]
        self.color_options["cat"] = [{}]
        self.color_options["ls"] = [{"color": "GREEN", "delimeter": "."}]
        self.color_options["exit"] = [{}]
        self.color_options["pwd"] = [{}]

        

    def exists(self, cmd):
        return cmd in self.invoke

    def runner(self, cmd, w, **kwargs):
        '''
        runs a command once a shell user presses 'enter' or 'return'
        '''
        return self.invoke[cmd](w, **kwargs)

    def __repr__(self):
        '''
        Help section of the shell. Shows the list of commands and
        helps explain the shell a little bit. 
        '''
        return f"""
            \n["grep"] = grep(*args, **kwargs) | 
            \n\t{grep.__doc__}
            \n["cat"] = cat(*args, **kwargs)   |
            \n\t{cat.__doc__}
            \n["ls"] = ls(*args, **kwargs)     |
            \n\t{ls.__doc__}
            \n["exit"] = exit(*args, **kwargs) |
            \n\t{exit.__doc__}
            \n["pwd"] = pwd(*args, **kwargs)   |
            \n\t{pwd.__doc__}
        """

    def help(self,cmd):
        return self.invoke[cmd].__doc__





if __name__ == "__main__":
    pass
