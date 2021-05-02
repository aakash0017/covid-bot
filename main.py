import sys
import json
from user import user
from utility._utility import take_input, read_user_input, idx_2_res, res_spliter, generate_dict
from user_utility.user_utility import validate_email, validate_mobile, check_plasma, save_details
from cms_queries.queries import get_request, post_request


def main():

    # response messages:
    success_message = 'Thank you for your response'
    plasma_message = 'Please provide blood groups for provided plasma'
    error_message = 'Please enter correct details'

    # creating a json read function later move to utility file
    f = open('telegram_request.json')
    user_data = json.load(f)
    chat_id = user_data["message"]["chat"]["id"]
    txt = user_data["message"]["text"]

    name, mobile, email, city, state, res_ids, description = read_user_input(txt)
    
    idx_2_res_map = idx_2_res()
    # print(name, mobile, email, city, state, res_ids, description)
    if validate_mobile(mobile) and validate_email(email):
        user_obj = user(name, email, mobile)
        user_obj.resource_provider()
        
        city = take_input(city, 'city')
        state = take_input(state, 'state')

        res_ids = res_spliter(res_ids)
        def Lambda_res(x): return idx_2_res_map[int(x)]
        resources = [Lambda_res(res_id) for res_id in res_ids]

        contains_plasma = check_plasma(resources)

        for res in resources:
            user_obj.update_attributes('resources', res)

        user_obj.update_attributes('state', state)
        user_obj.update_attributes('city', city)

        details = user_obj.get_details()
        gen_dict = generate_dict(details)
        
        if contains_plasma:
            save_details(gen_dict, chat_id)
            print(plasma_message)
            return plasma_message

        else:
            print(success_message)
            return success_message

    print(error_message)
    return error_message

if __name__ == "__main__":
    main()
