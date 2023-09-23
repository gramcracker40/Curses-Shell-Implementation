import curses
import time

def main(stdscr):
    stdscr.clear()
    curses.mousemask(1)

    # Define the dimensions of your window
    height, width = stdscr.getmaxyx()
    window_height = height - 2  # Leave space for status line at the bottom

    # Create a scrolling window
    window = curses.newpad(10000, width)  # Adjust the number of rows as needed
    window.scrollok(True)
    pad_pos = 0


    window.addstr(pad_pos, 0, f"This is line {pad_pos}. \n")
    window.refresh(pad_pos, 0, 1, 0, window_height, width - 1)
    pad_pos += 1
    
    while True:
        # Generate some text
        
        # for i in range(1000):  # Append some content to the line
        #     text += f"Lorem ipsum dolor sit amet, consectetur adipiscing elit. \n"

        # Add the text to the scrolling window

        key = window.getch()
        curs = window.getyx()


        refresh_y = curs[0] - height if pad_pos - height > 0 else 0

    
        # _, mx, my, _, _ = curses.getmouse()
        # y, x = window.getyx()
        # window.addstr(y, x, window.instr(my, mx, 5))
        

        if key == 43: # right side + button 
            pad_pos += 1
            refresh_y = pad_pos - height if pad_pos - height > 0 else 0
            window.refresh(refresh_y, 0, 1, 0, height - 1, width - 1)
        elif key == 45: # right side - button 
            pad_pos -= 1
            refresh_y = pad_pos - height if pad_pos - height > 0 else 0
            window.refresh(refresh_y, 0, 1, 0, height - 1, width - 1)
        else:
            window.addstr(f"{key}\n")

            window.refresh(refresh_y, 0, 1, 0, height - 1, width - 1)
            pad_pos += 1

        # Check for mouse events
        
            


        #window.refresh(pad_pos, 0, 1, 0, window_height, width - 1)

        # Sleep for a moment to control the scrolling speed

        # Check if we reached the end of the scrolling window
        # if pad_pos + window_height >= window.getyx()[0]:
        #     pad_pos -= 1


if __name__ == "__main__":
    curses.wrapper(main)












# #WORKS
# import re
# curs = [1, 3]
# cmd = "asdfgh"

# temp1 = cmd[:curs[0]]
# temp2 = cmd[curs[0] + 1:]
# temp = cmd[:curs[0]] + cmd[curs[0] + 1:]

# # print(temp1)
# # print(temp2)
# # print(temp)

# # Sample input string
# input_string = "This is a command < input.txt and this is < hello.txt another command > output.txt"

# # Define the regex pattern
# pattern1 = r'([<>])\s+(\S+)'

# # Find matches in the input string
# matches = list(re.finditer(pattern1, input_string))

# for match in matches:
#     symbol, file_name = match.groups()
#     start_index = match.start()
#     end_index = match.end()

#     print(f"Symbol: {symbol} FileName: {file_name} Start: {start_index} End: {end_index}")




# # Sample input string
# input_string = "This is a -f command < input.txt and this is another command < output.txt"

# # Define the regex pattern
# pattern = r'[<>]\s+\S+'

# # Use re.sub() to remove the pattern
# cleaned_string = re.sub(pattern, '', input_string)

# print(cleaned_string)
