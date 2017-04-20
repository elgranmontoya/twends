import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel

class Tweet(DjangoCassandraModel):
	id = columns.UUID(primary_key=True, default=uuid.uuid4)
	created_at = columns.DateTime()
	date = columns.Text()
	geo_lat = columns.Float()
	geo_long = columns.Float()
	status = columns.Text(required=True)
	hashtags = columns.Set(columns.Text())
	favorites = columns.Integer()
