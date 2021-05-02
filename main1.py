import sys
import json
from user import user
from utility._utility import take_input, read_user_input, idx_2_res, res_spliter, generate_dict
from user_utility.user_utility import validate_email, validate_mobile, check_plasma
from cms_queries.queries import get_request, post_request


def main():

    add_resources = None
    need_resources = None

    while True:

        converstion_type = input(
            'For checking resources in your city please enter 1 \n If you have verified leads for a city please enter 0')

        if converstion_type == '0':

            # load idx -> resource mapping
            idx_2_res_map = idx_2_res()
            for key, value in idx_2_res_map.items():
                print(key, ':', value)
            # # input from user
            # res_ids = '1 2 3'

            # name, email, mobile, city, state, res_id = input('name: '), input('email: '), input('mobile: '), input('ciy: '), input('state: '), input('resource: ')
            input_string = 'nidhir Bhavsar\nnidbhavsar989@gmail.com\n8160790964\nVakodara\nGujarat\n2 3 4\ndescription'
            name, mobile, email, city, state, res_ids, description = read_user_input(input_string)
            print(name, email, mobile, city, state, res_ids)
            if validate_mobile(mobile) and validate_email(email):
                user1 = user(name, email, mobile)
                user1.resource_provider()
                # lst, res, x = user1.get_details()
                # print(lst)
                # check city validity
                result_city = take_input(city, 'city')
                # check resource validity
                # result_res = _utility.take_input(resource, 'res')

                # convert res_id => resources
                res_ids = res_spliter(res_ids)
                def Lambda_res(x): return idx_2_res_map[int(x)]
                resources = [Lambda_res(res_id) for res_id in res_ids]
                contains_plasma = check_plasma(resources)
                for res in resources:
                    user1.update_attributes('resources', res)
                # if res list contains plasma
                if contains_plasma:
                    blood_grp = 'AB+ve B+ve'
                    user1.update_attributes('blood_grp', blood_grp)
                # check state validity
                result_state = take_input(state, 'state')
                user1.update_attributes('state', result_state)
                user1.update_attributes('city', result_city)
                # user1.update_attributes('resources', result_res)
                details = user1.get_details()
                myobj = generate_dict(details)
                print(myobj)
                # res = post_request('data', myobj)
                print(details)
                print(user1.has_plasma)

            bye = input("of you want to exit please enter 0 ")

            if bye == '0':
                break


if __name__ == "__main__":
    main()
