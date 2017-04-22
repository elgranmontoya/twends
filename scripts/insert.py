from cqlengine import columns
from cqlengine import Model
import uuid

class AllTweets(Model):
	created_at_year = columns.Integer(primary_key=True)
	created_at_month = columns.Integer(primary_key=True)
	created_at_day = columns.Integer(primary_key=True)
	created_at_time=columns.Integer(primary_key=True)
	status = columns.Text(required=True)
	hashtags = columns.Set(columns.Text())
	author_user_name= columns.Text()
	author_image=columns.Text()
	
	
#~ if you get connection errors change the port number to what you get in cqlsh
from cqlengine import connection
connection.setup(['10.0.2.15'], "testtweets")

#~ from cqlengine.management import sync_table
#~ sync_table(AllTweets)

myset={'Dylan','Elliot'}
row1=AllTweets.create( created_at_year=2016,created_at_month=04, created_at_day=22,created_at_time=1000, hashtags={'Dylan','Elliot'}, status= 'Hack CU is so lit', author_user_name='green-gophers', author_image='fake link')
	
