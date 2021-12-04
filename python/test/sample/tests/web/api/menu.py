import json
import requests


def menu(vtkt):
    url = 'https://onqtfv78nh.execute-api.ap-northeast-1.amazonaws.com/Prod/'

    headers = {
        'accept': 'application/json',
        'content-type': 'application/json'
    }

    data = {
        'vtkt': '911701'
    }

    response = requests.post(url, data=json.dumps(data), headers=headers)

    print(response)


menu('aaa')
