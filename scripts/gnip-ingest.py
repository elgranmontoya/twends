import requests
from requests.auth import HTTPBasicAuth
import json
import os

url = "https://gnip-api.twitter.com/search/fullarchive/accounts/greg-students/prod.json?"

query = '{\
			"query": 		"has:hashtags bounding_box:[-105.301758 39.964069 -105.178505 40.09455]",\
			"fromDate":		"201703310000",\
			"toDate":		"201704010000",\
			"maxResults":	"10"\
		}'

full_http_response = requests.post(url, auth = HTTPBasicAuth('elliot.whitehead@colorado.edu', 'silver2345'), data=query)
response_text = (full_http_response.text)
response_json = json.loads(response_text)

i = 1
for tweet in response_json['results']:
	print("Tweet #", i, " was posted at ", tweet['postedTime'], sep='')
	i += 1
try:
	next_key = response_json['next']
	print(next_key)
	while(next_key):
		print("the 'next' key is:", next_key)
		
except:
	print("You've reached the last page of data!")

# data = json.loads(response.text)

# if(data['next']):
# 	print(data['next'])



# while()

# print("\n\n\nNext token: ",next)

'''
for tweet in json.loads(response.text)['results']:
	print("Tweet posted at:", tweet['postedTime'])
'''