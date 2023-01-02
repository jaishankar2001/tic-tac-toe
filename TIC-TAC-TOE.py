# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 09:20:08 2021

@author: Jaishankar
"""

from tkinter import*
window=Tk()
window.title("welcome to tic_tac_toe.0.1")
window.geometry("500x500")
lb1=Label(window,text="the game begins",font=("arial","15"))
lb1.grid(row=0,column=0)
lb1=Label(window,text="player1=x:",font=("arial","15"))
lb1.grid(row=1,column=0)
lb1=Label(window,text="player2=o",font=("arial","15"))
lb1.grid(row=2,column=0)


turn=1

def c1():
    global turn
    if bt1["text"]==" ":
        if turn==1:
            turn=2
            bt1["text"]="x"
        elif turn==2:
            turn=1
            bt1["text"]="o"
        check()
def c2():
    global turn
    if bt2["text"]==" ":
        if turn==1:
            turn=2
            bt2["text"]="x"
        elif turn==2:
            turn=1
            bt2["text"]="o"
        check()
def c3():
    global turn
    if bt3["text"]==" ":
        if turn==1:
            turn=2
            bt3["text"]="x"
        elif turn==2:
            turn=1
            bt3["text"]="o"
        check()
def c4():
    global turn
    if bt4["text"]==" ":
        if turn==1:
            turn=2
            bt4["text"]="x"
        elif turn==2:
            turn=1
            bt4["text"]="o"
        check()
def c5():
    global turn
    if bt5["text"]==" ":
        if turn==1:
            turn=2
            bt5["text"]="x"
        elif turn==2:
            turn=1
            bt5["text"]="o"
        check()
def c6():
    global turn
    if bt6["text"]==" ":
        if turn==1:
            turn=2
            bt6["text"]="x"
        elif turn==2:
            turn=1
            bt6["text"]="o"
        check()
def c7():
    global turn
    if bt7["text"]==" ":
        if turn==1:
            turn=2
            bt7["text"]="x"
        elif turn==2:
            turn=1
            bt7["text"]="o"
        check()
def c8():
    global turn
    if bt8["text"]==" ":
        if turn==1:
            turn=2
            bt8["text"]="x"
        elif turn==2:
            turn=1
            bt8["text"]="o"
        check()
def c9():
    global turn
    if bt9["text"]==" ":
        if turn==1:
            turn=2
            bt9["text"]="x"
        elif turn==2:
            turn=1
            bt9["text"]="o"
        check()
flag=1
def check():
     global flag
     b1=bt1["text"]
     b2=bt2["text"]
     b3=bt3["text"]
     b4=bt4["text"]
     b5=bt5["text"]
     b6=bt6["text"]
     b7=bt7["text"]
     b8=bt8["text"]
     b9=bt9["text"]
     flag=flag+1
     if ((b1==b2 and b1==b3 and b1=="o") or (b1==b2 and b1==b3 and b1=="x")):
         win(bt1["text"])
     if ((b4==b5 and b4==b6 and b4=="o") or (b4==b5 and b4==b6 and b4=="x")):
         win(bt4["text"])
     if ((b7==b8 and b7==b9 and b7=="o") or (b7==b8 and b7==b9 and b7=="x")):
         win(bt7["text"]) 
     if ((b1==b4 and b1==b7 and b1=="o") or (b1==b4 and b1==b7 and b1=="x")):
         win(bt1["text"])
     if ((b5==b2 and b2==b8 and b2=="o") or (b5==b2 and b2==b8 and b2=="x")):
         win(bt2["text"])
     if ((b3==b6 and b6==b9 and b3=="o") or (b3==b6 and b3==b9 and b3=="x")):
         win(bt3["text"])
     if ((b1==b5 and b1==b9 and b1=="o") or (b1==b5 and b1==b9 and b1=="x")):
         win(bt1["text"])
     if ((b3==b5 and b3==b7 and b3=="o") or (b3==b5 and b3==b7 and b3=="x")):
         win(bt3["text"])
     if flag==10:
         win("tie")
def des():
    window.destroy()
def win(player):
    disp_text=""
    if(player!="tie"):
        disp_text="player "+ player + " wins"
    else:
        disp_text="tie"
    win_label=Label(window,text=disp_text,font=("arial","15"))
    win_label.grid(column=0,row=10)
bt1=Button(window,text=" ",bg="white",fg="black",width=3,height=1,font=("arial","20"),command=c1)
bt1.grid(column=1,row=1)
bt2=Button(window,text=" ",bg="white",fg="black",width=3,height=1,font=("arial","20"),command=c2)
bt2.grid(column=2,row=1)
bt3=Button(window,text=" ",bg="white",fg="black",width=3,height=1,font=("arial","20"),command=c3)
bt3.grid(column=3,row=1)
bt4=Button(window,text=" ",bg="white",fg="black",width=3,height=1,font=("arial","20"),command=c4)
bt4.grid(column=1,row=2)
bt5=Button(window,text=" ",bg="white",fg="black",width=3,height=1,font=("arial","20"),command=c5)
bt5.grid(column=2,row=2)
bt6=Button(window,text=" ",bg="white",fg="black",width=3,height=1,font=("arial","20"),command=c6)
bt6.grid(column=3,row=2)
bt7=Button(window,text=" ",bg="white",fg="black",width=3,height=1,font=("arial","20"),command=c7)
bt7.grid(column=1,row=3)
bt8=Button(window,text=" ",bg="white",fg="black",width=3,height=1,font=("arial","20"),command=c8)
bt8.grid(column=2,row=3)
bt9=Button(window,text=" ",bg="white",fg="black",width=3,height=1,font=("arial","20"),command=c9)
bt9.grid(column=3,row=3)
bt10=Button(window,text="close?",bg="white",fg="black",width=6,height=1,font=("arial","20"),command=des)
bt10.grid(column=5,row=10)   
window.mainloop()