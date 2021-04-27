import numpy as np
from user_utility import user_utility
from utility import _utility

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

        # remove later
        # resource file path 
        self.file_path = 'data/res.npy'

        # tokens
        tokens = ['state', 'city', 'resources']

        # load resource list saved under data/ directory
        # self.load_res()
        # initialize resource dict
        self.create_res_dict()

    def resource_provider(self):
        self.helper = True

    def help_required(self):
        self.aid = True

    def create_res_dict(self):
        # list of zeros of same lenght as of resources
        self.resource = user_utility.load_file(self.file_path)
        indicator = [0] * len(self.resource)
        self.res_dict = dict(zip(self.resource, indicator))

    def get_details(self):
        details = [self.name, self.email_Id, self.mobile, self.helper, self.aid, self.state, self.city]
        return details,self.resource, self.res_dict

    def mapping(self):
        res_available = []
        for key, value in self.res_dict():
            if value == 1:
                res_available.append(key)

    def update_attributes(self, token, update_key):
        if token == 'state':
            self.state = update_key
        elif token == 'city':
            self.city = update_key
        elif token == 'resources':
            self.res_dict =  user_utility.update_dict(self.res_dict, update_key)

if __name__ == "__main__":
    

    name, email, mobile, city, state, resource = input('name: '), input('email: '), input('mobile: '), input('ciy: '), input('state: '), input('resource: ')
    if user_utility.validate_mobile(mobile) and user_utility.validate_email(email):
        user1 = user(name, email, mobile)
        user1.resource_provider()
        lst, res, x = user1.get_details()
        print(lst)
        # check city validity
        result_city = _utility.take_input(city, 'city')
        # check resource validity
        result_res = _utility.take_input(resource, 'res')
        # check state validity
        result_state = _utility.take_input(state, 'state')
        user1.update_attributes('state', result_state)
        user1.update_attributes('city', result_city)
        user1.update_attributes('resources', result_res)
        lst, res, x = user1.get_details()
        print(lst, res)
    
