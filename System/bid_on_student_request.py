from tkinter import *
import requests

from subject import Subject


class BidOnStudent:
    window = None
    current_user = None
    api_key = None
    subject = None
    all_bids = None
    list_box = None
    selected_bid = None

    def __init__(self, current, api_key):
        self.current_user = current
        self.api_key = api_key
        self.all_bids = self.see_all_bids()

    def start(self):
        self.window = Tk()
        self.window.title("Bid on Student Request")
        self.window.geometry('700x700')

        Label(self.window, text="Search request for subject: ").grid(row=0, column=0)

        SUBJECTS = Subject().get_subject_names()

        self.subject = StringVar(self.window)
        self.subject.set(SUBJECTS[0])
        w = OptionMenu(self.window, self.subject, *SUBJECTS, command=self.display_bids_for_subject)
        w.configure(width=20)
        w.grid(row=0, column=1)

        Label(self.window, text="Available requests: ").grid(row=2, column=0)

        # left as text for now
        t = Text(self.window, height=10, width=35)
        t.grid(row=3)
        # x = self.see_all_bids()
        # Lb1 = Listbox(self.window)
        # n = 1
        # for i in x:
        #     if i['subject']['name'] == self.subject:
        #         Lb1.insert(1, str(i['id']) + "\n")
        #     n+=1
        # Lb1.grid(row=3)
        # Lb1.configure(width=40)
        t.config(state=DISABLED)
        # a.grid(row=3)

        Label(self.window, text="Request detail: ").grid(row=4, column=0)

        # left as text for now
        t = Text(self.window, height=5, width=40)
        t.grid(row=5)
        # a.grid(row=3)

        btn = Button(self.window, text='Display Selected Bid Details', command=self.get_selected_item).grid(row=6,
                                                                                                            column=0)

        Label(self.window, text="Create a bid: ").grid(row=7, column=0)

        Label(self.window, text="Hours per session: ").grid(row=8, column=0)

        NUMBERS = ["1", "2", "3", "4", "5", "6", "7"]

        variable = StringVar(self.window)
        variable.set(NUMBERS[0])
        w = OptionMenu(self.window, variable, *NUMBERS)
        w.configure(width=20)
        w.grid(row=8, column=1)
        # w.pack()

        Label(self.window, text="Rate per session: ").grid(row=9, column=0)

        NUMBERS = ["1", "2", "3", "4", "5", "6", "7"]

        variable = StringVar(self.window)
        variable.set(NUMBERS[0])
        w = OptionMenu(self.window, variable, *NUMBERS)
        w.configure(width=20)
        w.grid(row=9, column=1)
        # w.pack()

        Button(text="See All Bids", command=self.see_all_bids).grid(row=10, column=0)

        Button(text="Create Bid", command=self.create_bid).grid(row=10, column=1)

        Label(self.window, text="OR").grid(row=8, column=2)

        Button(text="Buy Out Request", command=self.buy_out_request).grid(row=8, column=3)

        Button(text="Message Student", command=self.message_student).grid(row=9, column=3)

        self.window.mainloop()

        return

    def see_all_bids(self):
        bidurl = "https://fit3077.com/api/v1/bid?fields="
        response = requests.get(url=bidurl, headers={'Authorization': 'mPRM67bLTWDwchrMCtBCrWbh89tQb6'})
        print(response.json())
        return response.json()
        pass

    def create_bid(self):
        pass

    def buy_out_request(self):
        pass

    def message_student(self):
        pass

    def display_bids_for_subject(self, subject):
        self.list_box = Listbox(self.window)
        n = 1
        for i in self.all_bids:
            # print(self.subject)
            # print(i['subject']['name'])
            if i['subject']['name'] == subject:
                self.list_box.insert(1, str(i['id']) + "\n")
            n += 1
        self.list_box.grid(row=3)
        self.list_box.configure(width=35)

    def get_selected_item(self):
        # Traverse the tuple returned by
        # curselection method and print
        # correspoding value(s) in the listbox
        for i in self.list_box.curselection():
            self.selected_bid = self.list_box.get(i)
            # print(self.selected_bid)
        for j in self.all_bids:
            # print(j['id'])
            # print(self.selected_bid)
            # print(j['id'])
            # print("a: " + str(self.selected_bid))
            # print(j['id'])
            current_id = j['id']
            selected_bid_id = str(self.selected_bid).rstrip("\n")
            if current_id == selected_bid_id:
                # print(j)
                self.listbox2 = Listbox(self.window)
                self.listbox2.insert(1, str("id: ") + str(j['id']) + "\n")
                self.listbox2.insert(2, str("type: ") + str(j['type']) + "\n")
                self.listbox2.insert(3, str("Initiator: ") + str(j['initiator']['givenName']) + " " + str(
                    j['initiator']['familyName']) + "\n")
                self.listbox2.insert(4, str("Date Created: ") + str(j['dateCreated']) + "\n")
                self.listbox2.insert(5, str("Date Closed: ") + str(j['dateClosedDown']) + "\n")
                self.listbox2.insert(6, str("Subject: ") + str(j['subject']['name']) + "\n")
                self.listbox2.grid(row=5)
                self.listbox2.configure(width=35)
                # print(j['id'])
