from tkinter import *


class SeeContracts:
    """
    This method is responsible for displaying the contracts the current user has
    """
    # Class Variables
    window = None

    def __init__(self):
        pass

    def main(self):
        """
        This method is responsible for creating the See Your Contracts screen and displaying the contracts the
        current user has
        """
        self.window = Tk()
        self.window.title("See Your Contracts")
        self.window.geometry('300x250')
        self.window.mainloop()
