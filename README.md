# Shell Implementation (Curses/Python) 

  Runs on Linux only. Tested with Ubuntu.
Once you clone the repo, simply type this command and press any key to enter the shell. 

  ### python3 shell_loop.py
![ShellExample](https://github.com/gramcracker40/Curses-Shell-Implementation/blob/main/ShellExample.png)

  First thing to do is type 'help'. This will give you a longwinded explanation of the inner details behind the shell. How I handle pipes, redirects, processing flags, etc.
The parsing method applied to the command is very unique. All those details are found in Execute.py. 

  Wanted to publish this code for the curses library because I found there to be little detail surrounding this style of project within the docs and across the internet. Most were single windowed basic projects that didn't show the nested potential of curses windows and pads. 

  All of the code that uses the `curses` library is found in `loop_helpers.py`, `window_helpers.py`, and `shell_loop.py`. 

  All of the code that implements the command execution and logic is found in `cmd_pkg_use` and `Execute.py`.

### Commands implemented with basic examples
grep    = grep keyword file.txt               |
help    = help                                | 
cat     = cat file1 file2 > file3             |
ls      = ls -lah                             |
exit    = exit                                |            
pwd     = pwd                                 |
mkdir   = mkdir dir1 dir2 dirN                | 
cd      = cd /valid/path/to/change            |
sort    = sort file.txt > sorted_file.txt     |
dir     = dir                                 |
cp      = cp directory1 directory2            |
rm      = rm dir1 dir2 dirN                   | 
rmdir   = rmdir dir1 dir2 dirN                |
head    = head file.txt -n 25                 |
tail    = tail file.txt -n 25                 |              
touch   = touch file1 file2 fileN             |
wc      = wc file1 -l                         |
mv      = mv directory1 directory2            |
history = history                             |
chmod   = chmod 777 file.txt                  |
!       = ! 2                                 |


