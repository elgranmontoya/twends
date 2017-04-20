import requests
from requests.auth import HTTPBasicAuth
import json
import os

url = "https://gnip-api.twitter.com/search/fullarchive/accounts/greg-students/prod.json?"

query = '{ "query": "has:hashtags point_radius:[-105.27346517 40.01924738 5mi]"}'

response = requests.post(url, auth = HTTPBasicAuth('elliot.whitehead@colorado.edu', 'silver2345'), data=query)
# next = response['next']

print(response.text)

'''
i = 0
for i in range(5):
	
	response = requests.get(url, auth = HTTPBasicAuth('elliot.whitehead@colorado.edu', 'silver2345'), params = {'next' : next}).json()
	next = response['next']

	# response_pretty = requests.get(url, auth = HTTPBasicAuth('elliot.whitehead@colorado.edu', 'silver2345'), params = {'next' : next})



	print (response)

	#print next
'''