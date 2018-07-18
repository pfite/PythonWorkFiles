'''
commands = []
f = open('C:/Users/peytonfite/Desktop/Python/try.txt','r')
message = f.read()

arr = message.split('**')

for i in range(0,len(arr)):
    step = arr[i].split(' ')
    commands.append(step)

print(commands[0])
'''
parts = []
f = open('C:/Users/peytonfite/Desktop/GitPush/pole_choices.txt','r')
message = f.read()

color_choice = message.split('***')
GALV = color_choice[1]
BLACK = color_choice[2]

GALV_categ = GALV.split('**')
BLACK_categ = BLACK.split('**')
BLACK_parts = []
GALV_parts = []

for i in range(0, len(GALV_categ)):
    cat = GALV_categ[i].split('\n')
    GALV_parts.append(cat)
for j in range(0, len(BLACK_categ)):
    cat = BLACK_categ[j].split('\n')
    BLACK_parts.append(cat)
del BLACK_parts[0]
del GALV_parts[0]
print(sorted(BLACK_parts[4]))


