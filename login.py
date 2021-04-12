import requests


def login():
    profile_data = []
    url = 'https://www.champions.dev.pesakit.co.ke/api/champions/auth/login'

    # declare dictionaries of unordered key:value pairs of params and headers dict types
    params = {
        'phone': '0700000001',
        'pin': '4444'
    }
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    try:
        response = requests.post(url, headers=headers, params=params)
        if response:
            profile_data.append(response.json()['profile'])
            print(profile_data)
        else:
            print('Unable to login')

    except KeyError:
        print('Array key profile not found')
    except ConnectionError:
        print('Server connection failed')