from flask import Flask, request
from flask import Response
import requests
import json
from utility._utility import send_resource_message, send_needhelp_reslist_msg
from data.message import contribute, start, need_help
from main import main

app = Flask(__name__)
token = "1797642990:AAH99XDMXSBycc2V3klWUHGG0Cn9-0EAEKE"
user_flag = None

# https://api.telegram.org/bot1797642990:AAH99XDMXSBycc2V3klWUHGG0Cn9-0EAEKE/getMe
# https://api.telegram.org/bot1797642990:AAH99XDMXSBycc2V3klWUHGG0Cn9-0EAEKE/sendMessage?chat_id=1721282209&text=Hello user 

# https://api.telegram.org/bot1797642990:AAH99XDMXSBycc2V3klWUHGG0Cn9-0EAEKE/setWebhook?url=https://aee48db30fe1.ngrok.io

# TODO BOT
# 1. Locally create a basic Flask application
# 2. Set up a tunnel
# 3. Set a webhook
# 4. Recieve and parse a user's messages'
# 5. Send message to a user.

def write_json(data, filename='response.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def send_message(chat_id, text='xyz-xyz-xyz'):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {'chat_id': chat_id, 'text': text, 'parse_mode': "Markdown"}

    r = requests.post(url, json=payload)
    return r

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
                msg0 = contribute()
                msg1 = send_resource_message()
                send_message(msg["message"]["chat"]["id"], msg0)
                send_message(msg["message"]["chat"]["id"], msg1)
                return Response('ok', status=200)
            elif txt == '/needhelp':
                print("Start block")
                # load variables
                msg0 = need_help()
                msg1 = send_needhelp_reslist_msg()
                send_message(msg["message"]["chat"]["id"], msg0)
                send_message(msg["message"]["chat"]["id"], msg1)
                return Response('ok', status=200)

        else:
            print("Else block")
            write_json(msg, 'telegram_request.json')

            chat_id = msg["message"]["chat"]["id"]
            txt = msg["message"]["text"]

            # process these text 
            reply = main()

            send_message(chat_id, text=reply)
        
            return Response('ok', status=200)
    else:
        return "<h1>Covid Relief Bot</h1>"

if __name__ == "__main__":
    app.run(debug=True)