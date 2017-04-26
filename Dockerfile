FROM luketillman/datastax-enterprise:5.1.0

COPY /home/ubuntu/cassandra.yaml /opt/dse/resources/cassandra/conf/