import datetime
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="susmi@123#sql",
    database="admini_db"
)
mycursor=mydb.cursor()
x=datetime.datetime.now()
f=open("file1.txt","r")
print(f.read())
#DATA OF STUDENT 
def insert_studentdata():
    sql=("insert into student_data(Name,Reg_No,DOB,Gender,Father_Name,Father_Occupation,Age,Address,email_id,Ph_No) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    Name=input("enter your name:")
    Reg_No=int(input("enter your reg_no:"))
    DOB=input("enter your brith date:")
    Gender=input("enter your gender:")
    Father_Name=input("enter your father name:")
    Father_Occupation=input("enter your father occupation:")
    Age=int(input("enter your age:"))
    Address=input("enter your address:")
    email_id=input("enter your email_id:")
    Ph_No=int(input("enter your phone number:"))
    val=(Name,Reg_No,DOB,Gender,Father_Name,Father_Occupation,Age,Address,email_id,Ph_No)
    mycursor.execute(sql,val)
    mydb.commit()
    print("Student Data saved sucessfuly")
def view_studentdata():
    mycursor.execute("select*from student_data")
    result=mycursor.fetchall()
    for i in result:
        print(i)
#DATA OF STAFF       
def insert_staffdata():
    sql=("insert into staff_data(Name,Department,Distingsion,email_id,Ph_No) values (%s,%s,%s,%s,%s)")
    Name=input("enter your name:")
    Department=input("enter your department:")
    Distingsion=input("enter your distingsion:")
    email_id=input("enter your email_id:")
    Ph_No=int(input("enter your phone number:"))
    val=(Name,Department,Distingsion,email_id,Ph_No)
    mycursor.execute(sql,val)
    mydb.commit()
    print("staff Data saved sucessfully")
def view_staffdata():
    mycursor.execute("select*from staff_data")
    result=mycursor.fetchall()
    for i in result:
        print(i)
#DATA OF DEPARTMENT
def insert_dptdata():
    sql=("insert into dep_data(Dpt_Name,Dept_Code,HOD_Name,Staff_Count,Student_Count,Dpt_mailId,DptPh_No) values (%s,%s,%s,%s,%s,%s,%s)")
    Dpt_Name=input("enter department name:")
    Dept_Code=int(input("enter department number:"))
    HOD_Name=input("enter HOD name:")
    Staff_Count=int(input("enter staff count:"))
    Student_Count=int(input("enter student count:"))
    Dpt_mailId=input("enter department mail id:")
    DptPh_No=int(input("enter department Phone number:"))
    val=(Dpt_Name,Dept_Code,HOD_Name,Staff_Count,Student_Count,Dpt_mailId,DptPh_No)
    mycursor.execute(sql,val)
    mydb.commit()
    print("Department data saved sucessfully")
def view_dptdata():
    mycursor.execute("select*from dep_data")
    result=mycursor.fetchall()
    for i in result:
        print(i)
#NON TEACHING STAFF DATA
def insert_Nonteachingdata():
    sql=("insert into nonteach_data(Name,Department,Work,email_id,Ph_No) values (%s,%s,%s,%s,%s)")
    Name=input("enter your name:")
    Department=input("enter your department:")
    Work=input("enter your distingsion:")
    email_id=input("enter your email_id:")
    Ph_No=int(input("enter your phone number:"))
    val=(Name,Department,Work,email_id,Ph_No)
    mycursor.execute(sql,val)
    mydb.commit()
    print("Nonteaching Data saved sucessfully")
def view_Nonteachingdata():
    mycursor.execute("select*from nonteach_data")
    result=mycursor.fetchall()
    for i in result:
        print(i)
#Ph.d scholars data
def insert_scholarsdata():
    sql=("insert into scholar_data(Name,Reg_No,DOB,Gender,Qualification,Father_Name,Father_Occupation,Age,Address,Email_Id,Ph_No) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    Name=input("enter your name:")
    Reg_No=int(input("enter your reg_no:"))
    DOB=input("enter your brith date:")
    Gender=input("enter your gender:")
    Qualification=input("enter your qualification:")
    Father_Name=input("enter your father name:")
    Father_Occupation=input("enter your father occupation:")
    Age=int(input("enter your age:"))
    Address=input("enter your address:")
    Email_Id=input("enter your mail id:")
    Ph_No=int(input("enter your phone number:"))
    val=(Name,Reg_No,DOB,Gender,Qualification,Father_Name,Father_Occupation,Age,Address,Email_Id,Ph_No)
    mycursor.execute(sql,val)
    mydb.commit()
    print("Scholar Data saved sucessfuly")
def view_scholardata():
    mycursor.execute("select*from scholar_data")
    result=mycursor.fetchall()
    for i in result:
        print(i)
#ALUMINI RECORD
def insert_aluminidata():
    sql=("insert into alumini_data(Name,Age,passout_year,current_position,address,email_id,ph_no) values (%s,%s,%s,%s,%s,%s,%s)")
    Name=input("enter your name:")
    Age=int(input("enter your age:"))
    passout_year=int(input("enter your passout year:"))
    current_position=input("enter your current position:")
    address=input("enter your address:")
    email_id=input("enter your email_id:")
    ph_no=int(input("enter your phone number:"))
    val=(Name,Age,passout_year,current_position,address,email_id,ph_no)
    mycursor.execute(sql,val)
    mydb.commit()
    print("Alumini data saved sucessfully")
def view_aluminidata():
    mycursor.execute("select*from alumini_data")
    result=mycursor.fetchall()
    for i in result:
        print(i)
#INSTRUCTION FOR OUTPUT
print("1->insert_departmentdata")
print("2->insert_staffdata")
print("3->insert_nonteachingdata")
print("4->insert_scholardata")
print("5->insert_studentdata")
print("6->insert_aluminidata")
print("7->view_departmentdata")
print("8->view_staffdata")
print("9->view_nonteachingdata")
print("10->view_scholardata")
print("11->view_studentdata")
print("12->view_aluminidata")
#OUTPUT EXECUTION
try:
    user=int(input("enter any number:"))
    if user==1:
        insert_dptdata()
    elif user==2:
        insert_staffdata()
    elif user==3:
        insert_Nonteachingdata()
    elif user==4:
        insert_scholarsdata()
    elif user==5:
        insert_studentdata()
    elif user==6:
        insert_aluminidata()
    elif user==7:
        view_dptdata()
    elif user==8:
        view_staffdata()
    elif user==9:
        view_Nonteachingdata()
    elif user==10:
        view_scholardata()
    elif user==11:
        view_studentdata()
    elif user==12:
        view_aluminidata()
    else:
        print("select 1 to 12 numbers only")
except:
    print("enter only numbers")
print(x)