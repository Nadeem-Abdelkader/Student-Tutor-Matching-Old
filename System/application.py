from session import *
from user_collection import *


class Application:
    API_KEY = "mPRM67bLTWDwchrMCtBCrWbh89tQb6"
    USERS = UserCollection(API_KEY)

    def __init__(self):
        a = Auth(self.API_KEY)
        jwt, uname = a.login()
        if jwt is not None:
            s = Session(self.USERS.getUserByUsername(uname))
            s.start()


a = Application()
