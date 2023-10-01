

def help(*args, **kwargs):
    '''
    \n: Command Syntax\n
    \n: Name : Must be a valid command name listed in help
    \n: Params : Must be a valid parameter listed in the help section of the specified command
    \n            ex: grep keyword file.txt --- valid   --> file.txt must exist
    \n            ex: grfsdc                --- not valid
    \n: Flags : -f -t -tl etc. does not matter on flag placement just ensure the order of your arguments
    \n                        are placed properly. Get passed to the function for proper output
    \n            ex: grep -l keyword -f file.txt
    \n            proper: grep -l -f keyword file
    \n            again, does not matter.

    \n: Pipe  : "|" as much as you want. The shell can parse it
    \n            NOTE: if you do a pipe, the previous cmd's output becomes the piped commands input.
    \n            ex. grep -l error app.log | cat -n > error_summary.txt
            

    \n: Redirects : input: '< file.txt' or  output:'> file.txt'
    \n                input  --> user can specify files they want sent to the function
    \n                output --> user can specify where they want the result of the cmd to be sent
    \n            NOTE: can only do one input and one output redirect per command
    \n ex command: grep keyword input.txt > occurences.txt | cat -n > showcase.txt
    \n\n\t\t Command Structure: NAME - ARGUMENTS - FLAGS - REDIRECTS - PIPES
    \n
    \nCOMMANDS:
    \n
    \n 

    '''
    pass