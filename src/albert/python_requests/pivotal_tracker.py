import requests
import json
from pprint import pprint

url = 'https://www.pivotaltracker.com/services/v5/projects'
headers = {'X-TrackerToken': 'b35fd30ada3099032b77c95dc4f05c38'}

projects = requests.get(url, headers=headers)
pj = json.loads(projects.text)
pprint(pj)

print("\nCREATE PROJECT")
data = {"name": "project-02"}
new_project = requests.post(url, data=data, headers=headers)
pj = json.loads(new_project.text)
pprint(pj)
pprint(pj['id'])

print("\nRENAME PROJECT")
url += '/' + str(pj['id'])
data = {"name": "new name project 02"}
new_name = requests.put(url, data=data, headers=headers)
pj = json.loads(new_name.text)
pprint(pj)

print("\nDELETE PROJECT")
delete_project = requests.delete(url, headers=headers)
pprint(delete_project.text)


