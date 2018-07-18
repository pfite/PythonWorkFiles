import tkinter
from tkinter import ttk
from tkinter import * 
from tkinter.scrolledtext import ScrolledText

import codecs



parts = []
f = open('pole_choices.txt','r')
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
 
root = Tk()
root.title("Intersection Pole Generator")

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
height = ''

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

#root.iconbitmap('sec.ico')
 
# Create a Tkinter variable

#row 1
tkvar_color = StringVar(root)
tkvar_length = StringVar(root)
tkvar_upright = StringVar(root)
tkvar_bplate = StringVar(root)
tkvar_peds = StringVar(root)
tkvar_height = StringVar(root)
tkvar_hdcnt = StringVar(root)



pole_name = ttk.Entry(mainframe, width =8) # set the default option
ttk.Label(mainframe, text= "Pole Name").grid(row = 1, column = 0)
pole_name.grid(row = 2, column = 0)
 
# Dictionary with options
pole_color = sorted({ '', 'Galv', 'Black'})
tkvar_color.set('')  # set the default option
popup_color = ttk.OptionMenu(mainframe, tkvar_color, *pole_color)
ttk.Label(mainframe, text= "Pole Color").grid(row = 1, column = 2)
popup_color.grid(row = 2, column = 2)




tkvar_length.set('') # set the default option
ttk.Label(mainframe, text= "Mast Arm Length").grid(row = 1, column = 3, padx =1)

tkvar_upright.set('')
ttk.Label(mainframe, text= "Upright").grid(row = 1, column = 4)

tkvar_bplate.set('')
ttk.Label(mainframe, text= "Back Plate Size - Inches").grid(row = 1, column = 5)



pole_height = ttk.Entry(mainframe, width =8) # set the default option
ttk.Label(mainframe, text= "Mast Arm Height -ft").grid(row = 1, column = 6, padx = 12)
pole_height.grid(row = 2, column = 6)

pole_hdcnt = sorted({'0','1', '2', '3', '4', '5' })
tkvar_hdcnt.set('0') # set the default option
popup_hdcnt = ttk.OptionMenu(mainframe, tkvar_hdcnt, *pole_hdcnt)
ttk.Label(mainframe, text= "SH Count").grid(row = 1, column = 1)
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
   

    delete_lines(sh_arr)
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
        sh_arr.append('sh_' + str(i + 1))
        sh_label.append('sh_' + str(i + 1))
        sh_arr[i] = Entry(mainframe, width =8) # set the default option
        sh_label[i] = Label(mainframe, text= "SH " + str(i + 1) + " Name")
        sh_label[i].grid(row = 4 + i, column = 0)
        sh_arr[i].grid(row = 4 + i, column = 1)

        sh_type.append(sorted({ '130', '130A3 LEFT', '130A3 RIGHT', '140A1 LEFT', '140A1 RIGHT', '150A2H LEFT', '150A2H RIGHTt', '150A4H'}))
        tkvar.append(StringVar(root))
        tkvar[i].set('130') # set the default option
        sh_popup.append(OptionMenu(mainframe, tkvar[i], *sh_type[i]))
        sh_type_label.append(Label(mainframe, text= "SH Type"))
        sh_type_label[i].grid(row = 4 + i, column = 2)
        sh_popup[i].grid(row = 4 + i, column = 3)

        sh_dist.append('sh_place_' + str(i + 1))
        sh_dist_label.append('sh_place_' + str(i + 1))
        sh_dist[i] = Entry(mainframe, width =8) # set the default option
        sh_dist_label[i] = Label(mainframe, text= "Placement Distance -ft:")
        sh_dist_label[i].grid(row = 4 + i, column = 4)
        sh_dist[i].grid(row = 4 + i, column = 5)



    
 
# link function to change dropdown
tkvar_color.trace('w', change_dropdown)
tkvar_height.trace('w', change_dropdown)
tkvar_hdcnt.trace('w', change_dropdown)

def getVals():
    pName = pole_name.get()
    color = tkvar_color.get()
    length = tkvar_length.get()
    up = tkvar_upright.get()
    plate = tkvar_bplate.get()
    height = pole_height.get()
    print(pName)
    print(color)
    print(length)
    print(plate)
    print(height)
    
    for i in range(0, len(sh_dist)):
        thisSH = []
        thisSH.append(sh_arr[i].get())
        if tkvar_color.get() == 'Galv':
            sig_galv = GALV_parts[3]
            for j in range(0, len(sig_galv)):
                if (str(tkvar[i].get()) + ' ') in sig_galv[j]:
                    thisSH.append(sig_galv[j])
        elif tkvar_color.get() == 'Black':
            sig_black = BLACK_parts[4]
            for k in range(0, len(sig_black)):
                if (str(tkvar[i].get()) + ' ') in sig_black[k]:
                    thisSH.append(sig_black[k])

        thisSH.append(sh_dist[i].get())
        SH.append(thisSH)
        print(SH[i])
        '''
        print(tkvar[i].get())
        print(sh_arr[i].get())
        print(sh_dist[i].get())
        '''
    mast_arm = length
    upright = up
    backplate = plate
    signal_head = '1003-ASSY - YELLOW - 130 SIGNAL HEAD W'
    text = pName
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

    for i in range(0, sh_dist):
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





    

        



b = ttk.Button(mainframe, text="Generate CAD Script", command = getVals)
b.grid(column = 3, columnspan = 2, row = 10)



               



 
root.mainloop()
