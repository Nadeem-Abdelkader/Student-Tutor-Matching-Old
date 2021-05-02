from tkinter import *
from tkinter import messagebox

import requests

from select_action import SelectAction
from user_collection import UserCollection

# Global variables
root_url = 'https://fit3077.com/api/v1'
users_url = root_url + "/user"


class Login:
    """
    This method is responsible for the first screen (login screen). It displays the screen and then authenticates the
    credentials entered
    """
    # Class variables
    API_KEY = "mPRM67bLTWDwchrMCtBCrWbh89tQb6"
    USERS = UserCollection(API_KEY)
    _api_key = None
    _window = None
    _unameIn = None
    _pwrdIn = None
    _jwt = None
    _uname = None

    def __init__(self, api_key):
        """
        This __init__ method assigns the input api_key given to the class variable _api_key
        """
        self._api_key = api_key

    def login(self):
        """
        This method is resposible to display the login screen and calling the api_sign_in() method to authenticate
        the user
        """
        # This portion is to display the login screen formatted properly
        self._window = Tk()
        self._window.title("Login")
        self._window.geometry('300x250')

        Label(self._window, text="Please enter login details").pack()

        Label(self._window, text="").pack()
        Label(self._window, text="Username").pack()
        self._unameIn = Entry(self._window, textvariable="username")
        self._unameIn.pack()

        Label(self._window, text="").pack()
        Label(self._window, text="Password").pack()
        self._pwrdIn = Entry(self._window, textvariable="password", show="*")
        self._pwrdIn.pack()

        Label(self._window, text="").pack()
        Button(self._window, text="Login", command=self.api_sign_in, width=10, height=1).pack()

        self._pwrdIn.insert(0, "mbrown123")
        self._unameIn.insert(0, "mbrown123")

        self._window.mainloop()

        return self._jwt, self._uname

    def api_sign_in(self):
        """
        This method is called when the login button is clicked and is used to authenticate the credentials entered by
        the user :return:
        """
        users_login_url = users_url + "/login"
        self._uname = self._unameIn.get()
        # Calling the post() method from the web service to authenticate the credentials entered
        response = requests.post(
            url=users_login_url,
            headers={'Authorization': self._api_key},
            params={'jwt': 'true'},
            data=
            {
                'userName': self._unameIn.get(),
                'password': self._pwrdIn.get()
            }
        )
        # if status code from web service is not 200, it means that credentials are incorrect, so inform user and dont
        # log in
        if response.status_code != 200:
            messagebox.showwarning(title="Login Error", message="Invalid Login")
        # Else (status code is 200), it means credntials are correct so inform user and advance to second screen by
        # calling the main() method in the SelectAction class
        else:
            messagebox.showinfo(title="Success", message="Login Successful!")
            self._window.destroy()
            SelectAction(self.USERS.get_user_by_user_name(self._uname)).main()
