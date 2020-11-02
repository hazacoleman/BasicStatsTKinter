# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 16:26:50 2020

@author: hazac
"""

import tkinter as tk
from tkinter import filedialog, Text
from tkinter import*
from tkinter import ttk

# def retrieve():
#     print(combo.get())


# class Giants_player():
#     def __init__(self, name, jerseynum, ppg):
#         self.name = name
#         self.jerseynum = jerseynum
#         self.ppg= ppg
        
#     def get_name(self):
#         print(f"This players name is {self.name}.") # "f" allows me to use {self.name}
    
#     def get_jerseynum(self):
#         print(f"This players jersey number is {self.jerseynum}.")
    
#     def change_jerseynum(self, jerseynum):
#         self.jerseynum = jerseynum
        
#     def get_ppg(self):
#         print(f"This players PPG is {self.ppg}.")


def player_selection():
    
    if combo.get() == "Harry":
        var.set(Giants_players[0])
    elif combo.get() == "Jayden":
        var.set(Giants_players[1])
    elif combo.get() == "Cran":
        var.set(Giants_players[2])
    elif combo.get() == "Muca":
        var.set(Giants_players[3])
    else:
        var.set("Please Select a Player")
    
    
    
Giants_players = [
    ("Harry, #32, 20 ppg"),
    ("Jayden, #16, 18 ppg"),
    ("Cran, #12, 10 ppg"),
    ("Muca, #48, 5 ppg")
    ]

# g1 = Giants_player("Harry", 32, 20.1)
# g2 = Giants_player("Jayden", 16, 18)
# g3 = Giants_player("Cran", 12, 10)
# g4 = Giants_player("Muca", 48, 5)

root =tk.Tk()
root.title('Giants Players Information')
root.configure(background='#d47313')

playerlist = ["Harry", "Jayden", "Cran", "Muca"]

canvas = tk.Canvas(root, height = 200, width=300, bg="#d47313") #creates a workable canvas to put stuff on (attach to root)
canvas.pack()

frame = tk.Frame(root, bg="black") #make frame
frame.place(relwidth=0.8, relheight=0.70, relx=0.1, rely=0.1) #places frame in specific spot (relx and y distance from border)



Button = Button(root, text = "Get Player Info",padx=10, 
                     pady=5, fg="white", bg="black", command = player_selection )
Button.pack(padx = 5, pady = 5)

# label = tk.Label(frame, text=app)
# label.pack() #displays the text of where the apps are

combo = ttk.Combobox(frame,   values = playerlist)
combo.set("Pick a Player")
combo.pack(padx = 15, pady= 15)

var= StringVar() #Need to do this to convert label so i can change it above
label = tk.Label(frame, textvariable=var, bg="black", fg="white")
label.config(font=(50))
label.pack()

# g1.get_name()
# g1.get_jerseynum()
# g1.get_ppg()

root.mainloop()    