# This code sample uses the 'requests' library:
# http://docs.python-requests.org
#https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-post
#https://github.com/mayurmadan/python-for-devops-Abhishek.Veeramalla/blob/main/Day-14/examples/create-jira.py


import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://groots-mayur.atlassian.net/rest/api/3/issue"

API_TOKEN = "<api token her>"
auth = HTTPBasicAuth("<email here>", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

#keep only required field in payload
payload = json.dumps( {
  "fields": {

    
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "This is my ticket using python api.",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },

    "issuetype": {
      "id": "10005"
    },
    "project": {
      "key": "TGIP"
    },
    "summary": "This is first ticket using python API",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
