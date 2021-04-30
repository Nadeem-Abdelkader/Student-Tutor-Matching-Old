from tkinter import *
from tkinter import messagebox
import requests

# from select_action import SelectAction
from user_collection import UserCollection

root_url = 'https://fit3077.com/api/v1'
users_url = root_url + "/user"


class NewTutorRequest:
    window = None

    def __init__(self):
        None

    def start(self):
        self.window = Tk()
        self.window.title("New Tutor Request")
        self.window.geometry('300x250')
        self.window.mainloop()
        return
