import requests
from requests.auth import HTTPBasicAuth
import json
import os

url = "https://gnip-api.twitter.com/search/fullarchive/accounts/greg-students/prod.json?"

query = '{\
			"query": 		"has:hashtags bounding_box:[-105.301758 39.964069 -105.178505 40.09455]",\
			"fromDate":		"201703310000",\
			"toDate":		"201704010000",\
			"maxResults":	500\
		}'

response = requests.post(url, auth = HTTPBasicAuth('elliot.whitehead@colorado.edu', 'silver2345'), data=query)

print(response.text)

# next = response['next']