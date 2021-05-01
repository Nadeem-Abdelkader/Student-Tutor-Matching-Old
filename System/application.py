from login import Login


class Application:
    """
    This is the main class that initialises the Login class and calls its main method (login()) which creates the
    login screen of the system
    """
    # Class variables
    API_KEY = "mPRM67bLTWDwchrMCtBCrWbh89tQb6"
    login_page = None

    def __init__(self):
        """
        This __init__ method creates an instance of the Login class and calls its login() method
        """
        self.login_page = Login(self.API_KEY)
        self.login_page.login()


if __name__ == "__main__":
    """
    This is to start up the application
    """
    Application()
