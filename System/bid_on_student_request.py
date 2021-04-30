from tkinter import *


class BidOnStudent:
    window = None

    def __init__(self):
        pass

    def start(self):
        self.window = Tk()
        self.window.title("Bid on Student Request")
        self.window.geometry('300x250')
        self.window.mainloop()

        Label(self.window, text="Search request for subject: ").grid(row=0, column=0)

        OPTIONS = ["Open", "Closed"]

        variable = StringVar(self.window)
        variable.set(OPTIONS[0])
        w = OptionMenu(self.window, variable, *OPTIONS)
        w.configure(width=20)
        w.grid(row=0, column=1)



        return
