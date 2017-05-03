from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel

class TrendList(DjangoCassandraModel):
	requested_year = columns.Integer(primary_key=True)
	requested_month = columns.Integer(primary_key=True)
	requested_day = columns.Integer(primary_key=True)
	tag_counts = columns.Set(columns.Text())
	class Meta:
		get_pk_field='requested_year'