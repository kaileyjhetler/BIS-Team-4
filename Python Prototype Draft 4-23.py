from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import tkinter as tk

import random
import datetime

root = Tk()
root.geometry("1100x950+0+0")
root.title("NLG Order Processing")
root.configure(background = 'light blue')

total_cost = 0

def Exit():
    root.destroy()
    return

def OrderNum():
    order1=random.randint(1000, 10000)
    order2=('FW'+str(order1))
    ordnum.set(order2)

def TotalCost():
    total_cost = 0
    if cmdCustomFitting.get() == "None":
        total_cost = total_cost + 0
    elif cmdCustomFitting.get() == "Iron Fitting-$125":
        total_cost = total_cost + 125
    elif cmdCustomFitting.get() == "Wood and Hybrid Fitting-$125":
        total_cost = total_cost + 125
    elif cmdCustomFitting.get() == "Full Set Fitting-$225":
        total_cost = total_cost + 225
    elif cmdCustomFitting.get() == "Putter Analysis-$75":
        total_cost = total_cost + 75
    else:
        total_cost = total_cost + 0
    
    
    if cmdClubRepair.get() == "None":
        total_cost = total_cost + 0
    elif cmdClubRepair.get() == "Grip installation-$4/each":
        total_cost = total_cost + 4
    elif cmdClubRepair.get() == "Save Grip-$6/each":
        total_cost = total_cost + 6
    elif cmdClubRepair.get() == "Lengthen Shaft-$8/each":
        total_cost = total_cost + 8
    elif cmdClubRepair.get() == "Loft Adjustments-$5/each":
        total_cost = total_cost + 5
    elif cmdClubRepair.get() == "Lie Adjustments-$5/each":
        total_cost = total_cost + 5
    elif cmdClubRepair.get() == "Re-Shaft/Shaft Installation-$15/each":
        total_cost = total_cost + 15
    elif cmdClubRepair.get() == "Save Adapter-$8/each":
        total_cost = total_cost + 8
    else:
        total_cost = total_cost + 0
    

    if cmdPrivateLesson.get() == "None":
        total_cost = total_cost + 0
    elif cmdPrivateLesson.get() == "Basic Birdie: One-Hour Lesson-$75":
        total_cost = total_cost + 75
    elif cmdPrivateLesson.get() == "Eager Eagle: (4) One-Hour Lessons-$275":
        total_cost = total_cost + 275
    elif cmdPrivateLesson.get() == "Double Eagle: (8) One-Hour Lessons-$500":
        total_cost = total_cost + 500
    else:
        total_cost = total_cost + 0

    
    if cmdSimulation.get() == "None":
        total_cost = total_cost + 0
    elif cmdSimulation.get() == "30 Minute Range-$10":
        total_cost = total_cost + 10
    elif cmdSimulation.get() == "30 Minute Range-$10":
        total_cost = total_cost + 10
    elif cmdSimulation.get() == "9 Hole Sim-Golf-$20/person":
        total_cost = total_cost + 20
    elif cmdSimulation.get() == "18 Hole Sim-Golf-$30/person":
        total_cost = total_cost + 30
    else:
        total_cost = total_cost + 0

    lbltcost["text"] = "Total cost: $" +str(total_cost)
    

EmpUsername=StringVar()
EmpPassword=StringVar()
CustID=StringVar()
F_name=StringVar()
L_name=StringVar()
Email=StringVar()
Cust_phone_num=StringVar()
discountcode=StringVar()
discountamount=StringVar
Usercardname=StringVar()
Usercardnum=StringVar()
Cardexpdate=StringVar()
Usersocialsec=StringVar()
ordnum=StringVar()
Service_num=StringVar()
Billing_total=StringVar()
Totalcost=StringVar("")


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
RightInsideLFF=Frame(RF, width=300, height=300, bd=8, relief = "raise")
RightInsideLFF.pack(side=TOP)

lblInfo = Label (Tops, font=("times", 50, 'bold'), text="    Next Level Golf Order Processing    ", bd=10, anchor="w")
lblInfo.grid(row=0, column=0)

#Log In Page 
lblLogIn=Label(LeftInsideLF,font=('times', 14, 'bold'),text="Employee Login",fg='black',bd=10,anchor='w')
lblLogIn.grid(row=0, column=0)
TextUsername=Entry(LeftInsideLF, font=('times', 12), width = 11, textvariable="EmpUsername").grid(row=1, column=1) #Enter username here
lblUsername=Label(LeftInsideLF, font=('times', 12), width=11, text="Username:", bd=10, anchor="w").grid(row=1, column=0)#Prompt username entry here
TextPassword=Entry(LeftInsideLF,font=('times', 12), width=11, textvariable='EmpPassword').grid(row=2, column=1)#Enter password here
lblPassword=Label(LeftInsideLF, font=('times', 12), width=11, text="Password:", bd=10, anchor="w").grid(row=2, column=0)#Prompt password entry here

#Log in Button
btnlogin = Button(LeftInsideLF, pady=8, bd=8, fg="black",font=('times', 12), width=11, text="Login").grid(row=3, column=0)

#Returning
lblCustInfo=Label(LeftInsideLFLF,font=('times', 14, 'bold'),text="Customer Information",fg='black',bd=10,anchor='w')
lblCustInfo.grid(row=0, column=0)
cmdReturningCustomer=Checkbutton(LeftInsideLFLF, font=('times', 12), text='Returning Customer (ID only)' , width=30) #Prompt user to indicate whether customer is returning 
cmdReturningCustomer.grid(row=1, column =0)

#Customer ID
lblCustomerID=Label(LeftInsideLFLF, font=('times', 12), width=11, text="Customer ID:", bd=10)
lblCustomerID.grid(row=3, column=0)
TextCustomerID=Entry(LeftInsideLFLF, font=('times', 12), textvariable='CustID')
TextCustomerID.grid(row=3, column=1)

#New Customer First Name
TextNewCustFName=Entry(LeftInsideLFLF, font=('times', 12), textvariable='F_name')
TextNewCustFName.grid(row=4, column=1)
lblNewCustFName=Label(LeftInsideLFLF, font=('times', 12), width=11, text="First Name:", bd=10)
lblNewCustFName.grid(row=4, column=0)
#New Customer Last Name
TextNewCustLName=Entry(LeftInsideLFLF, font=('times', 12), textvariable='L_name')
TextNewCustLName.grid(row=5, column=1)
lblNewCustLName=Label(LeftInsideLFLF, font=('times', 12), width=11, text="Last Name:", bd=10)
lblNewCustLName.grid(row=5, column=0)
#New Customer EMail
TextNewCustEMail=Entry(LeftInsideLFLF, font=('times', 12), textvariable='Email:')
TextNewCustEMail.grid(row=6, column=1)
lblNewCustEMail=Label(LeftInsideLFLF, font=('times', 12), width=11, text="Email:", bd=10)
lblNewCustEMail.grid(row=6, column=0)
#New Customer Phone 
TextNewCustPhone=Entry(LeftInsideLFLF, font=('times', 12), textvariable='User_phone_num')
TextNewCustPhone.grid(row=7, column=1)
lblNewCustPhone=Label(LeftInsideLFLF, font=('times', 12), width=11, text="Phone Number:", bd=10)
lblNewCustPhone.grid(row=7, column=0)

#Services entry
lblServiceSelect=Label(RightInsideLF,font=('times', 14, 'bold'),text="Service Selection",fg='black',bd=10,anchor='w')
lblServiceSelect.grid(row=0, column=0)
#Custom Fitting
lblCustomFitting=Label(RightInsideLF, font=('times',12,),text="Custom Fitting", fg='black',bd=10,anchor='w')
lblCustomFitting.grid(row=1, column=0)
cmdCustomFitting=ttk.Combobox(RightInsideLF,font=('times',12))
cmdCustomFitting['value']=('None','Iron Fitting-$125','Wood and Hybrid Fitting-$125','Full Set Fitting-$225','Putter Analysis-$75')
cmdCustomFitting.grid(row=1, column=1)
#Club Repair
lblClubRepair=Label(RightInsideLF, font=('times',12,),text="Club Repair", fg='black',bd=10,anchor='w')
lblClubRepair.grid(row=2, column=0)
cmdClubRepair=ttk.Combobox(RightInsideLF,font=('times',12))
cmdClubRepair['value']=('None','Grip installation-$4/each','Save Grip-$6/each','Lengthen Shaft-$8/each','Loft Adjustments-$5/each','Lie Adjustments-$5/each',
'Re-Shaft/Shaft Installation-$15/each','Save Adapter-$8/each')
cmdClubRepair.grid(row=2, column=1)
#Private Lesson
lblPrivateLesson=Label(RightInsideLF, font=('times',12,),text="Private Lesson", fg='black',bd=10,anchor='w')
lblPrivateLesson.grid(row=3, column=0)
cmdPrivateLesson=ttk.Combobox(RightInsideLF,font=('times',12))
cmdPrivateLesson['value']=('None','Basic Birdie: One-Hour Lesson-$75','Eager Eagle: (4) One-Hour Lessons-$275','Double Eagle: (8) One-Hour Lessons-$500')
cmdPrivateLesson.grid(row=3, column=1)
#Simulation
lblSimulation=Label(RightInsideLF, font=('times',12,),text="Simulation", fg='black',bd=10,anchor='w')
lblSimulation.grid(row=4, column=0)
cmdSimulation=ttk.Combobox(RightInsideLF,font=('times',12))
cmdSimulation['value']=('None','30 Minute Range-$10','60 Minute Range-$17','9 Hole Sim-Golf-$20/person','18 Hole Sim-Golf-$30/person')
cmdSimulation.grid(row=4, column=1)
#Discount Code
TextDiscountCode=Entry(RightInsideLF, font=('times', 12), textvariable='discountcode')
TextDiscountCode.grid(row=5, column=1)
lblDiscountCode=Label(RightInsideLF, font=('times', 12), text="Enter discount code (if applicable):",fg='black', bd=10, anchor='w')
lblDiscountCode.grid(row=5, column=0)


#Confirmation Page
lblConfPage=Label(RightInsideLFF, font=('times', 14,'bold'), text='Confirmation Page',fg='black', bd=10)
lblConfPage.grid(row=0, column=0)
lblbilltotal=Label(RightInsideLFF, font=('times', 12), width=11, text="Billing Total:", bd=10)
lblbilltotal.grid(row=3, column=0)
lbltcost=Label(RightInsideLFF, font=('times', 12), width=20, text="Total Cost: $", bd=10)
lbltcost.grid(row=3, column=1)

#Total cost button
btnTotalCost = Button(RightInsideLF, pady=8, bd=8, fg="black",font=('times', 12), width=16, text="Calculate Total Cost", command=TotalCost).grid(row=6, column=1)

#Exit Button
btnSubmit = Button(RightInsideLFF, pady=8, bd=8, fg="black",font=('times', 12), width=11, text="Submit", command=Exit).grid(row=5, column=2)



root.mainloop()
