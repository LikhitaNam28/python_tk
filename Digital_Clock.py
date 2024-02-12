from tkinter import *
from time import strftime
mw=Tk()
mw.title("DIGITAL CLOCK")
mw.minsize(470,100)
mw.maxsize(470,100)
def good_time():
    cur_time=strftime("%I:%M:%S %p")
    Lbl.config(text=cur_time)
    Lbl.after(1000,good_time)


Lbl=Label(mw,text="DIGITAL CLOCK",font=("",60),bg="black",fg="green")
Lbl.pack()
good_time()

mw.mainloop()
