import requests
from requests.auth import HTTPBasicAuth
import re
import json

username = 'your email'
token = 'your jira api token'

url = 'https://agoraio.atlassian.net/wiki/rest/api/space'
    
response = requests.get(url, auth=(username,token))
contents = json.loads(json.dumps(response.json()))

limit = contents['limit']

for i in range(limit):
    groupName = contents['results'][i]['name']
    groupKey = contents['results'][i]['key']
    groupId = contents['results'][i]['id']
    #    groupHomepage = contents['results'][i]['_expandable']['homepage']
    print str(i) + ': id: ' + str(groupId) + ' name: ' + groupName + ' homepage: ' + groupHomepage
