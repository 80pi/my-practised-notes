from tkinter import *
r=Tk()
r.configure(background="white")
r.title("simple calculator")
e=Entry(r,width=50,bd=10)
e.grid(row=0,column=0,columnspan=5)
#r.geometry("300*300")
def buttonsho(nn):
    c=e.get()
    e.delete(0,END)
    e.insert(0,c+nn)
def buttoncle():
    e.delete(0,END)
def buttonadd():
    f=e.get()
    global fn
    global m
    fn=int(f)
    m="+"
    e.delete(0,END)
def buttonmin():
    f=e.get()
    global fn
    global m
    fn=int(f)
    m="-"
    e.delete(0,END)
def buttonmul():
    f=e.get()
    global fn
    global m
    m="*"
    fn=int(f)
    e.delete(0,END)
def buttondiv():
    f=e.get()
    global fn
    global m
    fn=int(f)
    m="/"
    e.delete(0,END)
def buttoneq():
    se=e.get()
    if(m=='+'):
        a=fn+int(se)
        e.delete(0,END)
        e.insert(0,a)
    if(m=='-'):
        a=fn-int(se)
        e.delete(0,END)
        e.insert(0,a)
    if(m=='*'):
        a=fn*int(se)
        e.delete(0,END)
        e.insert(0,a)
    if(m=='/'):
        a=fn/int(se)
        e.delete(0,END)
        e.insert(0,a)


bp=Button(r,text="+",padx=45,pady=20,bd=5,bg="black",fg="white",command=buttonadd).grid(row=4,column=0)
bmi=Button(r,text="-",padx=45,pady=20,bd=5,bg="black",fg="white",command=buttonmin).grid(row=4,column=1)
bm=Button(r,text="*",padx=45,pady=20,bd=5,bg="black",fg="white",command=buttonmul).grid(row=4,column=2)
bud=Button(r,text="/",padx=45,pady=20,bd=5,bg="black",fg="white",command=buttondiv).grid(row=5,column=0)
b1=Button(r,text="7",padx=45,pady=20,bd=5,bg="black",fg="white",command=lambda:buttonsho('7')).grid(row=1,column=0)
b2=Button(r,text="8",padx=45,pady=20,bd=5,bg="black",fg="white",command=lambda:buttonsho('8')).grid(row=1,column=1)
b3=Button(r,text="9",padx=45,pady=20,bd=5,bg="black",fg="white",command=lambda:buttonsho('9')).grid(row=1,column=2)
b4=Button(r,text="4",padx=45,pady=20,bd=5,bg="black",fg="white",command=lambda:buttonsho('4')).grid(row=2,column=0)
b5=Button(r,text="5",padx=45,pady=20,bd=5,bg="black",fg="white",command=lambda:buttonsho('5')).grid(row=2,column=1)
b6=Button(r,text="6",padx=45,pady=20,bd=5,bg="black",fg="white",command=lambda:buttonsho('6')).grid(row=2,column=2)
b7=Button(r,text="1",padx=45,pady=20,bd=5,bg="black",fg="white",command=lambda:buttonsho('1')).grid(row=3,column=0)
b8=Button(r,text="2",padx=45,pady=20,bd=5,bg="black",fg="white",command=lambda:buttonsho('2')).grid(row=3,column=1)
b9=Button(r,text="3",padx=45,pady=20,bd=5,bg="black",fg="white",command=lambda:buttonsho('3')).grid(row=3,column=2)
be=Button(r,text="=",padx=45,pady=20,bd=5,bg="black",fg="white",command=buttoneq).grid(row=6,column=0)
bc=Button(r,text="c",padx=45,pady=20,bd=5,bg="black",fg="white",command=buttoncle).grid(row=5,column=2)
b0=Button(r,text="0",padx=45,pady=20,bd=5,bg="black",fg="white",command=lambda:buttonsho('0')).grid(row=5,column=1)

#bc=Button(r,text="0",font="underline",activeforeground="blue",activebackground="pink",padx=45,pady=20,bd=5).grid(row=1,column=2)
r.mainloop()
