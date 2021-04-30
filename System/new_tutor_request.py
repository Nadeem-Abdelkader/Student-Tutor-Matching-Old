from tkinter import *
from datetime import datetime
import requests

from subject import Subject


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

    def start(self):
        self.window = Tk()
        self.window.title("New Tutor Request")
        self.window.geometry('400x200')

        # Label(self.window, text="").pack()
        Label(self.window, text="Bid Type: ").grid(row=0, column=0)

        OPTIONS = ["Open", "Closed"]

        self.bid_type = StringVar(self.window)
        self.bid_type.set(OPTIONS[0])
        w = OptionMenu(self.window, self.bid_type, *OPTIONS)
        w.configure(width=20)
        w.grid(row=0, column=1)
        # print(variable.get())
        # w.pack()

        # Label(self.window, text="").pack()
        Label(self.window, text="Subject: ").grid(row=2, column=0)


        SUBJECTS = Subject().get_subject_names()
        # print(SUBJECTS)
        # SUBJECTS = ["148e0af0-699b-4c1f-9e49-4de8816d121e", "8a921487-859f-4931-8743-f69c38f91b25", "841199ac-d73e-4726-888d-dfeb538f49e2"]

        self.subject = StringVar(self.window)
        self.subject.set(SUBJECTS[0])
        w = OptionMenu(self.window, self.subject, *SUBJECTS)
        w.configure(width=20)
        w.grid(row=2, column=1)

        # Label(self.window, text="").pack()
        Label(self.window, text="Competency: ").grid(row=4, column=0)

        NUMBERS = ["1", "2", "3", "4", "5", "6", "7"]

        self.competency = StringVar(self.window)
        self.competency.set(NUMBERS[0])
        w = OptionMenu(self.window, self.competency, *NUMBERS)
        w.configure(width=20)
        w.grid(row=4, column=1)
        # w.pack()
        # Label(self.window, text="").pack()
        Label(self.window, text="Hours per session: ").grid(row=6, column=0)

        self.hours_per_session = StringVar(self.window)
        self.hours_per_session.set(NUMBERS[0])
        w = OptionMenu(self.window, self.hours_per_session, *NUMBERS)
        w.configure(width=20)
        w.grid(row=6, column=1)
        # w.pack()

        # Label(self.window, text="").pack()
        Label(self.window, text="Sessions per week: ").grid(row=8, column=0)

        self.sessions_per_week = StringVar(self.window)
        self.sessions_per_week.set(NUMBERS[0])
        w = OptionMenu(self.window, self.sessions_per_week, *NUMBERS)
        w.configure(width=20)
        w.grid(row=8, column=1)
        # w.pack()
        # Label(self.window, text="").pack()
        Label(self.window, text="Rate per session: ").grid(row=10, column=0)

        # variable = StringVar(self.window)
        # variable.set(NUMBERS[0])
        # w = OptionMenu(self.window, variable, *NUMBERS)
        # w.configure(width=20)
        # w.grid(row=10, column=1)
        # w.pack()

        self.rate_per_session = Entry(self.window, textvariable="rate")
        self.rate_per_session.configure(width=20)
        self.rate_per_session.grid(row=10, column=1)
        # print(self.rate_per_session.get())

        # Label(self.window, text="").pack()
        Button(text="Create Request", height="2", width="20", command=self.create_request).grid(row=12, column=1)

        self.window.mainloop()
        return


    # def set_bid_type(self,value):
    #     NewTutorRequest.bid_type = self.bid_type.get()
    #     print(NewTutorRequest.bid_type)
    #
    # def set_subject(self,value):
    #     NewTutorRequest.subject = self.subject.get()
    #     print(NewTutorRequest.subject)
    #
    # def set_competency(self, value):
    #     NewTutorRequest.competency = self.competency.get()
    #     print(NewTutorRequest.competency)
    #
    # def set_hours_per_session(self,value):
    #     NewTutorRequest.hours_per_session = self.hours_per_session.get()
    #     print(NewTutorRequest.hours_per_session)
    #
    # def set_session_per_week(self,value):
    #     NewTutorRequest.sessions_per_week  = self.sessions_per_week.get()
    #     print(NewTutorRequest.sessions_per_week)
    #
    # def set_rate_per_session(self,value):
    #     NewTutorRequest.rate_per_session =  self.rate_per_session.get()
    #     print(NewTutorRequest.rate_per_session)

    def create_request(self):
        createbidurl = 'https://fit3077.com/api/v1/bid'
        t = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
        present_time = t[0:-3] + 'Z'
        response = requests.post(url = createbidurl, headers={'Authorization': self.api_key}, data={
            "type": self.bid_type.get(),
            "initiatorId": self.current_user.id,
            "dateCreated": present_time,
            "subjectId": Subject().get_id_by_name(self.subject.get()),
            "additionalInfo": {}
            }
        )
        json_data = response.json()
        print('Status code is: {} {}'.format(response.status_code, response.reason))
        print('Full JSON response is: {}'.format(json_data))

        pass