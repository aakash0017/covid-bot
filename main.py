import sys
import json
import numpy as np
from os import path
from user import user
from utility._utility import take_input, read_user_input, idx_2_res, res_spliter, generate_dict, array2dict, regex_checker
from utility._utility import process_needhelp_input, process_needhelp_result, needhelp_message, decode_residx_op
from user_utility.user_utility import validate_email, validate_mobile, check_plasma, save_details, load_file, after_bg_save, create_empty_dict
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

    
    # unique filename for refrencing to dictionary
    file_name = 'data/user_objects_data/{}.npy'.format(chat_id)
    if path.exists(file_name):
        pass
    else:
        create_empty_dict(chat_id)
    
    Reply_from_regex = regex_checker(txt)
    if Reply_from_regex == '1':
        print("contributor")
        
        reload_dict = array2dict(load_file(file_name))
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
            blood_grps = txt.strip()
            # update blood attributes 
            user_object_Reload.update_attributes('blood_grp', blood_grps)
            gen_dict = generate_dict(user_object_Reload.get_details())
            after_bg_save(gen_dict, reload_chat_id, False)
            # add post method to update database
            print(gen_dict)
            print("if block")
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
            print(name, mobile, email, city, state, res_ids, description)
            idx_2_res_map = idx_2_res()
            # print(name, mobile, email, city, state, res_ids, description)
            if validate_mobile(mobile) and validate_email(email):
                user_obj = user(name, email, mobile)
                user_obj.resource_provider()
                
                city = take_input(city, 'city')
                # print(city)
                state = take_input(state, 'state')
                # print(state)

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
                    print(gen_dict)
                    a = gen_dict["Resources"]
                    stri = ''
                    for i in a:
                        stri += i + ',' 
                    gen_dict["Resources"] = stri
                    url = "https://covid-bot-cms.herokuapp.com/"
                    res = post_request(endpoint="data", body=gen_dict, url=url)
                    print(res)
                    print("else block")
                    print(success_message)
                    return success_message

            print(error_message)
            return error_message
    
        print('Here')
    elif Reply_from_regex == '2':
        print("need help")
        # process user input 
        res_idx, city = process_needhelp_input(txt)
        city = take_input(city, 'city')
        idx2res_map = decode_residx_op()
        res = idx2res_map[int(res_idx)]
        print(res)
        print(res_idx, city)
        # print(res, city)
        url = "https://covid-bot-cms.herokuapp.com/"
        res = get_request(res, endpoint="data", url=url, city=city)
        result_list = process_needhelp_result(res)
        print(result_list)
        return_message = needhelp_message(result_list)
        print(return_message)
        return return_message
        
    else:
        print("Not contributor or need help")
        print(error_message)
        return error_message
    
    # print(take_input('Vakodara', 'Vadodara'))

if __name__ == "__main__":
    main()
