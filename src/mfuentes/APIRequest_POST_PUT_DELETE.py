import requests


def post():
    url = 'https://www.pivotaltracker.com/services/v5/projects/'
    payload = "{\"name\":\"mytestMF1\"}"
    headers = {'X-TrackerToken': "93e1ec771e6477ed7e0e1edd792a2e75",
    'Content-Type': "application/json"
    }
    r = requests.post(url, data=payload, headers=headers)
    print(r.text)


def put():
    url = 'https://www.pivotaltracker.com/services/v5/projects/2231597'
    payload = "{\"name\":\"mytest update\"}"
    headers = {'X-TrackerToken': "93e1ec771e6477ed7e0e1edd792a2e75",
    'Content-Type': "application/json"
    }
    r = requests.put(url, data=payload, headers=headers)
    print(r.text)


def delete():
    url = 'https://www.pivotaltracker.com/services/v5/projects/2231597'
    payload = ""
    headers = {'X-TrackerToken': "93e1ec771e6477ed7e0e1edd792a2e75",
    'Content-Type': "application/json"
    }
    r = requests.delete(url, data=payload, headers=headers)
    print(r.text)


post()
put()
delete()
