from tkinter import *


class NewRequestDetails:
    """
    This class is responsible of displaying the request details when a student creates a new request
    """
    # Class Variables
    window = None
    json_data = None

    def __init__(self, json_data):
        """
        This __init__ method assigns the input json_daya given to the class variable json_data
        """
        self.json_data = json_data

    def main(self):
        """
        THis method displays the Request Details Screen which shows the newly created request details
        """
        # This portion is responsible for the formatting of the screen
        self.window = Tk()
        self.window.title("Request Details: " + str(self.json_data['id']))
        self.window.geometry('450x450')

        Label(self.window, text="Request Details: ").grid(row=0, column=0)

        text_area = Text(self.window, height=15, width=50)
        text_area.grid(row=3)
        text_area.insert(INSERT, str("Bid ID: ") + str(self.json_data['id']) + str("\n"))
        text_area.insert(INSERT, str("Bid Type: ") + str(self.json_data['type']) + str("\n"))
        text_area.insert(INSERT, str("Initiator: ") + str(self.json_data['initiator']['givenName']) + " " + str(
            self.json_data['initiator']['familyName']) + str("\n"))
        text_area.insert(INSERT, str("Date Created: ") + str(self.json_data['dateCreated']) + str("\n"))
        text_area.insert(INSERT, str("Date Closed: ") + str(self.json_data['dateClosedDown']) + str("\n"))
        text_area.insert(INSERT, str("Subject: ") + str(self.json_data['subject']['name']) + str("\n"))
        text_area.insert(INSERT, str("Competency: ") + str(self.json_data['additionalInfo']['competency']) + str("\n"))
        text_area.insert(INSERT,
                         str("Hours per Week: ") + str(self.json_data['additionalInfo']['hours_per_week']) + str("\n"))
        text_area.insert(INSERT,
                         str("Sessions per Week: ") + str(self.json_data['additionalInfo']['sessions_per_week']) + str(
                             "\n"))
        text_area.insert(INSERT, str("Rate per Session: ") + str(self.json_data['additionalInfo']['rate_per_session']))
        text_area.config(state=DISABLED)

        Label(self.window, text="Current Bids: ").grid(row=4, column=0)

        text_area = Text(self.window, height=5, width=40)
        text_area.grid(row=7)
        text_area.config(state=DISABLED)

        Label(self.window, text="Bid Details: ").grid(row=9, column=0)

        text_area = Text(self.window, height=5, width=40)
        text_area.grid(row=12)
        text_area.config(state=DISABLED)

        self.window.mainloop()
