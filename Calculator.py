from tkinter import *
mw=Tk()
mw.title("CALCULATOR")
def clear():
    Entry.delete(0,END)
def but_clk(num):
    cur_num=Entry.get()
    clear()
    finl_num=cur_num+num
    Entry.insert(0,finl_num)
first_num=0
math=''
math_sign=""
def calc(math_type,ms):
    global first_num,math,math_sign
    math=math_type
    math_sign=ms
    first_num=Entry.get()
    clear()
    Entry.insert(0,first_num+math_sign)
def equal():
    global first_num,math,math_sign
    second_num=Entry.get().replace(first_num+math_sign,"")
    clear()
    if math=="add":
        result=int(first_num)+int(second_num)
    elif math=="sub":
        result=int(first_num)-int(second_num)
    elif math=="mul":
        result=int(first_num)*int(second_num)
    elif math=="div":
        result=int(first_num)/int(second_num)
        round(result,3)
    Entry.insert(0,result)
    



Entry=Entry(mw,width=14,font=("Arial",24),justify=RIGHT)
Entry.grid(row=0,column=0,padx=10,pady=10,columnspan=3)
B1=Button(mw,text=1,font=("Arial",14),padx=36,pady=10,command=lambda : but_clk('1'))
B2=Button(mw,text=2,font=("Arial",14),padx=36,pady=10,command=lambda : but_clk('2'))
B3=Button(mw,text=3,font=("Arial",14),padx=36,pady=10,command=lambda : but_clk('3'))
B4=Button(mw,text=4,font=("Arial",14),padx=36,pady=10,command=lambda : but_clk('4'))
B5=Button(mw,text=5,font=("Arial",14),padx=36,pady=10,command=lambda : but_clk('5'))
B6=Button(mw,text=6,font=("Arial",14),padx=36,pady=10,command=lambda : but_clk('6'))
B7=Button(mw,text=7,font=("Arial",14),padx=36,pady=10,command=lambda : but_clk('7'))
B8=Button(mw,text=8,font=("Arial",14),padx=36,pady=10,command=lambda : but_clk('8'))
B9=Button(mw,text=9,font=("Arial",14),padx=36,pady=10,command=lambda : but_clk('9'))
B0=Button(mw,text=0,font=("Arial",14),padx=36,pady=10,command=lambda : but_clk('0'))
B7.grid(row=1,column=0,padx=2,pady=2)
B8.grid(row=1,column=1,padx=2,pady=2)
B9.grid(row=1,column=2,padx=2,pady=2)
B4.grid(row=2,column=0,padx=2,pady=2)
B5.grid(row=2,column=1,padx=2,pady=2)
B6.grid(row=2,column=2,padx=2,pady=2)
B1.grid(row=3,column=0,padx=2,pady=2)
B2.grid(row=3,column=1,padx=2,pady=2)
B3.grid(row=3,column=2,padx=2,pady=2)
B0.grid(row=4,column=0,padx=2,pady=2)

Bclear=Button(mw,text="clear",font=("Arial",14),padx=74,pady=10,command=clear)
Bclear.grid(row=4,column=1,columnspan=2)

Div=Button(mw,text="/",font=("Arial",14),padx=38,pady=10,command=lambda : calc("div",'/'))
Mul=Button(mw,text="*",font=("Arial",14),padx=38,pady=10,command=lambda : calc("mul",'*'))
Add=Button(mw,text="+",font=("Arial",14),padx=36,pady=10,command=lambda : calc("add",'+'))
Sub=Button(mw,text="-",font=("Arial",14),padx=38,pady=10,command=lambda : calc("sub",'-'))
Div.grid(row=5,column=0,padx=2,pady=2)
Mul.grid(row=5,column=1,padx=2,pady=2)
Add.grid(row=6,column=0,padx=2,pady=2)
Sub.grid(row=6,column=1,padx=2,pady=2)

Equal=Button(mw,text="=",font=("Arial",14),padx=36,pady=40,command=equal)
Equal.grid(row=5,column=2,rowspan=2,padx=2,pady=2)


mw.mainloop()
