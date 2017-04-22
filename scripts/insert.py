from cqlengine import columns
from cqlengine import Model
import uuid

class Tweet(Model):
	id = columns.UUID(primary_key=True, default=uuid.uuid4)
	created_at = columns.DateTime()
	date = columns.Text()
	status = columns.Text(required=True)
	hashtags = columns.Set(columns.Text())
	
	
from cqlengine import connection
connection.setup(['127.0.1.1'], "testTweets")

from cqlengine.management import sync_table
sync_table(ExampleModel)

row1=Tweet.create(created_at='7:00', date='4212017', hashtag={'Dylan','Evan','HackCU'}, status= 'Hack CU is lit')
	
