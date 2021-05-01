from login import Login


class Application:
    API_KEY = "mPRM67bLTWDwchrMCtBCrWbh89tQb6"

    def __init__(self):
        Login(self.API_KEY).login()


if __name__ == "__main__":
    a = Application()
