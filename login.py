
from asyncio.windows_events import NULL
from cProfile import label
from cgitb import text
from sqlite3 import Cursor
from tkinter import*
from tkinter import ttk
from turtle import bgcolor, color
import mysql.connector as mysql
from home import*
import signin


class Login_Window():
    def login_to_home(self, root):
        username = self.txtuser.get()
        if(self.txtuser.get() == '' or self.txtpass.get() == ''):
            MessageBox.showinfo("Insert Status", "All Field are required")
        else:
            con = mysql.connect(host='localhost', user='root',
                                password='Mahendra@$28', database='expensetracker')
            cursor = con.cursor()
            cursor.execute("select* from signupdata where username = %s and password = %s", (self.txtuser.get(), self.txtpass.get()))
            data = cursor.fetchone()
            cursor.execute("commit")
            con.close()
            if(data == None):
                MessageBox.showerror("ERROR", "Invalid Credentials")
            else:
                print(data)
                MessageBox.showinfo("Login Status", "Login Successfully")
                root.destroy()
                h = Home(username)

    def login_to_signin():
        signin.Sign_Window()

    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("1000x900+100+0")
        self.root.configure(bg='#b8c6db')

        frame = Frame(self.root, bg="#9921e8", border=15)
        frame.place(x=350, y=100, width=340, height=450)
        lab1 = Label(frame, text="Expense Tracker", font=(
            "times new roman", 22, "bold"), fg="black", bg="#9921e8")
        lab1.place(x=50, y=50)

        get_str = Label(frame, text="Get Started", font=(
            "times new roman", 20, "bold"), fg="Black", bg="#9921e8")
        get_str.place(x=80, y=100)

        # label
        username = lbl = Label(frame, text="Username :", font=(
            "times new roman", 19), fg="white", bg="#9921e8")
        username.place(x=60, y=155)

        self.txtuser = Entry(frame, font=("times new roman", 15))
        self.txtuser.place(x=60, y=185)

        password = lbl = Label(frame, text="Password :", font=(
            "times new roman", 19), fg="white", bg="#9921e8")
        password.place(x=60, y=220)

        self.txtpass = Entry(frame, font=(
            "times new roman", 15), show="*")
        self.txtpass.place(x=60, y=250)

        loginbtn = Button(frame, text="Login", font=("times new roman", 19, "bold"),
                          bd=3, relief=RIDGE, fg="Black", command =lambda: Login_Window.login_to_home(self, root))
        loginbtn.place(x=35, y=350, width=120, height=35)

        signinbtn = Button(frame, text="Sign in", font=("times new roman", 19, "bold"),
                           bd=3, relief=RIDGE, fg="Black", command=lambda: Login_Window.login_to_signin())
        signinbtn.place(x=175, y=350, width=120, height=35)


if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()
