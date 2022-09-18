# Imports

import os
from tkinter import Button, Entry, Frame, Label, Tk, font, messagebox
from tkinter.tix import *

# Changing the directory to where the file is.
os.chdir("Projects//Python//Minor Projects//01 Astrologer's Stars//GUI")

def Show(a):
    """Function to show the stars."""

    global b, n

    try:
        int(en1.get())
    except Exception as e:
        if len(en1.get()) == 0:
            messagebox.showerror("Error", "Please enter a number.")
        else:
            messagebox.showerror("Error", "Please enter a valid number.")
    
    try:
        int(en2.get())
    except Exception as e:
        if len(en2.get()) == 0:
            messagebox.showerror("Error", "Please enter a number.")
        else:
            messagebox.showerror("Error", "Please enter a valid number.")
    
    if int(en1.get())<=0 or int(en2.get())<0:
        messagebox.showerror("Error", "Please enter a positive number.")
    
    else:

        try:
            n = int(en1.get())
            b = int(en2.get())
            b = bool(b)

        except Exception as e:
            messagebox.showerror("Error", str(e))
        
        top1 = Toplevel(root1)

        top1.title("Stars Output")

        try:
            top1.iconbitmap("Images//Goodstuff-No-Nonsense-Free-Space-Stars.ico")
        except Exception as e:
            messagebox.showerror("Error", "icon.ico not found.")
        
        top1.geometry("500x500")
        top1.minsize(200, 200)
        top1.maxsize(850, 700)

        txt1 = Text(top1, relief=RIDGE, borderwidth=5, width=100, height=100)
        txt1.pack(padx=20, pady=10)

        v = list(range(1, n+1))

        if not b:
            v.reverse()
        
        for i in v:
            txt1.insert(END, "*"*i + "\n")


if __name__ == '__main__':
    """The Main Function Begins."""

    root1 = Tk()                                                                # Creating main window root1.

    root1.title("Astrologer's Stars")                                           # Setting the title of root1.

    # Trying to Add Icon to window.
    try:
        root1.iconbitmap("Images//Goodstuff-No-Nonsense-Free-Space-Stars.ico")

    except Exception as e:
        messagebox.showerror("Error", "Icon not found.")


    # Geometry of root1.

    root1.geometry('500x300')
    root1.minsize(400, 260)
    root1.maxsize(600, 450)

    # Background Color of root 1.

    root1['bg']= 'grey'

    # Heading

    Heading = Label(root1, text="Astrologer's Stars", bd=5, font='Aerial 22 underline', bg='black', fg='white')
    Heading.pack(pady=10, ipadx=10)

    # Creating a frame.

    f1 = Frame(root1, bd = 20)
    f1.pack()

    # Content.

    lb1 = Label(f1, text = "Enter the value of n :", font = "Arial 12")
    lb1.grid(row = 0, column=0, pady=10, ipadx=3)

    tip1 = Balloon()
    tip1['bg']='white'

    en1 = Entry(f1, font="Areal 12")
    en1.grid(row=0,column=1, pady=10)

    tip1.bind_widget(en1, balloonmsg = "Enter the value of n(Integer)")

    lb2=Label(f1, text="Enter the bool :", font="Areal 12")
    lb2.grid(row=1,column=0, pady=10)

    tip2 = Balloon()
    tip2['bg']='white'

    en2 = Entry(f1, font = "Areal 12")
    en2.grid(row=1, column=1, pady=10)
    en2.bind("<Return>", Show)

    tip2.bind_widget(en2, balloonmsg=" Enter the value of bool(1 or 0)")

    tip3 = Balloon()
    tip3['bg']='white'

    bt1 = Button(f1,text = "Show", cursor='hand2', font="Arial 12")
    bt1.grid(row=2, columnspan=2, pady=10, ipadx=7)

    bt1.bind("<Button-1>", Show)

    tip3.bind_widget(bt1, balloonmsg="Click to view the Pattern.")




    root1.mainloop()
