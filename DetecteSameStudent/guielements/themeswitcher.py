# Adding light and dark mode images 
from tkinter import Button, PhotoImage

#Based on this tutorial - https://www.geeksforgeeks.org/light-or-dark-theme-changer-using-tkinter/
#Set default value based on system
#Get the base setting from the system for black and white

img_light = PhotoImage(file="img/light.png") 
img_dark = PhotoImage(file="img/dark.png") 

switch_value = False

#Defining a function to toggle 
#between light and dark theme 
def toggle(app, switch): 
    global switch_value 
    if switch_value == True: 
        switch.config(image=img_dark, bg="#26242f", 
                      activebackground="#26242f") 
        # Changes the window to dark theme 
        app.config(bg="#26242f")   
        switch_value = False
    else: 
        switch.config(image=img_light, bg="white",  
                      activebackground="white") 
       # Changes the window to light theme 
        app.config(bg="white")   
        switch_value = True

def create_theme_switcher(app, px: int, py: int) -> Button:
    # Creating a button to toggle 
    # between light and dark themes
    switch = Button(app, image=img_dark,   
                    bg="#26242f",
                    activebackground="#26242f",
                    command=toggle) 
    switch.pack(padx=py, pady=px) 