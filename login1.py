from tkinter import *
from tkinter import ttk
from tkinter.ttk import Notebook
from typing_extensions import Self
from home import*


class Login:

    def __init__(Self, G):
        Self.G = G
        Self.G.title("Login Page")
        Self.G.geometry('700x500')

        Self.T = Notebook(Self.G)

        Self.F3 = Frame(Self.T)
        Self.T.add(Self.F3, text='Login')

        Self.T.pack(fill=BOTH, expand=1)
        Self.BF3Add = ttk.Button(
            Self.F3, text='Sign in')
        Self.BF3Add.grid(row=4, column=1, padx=5, pady=5,
                         sticky='w', ipadx=10, ipady=10)
        Self.BF4Add = ttk.Button(Self.F3, text='Login')
        Self.BF4Add.grid(row=5, column=1, padx=5, pady=5,
                         sticky='w', ipadx=10, ipady=10)


if __name__ == "__main__":
    G = Tk()
    app = Login(G)
    G.mainloop()
