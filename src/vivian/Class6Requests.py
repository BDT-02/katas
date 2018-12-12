#Requests
#GET
import requests
r = requests.get('https://www.pivotaltracker.com/services/v5/projects')
r.status_code
r.headers
{
    'content-type': 'application/json;',
    'X-TrackerToken': 'eca773db1a05aa626fea42c73f6384d2'
}
print r.text

#POST

