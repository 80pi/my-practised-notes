from tkinter import *
from PIL import ImageTk,Image
root=Tk()
#root.geometry("500x500")
root.title("practise")
root.iconbitmap("C:/Users/gopi varma/Downloads/test.ico")
f=LabelFrame(root,text="what is it")
f.pack(padx=50,pady=50)
b=Button(f,text="cccc",padx=100,pady=100).pack()
mainloop()
