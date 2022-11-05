import requests

url = 'https://auth.kdlapi.com/api/get_secret_token'
data = {
    'secret_id': 'oo0cx7cu9gqzdhby4m0d',
    'secret_key': 'uls3z647z4jrnb06dujwg12pps2hsthe'
}
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
response = requests.post(url, data=data, headers=headers)
print(response.content.decode('utf-8'))

# {"msg": "", "code": 0, "data": {"expire": 1750, "secret_token": "o8pubshp1x3c0c4ps84ka452tv"}}
