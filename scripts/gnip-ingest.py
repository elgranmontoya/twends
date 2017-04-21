import requests
from requests.auth import HTTPBasicAuth
import json
import os

url = "https://gnip-api.twitter.com/search/fullarchive/accounts/greg-students/prod.json?"

query = '{\
			"query": 		"has:hashtags bounding_box:[-105.301758 39.964069 -105.178505 40.09455]",\
			"fromDate":		"201703290000",\
			"toDate":		"201704010000",\
			"maxResults":	"10"\
		}'

full_http_response = requests.post(url, auth = HTTPBasicAuth('elliot.whitehead@colorado.edu', 'silver2345'), data=query)
response_text = (full_http_response.text)
response_json = json.loads(response_text)

def get_key(response):
	response_json = json.loads(response)
	return(response_json['next'])


def new_request(next_key):
	data = json.loads(query)
	new_key = {"next" : next_key}


	data.update(new_key)
	query_new = json.dumps(data)

	new_response = requests.post(url, auth = HTTPBasicAuth('elliot.whitehead@colorado.edu', 'silver2345'), data=query_new)
	return(new_response.text)




try:
	
	first_response = full_http_response.text
	next_key = get_key(first_response)
	
	for tweet in json.loads(first_response)['results']:
		print(tweet['postedTime'])

	j = 1
	while(next_key):
		print(j)
		#print(new_request(next_key))  #This if you want full tweet
		new = new_request(next_key)
		
		for tweet in json.loads(new)['results']:
			print(tweet['postedTime'])

		print("-----------------")
		
		next_key = get_key(new)
		j += 1
		
		
		
except:
	print("You've reached the last page of data!")