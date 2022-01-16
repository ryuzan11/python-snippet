import requests


def requests_post(name):
    url = 'https://httpbin.org/post'

    headers = {
        'Content-Type': 'application/json'
    }

    json_data = {
        'name': name
    }

    response = requests.post(url, headers=headers, json=json_data)

    print(response)

    response_json_data = response.json()
    response_data = response_json_data.get('data')

    print(response_data)

    return response_data


def test_request():
    name = 'taro'
    res = requests_post(name)
    assert res == '{"name": "taro"}'
