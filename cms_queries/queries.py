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
        return('raise flag')
    else: 
        _list
        return _list

    
    
def post_request(endpoint, body, environment  = 'local', url = 'http://localhost:1337/'):
    
    aakash_jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYwODY1ZDUxMDZiZWQyZDhlYzZjNmJjNyIsImlhdCI6MTYxOTk0MTE5NywiZXhwIjoxNjIyNTMzMTk3fQ.7DayQ2LgMItKpzXWXdTSwSLocXNUXN08yViGRrrkdLU"
    url = url + endpoint
    res = requests.post(url, data = body, headers = {"Authorization": f"Bearer {aakash_jwt}"} )
    return res.json()

def get_object(chat_id, endpoint, environment = 'local', url = 'http://localhost:1337/'):
    url = url + endpoint
    res = requests.get(url, headers = {"Authorization": f"Bearer {aakash_jwt}"}).json()
    
    temp_list = []
    for user_obj in res:
        if chat_id == user_obj['chatID']:
            temp_list.append(user_obj)
    
    if not temp_list:
        return dict()
    
    dict_ = {'Name': '', 'Mobile': '', 'Email': '', 'City': '', 'State': '', 'Resources': [''], 'Description': '', 'chat_id': '', 'has_plasma': ''}
    res_list = temp_list[len(temp_list) - 1]
    
    # TODO make the below statements more efficient
    
    dict_['Name'] = res_list['name']
    dict_['Mobile'] = res_list['mobile']
    dict_['Email'] = res_list['email']
    dict_['City'] = res_list['city']
    dict_['State'] = res_list['state']
    dict_['Resources'] = res_list['resources']
    dict_['Description'] = res_list['description']
    dict_['chat_id'] = res_list['chatID']
    dict_['has_plasma'] = res_list['hasPlasma']
    
    return dict_
