from tkinter import ttk
from login import *

root_url = 'https://fit3077.com/api/v1'
users_url = root_url + "/user"


class SelectAction:
    current_user = None
    window = None

    def __init__(self, current):
        self.current_user = current

    def start(self):
        self.window = Tk()
        self.window.geometry('300x250')
        self.window.title('Welcome')
        Label(text="Welcome back, what do you want to do today? ", width="300", height="2", font=("Calibri", 13)).pack()
        Label(text="").pack()
        Button(text="New Tutor Request", height="2", width="30").pack()
        # , command = login
        Label(text="").pack()
        Button(text="Bid on Student Request", height="2", width="30").pack()
        # , command=register
        Label(text="").pack()
        Button(text="See Your Contracts", height="2", width="30").pack()
        # , command=

        self.window.mainloop()
