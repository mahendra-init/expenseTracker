import calendar
import datetime
import locale
from tkinter import *
from tkinter import ttk
from turtle import bgcolor
from typing_extensions import Self
from tkinter import messagebox as MessageBox
from MySQLdb import Date
from numpy import var
from tkcalendar import DateEntry
from tkinter.ttk import Notebook
import mysql.connector as mysql


EX_CATEGORIES = ['Food', 'Clothing','Shopping', 'Entertainment', 'Education', 'Personal', 'Medical', 'Transportation', 'Bills']
PAY_WAYS = ['Cash', 'UPI', 'Cheque', 'Other']
IN_CATEGORIES = ['Salary', 'Others']
class Home():
    def AddtoDB(Self, a):
        if(a == "e"):
            date = Self.Edate.get()
            category = Self.choosed_cate.get()
            expense = Self.EExpense.get()
            edata = [date, category, expense]
            Self.TVExpenses.insert('', 'end', values=edata)
            # if(date == '' or category == '' or expense == ''):
            #     MessageBox.showinfo("Insert Status", "All Field are required")
            # else:
            #     con = mysql.connect(host='localhost', user='root',
            #                         password='Mahendra@$28', database='expensetracker')
            #     cursor = con.cursor()
            #     cursor.execute("insert into expenses values('" +
            #                    date+"','"+category+"','"+expense+"')")
            #     cursor.execute("commit")
            #     MessageBox.showinfo("Insert Status", "Inserted Successfully")
            #     con.close()
        elif(a == "i"):
            date = Self.Idate.get()
            source = Self.choosed_source.get()
            income = Self.EIncome.get()
            idata = [date, source, income]
            Self.TVIncome.insert('', 'end', values=idata)
            # if(date == '' or source == '' or income == ''):
            #     MessageBox.showinfo("Insert Status", "All Field are required")
            # else:
            #     try:
            #         con = mysql.connect(host='localhost', user='root',
            #                             password='Mahendra@$28', database='expensetracker')
            #         cursor = con.cursor()
            #         cursor.execute("insert into income values('" +
            #                        date+"','"+source+"','"+income+"')")
            #         cursor.execute("commit")
            #         MessageBox.showinfo(
            #             "Insert Status", "Inserted Successfully")
            #         con.close()
                # except:
                #     print("-----")

    def __init__(Self, username):
        Self.root = Tk()
        Self.root.title("Expense Tracker")
        Self.root.geometry('700x500+300+100')
        Self.root.configure(bg='#b8c6db')

        Self.Tab = Notebook(Self.root)

        Self.F1 = Frame(Self.Tab)
        Self.F2 = Frame(Self.Tab)

        Self.Tab.add(Self.F1, text='Expense')
        Self.Tab.add(Self.F2, text='Income')

        Self.Tab.pack(fill=BOTH, expand=1)

        # # --------------Expense------------------

        Self.LDate = Label(Self.F1, text='Date', font=(None, 18))
        Self.LDate.grid(row=1, column=0, padx=5, pady=5, sticky='w')

        Self.Edate = DateEntry(Self.F1)
        Self.Edate.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        # -------------------------------

        Self.category = Label(Self.F1, text='Category', font=(None, 18))
        Self.category.grid(row=2, column=0, padx=5, pady=5, sticky='w')

        Self.choosed_cate = StringVar()
        Self.choosed_cate.set(EX_CATEGORIES[0])
        Self.Ecategory = OptionMenu(Self.F1, Self.choosed_cate, *EX_CATEGORIES)
        Self.Ecategory.configure(highlightthickness=2, width=15)
        Self.Ecategory.grid(row=2, column=1, padx=5, pady=5, sticky='w')

        # --------------------------------

        Self.LExpense = Label(Self.F1, text='Expenses', font=(None, 18))
        Self.LExpense.grid(row=3, column=0, padx=5, pady=5, sticky='w')

        Self.EExpense = Entry(
            Self.F1,  font=(None, 18))
        Self.EExpense.grid(row=3, column=1, padx=5, pady=5, sticky='w')

        # ---------------------------------

        BF1Add = Button(Self.F1, text='Add Expense',
                        command=lambda: Home.AddtoDB(Self, "e"))
        BF1Add.grid(row=4, column=1, padx=5, pady=5,
                    sticky='w', ipadx=10, ipady=10)

        Self.Lbl = Label(Self.F1, text='Recents', font=(None, 15))
        Self.Lbl.place(x = 15, y = 220)

        # ----------------------------------

        TVList = ['Date', 'Category', 'Expenses']
        Self.TVExpenses = ttk.Treeview(
            Self.F1, columns=TVList, show='headings', height=5)
        Self.TVExpenses.place(x= 20, y= 245)
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


# obj = Home("mahendra123")