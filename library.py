from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime
import tkinter as tk
from tkinter import messagebox
import smtplib
import random



class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Libraey Management System")
        self.root.geometry("1550x800+0+0")


        #=========================variable==========================================
        self.member_var=StringVar()
        self.pnr_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.lateratefine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice=StringVar()



        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="papaya whip",fg="dark green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="papaya whip")
        frame.place(x=0,y=130,width=1530,height=400)



        #=========================DataFrameLeft=====================================


        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="papaya whip",fg="dark green",bd=20,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)


        lblMember=Label(DataFrameLeft,bg="papaya whip",text="Member Type:",font=("arial",12,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)
        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("arial",12,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin Staf","Student","Lecture")
        comMember.grid(row=0,column=1)

        lblPRN_NO=Label(DataFrameLeft,bg="papaya whip",text="PNR no:",font=("arial",12,"bold"),padx=2)
        lblPRN_NO.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,textvariable=self.pnr_var,font=("arial",13,"bold"),width=29)
        txtPRN_NO.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="ID No:",padx=2,pady=4,bg="papaya whip")
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,textvariable=self.id_var,font=("arial",13,"bold"),width=29)
        txtTitle.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,font=("arial",12,"bold"),text="FirstName:",padx=2,pady=6,bg="papaya whip")
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,textvariable=self.firstname_var,font=("arial",13,"bold"),width=29)
        txtFirstName.grid(row=3,column=1)

        
        lblLastName=Label(DataFrameLeft,font=("arial",12,"bold"),text="LastName:",padx=2,pady=6,bg="papaya whip")
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,textvariable=self.lastname_var,font=("arial",13,"bold"),width=29)
        txtLastName.grid(row=4,column=1)

        lblAddress1=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address1:",padx=2,pady=6,bg="papaya whip")
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,textvariable=self.address1_var,font=("arial",13,"bold"),width=29)
        txtAddress1.grid(row=5,column=1)

        
        lblAddress2=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address2:",padx=2,pady=6,bg="papaya whip")
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,textvariable=self.address2_var,font=("arial",13,"bold"),width=29)
        txtAddress2.grid(row=6,column=1)



        lblPostCode=Label(DataFrameLeft,font=("arial",12,"bold"),text="PostCode:",padx=2,pady=4,bg="papaya whip")
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,textvariable=self.postcode_var,font=("arial",13,"bold"),width=29)
        txtPostCode.grid(row=7,column=1)


        lblMobile=Label(DataFrameLeft,font=("arial",12,"bold"),text="Mobile:",padx=2,pady=6,bg="papaya whip")
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,textvariable=self.mobile_var,font=("arial",13,"bold"),width=29)
        txtMobile.grid(row=8,column=1)


        lblBookId=Label(DataFrameLeft,font=("arial",12,"bold"),text="BookId:",padx=2,bg="papaya whip")
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,textvariable=self.bookid_var,font=("arial",13,"bold"),width=29)
        txtBookId.grid(row=0,column=3)


        lblBookTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="BookTitle:",padx=2,bg="papaya whip")
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,textvariable=self.booktitle_var,font=("arial",13,"bold"),width=29)
        txtBookTitle.grid(row=1,column=3)


        lblAuther=Label(DataFrameLeft,font=("arial",12,"bold"),text="Auther Name:",padx=2,pady=6,bg="papaya whip")
        lblAuther.grid(row=2,column=2,sticky=W)
        txtAuther=Entry(DataFrameLeft,textvariable=self.auther_var,font=("arial",13,"bold"),width=29)
        txtAuther.grid(row=2,column=3)

        
        lblDateBorrowed=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Borrowed:",padx=2,pady=6,bg="papaya whip")
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,textvariable=self.dateborrowed_var,font=("arial",13,"bold"),width=29)
        txtDateBorrowed.grid(row=3,column=3)


        lblDateDue=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Due:",padx=2,pady=6,bg="papaya whip")
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,textvariable=self.datedue_var,font=("arial",13,"bold"),width=29)
        txtDateDue.grid(row=4,column=3)

        lblDaysOnBook=Label(DataFrameLeft,font=("arial",12,"bold"),text="Days on Book:",padx=2,pady=6,bg="papaya whip")
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,textvariable=self.daysonbook_var,font=("arial",13,"bold"),width=29)
        txtDaysOnBook.grid(row=5,column=3)


        lblLateReturnFine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Late Return Fine:",padx=2,pady=6,bg="papaya whip")
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,textvariable=self.lateratefine_var,font=("arial",13,"bold"),width=29)
        txtLateReturnFine.grid(row=6,column=3)


        lblDateOverdate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Over Due:",padx=2,pady=6,bg="papaya whip")
        lblDateOverdate.grid(row=7,column=2,sticky=W)
        txtDateOverdate=Entry(DataFrameLeft,textvariable=self.dateoverdue_var,font=("arial",13,"bold"),width=29)
        txtDateOverdate.grid(row=7,column=3)


        lblActualPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Actual Price:",padx=2,pady=6,bg="papaya whip")
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,textvariable=self.finalprice,font=("arial",13,"bold"),width=29)
        txtActualPrice.grid(row=8,column=3)

        #=========================Data Frame Right=================================


        DataFrameRight=LabelFrame(frame,text="Book Details",bg="papaya whip",fg="dark green",bd=20,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameRight.place(x=870,y=5,width=5800,height=350)

        self.txtBox=Text(DataFrameRight, font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=["The Shadow's Whisper",
"Secrets of the Forgotten Realm",
"The Silent City",
"Journey Beyond the Stars",
"Whispers in the Wind",
"Beneath the Crimson Sky",
"The Last Kingdom of Aethel",
"Echoes of the Abyss",
"The Time Traveler's Quest",
"Dawn of the Lost Empire",
"The Enchanted Forest Mystery",
"Through the Mirror of Worlds",
"The Alchemist's Secret",
"Rising Shadows",
"Tales of the Mystic Isles",
"The Forgotten Key",
"Dreams of the Eternal Flame",
"The Crystal of Destiny",
"The Moonlit Voyage",
"Legends of the Lost Sword",
"A Dance with Thunder",
"The Phantom of Avernus",
"Chronicles of the Hidden Temple",
"The Secret Garden of Shadows",
"Betrayal at Midnight",
"The Dragon's Heir",
"Winds of the Forgotten Land",
"Ember of the North",
"The Pirate Queen's Revenge",
"Return to Avalon",
"The Sorcerer's Tower",
"Realm of the Dark Mage",
"Shattered Dreams",
"The Golden Compass of Andor",
"Tides of Fate",
"The Emperor's Wrath",
"Cursed by the Moon",
"The Darkest Hour",
"The Royal Assassin",
"Guardians of the Celestial Gate",
"The Enigma of the Ice Cavern"
"A King's Redemption",
"Song of the Silver Sword",
"The Eternal Warlock",
"The Hidden Citadel",
"The Seventh Seal",
"Wings of Destiny",
"Storm over the Desert",
"The Forgotten Prophecy",
"The Fires of Valhalla"]
        

        def SelectBook(event=""):
            Selection = listBox.curselection()
            if Selection:
                value=str(listBox.get(Selection[0]))
                x=value
            
            
            if (x=="The Shadow's Whisper"):
                pass
                self.bookid_var.set("BKID8966")
                self.booktitle_var.set("Her Story")
                self.auther_var.set("Axe")


                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice.set("Rs.640")


            elif (x=="Secrets of the Forgotten Realm"):
                self.bookid_var.set("CDFID8966")
                self.booktitle_var.set("AK is back")
                self.auther_var.set("Thala")


                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.30")
                self.dateoverdue_var.set("NO")
                self.finalprice.set("Rs.780")

            elif (x=="The Silent City"):
                self.bookid_var.set("CyujID8966")
                self.booktitle_var.set("I'm back")
                self.auther_var.set("pradeep")


                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.60")
                self.dateoverdue_var.set("NO")
                self.finalprice.set("Rs.880")


            elif (x=="Journey Beyond the Stars"):
                self.bookid_var.set("CwedID8966")
                self.booktitle_var.set("Hey man")
                self.auther_var.set("Yaagu")


                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.70")
                self.dateoverdue_var.set("NO")
                self.finalprice.set("Rs.580")
            
            elif (x=="Whispers in the Wind"):
                self.bookid_var.set("CnmD8966")
                self.booktitle_var.set("Hey man")
                self.auther_var.set("Yaagu")


                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.70")
                self.dateoverdue_var.set("NO")
                self.finalprice.set("Rs.580")

            elif (x=="Beneath the Crimson Sky"):
                self.bookid_var.set("CtyID8966")
                self.booktitle_var.set("Hey man")
                self.auther_var.set("Yaagu")


                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.70")
                self.dateoverdue_var.set("NO")
                self.finalprice.set("Rs.580")


            else:
                print("No item selected.")


        
            


                

            
        

        listBox=Listbox(DataFrameRight,font=("arial",11,"bold"),width=23,height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)
        


        #==========================Buttons Frame====================================
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="papaya whip")
        Framebutton.place(x=0,y=530,width=1530,height=70)

        btnAddData=Button(Framebutton,command=self.adda_data,text="Add Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        
        btnShowData=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnShowData.grid(row=0,column=1)

        
        btnUpdate=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnUpdate.grid(row=0,column=2)


        
        btnDelete=Button(Framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnDelete.grid(row=0,column=3)


        btnReset=Button(Framebutton,command=self.reset,text="Reset",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnReset.grid(row=0,column=4)


        btnExit=Button(Framebutton,command=self.iExit,text="Exit",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnExit.grid(row=0,column=5)



        





        #==========================Information Frame====================================
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="papaya whip")
        FrameDetails.place(x=0,y=600,width=1530,height=195)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="papaya whip")
        Table_frame.place(x=0,y=2,width=1460,height=190)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame,column=("membertype","pnrno","title","firstname","lastname",
                                               "address1","address2","postid","mobile","booktitle","bookid",
                                               "auther","dateborrowed","datedue","days",
                                               "latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        
        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("pnrno",text="PNR NO.")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="Firs Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postid",text="Post Id")
        self.library_table.heading("mobile",text="Mobile")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("auther",text="Auther")
        self.library_table.heading("dateborrowed",text="Date of Borrowed")
        self.library_table.heading("datedue",text="Date of Due")
        self.library_table.heading("days",text="DaysOnBook")
        self.library_table.heading("latereturnfine",text="LateReturfine")
        self.library_table.heading("dateoverdue",text="DateOverDue")
        self.library_table.heading("finalprice",text="Final price")


        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)


        self.library_table.column("membertype",width=100)
        self.library_table.column("pnrno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("auther",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)



    def adda_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Axe@z4300",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute(
    "INSERT INTO library (Member,PNR_NO,ID,FirstName,LastName,Address1,Address2,postId,Mobile,Bookid,Booktitle,Auther,Dateborrowed,datedue,daysonbook,latereturnfine,dateoverdue,finalprice) "
    "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
    (self.member_var.get(),
     self.pnr_var.get(),
     self.id_var.get(),
     self.firstname_var.get(),
     self.lastname_var.get(),
     self.address1_var.get(),
     self.address2_var.get(),
     self.postcode_var.get(),
     self.mobile_var.get(),
     self.bookid_var.get(),
     self.booktitle_var.get(),
     self.auther_var.get(),
     self.dateborrowed_var.get(),
     self.datedue_var.get(),
     self.daysonbook_var.get(),
     self.lateratefine_var.get(),
     self.dateoverdue_var.get(),
     self.finalprice.get())
)


        conn.commit()
        self.fetch_data()
        conn.close()


        messagebox.showinfo("Success","Member has been inserted successfully ")


    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Axe@z4300",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute(
    "UPDATE library SET Member=%s, PNR_NO=%s, ID=%s, FirstName=%s, LastName=%s, Address1=%s, Address2=%s, postId=%s, Mobile=%s, Bookid=%s, Booktitle=%s, Auther=%s, Dateborrowed=%s, datedue=%s, daysonbook=%s, latereturnfine=%s, dateoverdue=%s, finalprice=%s WHERE PNR_NO=%s", (
        self.member_var.get(),
        self.pnr_var.get(),
        self.id_var.get(),
        self.firstname_var.get(),
        self.lastname_var.get(),
        self.address1_var.get(),
        self.address2_var.get(),
        self.postcode_var.get(),
        self.mobile_var.get(),
        self.bookid_var.get(),
        self.booktitle_var.get(),
        self.auther_var.get(),
        self.dateborrowed_var.get(),
        self.datedue_var.get(),
        self.daysonbook_var.get(),
        self.lateratefine_var.get(),
        self.dateoverdue_var.get(),
        self.finalprice.get(),
        self.pnr_var.get()
    )
)


        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success","Member has been Updated")



    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Axe@z4300",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()


        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
                conn.commit()
            conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']


        self.member_var.set(row[0]),
        self.pnr_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.auther_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.lateratefine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.finalprice.set(row[17])

    def showData(self):
        self.txtBox.insert(END,"Member Type:\t\t"+ self.member_var.get() + "\n")
        self.txtBox.insert(END,"PRN NO:\t\t"+ self.pnr_var.get() + "\n")
        self.txtBox.insert(END,"ID NO:\t\t"+ self.id_var.get() + "\n")
        self.txtBox.insert(END,"FirstName:\t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"LastName:\t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"Address1:\t\t"+ self.address1_var.get() + "\n")
        self.txtBox.insert(END,"Address2:\t\t"+ self.address2_var.get() + "\n")
        self.txtBox.insert(END,"Post Code:\t\t"+ self.postcode_var.get() + "\n")
        self.txtBox.insert(END,"Mobile No:\t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END,"Book ID:\t\t"+ self.bookid_var.get() + "\n")
        self.txtBox.insert(END,"Book Title:\t\t"+ self.booktitle_var.get() + "\n")
        self.txtBox.insert(END,"Auther:\t\t"+ self.auther_var.get() + "\n")
        self.txtBox.insert(END,"DateBorrowed:\t\t"+ self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END,"DateDue:\t\t"+ self.datedue_var.get() + "\n")
        self.txtBox.insert(END,"DaysOnBook:\t\t"+ self.daysonbook_var.get() + "\n")
        self.txtBox.insert(END,"LateRateFine:\t\t"+ self.lateratefine_var.get() + "\n")
        self.txtBox.insert(END,"DateOverDue:\t\t"+ self.dateoverdue_var.get() + "\n")
        self.txtBox.insert(END,"FinallPrice:\t\t"+ self.finalprice.get() + "\n")


    def reset(self):
        self.member_var.set(""),
        self.pnr_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.auther_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.lateratefine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finalprice.set("")
        self.txtBox.delete("1.0",END)


    def iExit(self):
        iExit=tkinter.messagebox.askyesno(LibraryManagementSystem,"Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return
        

    def delete(self):
        if self.pnr_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First select the Member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Axe@z4300",database="mydata")
            my_cursor=conn.cursor()
            query="delete from library where PNR_NO=%s"
            value=(self.pnr_var.get(),)
            my_cursor.execute(query,value)


            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()


            messagebox.showinfo("Vanakam da maapla","Mudichivittinga")


import tkinter as tk
import smtplib
import random
from tkinter import messagebox




class Sign:
    
    verification_code = ""
    verified_email = ""

    
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    SMTP_USER = 'praveenkumaran223@gmail.com'
    SMTP_PASSWORD = 'nljz tgfg phoo bqkz'

    def __init__(self, root):
        self.root = root
        self.root.title("Signup Page")
        self.root.geometry("1550x800+0+0")
        self.root.config(bg="#e0f7fa")
        self.open_signup_window()

    
    def send_verification_email(self, email):
        self.verification_code = str(random.randint(100000, 999999))  

        subject = "Your Verification Code"
        message = f"Your verification code is: {self.verification_code}"

        email_message = f"Subject: {subject}\n\n{message}"

        try:
            
            server = smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT)
            server.starttls()  
            server.login(self.SMTP_USER, self.SMTP_PASSWORD)
            server.sendmail(self.SMTP_USER, email, email_message)
            server.quit()

            messagebox.showinfo("Verification", f"A verification code has been sent to {email}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send email: {str(e)}")

   
    def handle_email_submission(self):
        email = self.email_entry.get()

        if not email:
            messagebox.showerror("Error", "Email is required!")
        else:
            self.verified_email = email  
            self.send_verification_email(email)
            self.show_verification_screen()

    
    def handle_verification(self):
        code = self.verification_code_entry.get()

        if code == self.verification_code:
            messagebox.showinfo("Success", "Email verified successfully!")
            self.show_password_screen()
        else:
            messagebox.showerror("Error", "Invalid verification code!")

    
    def handle_password_submission(self):
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if not password or not confirm_password:
            messagebox.showerror("Error", "Both password fields are required!")
        elif password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
        else:
           
            messagebox.showinfo("Success", "Signup complete!")
            self.show_library_button()

   
    def show_verification_screen(self):
        self.clear_frame()

        verification_label = tk.Label(self.root, text="Enter Verification Code", font=("Arial", 18), bg="#e0f7fa")
        verification_label.pack(pady=20)

        self.verification_code_entry = tk.Entry(self.root, width=30)
        self.verification_code_entry.pack(pady=10)

        verify_button = tk.Button(self.root, text="Verify", command=self.handle_verification, bg="#004d40", fg="white", width=15)
        verify_button.pack(pady=20)

   
    def show_password_screen(self):
        self.clear_frame()

        password_label = tk.Label(self.root, text="Create Password", font=("Arial", 18), bg="#e0f7fa")
        password_label.pack(pady=20)

        self.password_entry = tk.Entry(self.root, width=30, show="*")
        self.password_entry.pack(pady=10)

        confirm_password_label = tk.Label(self.root, text="Confirm Password", font=("Arial", 12), bg="#e0f7fa")
        confirm_password_label.pack(pady=10)

        self.confirm_password_entry = tk.Entry(self.root, width=30, show="*")
        self.confirm_password_entry.pack(pady=10)

        submit_button = tk.Button(self.root, text="Submit", command=self.handle_password_submission, bg="#004d40", fg="white", width=15)
        submit_button.pack(pady=20)

    
    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def open_signup_window(self):
        title_label = tk.Label(self.root, text="Signup", font=("Arial", 24), bg="#e0f7fa")
        title_label.pack(pady=20)

        email_label = tk.Label(self.root, text="Enter Email:", font=("Arial", 12), bg="#e0f7fa")
        email_label.pack(pady=10)

        self.email_entry = tk.Entry(self.root, width=30)
        self.email_entry.pack()

        email_button = tk.Button(self.root, text="Send Verification Code", command=self.handle_email_submission, bg="#004d40", fg="white", width=20)
        email_button.pack(pady=20)

    
    def show_library_button(self):
        self.clear_frame()

       
        open_library_button = tk.Button(self.root, text="Open Library Management System", command=self.open_library_management_system, bg="#004d40", fg="white", width=25)
        open_library_button.pack(pady=50)

    
    def open_library_management_system(self):
        library_window = tk.Toplevel(self.root)
        obj = LibraryManagementSystem(library_window)


if __name__ == "__main__":
    root = tk.Tk()
    sign = Sign(root)
    root.mainloop()



