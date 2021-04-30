from tkinter import *


class NewTutorRequest:
    window = None

    def __init__(self):
        None

    def start(self):
        self.window = Tk()
        self.window.title("New Tutor Request")
        self.window.geometry('400x250')

        # Label(self.window, text="").pack()
        Label(self.window, text="Bid Type: ").grid(row=0, column=0)

        OPTIONS = ["Open", "Closed"]

        variable = StringVar(self.window)
        variable.set(OPTIONS[0])
        w = OptionMenu(self.window, variable, *OPTIONS).grid(row=0, column=1)
        # w.pack()

        # Label(self.window, text="").pack()
        Label(self.window, text="Subject: ").grid(row=2, column=0)

        # Label(self.window, text="").pack()
        Label(self.window, text="Competency: ").grid(row=4, column=0)

        NUMBERS = ["1", "2", "3", "4", "5", "6", "7"]

        variable = StringVar(self.window)
        variable.set(NUMBERS[0])
        w = OptionMenu(self.window, variable, *NUMBERS).grid(row=4, column=1)
        # w.pack()

        # Label(self.window, text="").pack()
        Label(self.window, text="Hours per session: ").grid(row=6, column=0)

        variable = StringVar(self.window)
        variable.set(NUMBERS[0])
        w = OptionMenu(self.window, variable, *NUMBERS).grid(row=6, column=1)
        # w.pack()

        # Label(self.window, text="").pack()
        Label(self.window, text="Sessions per week: ").grid(row=8, column=0)

        variable = StringVar(self.window)
        variable.set(NUMBERS[0])
        w = OptionMenu(self.window, variable, *NUMBERS).grid(row=8, column=1)
        # w.pack()

        # Label(self.window, text="").pack()
        Label(self.window, text="Rate per session: ").grid(row=10, column=0)

        variable = StringVar(self.window)
        variable.set(NUMBERS[0])
        w = OptionMenu(self.window, variable, *NUMBERS).grid(row=10, column=1)
        # w.pack()

        # Label(self.window, text="").pack()
        Button(text="Create Request", height="2", width="20", command=self.create_request).grid(row=12, column=1)

        self.window.mainloop()
        return

    def create_request(self):
        None
