from tkinter import *
import requests

from subject import Subject


class BidOnStudent:
    window = None

    def __init__(self, current, api_key):
        self.current_user = current
        self.api_key = api_key

    def start(self):
        self.window = Tk()
        self.window.title("Bid on Student Request")
        self.window.geometry('700x500')

        Label(self.window, text="Search request for subject: ").grid(row=0, column=0)

        SUBJECTS = Subject().get_subject_names()

        variable = StringVar(self.window)
        variable.set(SUBJECTS[0])
        w = OptionMenu(self.window, variable, *SUBJECTS)
        w.configure(width=20)
        w.grid(row=0, column=1)

        Label(self.window, text="Available requests: ").grid(row=2, column=0)

        # left as text for now
        t = Text(self.window, height=5, width=40)
        t.grid(row=3)
        # a.grid(row=3)

        Label(self.window, text="Request detail: ").grid(row=4, column=0)

        # left as text for now
        t = Text(self.window, height=5, width=40)
        t.grid(row=5)
        # a.grid(row=3)

        Label(self.window, text="Create a bid: ").grid(row=6, column=0)

        Label(self.window, text="Hours per session: ").grid(row=7, column=0)

        NUMBERS = ["1", "2", "3", "4", "5", "6", "7"]

        variable = StringVar(self.window)
        variable.set(NUMBERS[0])
        w = OptionMenu(self.window, variable, *NUMBERS)
        w.configure(width=20)
        w.grid(row=7, column=1)
        # w.pack()

        Label(self.window, text="Rate per session: ").grid(row=8, column=0)

        NUMBERS = ["1", "2", "3", "4", "5", "6", "7"]

        variable = StringVar(self.window)
        variable.set(NUMBERS[0])
        w = OptionMenu(self.window, variable, *NUMBERS)
        w.configure(width=20)
        w.grid(row=8, column=1)
        # w.pack()

        Button(text="See All Bids", command=self.see_all_bids).grid(row=9, column=0)

        Button(text="Create Bid", command=self.create_bid).grid(row=9, column=1)

        Label(self.window, text="OR").grid(row=7, column=2)


        Button(text="Buy Out Request", command=self.buy_out_request).grid(row=7, column=3)

        Button(text="Message Student", command=self.message_student).grid(row=8, column=3)



        self.window.mainloop()

        return

    def see_all_bids(self):
        bidurl = "https://fit3077.com/api/v1/bid?fields="
        response = requests.get(url=bidurl, headers={'Authorization':'mPRM67bLTWDwchrMCtBCrWbh89tQb6'})
        return response.json()
        pass

    def create_bid(self):
        pass

    def buy_out_request(self):
        pass

    def message_student(self):
        pass
