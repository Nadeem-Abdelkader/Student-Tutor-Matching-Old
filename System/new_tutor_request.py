from tkinter import *
from datetime import datetime
import requests

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

        variable = StringVar(self.window)
        variable.set(OPTIONS[0])
        w = OptionMenu(self.window, variable, *OPTIONS, command= self.set_bid_type)
        w.configure(width=20)
        w.grid(row=0, column=1)
        # w.pack()

        # Label(self.window, text="").pack()
        Label(self.window, text="Subject: ").grid(row=2, column=0)

        SUBJECTS = ["148e0af0-699b-4c1f-9e49-4de8816d121e", "8a921487-859f-4931-8743-f69c38f91b25", "841199ac-d73e-4726-888d-dfeb538f49e2"]

        variable = StringVar(self.window)
        variable.set(SUBJECTS[0])
        w = OptionMenu(self.window, variable, *SUBJECTS, command= self.set_subject)
        w.configure(width=20)
        w.grid(row=2, column=1)

        # Label(self.window, text="").pack()
        Label(self.window, text="Competency: ").grid(row=4, column=0)

        NUMBERS = ["1", "2", "3", "4", "5", "6", "7"]

        variable = StringVar(self.window)
        variable.set(NUMBERS[0])
        w = OptionMenu(self.window, variable, *NUMBERS, command= self.set_competency)
        w.configure(width=20)
        w.grid(row=4, column=1)
        # w.pack()
        # Label(self.window, text="").pack()
        Label(self.window, text="Hours per session: ").grid(row=6, column=0)

        variable = StringVar(self.window)
        variable.set(NUMBERS[0])
        w = OptionMenu(self.window, variable, *NUMBERS, command= self.set_hours_per_session)
        w.configure(width=20)
        w.grid(row=6, column=1)
        # w.pack()

        # Label(self.window, text="").pack()
        Label(self.window, text="Sessions per week: ").grid(row=8, column=0)

        variable = StringVar(self.window)
        variable.set(NUMBERS[0])
        w = OptionMenu(self.window, variable, *NUMBERS,command= self.set_session_per_week)
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

        rate = Entry(self.window, textvariable="rate")
        rate.configure(width=20)
        rate.grid(row=10, column=1)
        # Label(self.window, text="").pack()
        Button(text="Create Request", height="2", width="20", command=lambda:[self.create_request(),self.set_rate_per_session(rate.get())]).grid(row=12, column=1)

        self.window.mainloop()
        return


    def set_bid_type(self,value):
        NewTutorRequest.bid_type = value
        print(NewTutorRequest.bid_type)

    def set_subject(self,value):
        NewTutorRequest.subject = value
        print(NewTutorRequest.subject)

    def set_competency(selfs, value):
        NewTutorRequest.competency = value
        print(NewTutorRequest.competency)

    def set_hours_per_session(self,value):
        NewTutorRequest.hours_per_session = value
        print(NewTutorRequest.hours_per_session)

    def set_session_per_week(self,value):
        NewTutorRequest.sessions_per_week  = value
        print(NewTutorRequest.sessions_per_week)

    def set_rate_per_session(self,value):
        NewTutorRequest.rate_per_session =  value
        print(NewTutorRequest.rate_per_session)

    def create_request(self):
        createbidurl = 'https://fit3077.com/api/v1/bid'
        t = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
        present_time = t[0:-3] + 'Z'
        response = requests.post(url = createbidurl, headers={'Authorization': self.api_key}, data={
            "type": NewTutorRequest.bid_type,
            "initiatorId": self.current_user.id,
            "dateCreated": present_time,
            "subjectId": NewTutorRequest.subject,
            "additionalInfo": {}
            }
        )
        json_data = response.json()
        print('Status code is: {} {}'.format(response.status_code, response.reason))
        print('Full JSON response is: {}'.format(json_data))

        pass