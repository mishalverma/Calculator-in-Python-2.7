#import sys
from Tkinter import *

def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    var.set(operator)
def Clear():
    global operator
    operator=""
    var.set(operator)
def Equal():
    global operator
    sumup=str(eval(operator))
    var.set(sumup)
    operator=""
root=Tk() 

frame=Frame(root)
frame.pack()

root.title("Calculator")

var=StringVar()
operator=""
topframe=Frame(root)
topframe.pack(side=TOP)
txtdisplay=Entry(frame,textvariable=var,bd=30,insertwidth=4,font=20,bg="burlywood1")
txtdisplay.pack(side=TOP)

#---------------------------------------------------------------------------------
button1=Button(topframe,padx=16,pady=16,bd=8,text="1",bg="burlywood2",fg="black",command=lambda:btnClick(1))
button1.pack(side=LEFT)
button1=Button(topframe,padx=16,pady=16,bd=8,text="2",bg="burlywood2",fg="black",command=lambda:btnClick(2))
button1.pack(side=LEFT)
button1=Button(topframe,padx=16,pady=16,bd=8,text="3",bg="burlywood2",fg="black",command=lambda:btnClick(3))
button1.pack(side=LEFT)
button1=Button(topframe,padx=16,pady=16,bd=8,text="+",bg="burlywood2",fg="black",command=lambda:btnClick("+"))
button1.pack(side=LEFT)

#-----------------------------------------------------------------------------------
frame1=Frame(root)
frame1.pack(side=TOP)

button1=Button(frame1,padx=16,pady=16,bd=8,text="4",bg="burlywood2",fg="black",command=lambda:btnClick(4))
button1.pack(side=LEFT)
button1=Button(frame1,padx=16,pady=16,bd=8,text="5",bg="burlywood2",fg="black",command=lambda:btnClick(5))
button1.pack(side=LEFT)
button1=Button(frame1,padx=16,pady=16,bd=8,text="6",bg="burlywood2",fg="black",command=lambda:btnClick(6))
button1.pack(side=LEFT)
button1=Button(frame1,padx=16,pady=16,bd=8,text="-",bg="burlywood2",fg="black",command=lambda:btnClick("-"))
button1.pack(side=LEFT)

#------------------------------------------------------------------------------------
frame2=Frame(root)
frame2.pack(side=TOP)

button1=Button(frame2,padx=16,pady=16,bd=8,text="7",bg="burlywood2",fg="black",command=lambda:btnClick(7))
button1.pack(side=LEFT)
button1=Button(frame2,padx=16,pady=16,bd=8,text="8",bg="burlywood2",fg="black",command=lambda:btnClick(8))
button1.pack(side=LEFT)
button1=Button(frame2,padx=16,pady=16,bd=8,text="9",bg="burlywood2",fg="black",command=lambda:btnClick(9))
button1.pack(side=LEFT)
button1=Button(frame2,padx=16,pady=16,bd=8,text="*",bg="burlywood2",fg="black",command=lambda:btnClick("*"))
button1.pack(side=LEFT)

#-------------------------------------------------------------------------------------
frame3=Frame(root)
frame3.pack(side=TOP)

button1=Button(frame3,padx=16,pady=16,bd=8,text="0",bg="burlywood2",fg="black",command=lambda:btnClick(0))
button1.pack(side=LEFT)
button1=Button(frame3,padx=16,pady=16,bd=8,text="C",bg="burlywood2",fg="black",command=Clear)
button1.pack(side=LEFT)
button1=Button(frame3,padx=16,pady=16,bd=8,text="=",bg="burlywood2",fg="black",command=Equal)
button1.pack(side=LEFT)
button1=Button(frame3,padx=16,pady=16,bd=8,text="/",bg="burlywood2",fg="black",command=lambda:btnClick("/"))
button1.pack(side=LEFT)

root.mainloop()
