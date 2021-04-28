from flask import Flask, redirect, url_for, request, jsonify, render_template
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/sms', methods=['POST'])
def sms():
    # Fetch the message
    msg = request.form.get('Body')

    # converstion_type = input(
    #         'For checking resources in your city please enter 1 \n If you have verified leads for a city please enter 0')

    # if converstion_type == '0':
    #     # load idx -> resource mapping
    #     idx_2_res_map = idx_2_res()
    #     for key, value in idx_2_res_map.items():
    #         print(key, ':', value)
    #     # # input from user
    #     # res_ids = '1 2 3'

    #     # name, email, mobile, city, state, res_id = input('name: '), input('email: '), input('mobile: '), input('ciy: '), input('state: '), input('resource: ')
    #     input_string = 'nidhir\nnid989@nid.com\n8160790964\nvakodara\ngujarat\n9 7 5\ndescription'
    #     name, email, mobile, city, state, res_ids, description = read_user_input(input_string)
    #     print(name, email, mobile, city, state, res_ids)
    #     if validate_mobile(mobile) and validate_email(email):
    #         user1 = user(name, email, mobile)
    #         user1.resource_provider()
    #         result_city = take_input(city, 'city')
    #         res_ids = res_spliter(res_ids)
    #         def Lambda_res(x): return idx_2_res_map[int(x)]
    #         resources = [Lambda_res(res_id) for res_id in res_ids]
    #         # contains_plasma = check_plasma(resources)
    #         for res in resources:
    #             user1.update_attributes('resources', res)
    #             # if res list contains plasma
    #             # if contains_plasma:
    #             #     blood_grp = 'AB+ve B+ve'
    #             #     user1.update_attributes('blood_grp', blood_grp)
    #             # check state validity
    #             result_state = take_input(state, 'state')
    #             user1.update_attributes('state', result_state)
    #             user1.update_attributes('city', result_city)
    #             # user1.update_attributes('resources', result_res)
    #             details = user1.get_details()
    #             myobj = generate_dict(details)
    #             print(myobj)
    #             res = post_request('data', myobj)
    #             print(details)

    # Create reply
    resp = MessagingResponse()
    resp.message("You said: {}".format(msg))

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
