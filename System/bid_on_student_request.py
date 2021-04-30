from tkinter import *

root_url = 'https://fit3077.com/api/v1'
users_url = root_url + "/user"


class BidOnStudent:
    window = None

    def __init__(self):
        None

    def start(self):
        self.window = Tk()
        self.window.title("Bid on Student Request")
        self.window.geometry('300x250')
        self.window.mainloop()
        return
