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
        tokens = ['state', 'city', 'resources', 'blood_grp']

        # blood_grp for plasma users
        self.blood_grps = []

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
        elif token == 'blood_grp':
            self.res_dict = user_utility.plasma_handler(self.res_dict, update_key)

if __name__ == "__main__":
    
    # load idx -> resource mapping
    idx_2_res_map = _utility.idx_2_res()
    for key, value in idx_2_res_map.items():
        print(key, ':', value)
    # # input from user
    # res_ids = '1 2 3'

    # name, email, mobile, city, state, res_id = input('name: '), input('email: '), input('mobile: '), input('ciy: '), input('state: '), input('resource: ')
    input_string = 'nidhir\nnid989@nid.com\n8160790964\nvakodara\ngujarat\n1 2 3\ndescription'
    name, email, mobile, city, state, res_ids, description = _utility.read_user_input(input_string)
    print(name, email, mobile, city, state, res_ids)
    if user_utility.validate_mobile(mobile) and user_utility.validate_email(email):
        user1 = user(name, email, mobile)
        user1.resource_provider()
        # lst, res, x = user1.get_details()
        # print(lst)
        # check city validity
        result_city = _utility.take_input(city, 'city')
        # check resource validity
        # result_res = _utility.take_input(resource, 'res')
        
        # convert res_id => resources
        res_ids = _utility.res_spliter(res_ids)
        Lambda_res = lambda x: idx_2_res_map[int(x)]
        resources = [Lambda_res(res_id) for res_id in res_ids]
        contains_plasma = user_utility.check_plasma(resources)
        for res in resources:
            user1.update_attributes('resources', res)
        # if res list contains plasma
        if contains_plasma:
            blood_grp = 'AB'
            user1.update_attributes('blood_grp', blood_grp)
        # check state validity
        result_state = _utility.take_input(state, 'state')
        user1.update_attributes('state', result_state)
        user1.update_attributes('city', result_city)
        # user1.update_attributes('resources', result_res)
        lst, res, x = user1.get_details()
        print(lst)
        print(x)
    
