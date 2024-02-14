# This code sample uses the 'requests' library:
# http://docs.python-requests.org
#https://github.com/mayurmadan/python-for-devops-Abhishek.Veeramalla/blob/main/Day-14/examples/list_projects.py
#https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-projects/#api-rest-api-3-project-get

import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://groots-mayur.atlassian.net/rest/api/3/project"

API_TOKEN="<token here>"
auth = HTTPBasicAuth("<email here>", API_TOKEN)
#auth = HTTPBasicAuth("<email here>", "<token-here>")


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
output = json.loads(response.text)

name = output[0]["name"]
print(name)
