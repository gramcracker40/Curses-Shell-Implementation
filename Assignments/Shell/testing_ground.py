#WORKS
curs = [1, 3]
cmd = "asdfgh"

temp1 = cmd[:curs[0]]
temp2 = cmd[curs[0] + 1:]
temp = cmd[:curs[0]] + cmd[curs[0] + 1:]

print(temp1)
print(temp2)
print(temp)
