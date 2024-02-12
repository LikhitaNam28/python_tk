from tkinter import *
from tkinter import messagebox
mw=Tk()
mw.title("Login")
mw.geometry("400x300")


def ok():
    user_name=entry1.get()
    password=entry2.get()
    if user_name=="" and password=="":
        messagebox.showinfo("Message Box","Blank is not allowed")
    elif user_name=="Admin" and password=="12345":
        messagebox.showinfo("Message Box","Login is Successful")
    elif user_name!="Admin" or password!="12345":
        messagebox.showinfo("Message Box","Invalid UserName and Password")

        
global entry1,entry2

Lbl1=Label(mw,text="UserName:",fg="red",font=("Arial",14))
Lbl1.grid(row=0,column=0)
entry1=Entry(mw,width=20)
entry1.grid(row=0,column=1)

Lbl2=Label(mw,text="Password:",fg="red",font=("Arial",14))
Lbl2.grid(row=1,column=0)
entry2=Entry(mw,width=20)
entry2.grid(row=1,column=1)
entry2.config(show="*")


B1=Button(mw,text="Login",command=ok)
B1.grid(row=4,column=2)
