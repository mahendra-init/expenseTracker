from tkinter import *
from tkinter import ttk
from turtle import bgcolor
from typing_extensions import Self
from tkinter import messagebox as MessageBox
from tkcalendar import DateEntry
from tkinter.ttk import Notebook
import mysql.connector as mysql


class Home():
    def AddtoDB(Self, a):
        if(a == "e"):
            date = Self.Edate.get()
            category = Self.ETitle.get()
            expense = Self.EExpense.get()
            print(date)
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
            date = Self.EDate2.get()
            source = Self.ESource.get()
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

    def __init__(Self):
        Self.GUI = Tk()
        Self.GUI.title("Expense Tracker")
        Self.GUI.geometry('700x500+300+100')
        Self.GUI.configure(bg='#b8c6db')

        Self.Tab = Notebook(Self.GUI)

        Self.F1 = Frame(Self.Tab)
        Self.F2 = Frame(Self.Tab)

        Self.Tab.add(Self.F1, text='Expense')
        Self.Tab.add(Self.F2, text='Income')

        Self.Tab.pack(fill=BOTH, expand=1)

        # # --------------Expense------------------

        Self.LDate = Label(Self.F1, text='Date', font=(None, 18))
        Self.LDate.grid(row=1, column=0, padx=5, pady=5, sticky='w')

        Self.Edate = Entry(Self.F1, font=(None, 18))
        Self.Edate.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        # -------------------------------

        Self.LTitle = Label(Self.F1, text='Title', font=(None, 18))
        Self.LTitle.grid(row=2, column=0, padx=5, pady=5, sticky='w')

        Self.ETitle = Entry(Self.F1,  font=(None, 18))
        Self.ETitle.grid(row=2, column=1, padx=5, pady=5, sticky='w')

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

        # ----------------------------------

        TVList = ['Date', 'Title', 'Expenses']
        Self.TVExpenses = ttk.Treeview(
            Self.F1, columns=TVList, show='headings', height=5)
        for i in TVList:
            Self.TVExpenses.heading(i, text=i.title())
        Self.TVExpenses.grid(row=5, column=0, padx=5, pady=5,
                             sticky='w', columnspan=3)

        # --------------------Expense End--------------

        # --------------------Income-------------------

        Self.LDate2 = Label(Self.F2, text='Date', font=(None, 18))
        Self.LDate2.grid(row=1, column=0, padx=5, pady=5, sticky='w')

        Self.EDate2 = Entry(Self.F2,  font=(None, 18))
        Self.EDate2.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        # -------------------------------

        Self.LSource = Label(Self.F2, text='Source', font=(None, 18))
        Self.LSource.grid(row=2, column=0, padx=5, pady=5, sticky='w')

        Self.ESource = Entry(Self.F2, font=(None, 18))
        Self.ESource.grid(row=2, column=1, padx=5, pady=5, sticky='w')

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

        # ----------------------------------
        TV = ['Date', 'Source', 'Income']
        Self.TVIncome = ttk.Treeview(
            Self.F2, columns=TV, show='headings', height=5)
        for j in TV:
            Self.TVIncome.heading(j, text=j.title())
        Self.TVIncome.grid(row=5, column=0, padx=5, pady=5,
                           sticky='w', columnspan=3)
        Self.GUI.mainloop()
