from tkinter import *
import pandas as pd
import numpy as np
def getvals():
    # f=open("details.txt","a")
    # f.write(f"user {namevalue.get()} Phone is {passvalue.get()} gender is {gendervalue.get()} Emergancy{emergancyvalue.get()} Payment Mode is {modevalue} foodservices {foodservices}")
    # f.close()

    #using pandas
    a=namevalue.get()
    b=passvalue.get()
    c=gendervalue.get()
    d=emergancyvalue.get()
    e=modevalue.get()
    f=foodservices.get()
    #list1={"Name":a,"Phone Number":b,"Gender":c,"Emergancy":d,"Payment Mode":e}
    list1=[a,b,c,d,e,f]
    df = pd.DataFrame(list1,["Name","Phone Number","Gender","Emergancy","Payment Mode","Food Services"])
    f = open("details.txt","a")
    f.write(str(df))
    f.close()


root=Tk()

root.geometry("644x344")
root.maxsize(644,344)
root.minsize(644,344)


Label(root,text="Welcome To Your Travels Agency",font=("comicsans 19 bold"),pady=15,fg="red",bg="light yellow").grid(row=0,column=4)

Name = Label(root,text="Name",pady=5,padx=50)
Phone = Label(root,text="Phone",pady=5)
Gender = Label(root,text="Gender",pady=5)
Emergancy = Label(root,text="Emergancy",pady=5)
Payment_mode= Label(root,text="Payment Mode",pady=5)
Name.grid(row=1,column=3)
Phone.grid(row=2,column=3)
Gender.grid(row=3,column=3)
Emergancy.grid(row=4,column=3)
Payment_mode.grid(row=5,column=3)

namevalue = StringVar()
passvalue=StringVar()
gendervalue=StringVar()
emergancyvalue=StringVar()
modevalue=StringVar()
foodservices = IntVar()

nameentry= Entry(root,textvariable=namevalue)
passentry= Entry(root,textvariable=passvalue)
genderentry= Entry(root,textvariable=gendervalue)
modeentry= Entry(root,textvariable=modevalue)
emergancyentry= Entry(root,textvariable=emergancyvalue)

nameentry.grid(row=1,column=4)
passentry.grid(row=2,column=4)
genderentry.grid(row=3,column=4)
emergancyentry.grid(row=4,column=4)
modeentry.grid(row=5,column=4)

foodservice = Checkbutton(text="Want To Prebook your meal??",variable=foodservices).grid(row=6,column=4)


b1 = Button(text="Submit Now",bg="light blue",fg="red",font=("comicsans 10 bold"),command=getvals).grid(row=7,column=4)

root.mainloop()