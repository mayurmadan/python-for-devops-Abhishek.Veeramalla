#importing flask module only from flask package to make it lightweight
from flask import Flask, request
import requests
from requests.auth import HTTPBasicAuth
import json

#below line is used to create flask application/api instance
app = Flask(__name__)

#use decorator (refer readme from same dir for details)
#here we use decorator with inbuild 'route' function to check request is on '/' path or not[in browser] for our program
#when request is on '/' path then only another function is execute , if not then throght error
@app.route("/")
def hello():
    return "this is a python program whch will create jira issue, to create jira ticket using this use 'http://<ip>/CreateJira' url with post type, so setup github webhook for same url with your custom trigger, i use is for github issue comment to create ticket for issue"

@app.route("/CreateJira",methods=['POST'])
def createjirs():
    ## Extracting the JSON payload from the request from github webhook
    data = request.json

    url = "https://groots-mayur.atlassian.net/rest/api/3/issue"

    API_TOKEN = "<api-token-here>"
    auth = HTTPBasicAuth("<email-here>", API_TOKEN)
    #here i use day14 create jira code
    # This code sample uses the 'requests' library:
    # http://docs.python-requests.org
    #https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-post
    #https://github.com/mayurmadan/python-for-devops-Abhishek.Veeramalla/blob/main/Day-14/examples/create-jira.py
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
    
    if '"body": "/jira"' in json.dumps(data):
        response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
        )
        return "", 200
    else:
        return "", 404
    

#define ip to allow access it on
app.run("0.0.0.0")

