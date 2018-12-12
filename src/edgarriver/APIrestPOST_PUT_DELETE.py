import requests
# get token
username = 'bdpython01@mailinator.com'
password = 'EE199909049qq'
url = 'https://www.pivotaltracker.com/services/v5/me'

r = requests.get(url, auth=(username, password))
response_json = r.json()
token = response_json['api_token']
print token
# create project
url = "https://www.pivotaltracker.com/services/v5/projects"
payload = "{\"name\":\"projecfromAPI6\"}"
headers = {
   'Content-Type': "application/json",
   'X-TrackerToken': token,
   }
response = requests.request("POST", url, data=payload, headers=headers)
projectId = response
print(response.text)
print projectId
# update project

url = "https://www.pivotaltracker.com/services/v5/projects/2231585"

payload = "{\"name\":\"projecfromAPI updatedd\"}"
headers = {
    'Content-Type': "application/json",
    'X-TrackerToken': '92a608e6c90eb1fac4aceee644be3b2f',
    }
response = requests.request("PUT", url, data=payload, headers=headers)
print(response.text)

# delete project

url = "https://www.pivotaltracker.com/services/v5/projects/2231585"
payload = ""
headers = {
    'Content-Type': "application/json",
    'X-TrackerToken': '92a608e6c90eb1fac4aceee644be3b2f',
    }
response = requests.request("DELETE", url, data=payload, headers=headers)
print(response.text)

