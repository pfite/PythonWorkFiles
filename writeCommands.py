mast_arm = '1047-MAST ARM - 25FT GALV - NMPW'
upright = '1073-UPRIGHT-20FT-18IN BC-MNPW-GALV'
backplate = '1026-BACK PLATE-MAST ARM-18.75IN'
signal_head = '1003-ASSY - YELLOW - 130 SIGNAL HEAD W'
text = 'P1-45'
dist = -120

chain = []
commands = []
f = open('C:/Users/peytonfite/Desktop/GitPush/try.txt','r')
message = f.read()
f.close()

arr = message.split('**')

for i in range(0,len(arr)):
    step = arr[i].split(' ')
    commands.append(step)

insert_mast = commands[0]
for a in range(0, len(insert_mast)):
    if insert_mast[a] == '"mast_arm"':
        insert_mast[a] = '"' + mast_arm + '"'
chain.append(insert_mast)

insert_upright = commands[1]
line_2 = insert_upright[0].replace('\n', '')
insert_upright[0] = line_2
for a in range(0, len(insert_upright)):
    if insert_upright[a] == '"upright"':
        insert_upright[a] = '"' + upright + '"'
chain.append(insert_upright)

insert_bp = commands[2]
line_3 = insert_bp[0].replace('\n', '')
insert_bp[0] = line_3
for a in range(0, len(insert_bp)):
    if insert_bp[a] == '"backplate"':
        insert_bp[a] = '"' + backplate + '"'
chain.append(insert_bp)

insert_SH = commands[3]
line_4 = insert_SH[0].replace('\n', '')
insert_SH[0] = line_4
for a in range(0, len(insert_SH)):
    if insert_SH[a] == '"signal_head"':
        insert_SH[a] = '"' + signal_head + '"'
    elif insert_SH[a] == 'num':
        insert_SH[a] = str(dist)
chain.append(insert_SH)

insert_text = commands[-1]
line_5 = insert_text[0].replace('\n', '', 1)
insert_text[0] = line_5
newName = insert_text[-1].replace('name', text)
insert_text[-1] = newName
chain.append(insert_text)


newFile = open('commands.scr', 'w')

for i in range(0, len(chain)):
    allCommands = chain[i]
    for j in range(0, len(allCommands)):
        if j == len(allCommands) - 1:
            newFile.write(allCommands[j])
        else:
            newFile.write(allCommands[j] + ' ')

newFile.close()


    
