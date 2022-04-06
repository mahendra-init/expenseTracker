import calendar
import datetime
import locale
from tabnanny import verbose
from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import ttk
from tkinter.ttk import Notebook, Style
from turtle import Screen, bgcolor

import mysql.connector as mysql
from click import style
from MySQLdb import Date
from numpy import var
from tkcalendar import DateEntry
from typing_extensions import Self

EX_CATEGORIES = ['Food', 'Clothing','Shopping', 'Entertainment', 'Education', 'Personal', 'Medical', 'Transportation', 'Bills']
PAY_WAYS = ['Cash', 'UPI', 'Cheque', 'Other']
IN_CATEGORIES = ['Salary', 'Others']
class Home():
    username = var
    def AddtoDB(Self, a):
        con = mysql.connect(host='localhost', user='root',
                                        password='Mahendra@$28', database='expensetracker')
        cursor = con.cursor()
        if(a == "e"):
            date = Self.Edate.get()
            category = Self.choosed_cate.get()
            description = Self.ExDescription.get()
            expense = Self.ExAmount.get()
            pay_ways = Self.choosed_method.get()
            edata = [date, category, description, expense, pay_ways]
            if(date == '' or category == '' or expense == '' or pay_ways == ''):
                MessageBox.showinfo("Insert Status", "All Field are required except 'Description' is optional!")
            else:
                cursor.execute("insert into expenses values('"+date+"','"+category+"','"+description+"','"+expense+"','"+pay_ways+"','"+Self.username+"')")
                cursor.execute("commit")
                MessageBox.showinfo("Insert Status", "Inserted Successfully")
                Self.TVExpenses.insert('', 'end', values=edata)
        elif(a == "i"):
            date = Self.Idate.get()
            source = Self.choosed_source.get()
            income = Self.EIncome.get()
            idata = [date, source, income]
            if(date == '' or source == '' or income == ''):
                MessageBox.showinfo("Insert Status", "All Field are required")
            else:
                cursor.execute("insert into incomes values('"+date+"','"+source+"','"+income+"','"+Self.username+"')")
                cursor.execute("commit")
                MessageBox.showinfo("Insert Status", "Inserted Successfully")
                Self.TVIncome.insert('', 'end', values=idata)
        con.close()

    def __init__(Self, username):
        Self.username = username
        Self.root = Tk()
        Self.root.title("Expense Tracker")
        Self.root.geometry('700x500+300+100')
        Self.root.configure(bg='#b8c6db')
        style = ttk.Style()
        style.theme_use('alt')
        Self.Tab = Notebook(Self.root)

        Self.F1 = Frame(Self.Tab)
        Self.F2 = Frame(Self.Tab)

        Self.Tab.add(Self.F1, text='Expense')
        Self.Tab.add(Self.F2, text='Income')

        Self.Tab.pack(fill=BOTH, expand=1)

        # # --------------Expense------------------

        Self.LDate = Label(Self.F1, text='Date', font=(None, 16))
        Self.LDate.grid(row=1, column=0, padx=5, pady=5, sticky='w')

        Self.Edate = DateEntry(Self.F1)
        Self.Edate.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        Self.Edate.configure(width=23)
        # -------------------------------

        Self.category = Label(Self.F1, text='Category', font=(None, 16))
        Self.category.grid(row=2, column=0, padx=5, pady=5, sticky='w')

        Self.choosed_cate = StringVar()
        Self.choosed_cate.set(EX_CATEGORIES[0])
        Self.Ecategory = OptionMenu(Self.F1, Self.choosed_cate, *EX_CATEGORIES)
        Self.Ecategory.configure(highlightthickness=2, width=20)
        Self.Ecategory.grid(row=2, column=1, padx=5, pady=5, sticky='w')

        # --------------------------------

        Self.LDescription = Label(Self.F1, text='Description', font=(None, 16))
        Self.LDescription.grid(row=3, column=0, padx=5, pady=5, sticky='w')

        Self.ExDescription = Entry(Self.F1,  font=(None, 18))
        Self.ExDescription.grid(row=3, column=1, padx=5, pady=5, sticky='w')

        Self.LAmount = Label(Self.F1, text='Amount', font=(None, 16))
        Self.LAmount.grid(row=4, column=0, padx=5, pady=5, sticky='w')

        Self.ExAmount = Entry(Self.F1,  font=(None, 18))
        Self.ExAmount.grid(row=4, column=1, padx=5, pady=5, sticky='w')

        Self.LPay_meth = Label(Self.F1, text='Paid By: ', font=(None, 16))
        Self.LPay_meth.grid(row=5, column=0, padx=5, pady=5, sticky='w')

        Self.choosed_method = StringVar()
        Self.choosed_method.set(PAY_WAYS[0])
        Self.ExPayMethod = OptionMenu(Self.F1, Self.choosed_method, *PAY_WAYS)
        Self.ExPayMethod.configure(highlightthickness=2, width=20)
        Self.ExPayMethod.grid(row=5, column=1, padx=5, pady=5, sticky='w')
        # ---------------------------------

        BF1Add = Button(Self.F1, text='Add Expense',
                        command=lambda: Home.AddtoDB(Self, "e"))
        BF1Add.grid(row=6, column=1, padx=20, pady=5,
                    sticky='w', ipadx=10, ipady=10)

        Self.Lbl = Label(Self.F1, text='Recents', font=(None, 15))
        Self.Lbl.place(x = 15, y = 250)

        # ----------------------------------

        TVList = ['Date', 'Category', 'Description', 'Amount Spent', 'Paid Through']
        Self.TVExpenses = ttk.Treeview(
            Self.F1, columns=TVList, show='headings', height=7)
        Self.TVExpenses.place(x= 20, y= 285)
        Self.TVExpenses.column("Date", minwidth=0, width=50, stretch=NO, anchor=CENTER)
        Self.TVExpenses.column("Category", minwidth=0, width=120, stretch=NO)
        Self.TVExpenses.column("Description", minwidth=0, width=280)
        Self.TVExpenses.column("Amount Spent", minwidth=0, width=120, stretch=NO, anchor=CENTER)
        Self.TVExpenses.column("Paid Through", minwidth=0, width=90, stretch=NO)


        for i in TVList:
            Self.TVExpenses.heading(i, text=i.title())
        # Self.TVExpenses.grid(row=5, column=0, padx=5, pady=5,
        #                      sticky='w', columnspan=3)

        # --------------------Expense End--------------


















        # --------------------Income-------------------

        Self.LDate2 = Label(Self.F2, text='Date', font=(None, 18))
        Self.LDate2.grid(row=1, column=0, padx=5, pady=5, sticky='w')

        Self.Idate = DateEntry(Self.F2)
        Self.Idate.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        # -------------------------------


        Self.source = Label(Self.F2, text='Source', font=(None, 18))
        Self.source.grid(row=2, column=0, padx=5, pady=5, sticky='w')

        Self.choosed_source = StringVar()
        Self.choosed_source.set(IN_CATEGORIES[0])
        Self.Icategory = OptionMenu(Self.F2, Self.choosed_source, *IN_CATEGORIES)
        Self.Icategory.configure(highlightthickness=2, width=15)
        Self.Icategory.grid(row=2, column=1, padx=5, pady=5, sticky='w')

        # --------------------------------

        Self.LIncome = Label(Self.F2, text='Income', font=(None, 18))
        Self.LIncome.grid(row=3, column=0, padx=5, pady=5, sticky='w')

        Self.EIncome = Entry(Self.F2, font=(None, 18))
        Self.EIncome.grid(row=3, column=1, padx=5, pady=5, sticky='w')

        # ---------------------------------

        BF2Add = Button(Self.F2, text='Add Income',
                        command=lambda: Home.AddtoDB(Self, "i"))
        BF2Add.grid(row=4, column=1, padx=5, pady=5,
                    sticky='w', ipadx=10, ipady=10)
        
        Self.Lbl = Label(Self.F2, text='Recents', font=(None, 15))
        Self.Lbl.place(x = 15, y = 220)
        # ----------------------------------
        TV = ['Date', 'Source', 'Income']
        Self.TVIncome = ttk.Treeview(
            Self.F2, columns=TV, show='headings', height=5)
        Self.TVIncome.place(x= 20, y= 245)
        for j in TV:
            Self.TVIncome.heading(j, text=j.title())
        # Self.TVIncome.grid(row=5, column=0, padx=5, pady=5,
        #                    sticky='w', columnspan=3)
        Self.root.mainloop()


obj = Home("mahendra123")
