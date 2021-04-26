import numpy as np

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

        # list of resources
        self.resource = []

        # load resource list saved under data/ directory
        self.load_res()
        # initialize resource dict
        self.create_res_dict()

    def resource_provider(self):
        self.helper = True

    def help_required(self):
        self.aid = True

    def load_res(self):
        self.resource = list(np.load('data/res.npy', allow_pickle=True))

    def create_res_dict(self):
        # list of zeros of same lenght as of resources
        indicator = [0] * len(self.resource)
        self.res_dict = dict(zip(self.resource, indicator))

    def get_details(self):
        details = [self.name, self.email_Id, self.mobile, self.helper, self.aid]
        return details,self.resource, self.res_dict

    def mapping(self):
        res_available = []
        for key, value in self.res_dict():
            if value == 1:
                res_available.append(key)

if __name__ == "__main__":
    
    user1 = user('nidhir', 'nid989@nid.com', '123456789')
    user1.resource_provider()
    lst, res, x = user1.get_details()
    print(x)