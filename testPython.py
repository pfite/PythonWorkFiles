import tkinter
from tkinter import ttk
from tkinter import * 
from tkinter.scrolledtext import ScrolledText

import codecs


outs = 1
pot = 1
callAmount = 1





def whatToDo():
    line_1 = ''
    line_2 = ''
    line_3 = ''
    if outs_entry.get() != '':
        outs = int(outs_entry.get())
        pot = int(pot_entry.get())
        callAmount = int(callAmount_entry.get())
        line_1 = "Your pot odds are " + str(round((outs/47), 2))
        line_2 = "Your hand equity is " + str(round((callAmount/pot), 2))
        if ((outs/47) > callAmount/pot):
            line_3 = "You should call."
            panel = ttk.Label(content, text = line_1 + '\n' + line_2 + '\n' + line_3).grid(row =5, column = 1)
        else:
            line_3 ="You should fold.\n"
            panel = ttk.Label(content, text = line_1 + '\n' + line_2 + '\n' + line_3).grid(row =5, column = 1)            
    else:
        print('empty')
        panel = ttk.Label(root, text = line_1 + '\n' + line_2 + '\n' + line_3).grid(row=0,column=0, sticky = W, padx = (550,0), pady = (0,150)) 






root = Tk()
content = ttk.Frame(root)
frame = ttk.Frame(content, borderwidth=5, relief="sunken")


content.grid(column=0, row=0, sticky=(N, E), rowspan = 3,)
frame.grid(column=0, row=0, columnspan=10, rowspan=10, sticky = (N,W))

one = ttk.Label(content, text="Outs: ").grid(row=0, sticky =W)
two = ttk.Label(content, text="Pot: ").grid(row=1, sticky=W)
three = ttk.Label(content, text="Amount to call ").grid(row=2, pady = (40,5),sticky = W)
four = ttk.Label(content, text=" ").grid(row=3, sticky = W)
five = ttk.Label(content, text=" ").grid(row=4, sticky = W)


outs_entry       = ttk.Entry(content, width = 25)
pot_entry        = ttk.Entry(content, width = 25)
callAmount_entry = ttk.Entry(content, width = 25)
Subject = ttk.Entry(content, width = 60)
MessageBody = Text(content, height = 8)

outs_entry.grid(row=0, column=1, pady = (10,5), sticky = W)
pot_entry.grid(row=1, column=1,sticky = W)
callAmount_entry.grid(row=2, column= 1, pady = (40,5), sticky = W)
Send = Button(content, text = "Should I fold?", width = 20, bg = "grey", command = whatToDo)
Send.grid(row =6, column = 1, pady = (0,10))

root.mainloop()
