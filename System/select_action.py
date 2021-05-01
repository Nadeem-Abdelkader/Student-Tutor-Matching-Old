from tkinter import *

from bid_on_student_request import BidOnStudent
from new_tutor_request import NewTutorRequest
from see_contracts import SeeContracts
from user_collection import UserCollection


class SelectAction:
    """
    This method is respnsible for displaying the Select Action screen that greets the user and lets him chose what he
    wants to do
    """
    # Class variables
    API_KEY = "mPRM67bLTWDwchrMCtBCrWbh89tQb6"
    USERS = UserCollection(API_KEY)
    current_user = None
    window = None

    def __init__(self, current_user):
        """
        This __init__ method assigns the input current_user given to the class variable current_user
        """
        self.current_user = current_user

    def main(self):
        """
        This method displays the Select Action screen that greets the user and asks him what to do and then jumps to
        the relevant screen according to what button (option) the user clicked on
        """
        # This portion is responsible for the formatting of the Select Action screen
        self.window = Tk()
        self.window.geometry('300x250')
        self.window.title('Welcome')
        Label(text="Welcome back, what do you want to do today? ", width="300", height="2", font=("Calibri", 13)).pack()
        Label(text="").pack()
        Button(text="New Tutor Request", height="2", width="30", command=self.new_request).pack()
        Label(text="").pack()
        Button(text="Bid on Student Request", height="2", width="30", command=self.bid_on_student).pack()
        Label(text="").pack()
        Button(text="See Your Contracts", height="2", width="30", command=self.see_contract).pack()
        self.window.mainloop()

    def new_request(self):
        """
        This method is called when the user clicks on the "New Tutor Request" button and it destroys the current window
        and jumps to the "New Tutor Request" screen by calling the main() method in the "NewTutorRequest" class.
        """
        self.window.destroy()
        NewTutorRequest(self.current_user, self.API_KEY).main()

    def bid_on_student(self):
        """
        This method is called when the user clicks on the "Bid on Student Request" button and it destroys the current
        window and jumps to the "Bid on Student Request" screen by calling the main() method in the "BidOnStudent"
        class.
        """
        self.window.destroy()
        BidOnStudent(self.current_user, self.API_KEY).main()

    def see_contract(self):
        """
        This method is called when the user clicks on the "See Contracts" button and it destroys the current
        window and jumps to the "See Contracts" screen by calling the main() method in the "SeeContracts" class
        class.
        """
        self.window.destroy()
        SeeContracts().main()
