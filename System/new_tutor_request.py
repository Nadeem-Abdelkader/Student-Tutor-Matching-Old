from tkinter import *


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
