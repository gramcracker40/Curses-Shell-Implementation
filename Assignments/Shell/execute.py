from cmd_pkg_use.cmd_pkg import CommandsHelper
import re

ex_cmds = [
    "ls -l",
    "ls -a",
    "ls",
    "pwd",
    "cd",
    "cd ~",
    "cd ..",
    "cp file1 file2",
    "mv file1 file2",
    "rm file.txt",
    "rm -r my_directory",
    "rm *file*",
    "rmdir empty_directory",
    "cat file.txt",
    "cat file1 file2 fileN",
    "less large_file.txt",
    "head -n 10 file.txt",
    "tail -n 20 file.txt",
    "grep keyword file.txt",
    "grep -l error app.log | cat -n > error_summary.txt",
]


commands = CommandsHelper()

capture_flag_pattern = r'\s*(-\w+)\b'
strip_flag_pattern = r'\s*-\w+\b'

def execute(cmd: str):
    """
    parses command/s and formulates correct output

    allows for only one redirect.
    """
    redirect = ">" if ">" in cmd else "<" if "<" in cmd else None
    redirects = cmd.split(redirect) if redirect else None

    command = cmd.strip()
    
    if redirects: # store file info, set command to first portion
        file_info = (redirect, redirects[1])
        command = redirects[0].strip()

    # split the commands if pipe exists
    piping = command.split("|") if "|" in command else command
    
    # parsing out any flags included with the commands
    cmd_obj = {}
    for count, cmd_temp in enumerate(piping):
        cmds_flags = re.findall(capture_flag_pattern, cmd_temp)
        result = re.sub(strip_flag_pattern, '', piping[count])
        piping[count] = result.strip()
        cmd_obj[piping[count].strip()] = cmds_flags

    # run each command, pass the params as args and the flags as kwargs
    for each in cmd_obj:
        parsed = each.split()
        name = parsed[0]
        args = parsed[1:]
        
        run_cmd = commands.exists(name)

        if run_cmd:
            cmd_result = commands.runner(name, args, cmd_obj[each])
        else:
            raise Exception(f"Command '{name}' does not exist")

    
    # 
    
    print(f"Command object: {cmd_obj}")
    
    print(f"Command: {command}")
    

    # formats an object that numbers the commands in order to 
    

    return cmd_obj


test = execute(ex_cmds[-1])

print(test)

print(commands)
