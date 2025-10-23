#checking if web api is working/not
import requests

request_status=requests.get('https://www.python.org')
print(request_status)