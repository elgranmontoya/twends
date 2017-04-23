import requests
from requests.auth import HTTPBasicAuth
import json
import os

url = "https://gnip-api.twitter.com/search/fullarchive/accounts/greg-students/prod.json?"

query = '{"query": "from:gogreengophers place:fd70c22040963ac7 "}'

while(True):

	full_http_response = requests.post(url, auth = HTTPBasicAuth('elliot.whitehead@colorado.edu', 'silver2345'), data=query)
		
	tweet_num = 1
	for tweet in full_http_response.json()['results']:
		print("Tweet #", tweet_num, "poste")
		print("#", tweet_num, "Tweet body", tweet['body'])
		tweet_num += 1