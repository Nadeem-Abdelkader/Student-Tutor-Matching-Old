root_url = 'https://fit3077.com/api/v1'
users_url = root_url + "/user"


class User:
    id = None
    username = None
    given_name = None
    family_name = None
    is_student = False
    is_tutor = False

    def __init__(self, json_data):
        self.id = json_data["id"]
        self.username = json_data["userName"]
        self.given_name = json_data["givenName"]
        self.family_name = json_data["familyName"]
        self.is_student = json_data["isStudent"]
        self.is_tutor = json_data["isTutor"]

    def __str__(self):
        return self.id + " " + self.username + " " + self.given_name + " " + self.family_name \
               + (" S " if self.is_student else "") + (" T " if self.is_tutor else "")
