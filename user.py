

class user:

    def __init__(self, name, email_Id, mobile):

        self.name = name
        self.email_Id = email_Id
        self.mobile = mobile

        # user's categories
        self.helper = False
        self.aid = False

        # user's location details
        self.state = None
        self.city = None

        # helper's resources
        

        def provide_Resources(self):
            self.helper = True

        def need_help(self):
            self.aid = True

