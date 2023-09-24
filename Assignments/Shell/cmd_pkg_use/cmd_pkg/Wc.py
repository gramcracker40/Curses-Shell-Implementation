
def wc(*args, **kwargs):
    '''
    \n given input, find the number of lines, words or characters.
    \n - \n -
    \n wc file.txt -l
    \n - \n -
    \n 
    \n Flags: 
    \n  -l: number of lines in file
    \n  -m: number of characters
    \n  -w: number of words
    '''

    try:
        data = kwargs['options']['input_data']
        flags = kwargs['options']['flags']
        args = kwargs['options']['args'] if kwargs['options']['args'] else []

        if len(args) > 0: ### if a file is passed as an arg, truncate any pipes or input redirects
            data = open(args[0], 'r').readlines()
        
        #lines, characters, words
        l, m, w = 0, 0, 0
        
        if type(data) == list:
            l = len(data)

            for each in data:
                m += len(each)
                w += len(each.split())

        elif type(data) == str:
            l = len(data.split('\n'))
            m = len(data)            
            w = len(data.split())
            
        elif data == None and len(args) == 0:
            return f"wc: no input data... Pipe command values or open input streams for wc to work with"

        if "l" in flags:
            return str(l)
        elif "m" in flags:
            return str(m)
        elif "w" in flags:
            return str(w)
        else:
            return f"flag the desired value you would like wc to return, pass -h for help on wc"


    except FileNotFoundError as err:
        return f"File not found -> {err}"
