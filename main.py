import sys
from user import user
from utility import _utility
from user_utility import user_utility


def main():

    while True:
        name, email, mobile, city, state = input('name: '), input('email: '), input('mobile: '), input('ciy: '), input('state: ')
        resource = []
        while True: 
            inp = input('Resource available: ')
            resource.append(inp)
            if inp == 'none':
                break
        user1 = user(name, email, mobile)
        user1.resource_provider()
        lst, res, x = user1.get_details()
        print(lst)
        # check city validity
        result_city = _utility.take_input(city, 'city')
        for i in resource:
            # check resource validity
            result_res = _utility.take_input(i, 'res')
            user1.update_attributes('resources', result_res)
        # check state validity
        result_state = _utility.take_input(state, 'state')
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
