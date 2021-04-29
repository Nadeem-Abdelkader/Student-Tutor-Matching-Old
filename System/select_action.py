from bid_on_student_request import bid_on_student_request
from new_tutor_request import new_tutor_request
from see_contracts import see_contracts
from tkinter import *

root_url = 'https://fit3077.com/api/v1'
users_url = root_url + "/user"
api_key = "mPRM67bLTWDwchrMCtBCrWbh89tQb6"


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
        Button(text="New Tutor Request", height="2", width="30", command=new_tutor_request).pack()
        Label(text="").pack()
        Button(text="Bid on Student Request", height="2", width="30", command=bid_on_student_request).pack()
        Label(text="").pack()
        Button(text="See Your Contracts", height="2", width="30", command=see_contracts).pack()
        self.window.mainloop()
