#!/usr/bin/env python
# from cmd_pkg.__init__ import ls, pwd, cat

from cmd_pkg import grep, cat, exit, ls, pwd, \
                mkdir, cd, sort, dir, cp, rm, rmdir, \
                head, tail, touch, wc

class CommandsHelper(object):
    """
        A helper class that abstracts the general usage of the various commands

        Methods:
            __init__(self)  : initializes the helper class
            __repr__(string): returns a doc string for (help)
            exists (string) : checks if a command exists
            runner (cmd)    : returns a pointer to the correct function
    """
    def __init__(self):
        self.invoke = {}
        self.color_options = {}

        self.invoke["grep"] = grep
        self.invoke["cat"] = cat
        self.invoke["ls"] = ls
        self.invoke["exit"] = exit
        self.invoke["pwd"] = pwd
        self.invoke['help'] = self.__repr__
        self.invoke['mkdir'] = mkdir
        self.invoke['cd'] = cd
        self.invoke['sort'] = sort
        self.invoke['dir'] = dir
        self.invoke['cp'] = cp
        self.invoke['rm'] = rm
        self.invoke['rmdir'] = rmdir
        self.invoke['head'] = head
        self.invoke['tail'] = tail
        self.invoke['touch'] = touch
        self.invoke['wc'] = wc

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

    def __repr__(self, w, **kwargs):
        '''
        Help section of the shell. Shows the list of commands and
        helps explain the shell a little bit. 

        look further down, actually returns a list of these string to split off \n
            helps with formatting
        '''
        return f""": Command Syntax\n\n
        \n: Name : Must be a valid command name listed in help
        \n: Arguments : Must be a valid parameter listed in the help section of the specified command
        \n    ex: grep keyword file.txt - valid   --> file.txt must exist
        \n    ex: grfsdc -not valid
        \n: Flags : -f -t -tl etc. does not matter on flag placement just ensure the order of your arguments
        \n        are placed in order according to the command.
        \n    ex: grep -l keyword -f file.txt
        \n    proper: grep -l -f keyword file
        \n         but both work...
        \n 
        \n
        \n: Pipe  : "|" as much as you want. The shell can parse it
        \n            NOTE: if you do a pipe, the previous cmd's output becomes the piped commands input.
        \n            ex. grep -l error app.log | cat -n > error_summary.txt
        \n
        \n: Redirects : input: '< file.txt' or  output:'> file.txt'
        \n       input  --> user can specify files they want sent to the function
        \n       output --> user can specify where they want the result of the cmd to be sent
        \n  NOTE: can only do one input redirect and unlimited output redirects per command
        \n        ex command: grep keyword input.txt > occurences.txt | cat -n > showcase.txt
        \n  NOTE: input redirects will truncate piped commands
        \n - \n - \n 
        Command Structure: NAME - FLAGS - ARGUMENTS - FLAGS - REDIRECTS - PIPES
        \n - \n - \n
        \nCOMMANDS:  'command' -h for more details
        \n["grep"] = grep(*args, **kwargs) | 
        \n{grep.__doc__}
        \n["cat"] = cat(*args, **kwargs)   |
        \n{cat.__doc__}
        \n["ls"] = ls(*args, **kwargs)     |
        \n{ls.__doc__}
        \n["exit"] = exit(*args, **kwargs) |
        \n{exit.__doc__}
        \n["pwd"] = pwd(*args, **kwargs)   |
        \n{pwd.__doc__}
        \n["mkdir"] = mkdir(*args, **kwargs) | 
        \n{mkdir.__doc__}
        \n["cd"] = cd(*args, **kwargs)   |
        \n{cd.__doc__}
        \n["sort"] = sort(*args, **kwargs)     |
        \n{sort.__doc__}
        \n["dir"] = dir(*args, **kwargs) |
        \n{dir.__doc__}
        \n["cp"] = cp(*args, **kwargs) |
        \n{cp.__doc__}
        \n""".split("\n")

    def help(self):
        return self.invoke["help"] # change to wrapper around cmd functions





if __name__ == "__main__":
    pass
