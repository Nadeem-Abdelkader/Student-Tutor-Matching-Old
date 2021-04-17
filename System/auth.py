from tkinter import *
from tkinter import messagebox

import requests

root_url = 'https://fit3077.com/api/v1'
users_url = root_url + "/user"


class Auth:
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
        self._window.geometry('400x150')
        self._window.title('Student - Tutor Matching Software (Login Page)')

        lbl1 = Label(self._window, text="User Name").grid(row=0, column=0)
        username = StringVar()
        self._unameIn = Entry(self._window, textvariable=username)
        self._unameIn.grid(row=0, column=1)

        lbl1 = Label(self._window, text="Password").grid(row=1, column=0)
        password = StringVar()
        self._pwrdIn = Entry(self._window, textvariable=password)
        self._pwrdIn.grid(row=1, column=1)

        loginBtn = Button(self._window, text="Login")
        loginBtn.grid(row=4, column=0)
        loginBtn.configure(command=self.apiSignIn)

        self._pwrdIn.insert(0, "mbrown123")
        self._unameIn.insert(0, "mbrown123")

        self._window.mainloop()

        return self._jwt, self._uname

    def apiSignIn(self):
        users_login_url = users_url + "/login"
        self._uname = self._unameIn.get()
        response = requests.post(
            url=users_login_url,
            headers={'Authorization': self._api_key},
            params={'jwt': 'true'},
            data={
                'userName': self._unameIn.get(),
                'password': self._pwrdIn.get()
            }
        )
        if response.status_code == 200:
            json_data = response.json()
            self._jwt = json_data['jwt']
            self._window.destroy()
        else:
            messagebox.showwarning(title="Login Error", message="Invalid Login")
