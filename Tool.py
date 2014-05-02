#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter
from Tkinter import *
from Responsetime import Transaction
from Throughput import *
from Hits import *
from Latency import *

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
		# You can define the size here
        FrameSizeX = 350
        FrameSizeY = 280
        FramePosX = 2
        FramePosY = 1
        self.geometry("%sx%s+%s+%s" % (FrameSizeX,FrameSizeY,FramePosX,FramePosY))
		# You can define whether the window can be resized. It currently disable maximize button
        self.resizable(0,0)

    def initialize(self):
        self.grid()
		# Header of the window
        self.titleLabelVariable = Tkinter.StringVar()
        titleLabel = Tkinter.Label(self,textvariable=self.titleLabelVariable,
                              anchor="w",fg="white",bg="red")
        titleLabel.grid(column=0,row=0,columnspan=2,sticky='EW')
        self.titleLabelVariable.set(u"Enter a website")  
		
		#Text box is defined here
        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=1,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"http://www.google.com")
		
		#defines the botton textbox for result
        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=4,columnspan=2,sticky='EW')
        self.labelVariable.set(u"Hello !")

		# Lisbox and scroll bar is defined here
        self.sbar = Tkinter.Scrollbar(self)
        self.list = Listbox(self, relief="sunken")
        self.list.config(yscrollcommand=self.sbar.set)
        self.list.grid(column=0, row=2)
        self.sbar.grid(column=1,row=2, sticky="NS")
        self.sbar.config(command=self.list.yview)

		#Change the Options in the List
        self.items = ("Average Response Time" , "Peak Response Time","Throughput","Latency Time","Hits")
        for i in range(len(self.items)):
             self.list.insert(i, self.items[i])  

		#Button is defined here
        button = Tkinter.Button(self,text=u"Calculate !",
                                command=self.OnButtonClick)
        button.grid(column=0,row=3)
		
        self.update()
        self.geometry(self.geometry())       
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
        
       
    def OnButtonClick(self):
       
        item1 = self.list.curselection()
        for i in range(len(item1)):
            index = int(item1[0])
		#Checks if Index is defined in the above line, that is selection was done or not.
        if 'index' not in locals():
            self.labelVariable.set( "Input1: "+self.entryVariable.get()+" Input2: "+"No Input selected")
        else:
                    if index==0: Transaction(self.entryVariable.get()).run()
                    elif index==2:getsize(self.entryVariable.get())
                    elif index==3: Transaction3(self.entryVariable.get()).run()
                    elif index==4: Transaction4(self.entryVariable.get()).run()
                 
                 
                 
        self.labelVariable.set( "Input1: "+self.entryVariable.get()+" Input2: "+self.items[index])
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnPressEnter(self,event):
        self.labelVariable.set( self.entryVariable.get()+" (You pressed ENTER)" )
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Web Performance Tool')
    app.mainloop()
