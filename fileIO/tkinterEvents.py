# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:31:59 2019

@author: marshall
"""
#https://www.tutorialspoint.com/python3/python_files_io.htm
#To read the current value of such a variable, call the method get().
#The value of such a variable can be changed with the set() method.
from tkinter import *
from tkinter import ttk


# ---------- TKINTER EVENTS  ----------
 
def get_sum(event):
 
    # Get the value stored in the entries
    num1 = int(num1Entry.get())
    num2 = int(num2Entry.get())
    sum = num1 + num2
    
    # Delete the value in the entry
    sumEntry.delete(0, "end")
 
    # Insert the sum into the entry
    sumEntry.insert(0, sum)
 
root = Tk()

Label(root, text="Entry field")#.grid(row=0, column=0, sticky=W)

num1Entry = Entry(root)
num1Entry.pack(side=LEFT)
 
Label(root, text="+").pack(side=LEFT)
 
num2Entry = Entry(root)
num2Entry.pack(side=LEFT)
 
equalButton = Button(root, text="=")
 
# When the left mouse button is clicked call the
# function get_sum
equalButton.bind("<Button-1>", get_sum)
 
equalButton.pack(side=LEFT)
 
sumEntry = Entry(root)
sumEntry.pack(side=LEFT)
 
root.mainloop()
 
    
    
