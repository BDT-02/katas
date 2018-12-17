import requests

from test.feature.environment import generic_data


class ConnectionPivotal:
    def __init__(self):
        self.url = generic_data['app']['url']
        self.api_token = generic_data['app']['api_token']
        self.headers = {'X-TrackerToken': self.api_token}

    def post(self, service, data):
        return requests.post(self.url % service, headers=self.headers, data=data)

    def get(self, service):
        return requests.get(self.url % service, headers=self.headers)

    def put(self, service, data):
        return requests.put(self.url % service, headers=self.headers, data=data)
