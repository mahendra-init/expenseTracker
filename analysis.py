from tkinter import *
from tkinter import ttk



class DataAnalysis():
    def analysisFrame():
        F3 = Frame()
        Lbl = Label(F3, text='Expense Sheet:', font=(None, 15))
        Lbl.place(x = 15, y = 10)

        ExList = ['Date', 'Category', 'Description', 'Amount Spent', 'Paid Through']
        ExListView = ttk.Treeview(
            F3, columns=ExList, show='headings', height=5)
        ExListView.place(x= 20, y= 45)
        ExListView.column("Date", minwidth=0, width=50, stretch=NO, anchor=CENTER)
        ExListView.column("Category", minwidth=0, width=120, stretch=NO)
        ExListView.column("Description", minwidth=0, width=280)
        ExListView.column("Amount Spent", minwidth=0, width=120, stretch=NO, anchor=CENTER)
        ExListView.column("Paid Through", minwidth=0, width=90, stretch=NO)

        for i in ExList:
            ExListView.heading(i, text=i.title())
        
        
        Lb2 = Label(F3, text='Income Sheet:', font=(None, 15))
        Lb2.place(x = 15, y = 250)

        InList = ['Date', 'Source', 'Amount']
        InListView = ttk.Treeview(
            F3, columns=InList, show='headings', height=3)
        InListView.place(x= 20, y= 295)
        InListView.column("Date", minwidth=0, width=50, stretch=NO, anchor=CENTER)
        InListView.column("Source", minwidth=0, width=120, stretch=NO)
        InListView.column("Amount", minwidth=0, width=280, anchor = CENTER)

        for i in InList:
            InListView.heading(i, text=i.title())
        return F3

