import requests
from requests.auth import HTTPBasicAuth
import json
import os

url = "https://gnip-api.twitter.com/search/fullarchive/accounts/greg-students/prod.json?"

query = '{\
			"query":		"has:hashtags point_radius:[-105.27346517 40.01924738 5mi]",\
			"fromDate":		"201703310000",\
			"toDate":		"201704010000",\
			"maxResults":	500\
		}'

response = requests.post(url, auth = HTTPBasicAuth('elliot.whitehead@colorado.edu', 'silver2345'), data=query)

print(response.text)

# next = response['next']