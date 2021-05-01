import requests

root_url = 'https://fit3077.com/api/v1'
subjects_url = root_url + "/subject"


class Subject:
    API_KEY = "mPRM67bLTWDwchrMCtBCrWbh89tQb6"

    def __init__(self):
        pass

    def main(self):
        response = requests.get(
            url=str(subjects_url) + str("?"),
            headers={'Authorization': self.API_KEY, "Content-Type": "application/json"}
        )
        return response.json()

    def get_subject_names(self):
        subject_data = self.main()
        subject_names = []
        for subject in subject_data:
            subject_names.append(subject['name'])
        return subject_names

    def get_id_by_name(self, subject_name):
        subject_data = self.main()
        for subject in subject_data:
            if subject['name'] == subject_name:
                return subject['id']
