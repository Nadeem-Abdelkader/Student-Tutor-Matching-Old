import requests

# Global Variables
root_url = 'https://fit3077.com/api/v1'
subjects_url = root_url + "/subject"


class Subject:
    """
    This Class is used to retrieve information regarding the subject
    """
    # Class variable
    API_KEY = "mPRM67bLTWDwchrMCtBCrWbh89tQb6"

    def __init__(self):
        pass

    def main(self):
        """
        This method uses the web service get() method to retrieve all data about the subjects
        :return: all data about subjects
        """
        # Using the web service to get information abut the subjects
        response = requests.get(
            url=str(subjects_url) + str("?"),
            headers={'Authorization': self.API_KEY, "Content-Type": "application/json"}
        )
        return response.json()

    def get_subject_names(self):
        """
        This method is used to retrieve the subject names which will be used in other classes to fill the drop down
        list of subjects
        :return: list of subject names
        """
        # Getting all info about the subjects
        subject_data = self.main()
        # creating empty subject_names list to append to in for loop
        subject_names = []
        # looping the subject data and appending only the subject name to the subject_names list
        for subject in subject_data:
            subject_names.append(subject['name'])
        # return subject_names list after appending subject names to
        return subject_names

    def get_id_by_name(self, subject_name):
        """
        This method is used to get a subjects id by providing its name. It will be used by other classes
        :param subject_name:
        :return: subject id for the subject name entered
        """
        # getting all the subjects information
        subject_data = self.main()
        # looping the subjects information and if the subject name matches the subject_name_entered, return the subject
        # id, else return None
        for subject in subject_data:
            if subject['name'] == subject_name:
                return subject['id']
        return None
