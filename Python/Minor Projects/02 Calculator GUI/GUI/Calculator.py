# Program to create a GUI-based calculator.

# Importing the required modules.
import os
import sys
from PIL import Image
from tkinter import *
from tkinter import messagebox
from tkinter.tix import *


# creating a path for the icon of the window.
def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller."""

    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

path = resource_path("./Icon//Icon.ico")


def btn(e):
    """Defining a function to perform functions
        when any of the button is pressed."""

    global val                                                                                                          # Defining a global variable.

    text = e.widget.cget("text")

    # If '=' button is pressed calculating the result.
    if text == "=":

        # If the input is valid, calculate the result.
        if val.get().isdigit():                                                                                        # If the input is a number evaluate the arithmetic expression.

            try:
                value = eval(val.get())
            except Exception as exp:
                messagebox.showerror("Error", "Error! : " + str(exp))
                value = "Error"
        
        else:                                                                                                          # If the input is not a number evaluate the expression in the screen.
            try:
                value = eval(cal_screen.get())
            except Exception as exp:
                value = "Error"
                messagebox.showerror("Error", "Error! : " + str(exp))

        val.set(value)                                                                                                  # Setting the value of entry box to the result.
        cal_screen.update()                                                                                             # Updating the Entry box.

    # If 'C' button is pressed clearing the screen.
    elif text == 'C':
        val.set("")
        root3.update()

    else:
        val.set(str(val.get()) + str(text))
        cal_screen.update()


def equals(n):
    """Defining a function which calculates the
        result when user presses Enter."""

    # Same as '=' condition above.
    if val.get().isdigit():
        try:
            value = eval(val.get())
        except Exception as exp:
            messagebox.showerror("Error", "Error! : " + str(exp))
            value = "Error"
    else:
        try:
            value = eval(cal_screen.get())
        except Exception as exp:
            value = "Error"
            messagebox.showerror("Error", "Error! : " + str(exp))

    val.set(value)
    cal_screen.update()


root3 = Tk()

# Title and icon.
root3.title("Question 3")

try:
    root3.iconbitmap(path)
except Exception as e:
    messagebox.showerror("Error", "icon - \"icon.ico\" not found.")

# Geometry.
root3.geometry('500x650')
root3.minsize(425, 620)

# Background Color.
root3['bg'] = 'grey'

# Heading.
Heading = Label(root3, text="Calculator Program", bd=5, font='Aerial 22 underline', bg='black', fg='white',relief=RAISED)
Heading.pack(pady=10, ipadx=10)

# Content.
val = StringVar()                                                                                                       # val(a String variable for entry box)
val.set("")                                                                                                             # setting val's value to ""
cal_screen = Entry(root3, textvariable=val, font=" Aerial 30 bold", width=19)                                           # cal_screen - Entry box for calculator input.
cal_screen.pack(fill=X, padx=25)
cal_screen.bind('<Return>', equals)

tip1 = Balloon()                                                                                                        # tip1 for suggestions.

tip1['bg'] = 'white'

tip1.bind_widget(cal_screen, balloonmsg="Enter the value using keyboard or buttons below.")

f1 = Frame(root3, bg='LightYellow3')                                                                                    # Frame 1.
f1.pack(pady=10, fill=BOTH, padx=25, side=TOP)

# Creating Buttons.
bt1 = Button(f1, text="C", font="Aerial 25 bold", width=3)
bt2 = Button(f1, text="/", font="Aerial 25 bold", width=3)
bt3 = Button(f1, text="*", font="Aerial 25 bold", width=3)
bt4 = Button(f1, text="-", font="Aerial 25 bold", width=3)
bt5 = Button(f1, text=7, font="Aerial 25 bold", width=3)
bt6 = Button(f1, text=8, font="Aerial 25 bold", width=3)
bt7 = Button(f1, text=9, font="Aerial 25 bold", width=3)
bt8 = Button(f1, text="+", font="Aerial 25 bold", height=4, width=3)
bt9 = Button(f1, text=4, font="Aerial 25 bold", width=3)
bt10 = Button(f1, text=5, font="Aerial 25 bold", width=3)
bt11 = Button(f1, text=6, font="Aerial 25 bold", width=3)
bt12 = Button(f1, text=1, font="Aerial 25 bold", width=3)
bt13 = Button(f1, text=2, font="Aerial 25 bold", width=3)
bt14 = Button(f1, text=3, font="Aerial 25 bold", width=3)
bt15 = Button(f1, text="=", font="Aerial 25 bold", height=4, width=3)
bt16 = Button(f1, text=0, font="Aerial 25 bold", width=8)
bt17 = Button(f1, text=".", font="Aerial 25 bold", width=3)

# Grid Configuring.
Grid.columnconfigure(f1, 0, weight=1)
Grid.columnconfigure(f1, 6, weight=1)

# Griding all the buttons.
bt1.grid(row=0, column=1, padx=10, pady=10)
bt2.grid(row=0, column=2, padx=10, pady=10)
bt3.grid(row=0, column=3, padx=10, pady=10)
bt4.grid(row=0, column=4, padx=10, pady=10)
bt5.grid(row=1, column=1, padx=10, pady=10)
bt6.grid(row=1, column=2, padx=10, pady=10)
bt7.grid(row=1, column=3, padx=10, pady=10)
bt8.grid(row=1, column=4, columnspan=2, rowspan=2, padx=10, pady=10)
bt9.grid(row=2, column=1, padx=10, pady=10)
bt10.grid(row=2, column=2, padx=10, pady=10)
bt11.grid(row=2, column=3, padx=10, pady=10)
bt12.grid(row=3, column=1, padx=10, pady=10)
bt13.grid(row=3, column=2, padx=10, pady=10)
bt14.grid(row=3, column=3, padx=10, pady=10)
bt15.grid(row=3, column=4, columnspan=2, rowspan=2, padx=10, pady=10)
bt16.grid(row=4, column=1, columnspan=2, rowspan=2, padx=10, pady=10)
bt17.grid(row=4, column=3, padx=10, pady=10)

# Binding all the buttons to functions.
bt1.bind("<Button-1>", btn)
bt2.bind("<Button-1>", btn)
bt3.bind("<Button-1>", btn)
bt4.bind("<Button-1>", btn)
bt5.bind("<Button-1>", btn)
bt6.bind("<Button-1>", btn)
bt7.bind("<Button-1>", btn)
bt8.bind("<Button-1>", btn)
bt9.bind("<Button-1>", btn)
bt10.bind("<Button-1>", btn)
bt11.bind("<Button-1>", btn)
bt12.bind("<Button-1>", btn)
bt13.bind("<Button-1>", btn)
bt14.bind("<Button-1>", btn)
bt15.bind("<Button-1>", btn)
bt16.bind("<Button-1>", btn)
bt17.bind("<Button-1>", btn)

root3.mainloop()
