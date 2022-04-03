
from cProfile import label
from cgitb import text
from logging import root
from sqlite3 import Cursor
from tkinter import*
from turtle import bgcolor, color
import mysql.connector
from home import*


class Sign_Window():

    def temp3(self):
        name1 = self.txtname.get()
        user1 = self.txtuser.get()
        pasw1 = self.txtpass.get()
        emailId1 = self.txtemail.get()
        mobile1 = self.txtmobile.get()
        # if(self.txtname == '' or self.txtuser == '' or self.txtpass == ''):
        #     MessageBox.showinfo("Insert Status", "All Field are required")
        # else:
        #     con = mysql.connect(host='localhost', user='root',
        #                         password='Shivam@$12', database='expensetracker')
        #     cursor = con.cursor()
        #     cursor.execute("insert into signin values('" + name1
        #                    + "','"+user1+"','"+pasw1+"','"+emailId1+"','"+mobile1+"')")
        #     cursor.execute("commit")
        #     MessageBox.showinfo("Sign In Status", "Sign In Successfully")
        #     con.close()
        self.root.destroy()
        o = Home()

    def __init__(self):
        self.root = Tk()
        self.root.title("Sign In Page")
        self.root.geometry("1000x900+100+0")
        self.root.configure(bg='#b8c6db')

# ----------Frame----------------
        frame = Frame(self.root, bg="#9921e8", border=15)
        frame.place(x=275, y=50, width=450, height=550)

        # img1 = Image.open(
        #     r"C:\\Users\\sspat\\OneDrive\\Desktop\\Expense Tracker\\images\\bgi1.png")
        # img1 = img1.resize((100, 100), Image.ANTIALIAS)
        # self.photoimage1 = IMAGETEXT.PhotoImage(img1)
        # lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        # lblimg1.place(x=730, y=175, width=100, height=100)

        lab1 = Label(frame, text="Expense Tracker", font=(
            "times new roman", 23, "bold"), fg="black", bg="#9921e8")
        lab1.place(x=110, y=50)

# -----------label-------------

        name = lbl = Label(frame, text="Name:", font=(
            "times new roman", 19), fg="white", bg="#9921e8")
        name.place(x=40, y=155)

        self.txtname = Entry(frame,  font=("times new roman", 15))
        self.txtname.place(x=160, y=155)

# ----------------------------------------

        username = lbl = Label(frame, text="Username:", font=(
            "times new roman", 19), fg="white", bg="#9921e8")
        username.place(x=40, y=205)

        self.txtuser = Entry(frame, font=("times new roman", 15))
        self.txtuser.place(x=160, y=205)

# ----------------------------------------

        password = lbl = Label(frame, text="Password:", font=(
            "times new roman", 19), fg="white", bg="#9921e8")
        password.place(x=40, y=255)

        self.txtpass = Entry(frame,  font=("times new roman", 15))
        self.txtpass.place(x=160, y=255)

# ------------------------------------------

        emailId = lbl = Label(frame, text="Email-id:", font=(
            "times new roman", 19), fg="white", bg="#9921e8")
        emailId.place(x=40, y=305)

        self.txtemail = Entry(frame, font=("times new roman", 15))
        self.txtemail.place(x=160, y=305)

# =========================================

        mobile = lbl = Label(frame, text="Mobile No:", font=(
            "times new roman", 19), fg="white", bg="#9921e8")
        mobile.place(x=40, y=355)

        self.txtmobile = Entry(frame,  font=("times new roman", 15))
        self.txtmobile.place(x=160, y=355)

# ===========================================

        signinbtn = Button(frame, text="Sign up", font=("times new roman", 19, "bold"),
                           bd=3, relief=RIDGE, fg="Black", command=lambda: Sign_Window.temp3(self))
        signinbtn.place(x=150, y=450, width=120, height=35)

# ============================================
        self.root.mainloop()
