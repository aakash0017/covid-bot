from flask import Flask, request
from flask import Response
import requests
import json
from user_utility.user_utility import save_details_app
from utility._utility import send_resource_message, send_needhelp_reslist_msg, generate_chat
from data.message import contribute, start, need_help, enter_correct_det
from cms_queries.queries import post_request, get_object
from main import main

app = Flask(__name__)
token = "1797642990:AAH99XDMXSBycc2V3klWUHGG0Cn9-0EAEKE"
user_flag = None

# https://api.telegram.org/bot1797642990:AAH99XDMXSBycc2V3klWUHGG0Cn9-0EAEKE/getMe
# https://api.telegram.org/bot1797642990:AAH99XDMXSBycc2V3klWUHGG0Cn9-0EAEKE/sendMessage?chat_id=1721282209&text=Hello user 

# https://api.telegram.org/bot1797642990:AAH99XDMXSBycc2V3klWUHGG0Cn9-0EAEKE/setWebhook?url=https://9795e3cac664.ngrok.io 

# TODO BOT
# 1. Locally create a basic Flask application
# 2. Set up a tunnel
# 3. Set a webhook
# 4. Recieve and parse a user's messages'
# 5. Send message to a user.

def write_json(data, filename='response.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def send_message(chat_id, text='abc'):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {'chat_id': chat_id, 'text': text, 'parse_mode': "HTML"}

    r = requests.post(url, json=payload)
    return r

url = "https://api.telegram.org/bot1797642990:AAH99XDMXSBycc2V3klWUHGG0Cn9-0EAEKE/setWebhook?url=https://telegram-covidbot.herokuapp.com/"

@app.route('/', methods=["POST", "GET"])
def index():
    
    if request.method == "POST":
        msg = request.get_json()
        
        try:
            txt = msg["message"]["text"]
        except:
            write_json(msg, 'telegram_request.json')
            chat_id = msg["edited_message"]["chat"]["id"]
            return_message = enter_correct_det()
            send_message(chat_id, return_message)
            return Response('ok', status=200)
        
        if txt == '/start':
            print("Start block")
            return_message = start()
            send_message(msg["message"]["chat"]["id"], return_message)
            return Response('ok', status=200)

        elif txt == '/contribute' or txt == '/needhelp':
            if txt == '/contribute':
                print("Start block")
                # load variables
                msg0 = send_resource_message()
                msg1 = contribute()
                send_message(msg["message"]["chat"]["id"], msg0)
                send_message(msg["message"]["chat"]["id"], msg1)
                return Response('ok', status=200)
            elif txt == '/needhelp':
                print("Start block")
                # load variables
                msg0 = send_needhelp_reslist_msg()
                msg1 = need_help()
                send_message(msg["message"]["chat"]["id"], msg0)
                send_message(msg["message"]["chat"]["id"], msg1)
                return Response('ok', status=200)

        else:
            print("Else block")
            # since heroku doesn't support dynamic file establishment hence saving these via strapi
            # write_json(msg, 'telegram_request.json')

            updateId = msg["update_id"]
            chatId = msg["message"]["chat"]["id"]
            Text = msg["message"]["text"]
            print(chatId)
            print(type(chatId))
            # process these text
            
            # doing something fishy here...
            url = "https://covid-bot-cms.herokuapp.com/"
            chat_id = str(chatId)
            reload_dict = get_object(endpoint='Beta-objects', chat_id=chat_id, url=url)
            if not reload_dict:
                dict_ = {'Name': '', 'Mobile': '', 'Email': '', 'City': '', 'State': '', 'Resources': '', 'Description': ''}
                save_details_app(dict_, chatId, False)
            
             
            send_message(chat_id=chatId, text="Stand By...")
            reply = main(chatId, Text)

            send_message(chat_id=chatId, text=reply)
            # send_message(chatId)
        
            return Response('ok', status=200)
    else:
        return "<h1>Covid Relief Bot</h1>"

if __name__ == "__main__":
    app.run(debug=True)