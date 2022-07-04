from decimal import MIN_ETINY
import pandas as pd
from tkinter import *
import sys
import time


v = Tk()
v.title('Morrón Trail Run Times')
v.configure(background='white')
v.geometry('1200x600')
v.iconbitmap()

#Button(v,text='Play').pack()
v.grid_rowconfigure(0, weight=1)
v.grid_columnconfigure(0, weight=1)
frame = Frame(v, height=500, width=500, background='black')
frame.grid(row=0, column=0,rowspan=2, columnspan=2)
clock = Label(v,font=('times',50,'bold'))
clock.grid(row=3,column=6, padx=10, pady=10)

fecha = Label(v,text=time.strftime("%a  %d  %b "),font='Arial 24 bold')
fecha.grid(row=1,column=6, padx=10, pady=150)


frame2 = Frame(v)
frame2.configure(width=200, height=400)
frame2.grid(row= 4, column= 0, columnspan=6)

def times():
    current_time= time.strftime("%H:%M:%S")
    clock.config(text=current_time,font="Arial 50 bold")
    clock.after(200,times)
times()
v.mainloop()