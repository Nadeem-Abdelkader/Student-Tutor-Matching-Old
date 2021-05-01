from tkinter import messagebox

import requests

from user import *

# Global variables
root_url = 'https://fit3077.com/api/v1'
users_url = root_url + "/user"


class UserCollection:
    """
    This class is responsible for storing the users of the system
    """
    # CLass variables
    users = []

    def __init__(self, api_key):
        """
        This __init__ method uses the web service get() method to get the users of the system and append them to the
        list users
        """
        # using web service to get user data
        response = requests.get(url=users_url, headers={'Authorization': api_key})

        # if call to web service is successful (status code = 200), loop the data and append each user to the list user
        if response.status_code == 200:
            json_data = response.json()
            for user in json_data:
                each_user = User(user)
                self.users.append(each_user)
        # else, display error message
        else:
            messagebox.showwarning(title="Load Users Error", message=response.reason)

    def get_user_by_user_name(self, uname):
        """
        This method is used to retrieve a user using his user name
        :param uname: user name of user were searching for
        :return: user with the user name entered
        """
        # loop the users list after all users have been appended to it, and if the username matches the username were
        # looking for return user
        for user in self.users:
            if user.username == uname:
                return user
        # else if theres no match, return None
        return None
