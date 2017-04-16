import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel

class Tweet(DjangoCassandraModel):
	tweet_id = columns.UUID(primary_key=True, default=uuid.uuid4)
	twitter_snowflake = columns.Text(required=True)
	tweet_lat = columns.Float()
	tweet_long = columns.Float()
	tweet_status = columns.Text(required=True)
	tweet_hashtags = columns.Set(columns.Text())