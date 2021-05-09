import requests

aakash_jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYwODY1ZDUxMDZiZWQyZDhlYzZjNmJjNyIsImlhdCI6MTYxOTQxODU1OSwiZXhwIjoxNjIyMDEwNTU5fQ.Y52bTH80hazoVPomjX9jyE4LyyOKkEnZIRjAwgPeIuY"


def get_request(resource, endpoint, city = '', state = '', environment  = 'local', url = 'http://localhost:1337/'): 
    url = url + endpoint
    res = requests.get(url, headers = {"Authorization": f"Bearer {aakash_jwt}"}).json()
    resource_list = resource.split(',')
    _list = []
    for i in res:
        temp = i['Resources'].split(',')
        for j in resource_list:
            if j in temp:
                if city == i['City'] or state == i['State'] :
                    _list.append([i['Name'], i['City'], i['State'], i['Mobile'], i['Resources'], i['Description'], i['published_at']])

    if len(_list) == 0:
        return('Currenntly we do not have the resources please try again later')
    else: 
        _list
        return _list

    
    
def post_request(endpoint, body, environment  = 'local', url = 'http://localhost:1337/'):
    
    aakash_jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYwODY1ZDUxMDZiZWQyZDhlYzZjNmJjNyIsImlhdCI6MTYxOTk0MTE5NywiZXhwIjoxNjIyNTMzMTk3fQ.7DayQ2LgMItKpzXWXdTSwSLocXNUXN08yViGRrrkdLU"
    url = url + endpoint
    res = requests.post(url, data = body, headers = {"Authorization": f"Bearer {aakash_jwt}"} )
    return res.json()


def post_chat(endpoint, body, environment = 'local', url = 'http://localhost:1337/'):
    
    aakash_jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYwODY1ZDUxMDZiZWQyZDhlYzZjNmJjNyIsImlhdCI6MTYxOTk0MTE5NywiZXhwIjoxNjIyNTMzMTk3fQ.7DayQ2LgMItKpzXWXdTSwSLocXNUXN08yViGRrrkdLU"
    url = url + endpoint
    res = requests.post(url, data = body, headers = {"Authorization": f"Bearer {aakash_jwt}"} )
    return res.json()


def get_chat(updateID, endpoint, environment = 'local', url = 'http://localhost:1337/'):
    url = url + endpoint
    res = requests.get(url, headers = {"Authorization": f"Bearer {aakash_jwt}"}).json()
    
    dict_ = {'text': '', 'chatId' : ''}
    
    for i in res:
        if i["updateID"] == updateID:
            dict_['text'] = i["Text"]
            dict_['chatId'] = i["chatID"]

    if dict_['text'] == '' or dict_['chatId'] == '':
        return "Empty get request"
    else:
        return dict_

# dict_ = {'chatID': "1158340805", 'updateID': "900071452", 'Text': 'Nidhir\nnidbhavsar989@gmail.com\n8160790964\nSurat\nGujaray\n2 3\nGood'}
# url = "https://covid-bot-cms.herokuapp.com"
# updateId = '900071462'
# res = get_chat(updateID=updateId, endpoint='/Chat-infos', url=url)
# print(res) 