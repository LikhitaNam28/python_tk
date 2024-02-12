from tkinter import *
from tkinter import messagebox
mw=Tk()
mw.title("Message Box")
mw.geometry('400x300')
def show_msg():
    res=messagebox.askquestion("Message Box","Do you want to save this file?")
    if res=="yes":
        messagebox.showinfo("Message Box","your file is Saved")
    else:
        messagebox.showwarning("Message Box","your file is trashed")
Button(mw,text="Click Me!",command=show_msg,font=('',15)).pack()
mw.mainloop()
