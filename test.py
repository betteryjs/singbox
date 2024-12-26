url="http://10.10.11.2/"


import requests


resp=requests.get(url)

print(resp.content.decode('gbk',errors='ignore'))
