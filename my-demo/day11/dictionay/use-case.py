import requests

#https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28
x = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

#using request with json it will automatically comvert json to dictioary
complete_details = x.json()
#get specific details
specific_output = print(complete_details[0]["user"]["login"])

#getting all user names using login key using for loop
for i in range(len(complete_details)):
        print(complete_details[i]["user"]["login"])



#x = requests.status_codes.{"https://api.github.com/kubernetes/kubernetes/pulls"}


