from tkinter import *


class NewRequestDetails:
    window = None
    json_data = None
    additional_info = None

    def __init__(self, json_data, additional_info):
        self.json_data = json_data
        self.additional_info = additional_info

    def start(self):
        self.window = Tk()
        self.window.title("Request Details" + str(self.json_data['id']))
        self.window.geometry('500x450')

        Label(self.window, text="Request Details: ").grid(row=0, column=0)

        t = Text(self.window, height=15, width=50)
        t.grid(row=3)
        t.insert(INSERT, str("Bid ID: ") + str(self.json_data['id']) + str("\n"))
        t.insert(INSERT, str("Bid Type: ") + str(self.json_data['type'])+ str("\n"))
        t.insert(INSERT, str("Initiator: ") + str(self.json_data['initiator']['givenName']) + " " + str(self.json_data['initiator']['familyName']) + str("\n"))
        t.insert(INSERT, str("Date Created: ") + str(self.json_data['dateCreated']) + str("\n"))
        t.insert(INSERT, str("Date Closed: ") + str(self.json_data['dateClosedDown'])+ str("\n"))
        t.insert(INSERT, str("Subject: ") + str(self.json_data['subject']['name'])+ str("\n"))
        t.insert(INSERT, str("Competency: ") + str(self.additional_info['competency'])+ str("\n"))
        t.insert(INSERT, str("Hours per Week: ") + str(self.additional_info['hours_per_week'])+ str("\n"))
        t.insert(INSERT, str("Sessions per Week: ") + str(self.additional_info['sessions_per_week'])+ str("\n"))
        t.insert(INSERT, str("Rate per Session: ") + str(self.additional_info['rate_per_session']))


        Label(self.window, text="Current Bids: ").grid(row=4, column=0)

        t = Text(self.window, height=5, width=40)
        t.grid(row=7)

        Label(self.window, text="Bid Details: ").grid(row=9, column=0)

        t = Text(self.window, height=5, width=40)
        t.grid(row=12)





        self.window.mainloop()
        return
