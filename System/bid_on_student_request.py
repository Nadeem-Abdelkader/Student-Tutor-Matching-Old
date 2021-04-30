from tkinter import *


class BidOnStudent:
    window = None

    def __init__(self):
        pass

    def start(self):
        self.window = Tk()
        self.window.title("Bid on Student Request")
        self.window.geometry('300x250')

        Label(self.window, text="Search request for subject: ").grid(row=0, column=0)

        SUBJECTS = ["", ""]

        variable = StringVar(self.window)
        variable.set(SUBJECTS[0])
        w = OptionMenu(self.window, variable, *SUBJECTS)
        w.configure(width=20)
        w.grid(row=0, column=1)

        Label(self.window, text="Search request for subject: ").grid(row=0, column=0)


        self.window.mainloop()


        return
