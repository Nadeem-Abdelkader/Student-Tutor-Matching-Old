from tkinter import *
import requests

from subject import Subject

root_url = 'https://fit3077.com/api/v1'
bid_url = root_url + "/bid"

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
        self.window.geometry('700x600')

        Label(self.window, text="Search request for subject: ").grid(row=0, column=0)

        subjects = Subject().get_subject_names()

        self.subject = StringVar(self.window)
        self.subject.set(subjects[0])
        option_menu = OptionMenu(self.window, self.subject, *subjects, command=self.display_bids_for_subject)
        option_menu.configure(width=20)
        option_menu.grid(row=0, column=1)

        Label(self.window, text="Available requests: ").grid(row=2, column=0)

        text_area = Text(self.window, height=10, width=35)
        text_area.grid(row=3)
        text_area.config(state=DISABLED)

        Label(self.window, text="Request detail: ").grid(row=4, column=0)

        Text(self.window, height=11, width=40).grid(row=5)

        Button(self.window, text='Display Selected Bid Details', command=self.get_selected_item).grid(row=6, column=0)

        Label(self.window, text="Create a bid: ").grid(row=7, column=0)

        Label(self.window, text="Hours per session: ").grid(row=8, column=0)

        numbers = ["1", "2", "3", "4", "5", "6", "7"]

        hours_per_session = StringVar(self.window)
        hours_per_session.set(numbers[0])
        option_menu = OptionMenu(self.window, hours_per_session, *numbers)
        option_menu.configure(width=20)
        option_menu.grid(row=8, column=1)

        Label(self.window, text="Rate per session: ").grid(row=9, column=0)

        numbers = ["1", "2", "3", "4", "5", "6", "7"]

        rate_per_session = StringVar(self.window)
        rate_per_session.set(numbers[0])
        option_menu = OptionMenu(self.window, rate_per_session, *numbers)
        option_menu.configure(width=20)
        option_menu.grid(row=9, column=1)

        Button(text="See All Bids", command=self.see_all_bids).grid(row=10, column=0)

        Button(text="Create Bid", command=self.create_bid).grid(row=10, column=1)

        Label(self.window, text="OR").grid(row=8, column=2)

        Button(text="Buy Out Request", command=self.buy_out_request).grid(row=8, column=3)

        Button(text="Message Student", command=self.message_student).grid(row=9, column=3)

        self.window.mainloop()

        return

    def see_all_bids(self):
        response = requests.get(url=bid_url, headers={'Authorization': 'mPRM67bLTWDwchrMCtBCrWbh89tQb6'})
        return response.json()

    def create_bid(self):
        pass

    def buy_out_request(self):
        pass

    def message_student(self):
        pass

    def display_bids_for_subject(self, subject):
        self.list_box = Listbox(self.window)
        n = 1
        for bid in self.all_bids:
            if bid['subject']['name'] == subject:
                self.list_box.insert(1, str(bid['id']) + "\n")
            n += 1
        self.list_box.grid(row=3)
        self.list_box.configure(width=35)

    def get_selected_item(self):
        for i in self.list_box.curselection():
            self.selected_bid = self.list_box.get(i)
        for bid in self.all_bids:
            current_id = bid['id']
            selected_bid_id = str(self.selected_bid).rstrip("\n")
            if current_id == selected_bid_id:
                selected_bid_details_text_area = Text(self.window)
                selected_bid_details_text_area.insert(INSERT, str("id: ") + str(bid['id']) + "\n")
                selected_bid_details_text_area.insert(INSERT, str("type: ") + str(bid['type']) + "\n")
                selected_bid_details_text_area.insert(INSERT, str("Initiator: ") + str(bid['initiator']['givenName']) + " " + str(
                    bid['initiator']['familyName']) + "\n")
                selected_bid_details_text_area.insert(INSERT, str("Date Created: ") + str(bid['dateCreated']) + "\n")
                selected_bid_details_text_area.insert(INSERT, str("Date Closed: ") + str(bid['dateClosedDown']) + "\n")
                selected_bid_details_text_area.insert(INSERT, str("Subject: ") + str(bid['subject']['name']) + "\n")
                try:
                    competency = bid['additionalInfo']['competency']
                except KeyError:
                    competency = None
                try:
                    hours_per_week = bid['additionalInfo']['hours_per_week']
                except KeyError:
                    hours_per_week = None
                try:
                    sessions_per_week = bid['additionalInfo']['sessions_per_week']
                except KeyError:
                    sessions_per_week = None
                try:
                    rate_per_session = bid['additionalInfo']['rate_per_session']
                except KeyError:
                    rate_per_session = None
                selected_bid_details_text_area.insert(INSERT, str("Competency: ") + str(competency) + "\n")
                selected_bid_details_text_area.insert(INSERT, str("Hours Per Week: ") + str(hours_per_week) + "\n")
                selected_bid_details_text_area.insert(INSERT, str("Sessions Per Week: ") + str(sessions_per_week) + "\n")
                selected_bid_details_text_area.insert(INSERT, str("Rate Per Session: ") + str(rate_per_session) + "\n")
                selected_bid_details_text_area.grid(row=5)
                selected_bid_details_text_area.configure(width=40, height=11)
                selected_bid_details_text_area.config(state=DISABLED)
