import sys
from user import user
from utility._utility import take_input, read_user_input
# from user_utility.user import user_utility
from cms_queries.queries import get_request, post_request


def main():
    
    add_resources = None
    need_resources = None
    
    while True:

        converstion_type = input(
            'For checking resources in your city please enter 1 \n If you have verified leads for a city please enter 0')

        if converstion_type == '0':

            sample_input = 'aakash bhatnagar\nakashbharat.bhatnagar@gmail.com\n8384041898\nvadodara\ngujraat\nplasmaAB+\ndescription'
            name, email, mobile, city, state, resources, x = read_user_input(sample_input)
            
            if city == '' and state == '':
                print('please try again')
                continue
            
            print(x)
            user1 = user(name, email, mobile)
            user1.resource_provider()
            lst, res, x = user1.get_details()
            print(lst)
            result_city = take_input(city, 'city')
            result_res = take_input(resources, 'res')
            result_state = take_input(state, 'state')
            user1.update_attributes('state', result_state)
            user1.update_attributes('city', result_city)
            user1.update_attributes('resources', result_res)
            lst, res, x = user1.get_details()
            print(lst, res)
            


            bye = input("of you want to exit please enter 0 ")

            if bye == '0':
                break


if __name__ == "__main__":
    main()
