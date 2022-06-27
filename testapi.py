
import sys
import requests
import json
from bs4 import BeautifulSoup
# print(requests.post('http://127.0.0.1:8000/log/login/?next=/api/post/', data= {"username": "ostap", "password": "12345"}).content)

import sys
import requests

URL = 'http://127.0.0.1:8000/log/login/?next=/api/post/'

client = requests.session()

# Retrieve the CSRF token first
client.get(URL)  # sets cookie
if 'csrftoken' in client.cookies:
    # Django 1.6 and up
    csrftoken = client.cookies['csrftoken']
else:
    # older versions
    csrftoken = client.cookies['csrf']

login_data = dict(username='ostap', password='12345', csrfmiddlewaretoken=csrftoken)
r = client.post(URL, data=login_data, headers=dict(Referer=URL))

# my_json = log.content.decode('utf8').replace("'", '"')


# # Load the JSON to a Python list & dump it back out as formatted JSON
# data = json.loads(my_json)
# s = json.dumps(data, indent=4, sort_keys=True)
# print(s)

log = requests.get('http://127.0.0.1:8000/api/post/')
print(log.content)


