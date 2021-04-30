from tkinter import *
from tkinter import messagebox
import requests

from select_action import SelectAction
from user_collection import UserCollection

root_url = 'https://fit3077.com/api/v1'
users_url = root_url + "/user"


class Login:
    API_KEY = "mPRM67bLTWDwchrMCtBCrWbh89tQb6"
    USERS = UserCollection(API_KEY)
    _api_key = None
    _window = None
    _unameIn = None
    _pwrdIn = None
    _jwt = None
    _uname = None

    def __init__(self, api_key):
        self._api_key = api_key

    def login(self):
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
        users_login_url = users_url + "/login"
        self._uname = self._unameIn.get()
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
        if response.status_code != 200:
            messagebox.showwarning(title="Login Error", message="Invalid Login")
        else:
            messagebox.showwarning(title="Success", message="Login Successful!")
            self._window.destroy()
            s = SelectAction(self.USERS.get_user_by_user_name(self._uname))
            s.start()
