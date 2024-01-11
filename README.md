---

# Shell Implementation in Curses/Python

## Overview
This project provides a custom shell implementation using the curses library in Python. It is designed to run on Linux systems and has been tested on Ubuntu. This shell offers a range of commands and showcases the capabilities of curses windows and pads, going beyond basic single-windowed examples found in GeeksforGeeks tutorials on this stuff. The docs on this module don't offer many examples on usage, and everytime I looked up anything for the curses module in python I was met with pure disappointment for the project already made. The shell is pretty cool and can be taken to new heights pretty quickly because it is super easy to add new commands, simply go to the cmd_pkg directory. 

## Installation and Usage
1. Clone the repository to your local machine.
2. Run the shell using the following command:
   ```
   python3 shell_loop.py
   ```

## Features
- **Custom Command Parsing:** The parsing method applied to commands is unique. Detailed explanations of the parsing logic are available in `Execute.py`.
- **Curses Library Usage:** Demonstrates advanced uses of curses windows and pads. Relevant code is found in `loop_helpers.py`, `window_helpers.py`, and `shell_loop.py`.
- **Command Execution Logic:** Implemented in `cmd_pkg_use` and `Execute.py`.

## Available Commands
- **Basic Navigation and File Management:** `ls`, `cd`, `mkdir`, `rmdir`, `touch`, `cp`, `mv`, `rm`
- **File Content Manipulation:** `cat`, `grep`, `sort`, `head`, `tail`, `wc`
- **System and Permissions:** `pwd`, `chmod`, `history`, `exit`
- **Examples:** Each command supports various flags and arguments. For example:
  - `grep keyword file.txt`
  - `cat file1 file2 > file3`
  - `ls -lah`
  - `chmod 777 file.txt`

## Getting Started
- To understand the shell's functionalities and command handling, type `help` after starting the shell. This will provide detailed information on command processing, pipe handling, redirections, and flag interpretations.

## Contributing
- Contributions to enhance the shell, add new features, or improve documentation are welcome. Please follow standard GitHub pull request procedures.

## Acknowledgments
- This project aims to contribute to the community by providing a detailed example of a shell implementation using curses in Python, addressing the lack of comprehensive resources on this topic across the internet and official documentation.

---
