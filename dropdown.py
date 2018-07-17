import tkinter
from tkinter import ttk
from tkinter import * 
from tkinter.scrolledtext import ScrolledText

import codecs
 
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
rise = ''
plate = ''
height = ''



 
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
tkvar_rise = StringVar(root)
tkvar_bplate = StringVar(root)
tkvar_peds = StringVar(root)
tkvar_height = StringVar(root)
tkvar_hdcnt = StringVar(root)



pole_name = ttk.Entry(mainframe, width =8) # set the default option
ttk.Label(mainframe, text= "Pole Name").grid(row = 1, column = 0)
pole_name.grid(row = 2, column = 0)
 
# Dictionary with options
pole_color = { 'Galv', 'Black'}
tkvar_color.set('Galv') # set the default option
popup_color = ttk.OptionMenu(mainframe, tkvar_color, *pole_color)
ttk.Label(mainframe, text= "Pole Color").grid(row = 1, column = 1)
popup_color.grid(row = 2, column = 1)

pole_length = sorted({ '25', '30', '35', '40', '45', '50', '55'})
tkvar_length.set('25') # set the default option
popup_length = ttk.OptionMenu(mainframe, tkvar_length, *pole_length)
ttk.Label(mainframe, text= "Mast Arm Length").grid(row = 1, column = 2, padx =1)
popup_length.grid(row = 2, column = 2)

pole_rise = {'5 - default', '3'}
tkvar_rise.set('5 - default') # set the default option
popup_rise = ttk.OptionMenu(mainframe, tkvar_rise, *pole_rise)
ttk.Label(mainframe, text= "Mast Arm Rise").grid(row = 1, column = 3)
popup_rise.grid(row = 2, column = 3)
 
pole_bplate = sorted({'18.75', '20.25', '22.25'})
tkvar_bplate.set('18.75') # set the default option
popup_bplate = ttk.OptionMenu(mainframe, tkvar_bplate, *pole_bplate)
ttk.Label(mainframe, text= "Back Plate Size - Inches").grid(row = 1, column = 4)
popup_bplate.grid(row = 2, column = 4)


pole_height = ttk.Entry(mainframe, width =8) # set the default option
ttk.Label(mainframe, text= "Mast Arm Height -ft").grid(row = 1, column = 5, padx = 12)
pole_height.grid(row = 2, column = 5)

pole_hdcnt = sorted({'0','1', '2', '3', '4', '5' })
tkvar_hdcnt.set('0') # set the default option
popup_hdcnt = ttk.OptionMenu(mainframe, tkvar_hdcnt, *pole_hdcnt)
ttk.Label(mainframe, text= "Signal Head Count").grid(row = 1, column = 6)
popup_hdcnt.grid(row = 2, column = 6)

def delete_lines(array):
    if len(array) > 0:
        for j in range(0, len(array)):
            array[j].destroy()
            
            
# on change dropdown value
def change_dropdown(*args):
    
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

        sh_type.append({ 'Three Section', 'Five Section'})
        tkvar.append(StringVar(root))
        tkvar[i].set('Three Section') # set the default option
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
tkvar_length.trace('w', change_dropdown)
tkvar_rise.trace('w', change_dropdown)
tkvar_bplate.trace('w', change_dropdown)
tkvar_height.trace('w', change_dropdown)
tkvar_hdcnt.trace('w', change_dropdown)

def getVals():
    color = tkvar_color.get()
    length = tkvar_length.get()
    rise = tkvar_rise.get()
    plate = tkvar_bplate.get()
    height = pole_height.get()
    print(color)
    print(length)
    print(rise)
    print(plate)
    print(height)
    
    for i in range(0, len(sh_dist)):
        thisSH = []
        thisSH.append(tkvar[i].get())
        thisSH.append(sh_arr[i].get())
        thisSH.append(sh_dist[i].get())
        SH.append(thisSH)
        print(SH[i])
        '''
        print(tkvar[i].get())
        print(sh_arr[i].get())
        print(sh_dist[i].get())
        '''
    text_file = open("C:/Users/peytonfite/Desktop/Python/Output.txt", "w")
    text_file.write(color + "\n")
    text_file.write(length + "\n")
    text_file.write(rise + "\n")
    text_file.write(plate + "\n")
    text_file.write(height + "\n")
    for k in range(0, len(SH)):
        stuff = SH[k]
        for l in range(0, len(stuff)):
            text_file.write(stuff[l] + ' ')
        text_file.write('\n')
    text_file.close()
        



b = ttk.Button(mainframe, text="Generate CAD Script", command = getVals)
b.grid(column = 3, columnspan = 2, row = 10)



               



 
root.mainloop()
