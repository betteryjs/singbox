import requests
import json

with open("URL.txt", 'r') as file:
    url=file.read()


parse={
    "url":url,
    "file":"https://raw.githubusercontent.com/betteryjs/singbox/master/remote/YJS.singbox.json"


}
resp=requests.get(url=url,params=parse).json()
print(resp)
with open("config.json", "w") as  file:
    file.write(json.dumps(resp))
