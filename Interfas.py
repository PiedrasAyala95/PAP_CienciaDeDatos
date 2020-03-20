# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 13:54:04 2020

@author: Piedras
"""
from tkinter import *
from PIL import ImageTk,Image
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import Mylib as mylib
import sqlite3

root = Tk()
root.title('PAP_CENACE- Clima')
root.geometry("400x400")

con = sqlite3.connect('bdAmeca.db')
cursorObj = con.cursor()

# Drop Down Boxes

def show():
	myLabel = Label(root, text=clicked.get()).pack()

options = [
	"Monday", 
	"Tuesday", 
	"Wednesday", 
	"Thursday", 
	"Friday",
	"Saturday"
]	

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()


root.mainloop()









