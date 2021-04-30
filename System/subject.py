from tkinter import *
from tkinter import messagebox
import requests

from user_collection import UserCollection
root_url = 'https://fit3077.com/api/v1'
subjects_url = root_url + "/subject"


class Subject:
    API_KEY = "mPRM67bLTWDwchrMCtBCrWbh89tQb6"
    subject_id = None
    subject_name = None

    def __init__(self):
        pass

    def start(self):
        response = requests.get(
            url= str(subjects_url) + str("?"),
            headers={'Authorization': self.API_KEY, "Content-Type":"application/json"}
        )
        return response.json()

    def get_subject_names(self):
        data = self.start()
        # print(data)
        names = []
        for i in data:
            names.append(i['name'])
            # print(i['name'])
            # print("\n")
        return names

    def get_id_by_name(self,name):
        data = self.start()
        # print(data)
        id = []
        for i in data:
            # print(i)
            # print(i['name'])
            if i['name'] == name:
                return i['id']
            # return
            # print(i['name'])
            # print("\n")
        # return id


# s = Subject()
# print(s.get_subject_names())
# print(Subject().get_id_by_name('IT'))
