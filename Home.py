import calendar
import datetime
from lib2to3.pgen2.token import NEWLINE
import locale
import time
from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import ttk
from tkinter.ttk import Notebook, Style
from turtle import Screen, bgcolor, color
import mysql.connector as mysql
from tkcalendar import DateEntry
import utilities as ut
import schedule

EX_CATEGORIES = ['Food', 'Clothing','Shopping', 'Entertainment', 'Education', 'Personal', 'Medical', 'Transportation', 'Bills', 'Others']
PAY_WAYS = ['Cash', 'UPI', 'Cheque', 'Card']
IN_CATEGORIES = ['Salary', 'Others']


class Home():

    ###  Function to add new data to database
    def AddtoDB(self, a):
        con = mysql.connect(host='localhost', user='root',
                                        password='Mahendra@$28', database='expensetracker')
        cursor = con.cursor()
        if(a == "e"):
            date = ut.dateFormat(self.Edate.get())
            category = self.choosed_cate.get()
            description = self.ExDescription.get()
            expense = self.ExAmount.get()
            pay_ways = self.choosed_method.get()
            if(date == '' or category == '' or expense == '' or pay_ways == ''):
                MessageBox.showinfo("Insert Status", "All Field are required except 'Description' is optional!")
            else:
                cursor.execute("insert into expenses values('"+date+"','"+category+"','"+description+"','"+expense+"','"+pay_ways+"','"+self.username+"')")
                cursor.execute("commit")
                MessageBox.showinfo("Insert Status", "Inserted Successfully")
                self.updateView()
        elif(a == "i"):
            date = ut.dateFormat(self.Idate.get())
            source = self.choosed_source.get()
            description = self.InDescription.get()
            income = self.EIncome.get()
            if(date == '' or source == '' or income == ''):
                MessageBox.showinfo("Insert Status", "All Field are required")
            else:
                cursor.execute("insert into incomes values('"+date+"','"+source+"','"+description+"','"+income+"','"+self.username+"')")
                cursor.execute("commit")
                MessageBox.showinfo("Insert Status", "Inserted Successfully")
                self.updateView()
        con.close()
    
    
    
    

    ###    Func to update treeviews
    def updateView(self):
        self.TVExpenses.delete(*self.TVExpenses.get_children())
        self.TVIncome.delete(*self.TVIncome.get_children())
        eFetchedData = ut.extractData(self.username, "e")
        iFetchedData = ut.extractData(self.username, "i")
        for i in eFetchedData:
            self.TVExpenses.insert('', 'end', values = i)
        for i in iFetchedData:
            self.TVIncome.insert('', 'end', values = i)


        self.ExListView.delete(*self.ExListView.get_children())
        self.InListView.delete(*self.InListView.get_children())
        date1 = ut.dateFormat(self.getDate1.get())
        date2 = ut.dateFormat(self.getDate2.get())
        dateList = [date1, date2]
        eSheetData = ut.analysisData(self.username, "e", dateList)
        iSheetData = ut.analysisData(self.username, "i", dateList)
        for i in eSheetData:
            self.ExListView.insert('', 'end', values = i)
        for i in iSheetData:
            self.InListView.insert('', 'end', values = i)
            


    def __init__(self, username):
        self.username = username
        self.root = Tk()
        self.root.title("Expense Tracker")
        self.root.geometry('700x500+300+100')
        self.root.configure(bg='#b8c6db')
        style = ttk.Style()
        style.theme_use('alt')
        self.Tab = Notebook(self.root)

        self.F1 = Frame(self.Tab)
        self.F2 = Frame(self.Tab)
        self.F3 = Frame(self.Tab)

        self.Tab.add(self.F1, text='Expense')
        self.Tab.add(self.F2, text='Income')
        self.Tab.add(self.F3, text='Analysis')

        self.Tab.pack(fill=BOTH, expand=1)

        # # --------------Expense------------------

        self.LDate = Label(self.F1, text='Date', font=(None, 16))
        self.LDate.grid(row=1, column=0, padx=5, pady=5, sticky='w')

        self.Edate = DateEntry(self.F1)
        self.Edate.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        # -------------------------------

        self.category = Label(self.F1, text='Category', font=(None, 16))
        self.category.grid(row=2, column=0, padx=5, pady=5, sticky='w')

        self.choosed_cate = StringVar()
        self.choosed_cate.set(EX_CATEGORIES[0])
        self.Ecategory = OptionMenu(self.F1, self.choosed_cate, *EX_CATEGORIES)
        self.Ecategory.configure(highlightthickness=2, width=20)
        self.Ecategory.grid(row=2, column=1, padx=5, pady=5, sticky='w')

        # --------------------------------

        self.LDescription = Label(self.F1, text='Description', font=(None, 16))
        self.LDescription.grid(row=3, column=0, padx=5, pady=5, sticky='w')

        self.ExDescription = Entry(self.F1,  font=(None, 18))
        self.ExDescription.grid(row=3, column=1, padx=5, pady=5, sticky='w')

        self.DescFormat = Label(self.F1, text='" Single & Double quotes are not allowed ! "', font=(None, 10), fg="#FF0000")
        self.DescFormat.grid(row=3, column=2, padx=5, pady=5, sticky='w')

        self.LAmount = Label(self.F1, text='Amount', font=(None, 16))
        self.LAmount.grid(row=4, column=0, padx=5, pady=5, sticky='w')

        self.ExAmount = Entry(self.F1,  font=(None, 18))
        self.ExAmount.grid(row=4, column=1, padx=5, pady=5, sticky='w')

        self.LPay_meth = Label(self.F1, text='Paid By: ', font=(None, 16))
        self.LPay_meth.grid(row=5, column=0, padx=5, pady=5, sticky='w')

        self.choosed_method = StringVar()
        self.choosed_method.set(PAY_WAYS[0])
        self.ExPayMethod = OptionMenu(self.F1, self.choosed_method, *PAY_WAYS)
        self.ExPayMethod.configure(highlightthickness=2, width=20)
        self.ExPayMethod.grid(row=5, column=1, padx=5, pady=5, sticky='w')
        # ---------------------------------

        BF1Add = Button(self.F1, text='Add Expense',command=lambda: Home.AddtoDB(self, "e"))
        BF1Add.grid(row=6, column=1, padx=20, pady=5,
                    sticky='w', ipadx=10, ipady=10)

        self.Lbl = Label(self.F1, text='Recents', font=(None, 15))
        self.Lbl.place(x = 15, y = 250)

        # ----------------------------------

        TVList = ['Date', 'Category', 'Description', 'Amount Spent', 'Paid Through']
        self.TVExpenses = ttk.Treeview(
            self.F1, columns=TVList, show='headings', height=7)
        self.TVExpenses.place(x= 20, y= 285)
        self.TVExpenses.column("Date", minwidth=0, width=80, stretch=NO, anchor=CENTER)
        self.TVExpenses.column("Category", minwidth=0, width=120, stretch=NO)
        self.TVExpenses.column("Description", minwidth=0, width=250)
        self.TVExpenses.column("Amount Spent", minwidth=0, width=120, stretch=NO, anchor=CENTER)
        self.TVExpenses.column("Paid Through", minwidth=0, width=90, stretch=NO)


        for i in TVList:
            self.TVExpenses.heading(i, text=i.title())

        # --------------------Expense End--------------







        # --------------------Income-------------------

        self.LDate2 = Label(self.F2, text='Date', font=(None, 18))
        self.LDate2.grid(row=1, column=0, padx=5, pady=5, sticky='w')

        self.Idate = DateEntry(self.F2)
        self.Idate.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        # -------------------------------


        self.source = Label(self.F2, text='Source', font=(None, 18))
        self.source.grid(row=2, column=0, padx=5, pady=5, sticky='w')

        self.choosed_source = StringVar()
        self.choosed_source.set(IN_CATEGORIES[0])
        self.Icategory = OptionMenu(self.F2, self.choosed_source, *IN_CATEGORIES)
        self.Icategory.configure(highlightthickness=2, width=15)
        self.Icategory.grid(row=2, column=1, padx=5, pady=5, sticky='w')

        # --------------------------------
        self.LDescription = Label(self.F2, text='Description', font=(None, 16))
        self.LDescription.grid(row=3, column=0, padx=5, pady=5, sticky='w')

        self.InDescription = Entry(self.F2,  font=(None, 18))
        self.InDescription.grid(row=3, column=1, padx=5, pady=5, sticky='w')

        self.DescFormat = Label(self.F2, text='" Single & Double quotes are not allowed ! "', font=(None, 10), fg="#FF0000")
        self.DescFormat.grid(row=3, column=2, padx=5, pady=5, sticky='w')

        # --------------------------------

        self.LIncome = Label(self.F2, text='Income', font=(None, 18))
        self.LIncome.grid(row=4, column=0, padx=5, pady=5, sticky='w')

        self.EIncome = Entry(self.F2, font=(None, 18))
        self.EIncome.grid(row=4, column=1, padx=5, pady=5, sticky='w')

        # ---------------------------------

        BF2Add = Button(self.F2, text='Add Income',
                        command=lambda: Home.AddtoDB(self, "i"))
        BF2Add.grid(row=5, column=1, padx=5, pady=5,
                    sticky='w', ipadx=10, ipady=10)
        
        self.Lbl = Label(self.F2, text='Recents', font=(None, 15))
        self.Lbl.place(x = 15, y = 250)
        # ----------------------------------
        TV = ['Date', 'Source', 'Description', 'Income']
        self.TVIncome = ttk.Treeview(
            self.F2, columns=TV, show='headings', height=5)
        self.TVIncome.place(x= 20, y= 285)
        self.TVIncome.column("Date", minwidth=0, width=80, stretch=NO, anchor=CENTER)
        self.TVIncome.column("Source", minwidth=0, width=120, stretch=NO)
        self.TVIncome.column("Description", minwidth=0, width=250)
        self.TVIncome.column("Income", minwidth=0, width=120, stretch=NO, anchor=CENTER)
        for j in TV:
            self.TVIncome.heading(j, text=j.title())

         # --------------------Income End--------------




        # --------------------Analysis-------------------

        LDate = Label(self.F3, text='Choose Date: ', font=(None, 16))
        LDate.place(x = 10, y = 10)

        self.getDate1 = DateEntry(self.F3)
        self.getDate1.place(x = 180, y = 15)

        self.getDate2 = DateEntry(self.F3)
        self.getDate2.place(x = 360, y = 15)

        Lb = Label(self.F3, text='to', font=(None, 15))
        Lb.place(x = 300, y = 10)


        self.Lbl = Label(self.F3, text='Expense Sheet:', font=(None, 15))
        self.Lbl.place(x = 5, y = 70)

        self.BF1Add = Button(self.F3, text='Track',command=lambda: self.updateView())
        self.BF1Add.place(x = 300, y = 50)


        ExList = ['Date', 'Category', 'Description', 'Amount Spent', 'Paid Through']
        self.ExListView = ttk.Treeview(
            self.F3, columns=ExList, show='headings', height=9)
        self.ExListView.place(x= 10, y= 105)
        self.ExListView.column("Date", minwidth=0, width=80, stretch=NO, anchor=CENTER)
        self.ExListView.column("Category", minwidth=0, width=120, stretch=NO)
        self.ExListView.column("Description", minwidth=0, width=250)
        self.ExListView.column("Amount Spent", minwidth=0, width=120, stretch=NO, anchor=CENTER)
        self.ExListView.column("Paid Through", minwidth=0, width=90, stretch=NO)


        for i in ExList:
            self.ExListView.heading(i, text=i.title())
        
        
        Lb2 = Label(self.F3, text='Income Sheet:', font=(None, 15))
        Lb2.place(x = 5, y = 320)

        InList = ['Date', 'Source', 'Description', 'Income']
        self.InListView = ttk.Treeview(
            self.F3, columns=InList, show='headings', height=3)
        self.InListView.place(x= 10, y= 365)
        self.InListView.column("Date", minwidth=0, width=80, stretch=NO, anchor=CENTER)
        self.InListView.column("Source", minwidth=0, width=120, stretch=NO)
        self.InListView.column("Description", minwidth=0, width=250)
        self.InListView.column("Income", minwidth=0, width=120, stretch=NO, anchor=CENTER)

        for i in InList:
            self.InListView.heading(i, text=i.title())


        self.updateView()   
        self.root.mainloop()

        # schedule.every().day.at("05:27").do(ut.send_notification)
        # while True:
        #     schedule.run_pending()
        #     time.sleep(1)


Home("mahendra123")
