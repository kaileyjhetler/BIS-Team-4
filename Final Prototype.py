'''
Program: Next Level Golf Payment System
Developers: The Fantastic Five
Spring 2021
'''

from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import tkinter as tk

import random
import datetime

root = Tk()
root.geometry("1100x950+0+0") #Configure size of application window
root.title("NXL Order Processing") #Title the file
root.configure(background = 'light blue') #Configure the background of application window

total_cost = 0 #Set initial total cost to zero

def Exit(): #Define function for exit process
    root.destroy()
    return



def TotalCost(): #Define function for total cost
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
    elif cmdClubRepair.get() == "Grip installation-$4":
        total_cost = total_cost + 4
    elif cmdClubRepair.get() == "Save Grip-$6":
        total_cost = total_cost + 6
    elif cmdClubRepair.get() == "Lengthen Shaft-$8":
        total_cost = total_cost + 8
    elif cmdClubRepair.get() == "Loft Adjustments-$5":
        total_cost = total_cost + 5
    elif cmdClubRepair.get() == "Lie Adjustments-$5":
        total_cost = total_cost + 5
    elif cmdClubRepair.get() == "Re-Shaft/Shaft Installation-$15":
        total_cost = total_cost + 15
    elif cmdClubRepair.get() == "Save Adapter-$":
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
    elif cmdSimulation.get() == "9 Hole Sim-Golf-$20":
        total_cost = total_cost + 20
    elif cmdSimulation.get() == "18 Hole Sim-Golf-$30":
        total_cost = total_cost + 30
    else:
        total_cost = total_cost + 0

    lbltcost["text"] = "Total cost: $" +str(total_cost) #Output the total cost of services purchased in USD
    

EmpUsername=StringVar()
EmpPassword=StringVar()
CustID=StringVar()
F_name=StringVar()
L_name=StringVar()
Email=StringVar()
Cust_phone_num=StringVar()
discountCode=StringVar()
discountAmount=StringVar
usercardName=StringVar()
usercardNum=StringVar()
cardExpDate=StringVar()
userSocialSec=StringVar()
ordNum=StringVar()
Service_num=StringVar()
Billing_total=StringVar()
TotalCost=StringVar("")


Tops=Frame(root, width=1350, height=50, bd=16, relief = "flat") #Configure the size and appearance of the top frame
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

lblInfo = Label (Tops, font=("times", 50, 'bold'), text="    Next Level Golf Order Processing    ", bd=10, anchor="w") #Display the title of the system
lblInfo.grid(row=0, column=0)

#Log In Page 
lblLogIn=Label(LeftInsideLF,font=('times', 14, 'bold'),text="Employee Login",fg='black',bd=10,anchor='w')
lblLogIn.grid(row=0, column=0)
TextUsername=Entry(LeftInsideLF, font=('times', 12), width = 11, textvariable="EmpUsername").grid(row=1, column=1) #Enter username here
lblUsername=Label(LeftInsideLF, font=('times', 12), width=11, text="Username:", bd=10, anchor="w").grid(row=1, column=0)#Prompt username entry here
TextPassword=Entry(LeftInsideLF,font=('times', 12), width=11, textvariable='EmpPassword').grid(row=2, column=1)#Enter password here
lblPassword=Label(LeftInsideLF, font=('times', 12), width=11, text="Password:", bd=10, anchor="w").grid(row=2, column=0)#Prompt password entry here


#Log in Button
btnLogin = Button(LeftInsideLF, pady=8, bd=8, fg="black",font=('times', 12), width=11, text="Login").grid(row=3, column=0)#User submits login information and continues to next page      


#Returning
lblCustInfo=Label(LeftInsideLFLF,font=('times', 14, 'bold'),text="Customer Information",fg='black',bd=10,anchor='w')
lblCustInfo.grid(row=0, column=0)
cmdReturningCustomer=Checkbutton(LeftInsideLFLF, font=('times', 12), text='Returning Customer (ID only)' , width=30) #Prompt user to indicate whether customer is returning 
cmdReturningCustomer.grid(row=1, column =0)

#Customer ID
lblCustomerID=Label(LeftInsideLFLF, font=('times', 12), width=11, text="Customer ID:", bd=10) #Prompt user to enter returning customer ID
lblCustomerID.grid(row=3, column=0)
TextCustomerID=Entry(LeftInsideLFLF, font=('times', 12), textvariable='CustID')#Enter returning customer's ID
TextCustomerID.grid(row=3, column=1)

#New Customer First Name
TextNewCustFName=Entry(LeftInsideLFLF, font=('times', 12), textvariable='F_name')#Enter new customer's first name
TextNewCustFName.grid(row=4, column=1)
lblNewCustFName=Label(LeftInsideLFLF, font=('times', 12), width=11, text="First Name:", bd=10)#Prompt user to enter new customer's first name
lblNewCustFName.grid(row=4, column=0)
#New Customer Last Name
TextNewCustLName=Entry(LeftInsideLFLF, font=('times', 12), textvariable='L_name') #Enter new customer's last name
TextNewCustLName.grid(row=5, column=1)
lblNewCustLName=Label(LeftInsideLFLF, font=('times', 12), width=11, text="Last Name:", bd=10)#Prompt new customer's last name
lblNewCustLName.grid(row=5, column=0)
#New Customer EMail
TextNewCustEMail=Entry(LeftInsideLFLF, font=('times', 12), textvariable='Email:')#Enter new customer's email 
TextNewCustEMail.grid(row=6, column=1)
lblNewCustEMail=Label(LeftInsideLFLF, font=('times', 12), width=11, text="Email:", bd=10)#Prompt new customer's email
lblNewCustEMail.grid(row=6, column=0)
#New Customer Phone 
TextNewCustPhone=Entry(LeftInsideLFLF, font=('times', 12), textvariable='User_phone_num')#Enter new customer's phone number 
TextNewCustPhone.grid(row=7, column=1)
lblNewCustPhone=Label(LeftInsideLFLF, font=('times', 12), width=11, text="Phone Number:", bd=10)#Prompt new customer's phone number 
lblNewCustPhone.grid(row=7, column=0)

#Services entry
lblServiceSelect=Label(RightInsideLF,font=('times', 14, 'bold'),text="Service Selection",fg='black',bd=10,anchor='w')#Prompt user to enter services being purchased
lblServiceSelect.grid(row=0, column=0)
#Custom Fitting
lblCustomFitting=Label(RightInsideLF, font=('times',12,),text="Custom Fitting", fg='black',bd=10,anchor='w')
lblCustomFitting.grid(row=1, column=0)
cmdCustomFitting=ttk.Combobox(RightInsideLF,font=('times',12))#Prompt to select applicable custom fitting
cmdCustomFitting['value']=('None','Iron Fitting-$125','Wood and Hybrid Fitting-$125','Full Set Fitting-$225','Putter Analysis-$75') #Display types of custom fitting and associated costs
cmdCustomFitting.grid(row=1, column=1)
#Club Repair
lblClubRepair=Label(RightInsideLF, font=('times',12,),text="Club Repair", fg='black',bd=10,anchor='w')
lblClubRepair.grid(row=2, column=0)
cmdClubRepair=ttk.Combobox(RightInsideLF,font=('times',12)) #Prompt to select applicable club repair
cmdClubRepair['value']=('None','Grip installation-$4','Save Grip-$6','Lengthen Shaft-$8','Loft Adjustments-$5','Lie Adjustments-$5',
'Re-Shaft/Shaft Installation-$15','Save Adapter-$8') #Display types of club repair and associated costs
cmdClubRepair.grid(row=2, column=1)
#Private Lesson
lblPrivateLesson=Label(RightInsideLF, font=('times',12,),text="Private Lesson", fg='black',bd=10,anchor='w')#Prompt to select applicable private lessons
lblPrivateLesson.grid(row=3, column=0)
cmdPrivateLesson=ttk.Combobox(RightInsideLF,font=('times',12))
cmdPrivateLesson['value']=('None','Basic Birdie: One-Hour Lesson-$75','Eager Eagle: (4) One-Hour Lessons-$275','Double Eagle: (8) One-Hour Lessons-$500')#Display types of private lessons and associated costs
cmdPrivateLesson.grid(row=3, column=1)
#Simulation
lblSimulation=Label(RightInsideLF, font=('times',12,),text="Simulation", fg='black',bd=10,anchor='w')#Prompt to select applicable simulation
lblSimulation.grid(row=4, column=0)
cmdSimulation=ttk.Combobox(RightInsideLF,font=('times',12))
cmdSimulation['value']=('None','30 Minute Range-$10','60 Minute Range-$17','9 Hole Sim-Golf-$20','18 Hole Sim-Golf-$30')#Display types of simulation and associated costs
cmdSimulation.grid(row=4, column=1)
#Discount Code
lblDiscountCode=Label(RightInsideLF, font=('times', 12), text="Enter discount code (if applicable):",fg='black', bd=10, anchor='w')#Prompt entry of any appropriate discount code
lblDiscountCode.grid(row=5, column=0)
TextDiscountCode=Entry(RightInsideLF, font=('times', 12), textvariable='discountcode')#Enter discount code
TextDiscountCode.grid(row=5, column=1)



#Confirmation Page
lblConfPage=Label(RightInsideLFF, font=('times', 14,'bold'), text='Confirmation Page',fg='black', bd=10)#Display confirmation of purchase
lblConfPage.grid(row=0, column=0)
lblBillTotal=Label(RightInsideLFF, font=('times', 12), width=20, text="BillingTotal: ", bd=10)
lblBillTotal.grid(row=3, column=0)
lbltcost=Label(RightInsideLFF, font=('times', 12), width=20, text="Total Cost: $", bd=10) #Display total cost in USD
lbltcost.grid(row=3, column=1)

#Total cost button
btnTotalCost = Button(RightInsideLF, pady=8, bd=8, fg="black",font=('times', 12), width=16, text="Calculate Total Cost", command=TotalCost).grid(row=6, column=1)#Calculate total cost

#Exit Button
btnSubmit = Button(RightInsideLFF, pady=8, bd=8, fg="black",font=('times', 12), width=11, text="Submit", command=Exit).grid(row=5, column=2)#Exit system



root.mainloop()
