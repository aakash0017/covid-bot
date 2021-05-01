from flask import Flask, request
import requests

app = Flask(__name__)
key = "1797642990:AAH99XDMXSBycc2V3klWUHGG0Cn9-0EAEKE"

# https://api.telegram.org/bot1797642990:AAH99XDMXSBycc2V3klWUHGG0Cn9-0EAEKE/getMe
# https://api.telegram.org/bot1797642990:AAH99XDMXSBycc2V3klWUHGG0Cn9-0EAEKE/sendMessage?chat_id=1721282209&text=Hello user 


def sendmessage(chatid):
    url = "https://api.telegram.org/bot{}/sendMessage".format(key)
    payload = {
        "text": "heyy",
        "chat_id": chatid
    }
    resp = requests.get(url, params=payload)

@app.route("/", methods=["POST", "GET"])
def index():
    if (request.method == "POST"):

        resp = request.get_json()
        msgtxt =  resp["message"]["text"]
        sendername = resp["message"]["from"]["first_name"]
        chatid = resp["message"]["chat"]["id"]
        print(msgtxt, sendername, chatid)

    return "Done"

@app.route("/setwebhook/")
def setwebhook():
    url = "https://ngrok-url.ngrok.io/"
    s = requests.get("https://api.telegram.org/bot{}/setWebhook?url={}".format(key,url))
    if s:
        return "yes"
    else:
        return "fail"

if __name__ == "__main__":
    app.run()