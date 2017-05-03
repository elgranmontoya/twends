from cqlengine import columns
from cqlengine import Model
from cqlengine import connection
import requests
from requests.auth import HTTPBasicAuth
import json
import os
#import gnip-ingest
import uuid

class geo_tweet(Model):
	
	tweet_id = columns.UUID(primary_key = True, default = uuid.uuid4)
	created_at_year = columns.Integer(primary_key=True)
	created_at_month = columns.Integer(primary_key=True)
	created_at_day = columns.Integer(primary_key=True)
	created_at_time=columns.Integer(primary_key=True)
	status = columns.Text(required=True)
	hashtags = columns.Set(columns.Text())
	author_user_name = columns.Text()
	author_image=columns.Text()
	
#time = columns.TimeUUID(primary_key=True, clustering_order = "DESC")
	
#~ if you get connection errors change the port number to what you get in cqlsh
#13.58.2.80
connection.setup(['52.14.189.33	'], "fromdjango")

# fromdjango toggle for creating table
'''
from cqlengine.management import sync_table
sync_table(geo_tweet)
:'''
#print(gnip-ingest.query)


url = "https://gnip-api.twitter.com/search/fullarchive/accounts/greg-students/prod.json?"

# Multi-page query (the real deal)
query = '{\
			"query": 		"has:hashtags (place:fd70c22040963ac7 OR bounding_box:[-105.301758 39.964069 -105.178505 40.09455])",\
			"fromDate":		"201401010000",\
			"toDate":		"201704222025",\
			"maxResults":	"500"\
		}'


# Authenticate and request a payload from gnip

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

print "\n-----------------"
print "Page", page_num
print "-----------------"


# Handling request limit

request_bool = True


while(request_bool):
	full_http_response = requests.post(url, auth = HTTPBasicAuth('elliot.whitehead@colorado.edu', 'silver2345'), data=query)
	first_payload = full_http_response.text

	if(full_http_response.status_code >= 400):

		print "Waiting..."

	else:
		for tweet in json.loads(first_payload)['results']:
			#print tweet_num, "Posted at:", tweet['postedTime'], "by @"+tweet['actor']['preferredUsername']," --> \"", tweet['body'], "\""

			#print "Hashtags:"
			first_hashtags = set()

			for hashtag in tweet['twitter_entities']['hashtags']:
				first_hashtags.add("#"+hashtag['text'])

			#print first_hashtags
			#'''
			post_year = tweet['postedTime'][0:4]
			post_month = tweet['postedTime'][5:7]
			post_day = tweet['postedTime'][8:10]
			post_time = tweet['postedTime'][11:13]+tweet['postedTime'][14:16]+tweet['postedTime'][17:19]
			#'''
			#post_time = tweet['postedTime']
			user_name = tweet['actor']['preferredUsername']
			user_image = tweet['actor']['image']
			tweet_body = tweet['body']
			
			if(len(first_hashtags) != 0):
				#'''
				geo_tweet.create( created_at_year = post_year, created_at_month = post_month,  created_at_day = post_day, created_at_time = post_time, hashtags = first_hashtags, status= tweet_body, author_user_name = user_name, author_image = user_image)
				'''
				AllTweets.create(time = post_time, hashtags = first_hashtags, status= tweet_body, author_user_name = user_name, author_image = user_image)
				'''
			tweet_num += 1
			first_hashtags.clear()

		page_num += 1

		try:
			next_key = getNextKey(first_payload)
			while(next_key):

				# Debug, remove later
				print "-----------------" 
				print "Page", page_num
				print "-----------------"
				next_page = nextRequest(next_key, query).text
				hashtag_set = set()

				for tweet in json.loads(next_page)['results']:
					'''
					print tweet_num, "Posted at:", tweet['postedTime'], "by @"+tweet['actor']['preferredUsername']," --> \"", tweet['body'], "\""

					print "Hashtags:"
					'''
					for hashtag in tweet['twitter_entities']['hashtags']:
						hashtag_set.add("#"+hashtag['text'])

					#print hashtag_set
					#'''
					post_year = tweet['postedTime'][0:4]
					post_month = tweet['postedTime'][5:7]
					post_day = tweet['postedTime'][8:10]
					post_time = tweet['postedTime'][11:13]+tweet['postedTime'][14:16]+tweet['postedTime'][17:19]
					#'''
					#post_time = tweet['postedTime']
					user_name = tweet['actor']['preferredUsername']
					user_image = tweet['actor']['image']
					tweet_body = tweet['body']
					
					if(len(hashtag_set) != 0):
						#'''
						geo_tweet.create( created_at_year = post_year, created_at_month = post_month,  created_at_day = post_day, created_at_time = post_time, hashtags = hashtag_set, status= tweet_body, author_user_name = user_name, author_image = user_image)
						'''
						AllTweets.create(time = post_time, hashtags = hashtag_set, status= tweet_body, author_user_name = user_name, author_image = user_image)

						'''
					hashtag_set.clear()
					tweet_num += 1

				next_key = getNextKey(next_page)

				# Debug, remove later
				page_num += 1


		except:
			request_bool = False
			print "---------------------------------\nYou've reached the last page of data!\n---------------------------------"		






			


#myset={'Dylan','Elliot'}
#row1=AllTweets.create( created_at_year=2016,created_at_month=04, created_at_day=22,created_at_time=1000, hashtags={'Dylan','Elliot'}, status= 'Hack CU is so lit', author_user_name='green-gophers', author_image='fake link')
	
