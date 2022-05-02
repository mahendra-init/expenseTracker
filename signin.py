
from tkinter import*
from tkinter import messagebox
import mysql.connector as mysql


class Sign_Window():

    def register(self):
        user1 = self.txtuser.get()
        name1 = self.txtname.get()
        pasw1 = self.txtpass.get()
        emailId1 = self.txtemail.get()
        mobile1 = self.txtmobile.get()
        if(user1 == '' or name1 == '' or mobile1 == '' or pasw1 == '' or emailId1 == ''):
            messagebox.showinfo("Insert Status", "All Field are required")
        else:
            con = mysql.connect(host='localhost', user='root',
                                password='Mahendra@$28', database='expensetracker')
            cursor = con.cursor()
            cursor.execute("select* from signupdata where username = '"+self.txtuser.get()+"'")
            data = cursor.fetchone()
            cursor.execute("commit")
            con.close()
            if(data == None):
                try:
                    con = mysql.connect(host='localhost', user='root',
                                        password='Mahendra@$28', database='expensetracker')
                    cursor = con.cursor()
                    cursor.execute("insert into signupdata values(%s,%s,%s,%s,%s)",(self.txtuser.get(),self.txtpass.get(),self.txtname.get(),self.txtemail.get(),self.txtmobile.get()))
                    cursor.execute("commit")
                    messagebox.showinfo("Sign In Status", "Sign In Successfully")
                    con.close()
                    self.root.destroy()
                except:
                    print("error occured")
            else:
                messagebox.showwarning("WARNING", "Username already existed!")

    def __init__(self):
        self.root = Tk()
        self.root.title("Sign In Page")
        self.root.geometry("1000x900+100+0")
        self.root.configure(bg='#b8c6db')
        
# ----------Frame----------------
        frame = Frame(self.root, bg="#9921e8", border=15)
        frame.place(x=275, y=50, width=450, height=550)

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
                           bd=3, relief=RIDGE, fg="Black", command=lambda: Sign_Window.register(self))
        signinbtn.place(x=150, y=450, width=120, height=35)

# ============================================
        self.root.mainloop()
        