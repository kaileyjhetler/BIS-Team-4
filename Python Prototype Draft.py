from tkinter import *
import tkinter as tkk

import random
import datetime

root = Tk()
root.geometry("1350x850+0+0")
root.title("NLG Order Processing")
root.configure(background = 'light blue')

def Exit():
    qExit = messagebox.askyesno("Order Process System", "Do you want to exit the systme?")
    if qExit > 0:
        root.destroy ()
        return

Tops=Frame(root, width=1350, height=50, bd=16, relief = "flat")
Tops.pack(side=TOP)
LF=Frame(root, width=700, height=650, bd=16, relief="flat")
LF.pack(side=LEFT)
RF=Frame(root, width=600, height=650, bd=16, relief="flat")
RF.pack(side=RIGHT)

Tops.configure(background="light blue")
LF.configure(background="light blue")
RF.configure(background= "light blue")

LeftInsideLF=Frame(LF, width=700, height=100, bd=8, relief= "raise")
LeftInsideLF.pack(side=TOP)
LeftInsideLFLF=Frame(LF, width=700, height=500, bd=8, relief="raise")
LeftInsideLFLF.pack(side=LEFT)

RightInsideLF=Frame(RF, width=700, height=500, bd=8, relief = "raise")
RightInsideLF.pack(side=TOP)
RightInsideLFLF=Frame(RF, width=700, height=500, bd=8, relief = "raise")
RightInsideLFLF.pack(side=RIGHT)

lblInfo = Label (Tops, font=("times", 50, 'bold'), text="    Next Level Golf Order Processing    ", bd=10, anchor="w")
lblInfo.grid(row=0, column=0)

#Log In Page 
TextUsername=Entry(LeftInsideLF, font=('times, 12'), width = 11, textvariable="Username").grid(row=0, column=1)
lblUsername=Label(LeftInsideLF, font=('times, 12'), width=11, text="Username:", bg='white', bd=10).grid(row=0, column=0)
TextPassword=Entry(LeftInsideLF,font=('times, 12'), textvariable='Password').grid(row=1, column=1)
lblPassword=Label(LeftInsideLF, font=('times, 12'), width=11, text="Password:", bg='white', bd=10).grid(row=1, column=0)

#Returning
cmdReturningCustomer=Checkbutton(LeftInsideLFLF, font=('times, 12'), text='Returning Customer (ID only)' , width=30, bg="white")
cmdReturningCustomer.grid(row=0, column =0)

#Customer ID
lblCustomerID=Label(LeftInsideLFLF, font=('times, 12'), width=11, text="Customer ID:", bg='white', bd=10)
lblCustomerID.grid(row=3, column=0)
TextCustomerID=Entry(LeftInsideLFLF, font=('times, 12'), textvariable='Customer ID:')
TextCustomerID.grid(row=3, column=1)

#New Customer First Name
TextNewCustFName=Entry(LeftInsideLFLF, font=('times, 12'), textvariable='First Name:')
TextNewCustFName.grid(row=4, column=1)
lblNewCustFName=Label(LeftInsideLFLF, font=('times, 12'), width=11, text="First Name:", bg='white', bd=10)
lblNewCustFName.grid(row=4, column=0)
#New Customer Last Name
TextNewCustLName=Entry(LeftInsideLFLF, font=('times,12'), textvariable='Last Name:')
TextNewCustLName.grid(row=5, column=1)
lblNewCustLName=Label(LeftInsideLFLF, font=('times, 12'), width=11, text="Last Name:", bg='white', bd=10)
lblNewCustLName.grid(row=5, column=0)
#New Customer EMail
TextNewCustEMail=Entry(LeftInsideLFLF, font=('times, 12'), textvariable='Email:')
TextNewCustEMail.grid(row=6, column=1)
lblNewCustEMail=Label(LeftInsideLFLF, font=('times, 12'), width=11, text="Email:", bg='white', bd=10)
lblNewCustEMail.grid(row=6, column=0)
#New Customer Phone 
TextNewCustPhone=Entry(LeftInsideLFLF, font=('times, 12'), textvariable='Phone Number:')
TextNewCustPhone.grid(row=7, column=1)
lblNewCustPhone=Label(LeftInsideLFLF, font=('times, 12'), width=11, text="Phone Number:", bg='white', bd=10)
lblNewCustPhone.grid(row=7, column=0)


#Next Page Button
btnTotalCost=Button(LeftInsideLFLF, pady=8, bd=8, fg="black", font= ("times", 16, 'italic'), width=11, text= "Next Page", bg="white").grid(row=8, column=1)

root.mainloop()
