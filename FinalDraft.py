# Login page __init__ file for user authentication
from tkinter import *
from tkinter import font
from tkinter.font import Font
from tkinter import messagebox
# Input Parameter Name, Id, Email, Password
# Creating a curser object for mysql query output
# Ankit is my MySQL password
import mysql.connector
#Main window of the Meeting Schedular API
root=Tk()
root.geometry('700x700')
root.title("Email Verifier -By YOUR NAME HERE")     # Change Name Here
mydb=mysql.connector.connect(host='localhost',database="id",user='root',password='Ankit')
mycursor=mydb.cursor()
try:
    mycursor.execute("Create table user(S_id varchar(20) primary key, name varchar(20), email varchar(20)")
    mycursor.execute("Create table passcode(id varchar(20), password varchar(40), foreign key(id) references user(S_id)")
except:
    print("")
#Check value Funtion
def getInput():
    value=(Name.get(),uID.get(),Email.get(),Password.get())
    sql="select * from user, passcode where name=%s and s_id=%s and email=%s and password=%s"
    mycursor.execute(sql,value)
    nameList=[]
    for i in mycursor:
        nameList.append(i)
    if(nameList == []):
        messagebox.askretrycancel("Not Found","Wrong Credientials Entered !")
    else:
        messagebox.showinfo("Welcome","Logged In !")

# Declaring Variables
headingFont=Font(family="Times New Roman",size=42)
subHeadingFont=Font(family="Times New Roman",size=20)
buttonFont=Font(family="Times New Roman",size=12)

# Main Panel
label=Label(root,text="Email Verifier",font=headingFont).pack()
label=Label(root,text="-Made by Your Name Here",font=subHeadingFont).pack()     # Change Name Here

label=Label(root,text="Name",font=subHeadingFont).place(x=220,y=200)
label=Label(root,text="ID",font=subHeadingFont).place(x=220,y=250)
label=Label(root,text="Email",font=subHeadingFont).place(x=220,y=300)
label=Label(root,text="Password",font=subHeadingFont).place(x=220,y=350)

# Entry Points
Name=Entry(root,borderwidth=5,width=50)
Name.place(x=330,y=200)
uID=Entry(root,borderwidth=5,width=50)
uID.place(x=330,y=250)
Email=Entry(root,borderwidth=5,width=50)
Email.place(x=330,y=300)
Password=Entry(root,borderwidth=5,width=50,show="*")
Password.place(x=330,y=350)
SubmitButton=Button(root,text="Submit",font=buttonFont,width=20,height=5,command=getInput)
SubmitButton.place(x=255,y=500)


root.mainloop()
