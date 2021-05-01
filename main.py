import sys
import json
from user import user
from utility._utility import take_input, read_user_input, idx_2_res, res_spliter, generate_dict
from user_utility.user_utility import validate_email, validate_mobile, check_plasma
from cms_queries.queries import get_request, post_request


def main(user_msg):
    
    # load idx -> resource mapping
    idx_2_res_map = idx_2_res()

    name, email, mobile, city, state, res_ids, description = read_user_input(user_msg)

    if validate_email(email) and validate_mobile(mobile):
        user_obj = user(name, email, mobile)
        
        # validate entered city and state 
        city = take_input(city, 'city')
        state = take_input(state, 'state')

        # convert res_ids => resources
        res_ids = res_spliter(res_ids)
        def Lambda_res(x): return idx_2_res_map[int(x)]
        resources = [Lambda_res(res_id) for res_id in res_ids]
        
        # update user object resources attributes
        for res in resources:
            user_obj.update_attributes('resources', res)

        # update user object's city and state attribute
        user_obj.update_attributes('city', city)
        user_obj.update_attributes('state', state)

        details = user_obj.get_details()
        myobj = generate_dict(details)
        print('---------------------------------------------')
        print(details)
        print(myobj)
        print('---------------------------------------------')

        return 'Thankyou {} for you support'.format(name)

if __name__ == "__main__":
    main()
