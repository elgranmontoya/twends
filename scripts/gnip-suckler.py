import requests
from requests.auth import HTTPBasicAuth
import json
import os

url = "https://gnip-api.twitter.com/search/fullarchive/accounts/greg-students/prod.json?query=point_radius:[-105.27346517 40.01924738 5mi]&maxResults=500"

i = 0
response_next = requests.get(url, auth = HTTPBasicAuth('elliot.whitehead@colorado.edu', 'silver2345')).json()
next = response_next['next']

for i in range(5):
	
	response = requests.get(url, auth = HTTPBasicAuth('elliot.whitehead@colorado.edu', 'silver2345'), params = {'next' : next}).json()
	next = response['next']

	response_pretty = requests.get(url, auth = HTTPBasicAuth('elliot.whitehead@colorado.edu', 'silver2345'), params = {'next' : next})



	print response_pretty.content

	#print next