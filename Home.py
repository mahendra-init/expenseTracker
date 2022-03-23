from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
from tkcalendar import DateEntry
from tkinter.ttk import Notebook
import mysql.connector as mysql


def AddtoDB(a):
    if(a == "e"):
        date = EDate.get()
        category = Title.get()
        expense = Expense.get()
        edata = [date, category, expense]
        TVExpenses.insert('', 'end', values=edata)
        if(date == '' or category == '' or expense == ''):
            MessageBox.showinfo("Insert Status", "All Field are required")
        else:
            con = mysql.connect(host='localhost', user='root',
                                password='Shivam@$12', database='expensetracker')
            cursor = con.cursor()
            cursor.execute("insert into expenses values('" +
                           date+"','"+category+"','"+expense+"')")
            cursor.execute("commit")
            MessageBox.showinfo("Insert Status", "Inserted Successfully")
            con.close()
    elif(a == "i"):
        date = EDate2.get()
        source = Source.get()
        income = Income.get()
        idata = [date, source, income]
        TVIncome.insert('', 'end', values=idata)
        if(date == '' or source == '' or income == ''):
            MessageBox.showinfo("Insert Status", "All Field are required")
        else:
            try:
                con = mysql.connect(host='localhost', user='root',
                                    password='Shivam@$12', database='expensetracker')
                cursor = con.cursor()
                cursor.execute("insert into income values('" +
                               date+"','"+source+"','"+income+"')")
                cursor.execute("commit")
                MessageBox.showinfo(
                    "Insert Status", "Inserted Successfully")
                con.close()
            except:
                print("-----")


GUI = Tk()
GUI.title("Expense Tracker")
GUI.geometry('700x500')

Tab = Notebook(GUI)

F1 = Frame(Tab)
F2 = Frame(Tab)

Tab.add(F1, text='Expense')
Tab.add(F2, text='Income')

Tab.pack(fill=BOTH, expand=1)

# # --------------Expense------------------

LDate = ttk.Label(F1, text='Date', font=(None, 18))
LDate.grid(row=1, column=0, padx=5, pady=5, sticky='w')

EDate = DateEntry(F1, width=18, background='blue',
                  foreground='white', font=(None, 18))
EDate.grid(row=1, column=1, padx=5, pady=5, sticky='w')

# -------------------------------

LTitle = ttk.Label(F1, text='Title', font=(None, 18))
LTitle.grid(row=2, column=0, padx=5, pady=5, sticky='w')

Title = StringVar()

ETitle = ttk.Entry(F1, textvariable=Title, font=(None, 18))
ETitle.grid(row=2, column=1, padx=5, pady=5, sticky='w')

# --------------------------------

LExpense = ttk.Label(F1, text='Expenses', font=(None, 18))
LExpense.grid(row=3, column=0, padx=5, pady=5, sticky='w')

Expense = StringVar()

EExpense = ttk.Entry(F1, textvariable=Expense, font=(None, 18))
EExpense.grid(row=3, column=1, padx=5, pady=5, sticky='w')

# ---------------------------------

BF1Add = ttk.Button(F1, text='Add Expense', command=lambda: AddtoDB("e"))
BF1Add.grid(row=4, column=1, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)

# ----------------------------------

TVList = ['Date', 'Title', 'Expenses']
TVExpenses = ttk.Treeview(F1, columns=TVList, show='headings', height=5)
for i in TVList:
    TVExpenses.heading(i, text=i.title())
TVExpenses.grid(row=5, column=0, padx=5, pady=5, sticky='w', columnspan=3)

# --------------------Expense End--------------

# --------------------Income-------------------

LDate2 = ttk.Label(F2, text='Date', font=(None, 18))
LDate2.grid(row=1, column=0, padx=5, pady=5, sticky='w')

EDate2 = DateEntry(F2, width=18, background='blue',
                   foreground='white', font=(None, 18))
EDate2.grid(row=1, column=1, padx=5, pady=5, sticky='w')

# -------------------------------

LSource = ttk.Label(F2, text='Source', font=(None, 18))
LSource.grid(row=2, column=0, padx=5, pady=5, sticky='w')

Source = StringVar()

ESource = ttk.Entry(F2, textvariable=Source, font=(None, 18))
ESource.grid(row=2, column=1, padx=5, pady=5, sticky='w')

# --------------------------------

LIncome = ttk.Label(F2, text='Income', font=(None, 18))
LIncome.grid(row=3, column=0, padx=5, pady=5, sticky='w')

Income = StringVar()

EIncome = ttk.Entry(F2, textvariable=Income, font=(None, 18))
EIncome.grid(row=3, column=1, padx=5, pady=5, sticky='w')

# ---------------------------------

BF2Add = ttk.Button(F2, text='Add Income', command=lambda: AddtoDB("i"))
BF2Add.grid(row=4, column=1, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)

# ----------------------------------
TV = ['Date', 'Source', 'Income']
TVIncome = ttk.Treeview(F2, columns=TV, show='headings', height=5)
for j in TV:
    TVIncome.heading(j, text=j.title())
TVIncome.grid(row=5, column=0, padx=5, pady=5, sticky='w', columnspan=3)


GUI.mainloop()
