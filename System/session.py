from tkinter import ttk
from login import *

root_url = 'https://fit3077.com/api/v1'
users_url = root_url + "/user"


class Session:
    current_user = None
    window = None

    def __init__(self, current):
        self.current_user = current

    def start(self):
        self.window = Tk()
        self.window.geometry('400x150')
        self.window.title('Student - Tutor Matching Software (Screen #2)')

        self.window.mainloop()
