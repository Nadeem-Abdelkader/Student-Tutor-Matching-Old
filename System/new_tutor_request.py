from datetime import datetime
from tkinter import *
import requests
from new_request_details import NewRequestDetails
from subject import Subject

# Global Variables
root_url = 'https://fit3077.com/api/v1'
bid_url = root_url + "/bid"


class NewTutorRequest:
    """
    THis class is responsible for displaying the New Tutor Request screen that allows student to create a request for 
    a tutor 
    """
    # Class  variables
    window = None
    bid_type = None
    subject = None
    competency = None
    hours_per_session = None
    sessions_per_week = None
    rate_per_session = None
    current_user = None
    api_key = None

    def __init__(self, current_user, api_key):
        """
        This __init__ method assigns the input current_user to the class variable current_user and the input api_key 
        to the class variale api_key 
        """
        self.current_user = current_user
        self.api_key = api_key

    def main(self):
        """
        THis method displays the New Tutor Request screen that allows students to create a ne request for a tutor
        """
        # This portion is responsible for the formatting of the screen
        self.window = Tk()
        self.window.title("New Tutor Request")
        self.window.geometry('400x200')

        Label(self.window, text="Bid Type: ").grid(row=0, column=0)

        options = ["open", "closed"]

        self.bid_type = StringVar(self.window)
        self.bid_type.set(options[0])
        option_menu = OptionMenu(self.window, self.bid_type, *options)
        option_menu.configure(width=20)
        option_menu.grid(row=0, column=1)

        Label(self.window, text="Subject: ").grid(row=2, column=0)

        subjects = Subject().get_subject_names()

        self.subject = StringVar(self.window)
        self.subject.set(subjects[0])
        option_menu = OptionMenu(self.window, self.subject, *subjects)
        option_menu.configure(width=20)
        option_menu.grid(row=2, column=1)

        Label(self.window, text="Competency: ").grid(row=4, column=0)

        numbers = ["1", "2", "3", "4", "5", "6", "7"]

        self.competency = StringVar(self.window)
        self.competency.set(numbers[0])
        option_menu = OptionMenu(self.window, self.competency, *numbers)
        option_menu.configure(width=20)
        option_menu.grid(row=4, column=1)

        Label(self.window, text="Hours per session: ").grid(row=6, column=0)

        self.hours_per_session = StringVar(self.window)
        self.hours_per_session.set(numbers[0])
        option_menu = OptionMenu(self.window, self.hours_per_session, *numbers)
        option_menu.configure(width=20)
        option_menu.grid(row=6, column=1)

        Label(self.window, text="Sessions per week: ").grid(row=8, column=0)

        self.sessions_per_week = StringVar(self.window)
        self.sessions_per_week.set(numbers[0])
        option_menu = OptionMenu(self.window, self.sessions_per_week, *numbers)
        option_menu.configure(width=20)
        option_menu.grid(row=8, column=1)

        Label(self.window, text="Rate per session: ").grid(row=10, column=0)

        self.rate_per_session = Entry(self.window, textvariable="rate")
        self.rate_per_session.configure(width=20)
        self.rate_per_session.grid(row=10, column=1)

        Button(text="Create Request", height="2", width="20", command=self.create_request).grid(row=12, column=1)

        self.window.mainloop()

    def create_request(self):
        """
        This method is called when the create request button is created. It creates a new request with the 
        information provided by the student :return: 
        """
        date_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
        present_time = date_time[0:-3] + 'Z'
        # Using the web service post() method to create request
        response = requests.post(url=bid_url, headers={'Authorization': self.api_key}, json={
            "type": self.bid_type.get(),
            "initiatorId": self.current_user.id,
            "dateCreated": present_time,
            "subjectId": Subject().get_id_by_name(self.subject.get()),
            "additionalInfo": {"competency": self.competency.get(), "hours_per_week": self.hours_per_session.get(),
                               "sessions_per_week": self.sessions_per_week.get(),
                               "rate_per_session": self.rate_per_session.get()}
        }
                                 )
        json_data = response.json()
        # Destroying current window and jumping to next screen by calling the main() method from the NewRequestDetails 
        # class
        self.window.destroy()
        NewRequestDetails(json_data).main()
