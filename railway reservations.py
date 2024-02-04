import random
from random import randint as i
PNR = i(4000000000,7000000000)
passenger={}
list=[]
list1=[12345,"MAS EXPRESS","Erode","Chennai central",165,720,560,110]
list2=[12346,"Guruvayur express","Chennai central","vellore",100,720,450,55]
def signin():
    global list
    user =input("Enter user name:")
    phone=int(input("Enter phone number:"))
    if (len(str(phone))==10):
        password=input("Enter password:")
        cnf=input("Confirm the password:")
        if(password!=cnf):
            print("PASSWORD DOES'NT MATCH, RECHECK YOUR PASSWORD")
            signin()
        else:
            x=[user,password]
            list.append(x)
        print("sign-in successful!!!")
        login()
    else:
        print("Enter a valid number:")
        signin()
def login():
    global list
    user=input("Enter username:")
    password=input("Enter the password:")
    if user=="admin" and password=="itsmepeeps":
        i=int(input("Admin="))
        if(i==1):
            for i in passenger.values():
                print(i)
        elif(i==2):
            print(list)
        login()
    elif[user,password] in list:
        print("LOGIN SUCCESSFUL!")
    else:
        print("INCORRECT LOGIN!")
        x=int(input("Enter 1 to signin \n Enter 2 to login again"))
        if(x==1):
            signin()
        elif(x==2):
            login()
def book1():
    global PNR,passengers,list1,list2
    from prettytable import PrettyTable as t
    table=t(["Name","Age","Gender","Seat","Seat no.","Fare","Train number"])
    x=int(input("Enter your choice(4 for 2S/6 for AC):"))
    seat1=x+1
    if x==6:
        seat="AC"
        fare=550
    else:
        seat="2S"
        fare=165 
    people=int(input("Enter total tickets to be booked:"))
    if(people>list1[x]):
        print("sorry number of seats available is low")
        book1(list1)
    else:
        for i in range(people):
            name=input("Enter the name of passenger:")
            age=int(input("Enter the age:"))
            gender=input("Enter gender(M/f/T):")
            x=[name,age,gender,seat,list1[seat1],fare,list1[0]]
            list1[seat1]=list1[seat1]-1
            table.add_row(x)
    passenger[PNR]=table
    print("pnr no:",PNR)
    print("The train number :",12345)
    PNR+=1
    print(table)
    print("The totale cost is",people*fare)
def book2():
    global PNR,passengers,list1,list2
    from prettytable import PrettyTable as t
    table=t(["Name","Age","Gender","Seat","Seat no.","Fare","Train number"])
    x=int(input("Enter your choice(4 for 2S/6 for AC):"))
    seat1=x+1
    if x==6:
        seat="AC"
        fare=550
    else:
        seat="2S"
        fare=165 
    people=int(input("Enter total tickets to be booked:"))
    if(people>list2[x]):
        print("sorry number of seats available is low")
        book1(list2)
    else:
        for i in range(people):
            name=input("Enter the name of passenger:")
            age=int(input("Enter the age:"))
            gender=input("Enter gender(M/F/T):")
            x=[name,age,gender,seat,list1[seat1],fare,list1[0]]
            list2[seat1]=list2[seat1]-1
            table.addrow(x)
    passenger[PNR]=table
    print("pnr no:",PNR)
    print("The train number :",12346)
    PNR+=1
    print(table)
    print("The totale cost is",people*fare)
def check():
    p=int(input("Enter the pne:"))
    if (p in passenger):
        print(passenger[p])
    else:
        print("Enter correct pnr")
def book():
    train_no=int(input("train no:"))
    if train_no in list1:
        print("availabe seats:\n{} for 2S \n {} for AC".format(list1[5],list1[7]))
        book1()
    elif train_no in list2:
        print("available seats :\n{} for 2S\n {} for AC".format(list2[5],list1[7]))
def cancel():
    p=int(input("Enter the pnr number:"))
    del passenger[p]
    print("Ticket cancelled successfully")
def train():
    from prettytable import PrettyTable as t
    global list1,list2
    global table
    head=["Train no","Train name","Start","End","2S Fare","seats","ACFare","ACSeats"]
    table=t(head)
    table.add_row(list1)
    table.add_row(list2)
    print(table)
    book()
while True:
    print("Welcome\n\t\tTo\n\t\t\tVVV")
    x=input("New user?(Y/N):")
    if x=="Y":
        signin()
    else:
        login()
    while True:
        print("'1.book tivket\n 2.PNR Status\n3.Cancel ticket\n4.Logout'")
        x=int(input("Enter your choice:"))
        if(x==1):
            train()
        elif(x==2):
            check()
        elif(x==3):
            cancel()
        elif(x==4):
            break
    print("{:*^100}".format("THANK YOU!!!"))
    _=input()