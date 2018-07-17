commands = []
f = open('C:/Users/peytonfite/Desktop/Python/try.txt','r')
message = f.read()

arr = message.split('**')

for i in range(0,len(arr)):
    step = arr[i].split(' ')
    commands.append(step)

print(commands[0])


