from datetime import datetime
from tkinter import *

import requests

from new_request_details import NewRequestDetails
from subject import Subject

root_url = 'https://fit3077.com/api/v1'
bid_url = root_url + "/bid"


class NewTutorRequest:
    window = None
    bid_type = None
    subject = None
    competency = None
    hours_per_session = None
    sessions_per_week = None
    rate_per_session = None

    def __init__(self, current, api_key):
        self.current_user = current
        self.api_key = api_key

    def main(self):
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
        return

    def create_request(self):
        date_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
        present_time = date_time[0:-3] + 'Z'
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
        self.window.destroy()
        NewRequestDetails(json_data).main()
