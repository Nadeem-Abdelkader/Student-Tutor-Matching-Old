from tkinter import *


class SeeContracts:
    window = None

    def __init__(self):
        pass

    def start(self):
        self.window = Tk()
        self.window.title("See Your Contracts")
        self.window.geometry('300x250')
        self.window.mainloop()
        return
