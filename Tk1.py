from tkinter import *
from tkinter.ttk import *
a=Tk()
a.title("My first Window")
p1 = PhotoImage(file = 'C:\\Users\\likhi\\Downloads\\download.png') 
  
# Setting icon of master window 
a.iconphoto(False, p1) 
a.geometry("500x500")
a.mainloop()
