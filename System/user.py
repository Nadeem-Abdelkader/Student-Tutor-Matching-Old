class User:
    """
    This class represents a user and stores all his/her information
    """
    # Class variables
    id = None
    username = None
    given_name = None
    family_name = None
    is_student = False
    is_tutor = False

    def __init__(self, json_data):
        """
        This __init__ method assigns the user info according to the json_data provided
        :param json_data: json_data with information about the user
        """
        self.id = json_data["id"]
        self.username = json_data["userName"]
        self.given_name = json_data["givenName"]
        self.family_name = json_data["familyName"]
        self.is_student = json_data["isStudent"]
        self.is_tutor = json_data["isTutor"]

    def __str__(self):
        """
        __str__ method to return the users information neatly
        :return: string containing the user information formatted neatly
        """
        return self.id + " " + self.username + " " + self.given_name + " " + self.family_name \
               + (" S " if self.is_student else "") + (" T " if self.is_tutor else "")
