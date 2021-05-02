from tkinter import *
from datetime import datetime
import requests

from subject import Subject

# Global variables
root_url = 'https://fit3077.com/api/v1'
bid_url = root_url + "/bid"


class BidOnStudent:
    """
    This class is responsible for the Bid on Student Request screen that allows tutors to view students requests and
    bid on them
    """
    # Class variables
    window = None
    current_user = None
    api_key = None
    subject = None
    all_bids = None
    list_box = None
    selected_bid = None

    def __init__(self, current_user, api_key):
        """
        This __init__ method initialises some of class variables, either according to input ot by calling another method
        :param current_user: current user of the system
        :param api_key: api key
        """
        self.current_user = current_user
        self.api_key = api_key
        self.all_bids = self.see_all_bids()

    def main(self):
        """
        This method creates the Bid on Student Request screen which will show tutors the available requests for each
        subject and if the tutor wishes the request details
        """
        # This portion is responsible of creating the window and formatting it
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
        for i in self.see_all_bids():
            text_area.insert(INSERT, i['id'])
        text_area.grid(row=3)
        text_area.config(state=DISABLED)

        Label(self.window, text="Request detail: ").grid(row=4, column=0)

        Text(self.window, height=11, width=40).grid(row=5)

        Button(self.window, text='Display Selected Bid Details', command=self.get_selected_bid_details).grid(row=6,
                                                                                                             column=0)

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

    def see_all_bids(self):
        """
        This methods retrieves all bids available
        :return: all bids available
        """
        response = requests.get(url=bid_url, headers={'Authorization': 'mPRM67bLTWDwchrMCtBCrWbh89tQb6'})
        return response.json()

    def create_bid(self):
        pass

    def buy_out_request(self):
        """
        This method is responsible for allowing the tutor to buy out a student request
        """
        # buyouturl = 'https://fit3077.com/api/v1/bid/' + self.selected_bid.id + '/close-down'
        buy_out_url = 'https://fit3077.com/api/v1/bid/bc06e9ad-5d20-4dce-a176-a6ac73b26b35/close-down'
        response = requests.post(url=buy_out_url, headers={'Authorization':self.api_key})
        json_data = response.json()

    def message_student(self):
        """
        This method is responsible for allowing tutor to message student
        """
        msg_url = 'https://fit3077.com/api/v1/message'
        date_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
        present_time = date_time[0:-3] + 'Z'
        # Using the web service post() method to create request
        response = requests.post(url=msg_url, headers={'Authorization': self.api_key}, json={
            # "bidId": self.selected_bid.id
            "bidId": self.see_all_bids()[0]['id'],
            "posterId": self.current_user.id,
            "datePosted": present_time,
            "content": 'testing12345',
            "additionalInfo":{}
        }
                                 )
        json_data = response.json()

    def display_bids_for_subject(self, subject):
        """
        This method displays all bids available to the selected subject in a clickable list box
        :param subject: subject to display bids for
        """
        self.list_box = Listbox(self.window)
        n = 1
        # loops in bids and if name of subject matches the subject name were looking for then add to listbox
        for bid in self.all_bids:
            if bid['subject']['name'] == subject:
                self.list_box.insert(1, str(bid['id']) + "\n")
            n += 1
        self.list_box.grid(row=3)
        self.list_box.configure(width=35)

    def get_selected_bid_details(self):
        """
        This method gets the selected bid details and inserts them into a text area
        """
        # getting the selected bid
        for i in self.list_box.curselection():
            self.selected_bid = self.list_box.get(i)
        # looping the bids and if id matches the id were looking for add its details to text area
        for bid in self.all_bids:
            current_id = bid['id']
            selected_bid_id = str(self.selected_bid).rstrip("\n")
            if current_id == selected_bid_id:
                selected_bid_details_text_area = Text(self.window)
                selected_bid_details_text_area.insert(INSERT, str("id: ") + str(bid['id']) + "\n")
                selected_bid_details_text_area.insert(INSERT, str("type: ") + str(bid['type']) + "\n")
                selected_bid_details_text_area.insert(INSERT, str("Initiator: ") + str(
                    bid['initiator']['givenName']) + " " + str(
                    bid['initiator']['familyName']) + "\n")
                selected_bid_details_text_area.insert(INSERT, str("Date Created: ") + str(bid['dateCreated']) + "\n")
                selected_bid_details_text_area.insert(INSERT, str("Date Closed: ") + str(bid['dateClosedDown']) + "\n")
                selected_bid_details_text_area.insert(INSERT, str("Subject: ") + str(bid['subject']['name']) + "\n")
                # this portion is responsible to get the additional info if available, if not assign to None
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
                selected_bid_details_text_area.insert(INSERT,
                                                      str("Sessions Per Week: ") + str(sessions_per_week) + "\n")
                selected_bid_details_text_area.insert(INSERT, str("Rate Per Session: ") + str(rate_per_session) + "\n")
                selected_bid_details_text_area.grid(row=5)
                selected_bid_details_text_area.configure(width=40, height=11)
                selected_bid_details_text_area.config(state=DISABLED)
