import datetime
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="susmi@123#sql",
    database="covid19_db"
)
mycursor=mydb.cursor()
x=datetime.datetime.now()
f=open("file2.txt","r")
print(f.read())
#DATA OF Country details
def insert_countrydata():
    sql=("insert into country_data(C_Name,active_case,dead_case,recovery_case,dose1_count,dose2_count) values (%s,%s,%s,%s,%s,%s)")
    C_Name=input("enter the country name:")
    active_case=int(input("enter the active case count:"))
    dead_case=int(input("enter the dead case count:"))
    recovery_case=input("enter the recovery case count:")
    dose1_count=input("enter the dose1 count:")
    dose2_count=input("enter the dose2 count:")
    val=(C_Name,active_case,dead_case,recovery_case,dose1_count,dose2_count)
    mycursor.execute(sql,val)
    mydb.commit()
    print("country data saved sucessfuly")
def view_countrydata():
    mycursor.execute("select*from country_data")
    result=mycursor.fetchall()
    for i in result:
        print(i)
#DATA OF STATE       
def insert_statedata():
    sql=("insert into state_data(S_Name,active_case,dead_case,recovery_case,dose1_count,dose2_count) values (%s,%s,%s,%s,%s,%s)")
    S_Name=input("enter the state name:")
    active_case=int(input("enter the active case:"))
    dead_case=int(input("enter the dead case:"))
    recovery_case=int(input("enter the recovery case:"))
    dose1_count=int(input("enter the dose1 count:"))
    dose2_count=int(input("enter the dose2 count:"))
    val=(S_Name,active_case,dead_case,recovery_case,dose1_count,dose2_count)
    mycursor.execute(sql,val)
    mydb.commit()
    print("state data saved sucessfully")
def view_statedata():
    mycursor.execute("select*from state_data")
    result=mycursor.fetchall()
    for i in result:
        print(i)
#DATA OF District
def insert_districtdata():
    sql=("insert into district_data(D_Name,active_case,dead_case,recovery_case,dose1_count,dose2_count) values (%s,%s,%s,%s,%s,%s)")
    D_Name=input("enter the district name:")
    active_case=int(input("enter the active case count:"))
    dead_case=int(input("enter the dead case count:"))
    recovery_case=int(input("enter the recovery case count:"))
    dose1_count=int(input("enter the dose1 count:"))
    dose2_count=int(input("enter the dose2 count:"))
    val=(D_Name,active_case,dead_case,recovery_case,dose1_count,dose2_count)
    mycursor.execute(sql,val)
    mydb.commit()
    print("District data saved sucessfully")
def view_districtdata():
    mycursor.execute("select*from district_data")
    result=mycursor.fetchall()
    for i in result:
        print(i)
#Patient DATA
def insert_Patientdata():
    sql=("insert into patient_data(P_Name,age,stage,address,Ph_No) values (%s,%s,%s,%s,%s)")
    P_Name=input("enter the patient name:")
    age=int(input("enter the patient age:"))
    stage=input("enter virus stage:")
    address=input("enter your address:")
    Ph_No=int(input("enter your phone number:"))
    val=(P_Name,age,stage,address,Ph_No)
    mycursor.execute(sql,val)
    mydb.commit()
    print("Patient Data saved sucessfully")
def view_Patientdata():
    mycursor.execute("select*from patient_data")
    result=mycursor.fetchall()
    for i in result:
        print(i)
#Vaccination data
def insert_vaccinationdata():
    sql=("insert into vaccination_data(V_Name,age_limit,dose1,dose2,total) values (%s,%s,%s,%s,%s)")
    V_Name=input("enter your vaccination name:")
    age_limit=input("enter the age limit:")
    dose1=input("It is dose1:")
    dose2=input("It is dose2:")
    total=int(input("enter total vaccination count:"))
    val=(V_Name,age_limit,dose1,dose2,total)
    mycursor.execute(sql,val)
    mydb.commit()
    print("Vaccination Data saved sucessfuly")
def view_vaccinationdata():
    mycursor.execute("select*from vaccination_data")
    result=mycursor.fetchall()
    for i in result:
        print(i)
#ALUMINI RECORD
def insert_campdata():
    sql=("insert into camp_data(C_No,Pl_Name,child,adult,old,district,state,country,total) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    C_No=int(input("enter your camp no:"))
    Pl_Name=input("enter your place name:")
    child=input("are you child:")
    adult=input("are you adult:")
    old=input("are you old:")
    district=input("enter the district:")
    state=input("enter the state:")
    country=input("enter the country:")
    total=int(input("enter total no of vaccination held:"))
    val=(C_No,Pl_Name,child,adult,old,district,state,country,total)
    mycursor.execute(sql,val)
    mydb.commit()
    print("camp data saved sucessfully")
def view_campdata():
    mycursor.execute("select*from camp_data")
    result=mycursor.fetchall()
    for i in result:
        print(i)
#INSTRUCTION FOR OUTPUT
print("1->insert_countrydata")
print("2->insert_statedata")
print("3->insert_districtdata")
print("4->insert_Patientdata")
print("5->insert_vaccinationdata")
print("6->insert_campdata")
print("7->view_countrydata")
print("8->view_statedata")
print("9->view_districtdata")
print("10->view_Patientdata")
print("11->view_vaccinationdata")
print("12->view_campdata")
#OUTPUT EXECUTION
try:
    user=int(input("enter any number:"))
    if user==1:
        insert_countrydata()
    elif user==2:
        insert_statedata()
    elif user==3:
        insert_districtdata()
    elif user==4:
        insert_Patientdata()
    elif user==5:
        insert_vaccinationdata()
    elif user==6:
        insert_campdata()
    elif user==7:
        view_countrydata()
    elif user==8:
        view_statedata()
    elif user==9:
        view_districtdata()
    elif user==10:
        view_Patientdata()
    elif user==11:
        view_vaccinationdata()
    elif user==12:
        view_campdata()
    else:
        print("select 1 to 12 numbers only")
except:
    print("enter only numbers")
print(x)