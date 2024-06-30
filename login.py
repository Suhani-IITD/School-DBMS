import pymysql

db = pymysql.connect(host = "localhost", user="root", passwd="root1234")
cur = db.cursor()

def create_db():
    cur.execute("create database project;")


def create_table_faculty():
    data = {101:["Ruchika","MATHS","XII-B",5],102:["Pooja","PHYSICS","XII-C",6],103:["Suman","ENGLISH"],104:["Kanupria","CHEMISTRY","XII-A",4],105:["Amit","CS"]}
    cur.execute("create table faculty(ID int primary key, NAME varchar(30), SUBJECT varchar(20), CLASS varchar(10), TOTAL_STRENGTH int);")
    for i in data:
        if len(data[i])==4:
            r = f"insert into faculty VALUES({i},'{data[i][0]}','{data[i][1]}','{data[i][2]}',{data[i][3]});"
            cur.execute(r)
        else:
            r = f"insert into faculty(ID,NAME,SUBJECT) VALUES({i},'{data[i][0]}','{data[i][1]}');"
            cur.execute(r)
    db.commit()


def create_table_students():
    data = {1001:["Gautam", "2004-03-15", "XII-B"],1002:["Aditya", "2004-08-15", "XII-A"], 1003:["Dhruv", "2004-06-25", "XII-A"]
            ,1004:["Anmol", "2004-12-14", "XII-C"],1005:["Mahi", "2004-03-09", "XII-B"],1006:["Sanika", "2004-11-15", "XII-B"]
            ,1007:["Apurv", "2004-06-03", "XII-C"], 1008:["Gunika", "2004-05-27", "XII-A"],1009:["Sumedha", "2005-07-23", "XII-A"]
            ,1010:["Mukta", "2004-03-09", "XII-B"],1011:["Naina", "2004-12-09", "XII-B"],1012:["Prashant", "2004-01-13", "XII-C"]
            ,1013:["Ruchir", "2004-02-19", "XII-C"],1014:["Vats", "2004-07-29", "XII-C"]}
    cur.execute("create table Students(Admission_Number int primary key, NAME varchar(30), DOB Date, CLASS varchar(10));")
    for i in data:
        r = f"insert into Students VALUES({i},'{data[i][0]}','{data[i][1]}','{data[i][2]}');"
        cur.execute(r)
    db.commit()


def create_tt_A():
    cur.execute("create table XII_A(Sno int,DAY varchar(10),First varchar(10),Second varchar(10),BREAK varchar(5),Third varchar(10),Fourth varchar(10));")
    cur.execute("insert into XII_A values(1,'MONDAY','Physics','Maths','Break','Chemistry','CS');")
    cur.execute("insert into XII_A values(2,'TUESDAY','Maths','English','Break','Physics','Chemistry');")
    cur.execute("insert into XII_A values(3,'WEDNESDAY','Physics','English','Break','CS','Maths');")
    cur.execute("insert into XII_A values(4,'THURSDAY','Chemistry','CS','Break','Maths','Physics');")
    cur.execute("insert into XII_A values(5,'FRIDAY','CS','Physics','Break','English','Chemistry');")
    db.commit()

def create_tt_B():
    cur.execute("create table XII_B(Sno int,DAY varchar(10),First varchar(10),Second varchar(10),BREAK varchar(5),Third varchar(10),Fourth varchar(10));")
    cur.execute("insert into XII_B values(1,'MONDAY','CS','Physics','Break','English','Chemistry');")
    cur.execute("insert into XII_B values(2,'TUESDAY','Physics','Maths','Break','Chemistry','CS');")
    cur.execute("insert into XII_B values(3,'WEDNESDAY','Chemistry','CS','Break','Maths','Physics');")
    cur.execute("insert into XII_B values(4,'THURSDAY','Maths','English','Break','Physics','Chemistry');")
    cur.execute("insert into XII_B values(5,'FRIDAY','Physics','English','Break','CS','Maths');")
    db.commit()

def create_tt_C():
    cur.execute("create table XII_C(Sno int,DAY varchar(10),First varchar(10),Second varchar(10),BREAK varchar(5),Third varchar(10),Fourth varchar(10));")
    cur.execute("insert into XII_C values(1,'MONDAY','Chemistry','CS','Break','Maths','Physics');")
    cur.execute("insert into XII_C values(2,'TUESDAY','CS','Physics','Break','English','Maths');")
    cur.execute("insert into XII_C values(3,'WEDNESDAY','Maths','Physics','Break','English','Chemistry');")
    cur.execute("insert into XII_C values(4,'THURSDAY','Physics','Maths','Break','Chemistry','CS');")
    cur.execute("insert into XII_C values(5,'FRIDAY','Chemistry','CS','Break','Physics','English');")
    db.commit()
    
create_db()
cur.execute("use project;")
create_table_faculty()
create_table_students()
create_tt_A()
create_tt_B()
create_tt_C()



