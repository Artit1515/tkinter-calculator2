from cgitb import text
from tkinter import*
import tkinter.messagebox 
import math

app=Tk()
app.title("calculator")
#app.geometry("600x600")
app.config(bg="#374353")

ansresult=""

dpshow=StringVar(value="0")

def enter(number):
    global ansresult
    ansresult=ansresult+str(number)
    dpshow.set(ansresult)

def clear():
    global ansresult
    ansresult=""
    dpshow.set(0)

def equal():
    sub_str ="/0"
    sub_str2=")("
    countdot=0
    countmutiply=0
    countdivide=0
    countopblacket=0
    countclblacket=0
    global ansresult
    firstchar=ansresult[0]
    lastchar=ansresult[-1]
    for A in ansresult:
        if A ==".":
            countdot+=1

    if countdot >1:
        ansresult=""
        dpshow.set("syntrax error")
        return
###########################################       
    for B in ansresult:
        if B =="*":
            countmutiply+=1

    if countmutiply >2:
        ansresult=""
        dpshow.set("syntrax error")
        return
#######################################
    for E in ansresult:
        if E =="/":
            countdivide+=1

    if countdivide >1:
        ansresult=""
        dpshow.set("syntrax error")
        return
#######################################
    for C in ansresult:
        if C =="(":
            countopblacket+=1

    for D in ansresult:
        if D ==")":
            countmutiply+=1

    if countopblacket >0:
        if countopblacket != countclblacket:
            ansresult=""
            dpshow.set("syntrax error")
            return
#######################################
    if firstchar == "*" or firstchar == "/" or firstchar == ")":
        ansresult=""
        dpshow.set("syntrax error")
        return
    if "**" in ansresult and ansresult=="":
        ansresult=0

    #if firstchar == "+" or firstchar == "-":
    #    ansresult=""
     #   dpshow.set("0")
     #   return

    if lastchar == "+" or lastchar == "-" or lastchar == "*" or lastchar == "/" or lastchar == "(":
        ansresult=""
        dpshow.set("syntrax error")
        return

    if sub_str in ansresult or sub_str2 in ansresult :
        ansresult=""
        dpshow.set("syntrax error")
        return

    if ansresult=="()":
        ansresult=""
        dpshow.set("0")
        return


    finalans=float(eval(ansresult))
    dpshow.set(str(finalans))
    
    ansresult=str(finalans)
    with open("history calculation.txt", "a") as f:
        writehistory=ansresult+"\n"
        f.write(writehistory)
        f.close()

def delete():
    global ansresult
    ans=dpshow.get()
    lenght=len(ans)
    dp.delete(lenght-1,END)
    rubkar=dp.get()
    ansresult=rubkar
    if lenght == 1:
        dpshow.set(0)
        ansresult=""
    if ans == "syntrax error":
        dp.delete(0,END)
        dpshow.set(0)
        ansresult=""

def rootmath():
    global ansresult
    firstchar=ansresult[0]
    if firstchar=="-":
        ansresult=""
        dpshow.set("syntrax error")
        return
    #if ansresult=="":
     #   ansresult=""
     #   dpshow.set("syntrax error")
     #   return
    sqroot= (math.sqrt(eval(ansresult)))
    dpshow.set(str(sqroot))
    ansresult=str(sqroot)
    with open("history calculation.txt", "a") as f:
        writehistory=ansresult+"\n"
        f.write(writehistory)
        f.close()


def pimath():
    global ansresult
    pimath=(math.pi(eval(ansresult)))
    dpshow.set(str(pimath))
    ansresult=str(pimath)
    with open("history calculation.txt", "a") as f:
        writehistory=ansresult+"\n"
        f.write(writehistory)
        f.close()

def absmath():
    global ansresult
    absmath=(abs(eval(ansresult)))
    dpshow.set(str(absmath))
    ansresult=str(absmath)

    with open("history calculation.txt", "a") as f:
        writehistory=ansresult+"\n"
        f.write(writehistory)
        f.close()

def log():
    global ansresult
    firstchar=ansresult[0]
    if firstchar=="-":
        ansresult=""
        dpshow.set("syntrax error")
        return
    
    logmath=(math.log(eval(ansresult)))
    dpshow.set(str(logmath))
    ansresult=str(logmath)

    with open("history calculation.txt", "a") as f:
        writehistory=ansresult+"\n"
        f.write(writehistory)
        f.close()
        

def factorial():
    global ansresult
    factorialmath=(math.factorial(eval(ansresult)))
    dpshow.set(str(factorialmath))
    ansresult=str(factorialmath)
        
    with open("history calculation.txt", "a") as f:
        writehistory=ansresult+"\n"
        f.write(writehistory)
        f.close()

dp=Entry(font=90,width=35,textvariable=dpshow,justify="right")
dp.grid(columnspan=7)

def history():
    app2=Tk()
    #app2.title(text="calculation history")
    Lb = Listbox(app2)
    Lb.grid()
    with open("history calculation.txt","r") as f:
        for x in f:
            Lb.insert(END,x)
        
    f.close()   
    app2.mainloop




myMenu = Menu()
app.config(menu=myMenu)
#minimenu = Menu()

#minimenu.add_command(label="scitific calculator mode")
#minimenu.add_command(label="history",command=history)
#minimenu.add_command(label="")




myMenu.add_cascade(label="calculate history",command=history)




#ที่เก็บเลข
bt7=Button(text="7",padx=30,bg="#393030",fg="white",pady=30,command=lambda:enter(7)).grid(row=2,column=0)
bt8=Button(text="8",padx=30,bg="#393030",fg="white",pady=30,command=lambda:enter(8)).grid(row=2,column=1)
bt9=Button(text="9",padx=30,bg="#393030",fg="white",pady=30,command=lambda:enter(9)).grid(row=2,column=2)

bt4=Button(text="4",padx=30,bg="#393030",fg="white",pady=30,command=lambda:enter(4)).grid(row=3,column=0)
bt5=Button(text="5",padx=30,bg="#393030",fg="white",pady=30,command=lambda:enter(5)).grid(row=3,column=1)
bt6=Button(text="6",padx=30,bg="#393030",fg="white",pady=30,command=lambda:enter(6)).grid(row=3,column=2)

bt1=Button(text="1",padx=30,bg="#393030",fg="white",pady=30,command=lambda:enter(1)).grid(row=4,column=0)
bt2=Button(text="2",padx=30,bg="#393030",fg="white",pady=30,command=lambda:enter(2)).grid(row=4,column=1)
bt3=Button(text="3",padx=30,bg="#393030",fg="white",pady=30,command=lambda:enter(3)).grid(row=4,column=2)

bt0=Button(text="0",padx=30,pady=30,bg="#393030",fg="white",command=lambda:enter(0)).grid(row=5,column=1)
btdot=Button(text=".",padx=31.25,bg="#393030",fg="white",pady=30,command=lambda:enter(".")).grid(row=5,column=0)
btequal=Button(text="=",padx=30,bg="#015DB2",pady=30,command=equal).grid(row=5,column=2)

btplus=Button(text="+",padx=30,bg="light gray",pady=30,command=lambda:enter("+")).grid(row=5,column=3)
btminus=Button(text="-",padx=31.75,bg="light gray",pady=30,command=lambda:enter("-")).grid(row=4,column=3)
btmultiply=Button(text="x",padx=31,bg="light gray",pady=30,command=lambda:enter("*")).grid(row=3,column=3)
btdivide=Button(text="÷",padx=30,bg="light gray",pady=30,command=lambda:enter("/")).grid(row=2,column=3)

btdelelte=Button(text="del",padx=26.5,bg="light gray",fg="red",pady=30,command=delete).grid(row=1,column=3)
dtclear=Button(text="c",padx=30,bg="light gray",fg="red",pady=30,command=clear).grid(row=1,column=2)
btopblacket=Button(text=")",padx=30.5,bg="light gray",pady=30,command=lambda:enter(")")).grid(row=1,column=1)
btclblacket=Button(text="(",padx=30.5,bg="light gray",pady=30,command=lambda:enter("(")).grid(row=1,column=0)

mathbt1=Button(text="x!",padx=32.5,bg="light gray",pady=30,command=factorial).grid(row=1,column=4)
mathbt2=Button(text="√",padx=32.5,bg="light gray",pady=30,command=rootmath).grid(row=2,column=4)
mathbt3=Button(text="x^y",padx=27,bg="light gray",pady=30,command=lambda:enter("**")).grid(row=3,column=4)
mathbt4=Button(text="lxl",padx=30.5,bg="light gray",pady=30,command=absmath).grid(row=4,column=4)
mathbt5=Button(text="log",padx=29,bg="light gray",pady=30,command=log).grid(row=5,column=4)

app.mainloop()
