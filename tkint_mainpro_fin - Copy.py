from stu_opt_fac_opt_fin import *

d = {101: "101_ruchika",102:"102_pooja",103:"103_suman",104:"104_kanu",105:"105_amit"}
s = {1001:'1001', 1002:'1002', 1003:'1003', 1004:'1004', 1005:'1005', 1006:'1006', 1007:'1007', 1008:'1008', 1009:'1009',
     1010:'1010', 1011:'1011', 1012:'1012', 1013:'1013', 1014:'1014'} 

def reg_log(x,t):
    global mw
    r = Toplevel()
    r.geometry("686x454")
    bg = PhotoImage(file='img3.png')
    Label(r,image=bg).place(relwidth=1,relheight=1)
    f = Frame(r,bg='white')
    f.place(x=150,y=150,width='280',height='250')
    Label(f,text='Username',fg='black',bg='white').place(x=18,y=80)
    e = Entry(f,bg='light gray')
    e.place(x=18,y=110)
    Label(f,text='Password',fg='black',bg='white').place(x=18,y=140)
    e2 = Entry(f,bg='light gray')
    e2.place(x=18,y=170)
    if x==1:
        Label(f,text='Register Here',font=('Impact',30),fg='orange',bg='white').place(x=18,y=20)
        b = Button(r,text='Register',command = lambda : reg(int(e.get()),e2.get(),t),font=("Times New Roman",15),fg='white',bg='orange').place(x=250,y=380)
    else:
        Label(f,text='Login Here',font=('Impact',30),fg='orange',bg='white').place(x=18,y=20)
        b = Button(r,text='Login',command = lambda : check(int(e.get()),e2.get(),t),font=("Times New Roman",15),fg='white',bg='orange').place(x=250,y=380)
    def reg(i,p,t):
        global d
        global s
        if i not in d and i not in s:
            if t==2:
                d[i]=p
                messagebox.showinfo('Messgae','Registered Succesfully!!')
                r.destroy()
                a_fac()
            else:
                s[i]=p
                messagebox.showinfo('Messgae','Registered Succesfully!!')
                r.destroy()
                a_stu()
        else:
            messagebox.showerror('Messgae','Account Already exists with same credentials!!')
        
    def check(i,p,t):
        if t==1:
            if (i,p)==(123,'123'):
                r.destroy()
                mw.destroy()
                adm_opt()
                return
            else:
                messagebox.showinfo('Messgae','Invalid Credentials!!')
                
        elif t==2:
            for i in d:
                if (i,p) == (i,d[i]):
                    r.destroy()
                    mw.destroy()
                    fac_opt(i)
                    return
            else:
                messagebox.showinfo('Messgae','Invalid Credentials!!')
        else:
            for i in s:
                if (i,p) == (i,s[i]):
                    r.destroy()
                    mw.destroy()
                    stu_opt(i)
                    return
            else:
                messagebox.showinfo('Messgae','Invalid Credentials!!')
    r.mainloop()

def a_stu():
    aw = Toplevel()
    aw.geometry("450x300")
    Label(aw,text = "Admission Number",font=("Times New Roman Bold",15),fg='blue',bg='light blue',padx=10).place(x=20,y=20)
    e1 = Entry(aw)
    e1.place(x=240,y=30)
    Label(aw,text = "Name",font=("Times New Roman Bold",15),fg='blue',bg='light blue',padx=10).place(x=20,y=60)
    e2 = Entry(aw)
    e2.place(x=240,y=70)
    Label(aw,text = "DOB(YYYY-MM-DD)",font=("Times New Roman Bold",15),fg='blue',bg='light blue',padx=10).place(x=20,y=100)
    e3 = Entry(aw)
    e3.place(x=240,y=110)
    Label(aw,text = "Class-Section",font=("Times New Roman Bold",15),fg='blue',bg='light blue',padx=10).place(x=20,y=140)
    e4 = Entry(aw)
    e4.place(x=240,y=150)
    def add_d():
        try:
            i,n,dob,c = int(e1.get()),e2.get(),e3.get(),e4.get()
            r = f"insert into Students(Admission_Number, Name, DOB, Class) VALUES({i},'{n}','{dob}','{c}');"
            cur.execute(r)
            db.commit()
            messagebox.showinfo('Messgae','ADDED SUCCESFULLY!!')
        except pymysql.err.IntegrityError:
            print("Duplicate record!!!")
        aw.destroy()
            
    b1 = Button(aw,text="SUBMIT",command = add_d,font=("Times New Roman Bold",20),fg='white',bg='red')
    b1.place(x=150,y=200)
    aw.mainloop()


def a_fac():
    aw = Tk()
    aw.geometry("450x300")
    Label(aw,text = "ID",font=("Times New Roman Bold",15),fg='blue',bg='light blue',padx=10).place(x=20,y=20)
    e1 = Entry(aw)
    e1.place(x=240,y=30)
    Label(aw,text = "Name",font=("Times New Roman Bold",15),fg='blue',bg='light blue',padx=10).place(x=20,y=60)
    e2 = Entry(aw)
    e2.place(x=240,y=70)
    Label(aw,text = "Subject",font=("Times New Roman Bold",15),fg='blue',bg='light blue',padx=10).place(x=20,y=100)
    e3 = Entry(aw)
    e3.place(x=240,y=110)
    Label(aw,text = "Class-Section",font=("Times New Roman Bold",15),fg='blue',bg='light blue',padx=10).place(x=20,y=140)
    e4 = Entry(aw)
    e4.place(x=240,y=150)
    Label(aw,text = "Total Strength",font=("Times New Roman Bold",15),fg='blue',bg='light blue',padx=10).place(x=20,y=180)
    e5 = Entry(aw)
    e5.place(x=240,y=190)
        
    def add_d():
        try:
            i,n,s,c,t = int(e1.get()), e2.get(), e3.get(), e4.get(), int(e5.get())
            if c!="null":
                r = f"insert into faculty(ID,NAME,SUBJECT,CLASS,TOTAL_STRENGTH) VALUES({i},'{n}','{s}','{c}',{t});"
            else:
                r = f"insert into faculty(ID,NAME,SUBJECT) VALUES({i},'{n}','{s}');"
            cur.execute(r)
            db.commit()
            messagebox.showinfo('Messgae','ADDED SUCCESFULLY!!')
        except pymysql.err.IntegrityError:
            print("Duplicate record!!!")
        aw.destroy()
    b1 = Button(aw,text="SUBMIT",command = lambda: add_d(),font=("Times New Roman Bold",20),fg='white',bg='red')
    b1.place(x=150,y=230)
    aw.mainloop()

def r_rec(tab_n,col_n,i):
        r = f"delete from {tab_n} where {col_n} = {i};"
        cur.execute(r)
        db.commit()
        messagebox.showinfo('Messgae','REMOVED SUCCESFULLY!!')        
        
def remove_window(t):
    aw = Toplevel()
    aw.geometry("450x300")
    if t=="Students":
        col = "Admission_Number"
        Label(aw,text = "Admission Number",font=("Times New Roman Bold",15),fg='blue',bg='light blue',padx=10).place(x=20,y=20)
    else:
        col = "ID"
        Label(aw,text = "Employee ID",font=("Times New Roman Bold",15),fg='blue',bg='light blue',padx=10).place(x=20,y=20)        
    e1 = Entry(aw)
    e1.place(x=240,y=30)
    b1 = Button(aw,text="SUBMIT",command = lambda: r_rec(t,col,int(e1.get())),font=("Times New Roman Bold",20),fg='white',bg='red')
    b1.place(x=150,y=200)
    aw.mainloop()

def adm_opt():
    global w
    w = Tk()
    w.geometry("685x456")
    bg1 = PhotoImage(file="img2.png")
    Label(w,image=bg1).place(relwidth=1,relheight=1)
    b1 = Button(w,text="ADD STUDENT RECORD",command = lambda : reg_log(1,3),font=("Times New Roman Bold",15),fg='blue',bg='light blue',padx=23,pady=10)
    b1.place(x=350,y=50)
    b2 = Button(w,text="ADD FACULTY RECORD",command = lambda: reg_log(1,2),font=("Times New Roman Bold",15),fg='blue',bg='light blue',padx=23,pady=10)
    b2.place(x=350,y=130)
    b3 = Button(w,text="REMOVE STUDENT RECORD", command = lambda:remove_window("Students"), font=("Times New Roman Bold",15),fg='blue',bg='light blue',pady=10)
    b3.place(x=350,y=210)
    b4 = Button(w,text="REMOVE FACULTY RECORD", command = lambda:remove_window("Faculty"),font=("Times New Roman Bold",15),fg='blue',bg='light blue',pady=10)
    b4.place(x=350,y=290)
    eb = Button(w,text='EXIT',command= w.destroy,fg='blue',bg='white')
    eb.place(x=300,y=420)
    w.mainloop()

mw = Tk()
mw.title("Menu")
mw.geometry("999x563")
mw.resizable(width=0,height = 0)
bg1 = PhotoImage(file="backimg.png")
Label(mw,image=bg1).place(relwidth=1,relheight=1)
adimg = PhotoImage(file='logo.png')
Button(mw,image = adimg,command = lambda: reg_log(2,1),cursor='hand2',border=0).place(x=100,y=10)
Label(mw,text="ADMIN LOGIN",font=("Times New Roman",15,'bold'),fg='black',bg='light gray',padx=5).place(x=100,y=140)
adimg2 = PhotoImage(file='sir.png')
Button(mw,image = adimg2,command = lambda : reg_log(2,2),cursor='hand2',border=0).place(x=100,y=180)
Label(mw,text="FACULTY LOGIN",font=("Times New Roman",13,'bold'),fg='black',bg='light gray',padx=5).place(x=100,y=310)
adimg1 = PhotoImage(file='child.png')
Button(mw,image = adimg1,command = lambda : reg_log(2,3),cursor='hand2',border=0).place(x=100,y=350)
Label(mw,text="STUDENT LOGIN",font=("Times New Roman",13,'bold'),fg='black',bg='light gray',padx=6).place(x=100,y=480)
Button(mw,text='EXIT',font=("Times New Roman",15,'bold'), command= mw.destroy,fg='black',bg='light gray', padx=5).place(x=100,y=520)
mw.mainloop()
