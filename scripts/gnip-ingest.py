import requests
from requests.auth import HTTPBasicAuth
import json
import os


url = "https://gnip-api.twitter.com/search/fullarchive/accounts/greg-students/prod.json?"

# Multi-page query (the real deal)
# '''
query = '{\
			"query": 		"has:hashtags bounding_box:[-105.301758 39.964069 -105.178505 40.09455]",\
			"fromDate":		"201703290000",\
			"toDate":		"201704010000",\
			"maxResults":	"10"\
		}'
# '''

# Single page query (for testing)
#query = '{"query": "has:hashtags from:gogreengophers", "maxResults": "100"}'

# Authenticate and request a payload from gnip
full_http_response = requests.post(url, auth = HTTPBasicAuth('elliot.whitehead@colorado.edu', 'silver2345'), data=query)

# Returns 'next' key from a given Gnip response's body
def getNextKey(response_payload):
	response_dict = json.loads(response_payload)
	return(response_dict['next'])

def nextRequest(next_key, query_params):
	next_query = json.loads(query_params)
	next_key_dict = {"next" : next_key}
	next_query.update(next_key_dict)
	query_new = json.dumps(next_query)
	new_response = requests.post(url, auth = HTTPBasicAuth('elliot.whitehead@colorado.edu', 'silver2345'), data=query_new)
	return(new_response.text)


# Where the magic happens!
try:
	# Debug, remove later
	page_num = 1
	tweet_num = 1

	# There's always a first page of data, so handle that first
	first_payload = full_http_response.text
	next_key = getNextKey(first_payload)

	# Debug, remove later
	print("\n-----------------")
	print("Page", page_num)
	print("-----------------")
	#

	for tweet in json.loads(first_payload)['results']:
		print(tweet_num,tweet['postedTime'])
		tweet_num += 1

	page_num += 1

	while(next_key):

		# Debug, remove later
		print("\n-----------------")
		print("Page", page_num)
		print("-----------------")
		#

		next_page = nextRequest(next_key, query)
		for tweet in json.loads(next_page)['results']:
			print(tweet_num,tweet['postedTime'])
			tweet_num += 1

		
		next_key = getNextKey(next_page)

		# Debug, remove later
		page_num += 1
		
except:
	print("You've reached the last page of data!")