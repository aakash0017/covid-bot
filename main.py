import sys
import json
import numpy as np
import os
from user import user
from utility._utility import take_input, read_user_input, idx_2_res, res_spliter, generate_dict, array2dict
from user_utility.user_utility import validate_email, validate_mobile, check_plasma, save_details, load_file, after_bg_save
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

    reload_dict = array2dict(load_file('data/beta_dict.npy'))
    reload_chat_id = reload_dict[1]["chat_id"]
    reload_has_plasma = reload_dict[1]["has_plasma"]
    # print(reload_dict)

    if reload_chat_id == chat_id and reload_has_plasma:
        # new user object 
        user_object_Reload = user(reload_dict[1]["Name"], reload_dict[1]["Email"], reload_dict[1]["Mobile"])
        user_object_Reload.update_attributes('state', reload_dict[1]["State"])
        user_object_Reload.update_attributes('city', reload_dict[1]["City"])
        for i in reload_dict[1]["Resources"]:
            user_object_Reload.update_attributes('resources', i)
        blood_grps = txt
        # update blood attributes 
        user_object_Reload.update_attributes('blood_grp', blood_grps)
        gen_dict = generate_dict(user_object_Reload.get_details())
        after_bg_save(gen_dict, reload_chat_id, False)
        # add post method to update database
        a = gen_dict["Resources"]
        stri = ''
        for i in a:
            stri += i + ',' 
        gen_dict["Resources"] = stri
        url = "https://covid-bot-cms.herokuapp.com/"
        res = post_request(endpoint="data", body=gen_dict, url=url)
        print(res)
        print(success_message)
        return success_message
    else:
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
            # print(gen_dict)
            if contains_plasma:
                save_details(gen_dict, chat_id, True)
                print(plasma_message)
                return plasma_message

            else:
                # add post method to update database
                # print(gen_dict)
                a = gen_dict["Resources"]
                stri = ''
                for i in a:
                    stri += i + ',' 
                gen_dict["Resources"] = stri
                url = "https://covid-bot-cms.herokuapp.com/"
                res = post_request(endpoint="data", body=gen_dict, url=url)
                print(res)
                print(success_message)
                return success_message

        print(error_message)
        return error_message

if __name__ == "__main__":
    main()
