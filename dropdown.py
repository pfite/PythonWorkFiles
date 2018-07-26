import tkinter
from tkinter import ttk
from tkinter import * 
from tkinter.scrolledtext import ScrolledText
import os
import codecs

initPath = os.getcwd()
if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

parts = []
f = open('pole_choices.txt','r')
message = f.read()

x = open('parts.txt','r')
x_message = x.read()

parts = x_message.split('\n')
x.close()

y = open('partno.txt','r')
y_message = y.read()

partno = y_message.split('\n')
y.close()

z = open('manu.txt','r')
z_message = z.read()

manu = z_message.split('\n')
z.close()

searchPart = dict(zip(parts, partno))
searchManu = dict(zip(parts, manu))

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
 
root = Tk()
root.title("Intersection Pole Generator 1.0")

def finished(file):
    ttk.Label(mainframe, text = "Finished Generating " + file + " Script!", relief = RAISED,  foreground = "dark green" ,font='Helvetica 12 bold').grid(row = 11, column = 4)
    



sh_arr = []
sh_label = []
sh_type = []
sh_popup = []
sh_type_label = []
tkvar = []
sh_dist = []
sh_dist_label = []

SH = []
name = ''
color = ''
length = ''
plate = ''


def getMast():
    if  tkvar_color.get() == 'Galv':
        pole_length = GALV_parts[0]
        pole_length[0] = ''
    elif tkvar_color.get() == 'Black':
        pole_length = BLACK_parts[0]
        pole_length[0] = ''
    else:
        pole_length = ['']
    return pole_length

def getBP():
    if  tkvar_color.get() == 'Galv':
        pole_bplate = GALV_parts[2]
        pole_bplate[0] = ''
    elif tkvar_color.get() == 'Black':
        pole_bplate = BLACK_parts[3]
        pole_bplate[0] = ''
    else:
        pole_bplate = ['']
    return pole_bplate

def getUpright():
    if  tkvar_color.get() == 'Galv':
        pole_upright = GALV_parts[1]
        pole_upright[0] = ''
    elif tkvar_color.get() == 'Black':
        pole_upright = BLACK_parts[2]
        pole_upright[0] = ''
    else:
        pole_upright = ['']
    return pole_upright


 
# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 10, padx = 70)

root.iconbitmap('sec.ico')

# Create a Tkinter variable

#row 1
tkvar_color = StringVar(root)
tkvar_length = StringVar(root)
tkvar_upright = StringVar(root)
tkvar_bplate = StringVar(root)
tkvar_height = StringVar(root)
tkvar_hdcnt = StringVar(root)
tkvar_ped = StringVar(root)



pole_name = ttk.Entry(mainframe, width =8) # set the default option
ttk.Label(mainframe, text= "Pole Name", font='Helvetica 9 bold').grid(row = 1, column = 0, padx = 10)
pole_name.grid(row = 2, column = 0)
 
# Dictionary with options
pole_color = sorted({ '', 'Galv', 'Black'})
tkvar_color.set('')  # set the default option
popup_color = ttk.OptionMenu(mainframe, tkvar_color, *pole_color)
ttk.Label(mainframe, text= "Pole Color", font='Helvetica 9 bold').grid(row = 1, column = 2)
popup_color.grid(row = 2, column = 2)




tkvar_length.set('') # set the default option
ttk.Label(mainframe, text= "Mast Arm Length", font='Helvetica 9 bold').grid(row = 1, column = 3, padx =5)

tkvar_upright.set('')
ttk.Label(mainframe, text= "Upright", font='Helvetica 9 bold').grid(row = 1, column = 4)

tkvar_bplate.set('')
ttk.Label(mainframe, text= "Back Plate Size - Inches", font='Helvetica 9 bold').grid(row = 1, column = 5)



pole_height = ttk.Entry(mainframe, width =8) # set the default option
ttk.Label(mainframe, text= "Mast Arm Height -ft", font='Helvetica 9 bold').grid(row = 1, column = 6, padx = 12)
pole_height.grid(row = 2, column = 6)

ped_type = sorted({ '', 'Drilled Left', 'Drilled Right', 'None'})
tkvar_ped.set('')  # set the default option
popup_ped = ttk.OptionMenu(mainframe, tkvar_ped, *ped_type)
ttk.Label(mainframe, text= "Ped Heads", font='Helvetica 9 bold').grid(row = 1, column = 7)
popup_ped.grid(row = 2, column = 7)

pole_hdcnt = sorted({'0','1', '2', '3', '4', '5' })
tkvar_hdcnt.set('0') # set the default option
popup_hdcnt = ttk.OptionMenu(mainframe, tkvar_hdcnt, *pole_hdcnt)
ttk.Label(mainframe, text= "SH Count", font='Helvetica 9 bold').grid(row = 1, column = 1, padx =5)
popup_hdcnt.grid(row = 2, column = 1)

def delete_lines(array):
    if len(array) > 0:
        for j in range(0, len(array)):
            array[j].destroy()
            
            
# on change dropdown value
def change_dropdown(*args):

    mast = getMast()
    tkvar_length.set('Choose Mast Arm')
    popup_length = ttk.OptionMenu(mainframe, tkvar_length, *mast)
    popup_length.grid_remove()
    popup_length.grid(row = 2, column = 3)

    upright = getUpright()
    tkvar_upright.set('Choose Upright')
    popup_upright = ttk.OptionMenu(mainframe, tkvar_upright, *upright)
    popup_upright.grid_remove()
    popup_upright.grid(row = 2, column = 4)

    bp = getBP()
    tkvar_bplate.set('Choose Backplate')
    popup_bplate = ttk.OptionMenu(mainframe, tkvar_bplate, *bp)
    popup_bplate.grid_remove()
    popup_bplate.grid(row = 2, column = 5)
   

    #delete_lines(sh_arr)
    delete_lines(sh_label)
    delete_lines(sh_popup)
    delete_lines(sh_type_label)
    delete_lines(sh_dist)
    delete_lines(sh_dist_label)
    del sh_arr[:]
    del sh_label[:]
    del sh_popup[:]
    del sh_type_label[:]
    del sh_label[:]
    del sh_dist[:]
    del sh_dist_label[:]


            
    for i in range(0, int(tkvar_hdcnt.get())):
        #sh_arr.append('sh_' + str(i + 1))
        sh_label.append('sh_' + str(i + 1))
        #sh_arr[i] = Entry(mainframe, width =8) # set the default option
        sh_label[i] = Label(mainframe, text= "SH " + str(i + 1), font='Helvetica 9 bold')
        sh_label[i].grid(row = 4 + i, column = 1)
        #sh_arr[i].grid(row = 4 + i, column = 1)

        sh_type.append(sorted({ '130', '130A3 LEFT', '130A3 RIGHT', '140A1 LEFT', '140A1 RIGHT', '150A2H LEFT', '150A2H RIGHT', '150A4H'}))
        tkvar.append(StringVar(root))
        tkvar[i].set('130') # set the default option
        sh_popup.append(OptionMenu(mainframe, tkvar[i], *sh_type[i]))
        sh_type_label.append(Label(mainframe, text= "SH Type:"))
        sh_type_label[i].grid(row = 4 + i, column = 2)
        sh_popup[i].grid(row = 4 + i, column = 3)

        sh_dist.append('sh_place_' + str(i + 1))
        sh_dist_label.append('sh_place_' + str(i + 1))
        sh_dist[i] = Entry(mainframe, width =8) # set the default option
        sh_dist_label[i] = Label(mainframe, text= "Placement Distance- Inches:")
        sh_dist_label[i].grid(row = 4 + i, column = 4)
        sh_dist[i].grid(row = 4 + i, column = 5)



    
 
# link function to change dropdown
tkvar_color.trace('w', change_dropdown)
tkvar_height.trace('w', change_dropdown)
tkvar_hdcnt.trace('w', change_dropdown)

def getVals():
    pName = pole_name.get()
    color = tkvar_color.get()
    length = str(tkvar_length.get())
    plate = tkvar_bplate.get()
    height = str((int(pole_height.get())*12)-10)
    print(pName)
    print(color)
    print(length)
    print(plate)
    print(height)

    print(length[9:11])

    mast_arm = length
    up = tkvar_upright.get()
    backplate = plate
    text = pName

    chain = []
    commands = []
    f = open('try.txt','r')
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
        elif insert_mast[a] == 'num':
            insert_mast[a] = height
        elif insert_mast[a] == 'part_no':
            insert_mast[a] = searchPart[mast_arm]
    chain.append(insert_mast)

    insert_upright = commands[1]
    line_2 = insert_upright[0].replace('\n', '')
    insert_upright[0] = line_2
    for a in range(0, len(insert_upright)):
        if insert_upright[a] == '"upright"':
            insert_upright[a] = '"' + up + '"'
        elif insert_upright[a] == '\npart_no\n':
            insert_upright[a] = '\n' + searchPart[up] + '\n'
    chain.append(insert_upright)

    insert_bp = commands[2]
    line_3 = insert_bp[0].replace('\n', '')
    insert_bp[0] = line_3
    for a in range(0, len(insert_bp)):
        if insert_bp[a] == '"backplate"':
            insert_bp[a] = '"' + backplate + '"'
        elif insert_bp[a] == 'num':
            insert_bp[a] = height
        elif insert_bp[a] == '\npart_no\n':
            insert_bp[a] = '\n' + searchPart[backplate] + '\n'
    chain.append(insert_bp)

    peds = ''
    if tkvar_ped.get() != 'None':
        if tkvar_ped.get() == "Drilled Left":
            insert_ped = commands[4]
        elif tkvar_ped.get() == "Drilled Right":
            insert_ped = commands[5]
        line_6 = insert_ped[0].replace('\n', '')
        insert_upright[0] = line_6
        if tkvar_color.get() == 'Galv':
            if tkvar_ped.get() == "Drilled Left":
                peds = 'PEDESTRIAN SIGNAL HEAD-YELLOW-DRILLED LEFT'
            elif tkvar_ped.get() == "Drilled Right":
                peds = 'PEDESTRIAN SIGNAL HEAD-YELLOW-DRILLED RIGHT'
        elif tkvar_color.get() == 'Black':
            if tkvar_ped.get() == "Drilled Left":
                peds = 'PEDESTRIAN SIGNAL HEAD-BLACK-DRILLED LEFT'
            elif tkvar_ped.get() == "Drilled Right":
                peds = 'PEDESTRIAN SIGNAL HEAD-BLACK-DRILLED RIGHT'
        for a in range(0, len(insert_ped)):
            if insert_ped[a] == '"ped_head"':
                insert_ped[a] = '"' + peds + '"'
            elif insert_ped[a] == 'part_no':
                insert_ped[a] == searchPart[peds]
            elif insert_ped[a] == 'part_no\n':
                insert_ped[a] == searchPart[peds] + '\n'
            elif insert_ped[a] == '\npart_no\n':
                insert_ped[a] == '\n' + searchPart[peds] + '\n'
        print(insert_ped)
        insert_ped[14] = '\n' + searchPart[peds]
        insert_ped[-1] = '\n' + searchPart[peds] + '\n'

        chain.append(insert_ped)

    pole_dist = []
    for i in range(0, len(sh_dist)):
        if tkvar_color.get() == 'Galv':
            sig_galv = GALV_parts[3]
            for j in range(0, len(sig_galv)):
                dist = (int(round((int(sh_dist[i].get())*-1) + 2)))
                if (str(tkvar[i].get()) + ' ') in sig_galv[j]:
                    pole_dist.append(str(dist))
                    thisSH = []
                    thisAstro = []
                    signal_head = sig_galv[j]
                    print(signal_head)
                    for k in range(0, len(commands[3])):
                        sh_com = commands[3]
                        insert_astro = commands[-1]
                        if k == 0:
                            thisSH.append('(command')
                            thisAstro.append('(command')
                        elif k == 5:
                            thisSH.append('"' + signal_head + '"')
                            thisAstro.append('"ASTRO BRAC-GALV"')
                        elif k == 9:
                            thisSH.append(str(dist))
                            thisAstro.append(str(dist))
                        elif k == 14:
                            thisSH.append('\n' + searchPart[signal_head] + '\n')
                            thisAstro.append( '\n' +'1021' + '\n')
                        else:
                            thisSH.append(sh_com[k])
                            thisAstro.append(insert_astro[k])
                    chain.append(thisSH)
                    chain.append(thisAstro)
        elif tkvar_color.get() == 'Black':
            sig_black = BLACK_parts[4]
            for j in range(0, len(sig_black)):
                dist = (int(round((int(sh_dist[i].get())*-1) + 2)))
                if (str(tkvar[i].get()) + ' ') in sig_black[j]:
                    pole_dist.append(str(dist))
                    thisSH = []
                    thisAstro = []
                    signal_head = sig_black[j]
                    for k in range(0, len(commands[3])):
                        sh_com = commands[3]
                        insert_astro = commands[-1]
                        if k == 0:
                            thisSH.append('(command')
                            thisAstro.append('(command')
                        elif k == 5:
                            thisSH.append('"' + signal_head + '"')
                            thisAstro.append('"ASTRO BRAC-BLACK"')
                        elif k == 9:
                            thisSH.append(str(dist))
                            thisAstro.append(str(dist))
                        elif k == 14:
                            thisSH.append('\n' + searchPart[signal_head] + '\n')
                            thisAstro.append('\n' + '1020' + '\n')
                        else:
                            thisSH.append(sh_com[k])
                            thisAstro.append(insert_astro[k])
                    chain.append(thisSH)
                    chain.append(thisAstro)

        
        

    insert_text = commands[6]
    line_5 = insert_text[0].replace('\n', '', 1)
    insert_text[0] = line_5
    newName = insert_text[-1].replace('name', text)
    insert_text[-1] = newName
    chain.append(insert_text)

    os.chdir(initPath)
    newFile = open( pName + '.scr', 'w')

    for i in range(0, len(chain)):
        allCommands = chain[i]
        for j in range(0, len(allCommands)):
            if j == len(allCommands) - 1:
                newFile.write(allCommands[j])
            else:
                newFile.write(allCommands[j] + ' ')

    newFile.close()
    finished(pName)
    if getattr(sys, 'frozen', False):
        os.chdir(sys._MEIPASS)





b = ttk.Button(mainframe,text="Generate CAD Script", command = getVals)
b.grid(column = 4, columnspan = 1, row = 10, pady = 12)


               



 
root.mainloop()
