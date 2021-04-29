from tkinter import messagebox

import requests

from User import *

root_url = 'https://fit3077.com/api/v1'
users_url = root_url + "/user"


class UserCollection:
    users = []

    def __init__(self, api_key):

        response = requests.get(url=users_url, headers={'Authorization': api_key})

        if response.status_code == 200:
            json_data = response.json()
            for user in json_data:
                each = User(user)
                self.users.append(each)
        else:
            messagebox.showwarning(title="Load Users Error", message=response.reason)

    def getUserByUsername(self, uname):
        for user in self.users:
            if user.username == uname:
                return user
        return None
