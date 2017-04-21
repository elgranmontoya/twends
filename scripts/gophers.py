import requests
from requests.auth import HTTPBasicAuth
import json
import os

url = "https://gnip-api.twitter.com/search/fullarchive/accounts/greg-students/prod.json?"

query = '{"query": "from:gogreengophers"}'

response = requests.post(url, auth = HTTPBasicAuth('elliot.whitehead@colorado.edu', 'silver2345'), data=query)

print(response.text)