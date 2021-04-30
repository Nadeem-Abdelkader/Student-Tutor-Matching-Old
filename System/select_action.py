from tkinter import *

from bid_on_student_request import BidOnStudent
from new_tutor_request import NewTutorRequest
from see_contracts import SeeContracts
from user_collection import UserCollection


class SelectAction:
    API_KEY = "mPRM67bLTWDwchrMCtBCrWbh89tQb6"
    USERS = UserCollection(API_KEY)
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
        Button(text="New Tutor Request", height="2", width="30", command=self.new_request).pack()
        Label(text="").pack()
        Button(text="Bid on Student Request", height="2", width="30", command=self.bid_on_student).pack()
        Label(text="").pack()
        Button(text="See Your Contracts", height="2", width="30", command=self.see_contract).pack()
        self.window.mainloop()
        return

    def new_request(self):
        self.window.destroy()
        s = NewTutorRequest()
        s.start()

    def bid_on_student(self):
        self.window.destroy()
        s = BidOnStudent()
        s.start()

    def see_contract(self):
        self.window.destroy()
        s = SeeContracts()
        s.start()
