import tkinter
from tkinter import *
from tkinter import messagebox
from login import *
from datetime import datetime as dt
import random
import time

def data_fetch(table,i,col):
    cur.execute(f"select * from {table} where {col} = {i};")
    r = cur.fetchall()
    return r


def u_rec(i,col,table):
    d(0,table)
    Label(f,text = "Enter Column Name",font=("Times New Roman",15),fg='forest green',bg='gold',padx=10, pady=10).place(x=300,y=170)
    e1 = Entry(f)
    e1.place(x=490,y=180)
    Label(f,text = "Enter Data",font=("Times New Roman",15),fg='forest green',bg='gold',padx=10, pady=10).place(x=300,y=270)
    e2 = Entry(f)
    e2.place(x=415,y=280)
    def up():
        field,val = e1.get(),e2.get()
        if field == "Total":
            val = int(val)
            cur.execute(f"update {table} set {field} = {val} where {col} = {i};")
        else:
            cur.execute(f"update {table} set {field} = '{val}' where {col} = {i};")
        db.commit()
        messagebox.showinfo("Message","Record has been Updated Succesfully!")
        r = data_fetch(table,i,col)
        if table.lower()=='faculty':
            w.title("Welcome " + r[0][1])
        else:
            w.title("Welcome " + r[0][1] + " Class " + r[0][3])
        d(i,table)
    Button(f,text="SUBMIT",command = lambda: up(),font=("Times New Roman",15),fg='forest green',bg='gold').place(x=400,y=350)
    Button(f,text='< BACK',command = lambda: d(i,table),font=("Times New Roman" ,10),fg='forest green',bg='gold').place(x=0,y=0)

def status(i,table,sec):
    d(0,table)
    current = dt.now()
    day = current.strftime("%A")
    tt = {9:'first',10:'second',11:'break',12:'third',13:'fourth'}
    p = {1:'Your Child is Present!!',0:'Your Child is Out of The Class!!'}
    l=[1,1,1,1,1,1,1,1,1,0]
    m = p[random.choice(l)]
    if current.hour in tt and day not in ['Saturday','Sunday']:
        cur.execute(f'select {tt[current.hour]} from xii_{sec} where day = "{day}";')
        cl = cur.fetchone()
        try:
            cur.execute(f'select name from faculty where subject = "{cl[0]}"')
            n = cur.fetchone()
            Label(f,text=f'Teacher ---> {n[0]}',font=("Times New Roman Bold",20),fg='black',bg='lightsteelblue',padx=10).place(x=270,y=250)
        except:
            pass
        Label(f,text=f'Subject ---> {cl[0]}',font=("Times New Roman Bold",20),fg='black',bg='lightsteelblue',padx=10).place(x=300,y=180)
        if table.lower()=="students":
            Label(f,text=m,font=("Times New Roman Bold",20),fg='black',bg='lightsteelblue',padx=10).place(x=240,y=320)
        else:
            cur.execute(f'select name from students where class="{cl}";')
            raw = cur.fetchall()
            l1=[1,1,1,1,1,1,1,1,1,0,0,0]
            if l1==0:
                g = raw[0][random.choice(l1)] + "is out"
            else:
                g = 'Everyone is present'
            Label(f,text=g,font=("Times New Roman Bold",20),fg='black',bg='lightsteelblue',padx=10).place(x=240,y=320)
    else:
        Label(f,text="School Timings are from 9:00 AM to 2:00 PM ",font=("Times New Roman Bold",15),fg='forest green',bg='gold', padx=1).place(x=140,y=220)
        Label(f,text="MONDAY to FRIDAY ONLY",font=("Times New Roman Bold",15),fg='forest green',bg='gold', padx=1).place(x=200,y=280)
    Button(f,text='< BACK',command = lambda: d(i,table),font=("Times New Roman Bold",10),fg='forest green',bg='gold').place(x=0,y=0)

def d(x=0,tab='students'):
    global f
    try:
        f.place_forget()
    except:
        pass
    f = Frame(w)
    if tab.lower()=='students':
        f.place(x=0,y=0,width='762',height='427')
        global bg
        bg = PhotoImage(file = "stu.png")
        Label(f,image = bg).place(relwidth=1,relheight=1)
        if x==0:
            return
        else:
            stu_window(x)
    elif tab.lower()=='faculty':
        f.place(x=0,y=0,width='632',height='414')
        global bg1
        bg1 = PhotoImage(file = "fac.png")
        Label(f,image = bg1).place(relwidth=1,relheight=1)
        if x==0:
            return
        else:
            fac_window(x)


def stu_opt(i):
    global r
    r = data_fetch("Students",i,"Admission_Number")
    global w
    w=Tk()
    w.geometry("762x427")
    w.title("Welcome " + r[0][1] + " Class " + r[0][3])
    d(i)
    w.mainloop()


def stu_window(i):
    Button(f,text="UPDATE RECORD",command = lambda: u_rec(i,"Admission_Number","Students"),cursor='hand2',font=("Times New Roman",15, 'bold')
           ,fg='forest green',bg = 'gold' ,padx=40,pady=8).place(x=300,y=160)
    Button(f,text="LIVE STATUS",command = lambda: status(i,"Students",r[0][3][-1]) , font=("Times New Roman",15, 'bold'),cursor='hand2'
           ,fg='forest green',bg='gold',padx=28,pady=8).place(x=300,y=250)
    Button(f,text='EXIT',command = lambda: w.destroy(), font = ("Times New Roman", 15, 'bold') ,fg='forest green',bg='gold', padx=20, pady= 5).place(x=300,y=340)


def attend(i,cl,table):
    d(0,table)
    cur.execute(f'select name from students where class="{cl}";')
    raw = cur.fetchall()
    for i in range(len(raw)):
        Label(f,text=raw[i][0],font=("Times New Roman Bold",20),fg='black',bg='lightsteelblue',padx=10).place(x=400,y=140+50*i)
    Button(f,text='< BACK',command = lambda: d(i,'faculty'),font=("Times New Roman Bold",10),fg='forest green',bg='gold').place(x=0,y=0)
                
def fac_opt(i):
    global r
    r = data_fetch("faculty",i,"ID")
    global w
    w=Tk()
    w.geometry("632x414")
    w.title("Welcome " + r[0][1])
    d(i,"faculty")
    w.mainloop()


def fac_window(i):
    Button(f,text="UPDATE RECORD",command = lambda: u_rec(i,"ID","Faculty"),cursor='hand2',font=("Times New Roman",15)
           ,fg='black',bg='lightsteelblue',padx=30,pady=8).place(x=350,y=170)
    if r[0][3]!=None:
        Button(f,text="CLASS STATUS",command = lambda: status(i,"Faculty",r[0][3][-1]) , font=("Times New Roman",15),cursor='hand2'
               ,fg='black',bg='lightsteelblue',padx=26,pady=8).place(x=350,y=230)
        Button(f,text="CLASS LIST",command = lambda: attend(i,r[0][3], "Faculty") , font=("Times New Roman",15),cursor='hand2'
               ,fg='black',bg='lightsteelblue',padx=26,pady=8).place(x=350,y=290)
    else:
        pass
    Button(f,text='EXIT',command = lambda: w.destroy() ,fg='black',bg='lightsteelblue', padx=10, pady=10).place(x=350,y=350)
