# This code sample uses the 'requests' library:
# http://docs.python-requests.org
#https://github.com/mayurmadan/python-for-devops-Abhishek.Veeramalla/blob/main/Day-14/examples/list_projects.py
#https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-projects/#api-rest-api-3-project-get

import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://groots-mayur.atlassian.net/rest/api/3/project"

auth = HTTPBasicAuth("mayur@groots.in", "ATATT3xFfGF0xp__yIHK4Cj7j1vJQsTTJWAmvrPx8uXj60edzsfYCWE9tNjR3YvUqfNRcn-_HrbhEAs-mcJ_rhV0ID2wORhJAvkb4VRy8okegGm71Tnkxd-3dAP3DfsmrzLGz7Z1e7tspoeZ4bx6Beyb32VKKSptR7jxw6tM-GRUO6lijMDoaVY=9585F3E")

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
#get specific output 
output = json.loads(response.text)

print(output)
name = output[0]["name"]

print(name)

