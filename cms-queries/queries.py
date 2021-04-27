import requests

aakash_jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYwODY1ZDUxMDZiZWQyZDhlYzZjNmJjNyIsImlhdCI6MTYxOTQxODU1OSwiZXhwIjoxNjIyMDEwNTU5fQ.Y52bTH80hazoVPomjX9jyE4LyyOKkEnZIRjAwgPeIuY"


def get_request(endpoint, environment  = 'local', url = 'http://localhost:1337/'): 
    
    url = url + endpoint    
    res = requests.get(url, headers = {"Authorization": f"Bearer {aakash_jwt}"})
    return res.json()
    
    
def post_request(endpoint, body, environment  = 'local', url = 'http://localhost:1337/'):
    
    url = url + endpoint
    res = requests.post(url, data = body, headers = {"Authorization": f"Bearer {aakash_jwt}"} )
    return res.json()


