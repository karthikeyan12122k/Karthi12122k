import datetime
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="susmi@123#sql",
    database="travel_db"
)
mycursor=mydb.cursor()
x=datetime.datetime.now()
f=open("file1.txt","r")
print(f.read())
#PACKAGE DATA
def insert_Packagedata():
    sql=("insert into Package_data(World_Tour,All_India,Going_Date,PassOut_Date) values (%s,%s,%s,%s)")
    World_Tour=input("World Tour-Type Yes OR No:")
    All_India=input("AllIndia Tour-Type Yes OR No:")
    Going_Date=input("enter the going date:")
    PassOut_Date=input("enter the pass out date:")
    val=(World_Tour,All_India,Going_Date,PassOut_Date)
    mycursor.execute(sql,val)
    mydb.commit()
    print("Packagedata saved sucessfuly")
def view_Packagedata():
    mycursor.execute("select*from Package_data")
    result=mycursor.fetchall()
    for i in result:
        print(i)
def insert_cardata():
    sql=("insert into car_data(TypeOfCar,Car_Name,Members_count,email_id,Ph_No) values (%s,%s,%s,%s,%s)")
    TypeOfCar=input("enter the Type of Car:")
    Car_Name=input("enter the car name:")
    Members_count=int(input("enter the members count:"))
    email_id=input("enter the email id:")
    Ph_No=int(input("enter the phone number:"))
    val=(TypeOfCar,Car_Name,Members_count,email_id,Ph_No)
    mycursor.execute(sql,val)
    mydb.commit()
    print("Cardata saved sucessfuly")
def view_cardata():
    mycursor.execute("select*from car_data")
    result=mycursor.fetchall()
    for i in result:
        print(i)
#BUS DATA
def insert_busdata():
    sql=("insert into bus_data(TypeOfBus,Seat_Type,Members_count,Email_Id,Ph_No) values (%s,%s,%s,%s,%s)")
    TypeOfBus=input("enter the Type of Bus:")
    Seat_Type=input("enter the Type of Seat:")
    Members_count=int(input("enter the members count:"))
    Email_Id=input("enter the email id:")
    Ph_No=int(input("enter the phone number:"))
    val=(TypeOfBus,Seat_Type,Members_count,Email_Id,Ph_No)
    mycursor.execute(sql,val)
    mydb.commit()
    print("Busdata saved sucessfuly")
def view_busdata():
    mycursor.execute("select*from bus_data")
    result=mycursor.fetchall()
    for i in result:
        print(i)
#AIRWAYS DATA
def insert_airwaysdata():
    sql=("insert into Airway_data(Airways_Name,Members_count,Place,email_id,Ph_No) values (%s,%s,%s,%s,%s)")
    Airways_Name=input("enter the Airways name:")
    Place=input("enter the place to be go:")
    Members_count=int(input("enter the members count:"))
    email_id=input("enter the email id:")
    Ph_No=int(input("enter the phone number:"))
    val=(Airways_Name,Members_count,Place,email_id,Ph_No)
    mycursor.execute(sql,val)
    mydb.commit()
    print("Airwaydata saved sucessfuly")
def view_airwaysdata():
    mycursor.execute("select*from Airway_data")
    result=mycursor.fetchall()
    for i in result:
        print(i)
#ROOMSDATA
def insert_roomsdata():
    sql=("insert into Rooms_data(Name,Count,Date,Male_count,Female_count,TypeOfHotel,Room_Type,Address,Email_Id,Ph_No) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    Name=input("enter your name:")
    Count=int(input("enter the members count:"))
    Date=input("enter the date:")
    Male_count=int(input("enter the male count:"))
    Female_count=int(input("enter the female count:"))
    TypeOfHotel=input("enter the type of hotel:")
    Room_Type=input("enter the type of room:")
    Address=input("enter your address:")
    Email_Id=input("enter the email id:")
    Ph_No=int(input("enter the phone number:"))
    val=(Name,Count,Date,Male_count,Female_count,TypeOfHotel,Room_Type,Address,Email_Id,Ph_No)
    mycursor.execute(sql,val)
    mydb.commit()
    print("Roomsdata saved sucessfuly")
def view_roomsdata():
    mycursor.execute("select*from Rooms_data")
    result=mycursor.fetchall()
    for i in result:
        print(i)
#COUNTRY DATA
def insert_countrydata():
    sql=("insert into Country_data(C_Name,Days,Place,Package_Type,address,email_id,ph_no) values (%s,%s,%s,%s,%s,%s,%s)")
    C_Name=input("enter the Country name:")
    Days=int(input("enter how many days:"))
    Place=input("enter the place to be go:")
    Package_Type=input("enter the package type:")
    address=input("enter your addresss:")
    email_id=input("enter the email id:")
    ph_no=int(input("enter the phone number:"))
    val=(C_Name,Days,Place,Package_Type,address,email_id,ph_no)
    mycursor.execute(sql,val)
    mydb.commit()
    print("countrydata saved sucessfuly")
def view_countrydata():
    mycursor.execute("select*from Country_data")
    result=mycursor.fetchall()
    for i in result:
        print(i)
#FEEDBACK DATA
def insert_feedbackdata():
    sql=("insert into FeedBack_data(Name,Age,Feedback,address,email_id,ph_no) values (%s,%s,%s,%s,%s,%s)")
    Name=input("enter your name:")
    Age=int(input("enter your age:"))
    Feedback=input("enter your Feedback:")
    address=input("enter your addresss:")
    email_id=input("enter the email id:")
    ph_no=int(input("enter the phone number:"))
    val=(Name,Age,Feedback,address,email_id,ph_no)
    mycursor.execute(sql,val)
    mydb.commit()
    print("feedbackdata saved sucessfuly")
def view_feedbackdata():
    mycursor.execute("select*from FeedBack_data")
    result=mycursor.fetchall()
    for i in result:
        print(i)
#INSTRUCTION FOR OUTPUT
print("1->Insert Package Data")
print("2->Insert Country Data")
print("3->Insert Airways Data")
print("4->Insert Car Data")
print("5->Insert Bus Data")
print("6->Insert Rooms Data")
print("7->Insert FeedBack Data")
print("8->View Package Data")
print("9->View Country Data")
print("10->View Airways Data")
print("11->View Car Data")
print("12->View Bus Data")
print("13->View Rooms Data")
print("14->View FeedBack Data")
#OUTPUT EXECUTION
try:
    user=int(input("enter your number:"))
    if user==1:
        insert_Packagedata()
    elif user==2:
        insert_countrydata()
    elif user==3:
        insert_airwaysdata()
    elif user==4:
        insert_cardata()
    elif user==5:
        insert_busdata()
    elif user==6:
        insert_roomsdata()
    elif user==7:
        insert_feedbackdata()
    elif user==8:
        view_Packagedata()
    elif user==9:
        view_countrydata()
    elif user==10:
        view_airwaysdata()
    elif user==11:
        view_cardata()
    elif user==12:
        view_busdata()
    elif user==13:
        view_roomsdata()
    elif user==14:
        view_feedbackdata()
    else:
        ("Enter numbers between 1 to 14 only")
except:
    print("Enter only Numbers")
print(x)