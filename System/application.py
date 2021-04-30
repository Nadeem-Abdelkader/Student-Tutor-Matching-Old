from login import Login
from user_collection import UserCollection


class Application:
    API_KEY = "mPRM67bLTWDwchrMCtBCrWbh89tQb6"
    USERS = UserCollection(API_KEY)

    def __init__(self):
        a = Login(self.API_KEY)
        a.login()
        # jwt, uname = a.login()
        # if jwt is not None:
        #     s = SelectAction(self.USERS.getUserByUsername(uname))
        #     s.start()


if __name__ == "__main__":
    a = Application()
