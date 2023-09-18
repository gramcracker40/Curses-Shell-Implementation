#WORKS
import re
curs = [1, 3]
cmd = "asdfgh"

temp1 = cmd[:curs[0]]
temp2 = cmd[curs[0] + 1:]
temp = cmd[:curs[0]] + cmd[curs[0] + 1:]

# print(temp1)
# print(temp2)
# print(temp)

# Sample input string
input_string = "This is a command < input.txt and this is < hello.txt another command > output.txt"

# Define the regex pattern
pattern1 = r'([<>])\s+(\S+)'

# Find matches in the input string
matches = list(re.finditer(pattern1, input_string))

for match in matches:
    symbol, file_name = match.groups()
    start_index = match.start()
    end_index = match.end()

    print(f"Symbol: {symbol} FileName: {file_name} Start: {start_index} End: {end_index}")




# Sample input string
input_string = "This is a -f command < input.txt and this is another command < output.txt"

# Define the regex pattern
pattern = r'[<>]\s+\S+'

# Use re.sub() to remove the pattern
cleaned_string = re.sub(pattern, '', input_string)

print(cleaned_string)
