import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel

#~ class Tweet(DjangoCassandraModel):
	#~ id = columns.UUID(primary_key=True, default=uuid.uuid4)
	#~ created_at = columns.DateTime()
	#~ date = columns.Text()
	#~ geo_lat = columns.Float()
	#~ geo_long = columns.Float()
	#~ status = columns.Text(required=True)
	#~ hashtags = columns.Set(columns.Text())
	#~ favorites = columns.Integer()

class AllTweets(Model):
	tweet_id = columns.UUID(primary_key = True, default= uuid.uuid4)
	created_at_year = columns.Integer(primary_key=True)
	created_at_month = columns.Integer(primary_key=True)
	created_at_day = columns.Integer(primary_key=True)
	created_at_time=columns.Integer(primary_key=True)
	status = columns.Text(required=True)
	hashtags = columns.Set(columns.Text())
	author_user_name= columns.Text()
	author_image=columns.Text()
