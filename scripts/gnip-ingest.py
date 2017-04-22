import requests
from requests.auth import HTTPBasicAuth
import json
import os
from time import sleep



url = "https://gnip-api.twitter.com/search/fullarchive/accounts/greg-students/prod.json?"

# Multi-page query (the real deal)
#"query": 		"has:hashtags bounding_box:[-105.301758 39.964069 -105.178505 40.09455]",\
#'''
query = '{\
			"query": 		"has:hashtags (place:fd70c22040963ac7 OR bounding_box:[-105.301758 39.964069 -105.178505 40.09455])",\
			"fromDate":		"200701010000",\
			"toDate":		"201704222025",\
			"maxResults":	"500"\
		}'
#'''

# Single page query (for testing)
#query = '{"query": "has:hashtags from:gogreengophers (place:fd70c22040963ac7 OR bounding_box:[-105.301758 39.964069 -105.178505 40.09455])", "maxResults": "10"}'

# Authenticate and request a payload from gnip
#full_http_response = requests.post(url, auth = HTTPBasicAuth('elliot.whitehead@colorado.edu', 'silver2345'), data=query)

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
	return(new_response)


# Where the magic happens!

# Debug, remove later
page_num = 1
tweet_num = 1

# There's always a first page of data, so handle that first


# Debug, remove later
print("\n-----------------")
print("Page", page_num)
print("-----------------")

# Handling request limit
#print(full_http_response.status_code)

request_bool = True

while(request_bool):
	full_http_response = requests.post(url, auth = HTTPBasicAuth('elliot.whitehead@colorado.edu', 'silver2345'), data=query)
	first_payload = full_http_response.text
	if(full_http_response.status_code >= 400):

		print("Waiting...")
		

	else:

		for tweet in json.loads(first_payload)['results']:
			print(tweet_num, " Posted at: ", tweet['postedTime'], " by @", tweet['actor']['preferredUsername'], " --> \"", tweet['body'], "\"", sep="")
			print("Hashtags:", end=" ")
			for hashtag in tweet['twitter_entities']['hashtags']:
				print("#", hashtag['text'], sep="", end=" ")
			print("\nLink:", tweet['link'])
			tweet_num += 1

		page_num += 1

		try:
			next_key = getNextKey(first_payload)
			while(next_key):

				# Debug, remove later
				print("\n-----------------")
				print("Page", page_num)
				print("-----------------")
				#


				next_page = nextRequest(next_key, query).text
				for tweet in json.loads(next_page)['results']:
					print(tweet_num, " Posted at: ", tweet['postedTime'], " by @", tweet['actor']['preferredUsername'], " --> \"", tweet['body'], "\"", sep="")

					print("Hashtags:", end=" ")

					for hashtag in tweet['twitter_entities']['hashtags']:
						print("#", hashtag['text'], sep="", end=" ")


					print("\nLink:", tweet['link'])
					tweet_num += 1

				
				next_key = getNextKey(next_page)

				# Debug, remove later
				page_num += 1
				
		except:
			request_bool = False
			print("\n---------------------------------\nYou've reached the last page of data!\n---------------------------------")