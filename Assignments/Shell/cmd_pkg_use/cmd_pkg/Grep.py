from cmd_pkg.cmd_helpers import check_for_help_flag

@check_for_help_flag()
def grep(*args, **kwargs):
    '''given a keyword, search a file or files for the number of occurences of the specified keyword
    \n grep 'keyword' file1.txt file2.txt fileN.txt
    \nFLAGS: 
    \n  -l: only return the file names of where the pattern is found
    \nRETURN:
    \n  int: number of occurences of keyword in given files
    \n  str: file names where keyword exists, only on -l flag'''
    
    args = kwargs['options']['args']
    flags = kwargs['options']['flags']
    
    try:
        keyword = args[0]
        files = []
        lines = []
        if len(args) >= 2:
            for arg in args[1:]:
                temp = open(arg, "r").readlines()
                count = 0
                for each in temp:       # grab the line and count of occurences
                    if keyword in each:
                        lines.append(each)
                        count += each.count(keyword)

                if count > 0:
                    files.append(arg)

            return lines if "l" not in flags else files
        else:
            return f"Please pass valid arguments to grep"
        
    except FileNotFoundError as err:
        return f"grep: one of the files specified does not exist"
    except IndexError as err:
        return f"grep: please pass arguments"



    