from select_action import *
from user_collection import *


class Application:
    API_KEY = "mPRM67bLTWDwchrMCtBCrWbh89tQb6"
    USERS = UserCollection(API_KEY)

    def __init__(self):
        a = LoginLayout(self.API_KEY)
        jwt, uname = a.login()
        if jwt is not None:
            s = SelectAction(self.USERS.getUserByUsername(uname))
            s.start()


if __name__ == "__main__":
    a = Application()
