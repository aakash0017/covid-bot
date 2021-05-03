from flask import Flask, request
from flask import Response
import requests
import json
from utility._utility import send_resource_message

from main import main

app = Flask(__name__)
token = "1797642990:AAH99XDMXSBycc2V3klWUHGG0Cn9-0EAEKE"
user_flag = None

# https://api.telegram.org/bot1797642990:AAH99XDMXSBycc2V3klWUHGG0Cn9-0EAEKE/getMe
# https://api.telegram.org/bot1797642990:AAH99XDMXSBycc2V3klWUHGG0Cn9-0EAEKE/sendMessage?chat_id=1721282209&text=Hello user 

# https://api.telegram.org/bot1797642990:AAH99XDMXSBycc2V3klWUHGG0Cn9-0EAEKE/setWebhook?url=https://4c47bf054079.ngrok.io 

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
        
        txt = msg["message"]["text"]
        if txt == '/start':
            # load variables
            return_message = send_resource_message()
            send_message(msg["message"]["chat"]["id"], return_message)
            return Response('ok', status=200)
        else:
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