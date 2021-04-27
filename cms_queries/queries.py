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
        return _list

    
    
def post_request(endpoint, body, environment  = 'local', url = 'http://localhost:1337/'):
    
    url = url + endpoint
    res = requests.post(url, data = body, headers = {"Authorization": f"Bearer {aakash_jwt}"} )
    return res.json()


