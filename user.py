import numpy as np
from user_utility import user_utility
from data.res_list import res_list
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
        self.state = ''
        self.city = ''

        # list of resources
        self.resource = []

        # list of user_resources
        self.user_res = []
        self.description = ''

        # remove later
        # resource file path
        self.file_path = 'data/res.npy'

        # tokens
        tokens = ['state', 'city', 'resources', 'blood_grp']

        # user_providance for plasma
        self.has_plasma = False

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
        # self.resource = res_list() 
        indicator = [0] * len(self.resource)
        self.res_dict = dict(zip(self.resource, indicator))

    def get_details(self):
        if self.has_plasma:
            self.user_res = user_utility.user_res(self.res_dict)
            details = [self.name, self.mobile, self.email_Id, self.city, self.state, self.user_res, '']
        else:
            self.factor_res()
            details = [self.name, self.mobile, self.email_Id, self.city, self.state, self.user_res, '']
        return details

    # update user attributes
    def update_attributes(self, token, update_key):
        if token == 'state':
            self.state = update_key
        elif token == 'city':
            self.city = update_key
        elif token == 'resources':
            self.res_dict = user_utility.update_dict(self.res_dict, update_key)
        elif token == 'blood_grp':
            self.blood_grps = user_utility.plasma_handler(self.res_dict, self.blood_grps, update_key)

    # update user resource list based on mentioned resources.
    # def factor_res(self):
    #     self.user_res = user_utility.user_res(self.res_dict)
    #     if user_utility.check_plasma(self.user_res):
    #         # concate blood groups
    #         user_utility.concat_grps(self.user_res, self.blood_grps)

    def factor_res(self):
        self.user_res = user_utility.user_res(self.res_dict)
        # concate blood groups
        user_utility.concat_grps(self.user_res, self.blood_grps)
