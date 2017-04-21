# Project: Twends
Twends is an app for discovering hyper-local Twitter trends


## Team Members
* Dylan Ahearn
* Peter Wang
* Elliot Whitehead
* Evan Yin

## Installation
1. Install pip (if needed)
    * Ubuntu: `apt-get update; apt-get -y install python-pip`
    * MacOS: `sudo easy_install pip`
2. Install [virtualenv](https://virtualenv.pypa.io/en/stable/): `sudo pip install virtualenv`
3. Create a new virtualenv environment to isolate dependancies: `virtualenv venv`
4. Activate your new virtual environment (Must be done every time to run the codebase): `source venv/bin/activate`
    * To deactivate the virtual environment, simply run `deactivate` (or kill terminal session)
5. Install project dependencies: `pip install -r requirements.txt` (give it a minute, the Cassandra driver will take a while!)
6. Start a Cassandra server running in the foreground: `cassandra/bin/cassandra -f` (to check on node statuses, run `cassandra/bin/nodetool status`)
7. Sync the db: `twends/manage.py sync_cassandra`
8. To start the Django app server, run `python twends/manage.py runserver`
9. Visit [http://localhost:8000](https://goo.gl/H8y9c7) to see your running Django app!

10. Dowload DataStax at https://academy.datastax.com/ , you will have to create a free account.
11. Download for Mac or linux, select the install directory to be green-gopher.
12. To run cassandra go into the dse folder an type "bin/dse cassandra"
13. possible errors- if log error delete the logs in "dse/commitlog", if an error with gossiping to seeds, go into "dse/resources/cassandra/conf/cassandra.yaml and make the listen address blank.
14. go into the cql shell with "bin/dse cqlsh".
15. to set up a test database do: 
CREATE KEYSPACE testTweets WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 3} AND DURABLE_WRITES=true;
use testTweets;
CREATE TABLE tweets(id uuid PRIMARY KEY, created_at text , date text, status text, hashtags set<text>);
INSERT INTO tweets (id, created_at, date, hashtags, status) VALUES (4214783a-f687-47ff-b370-5ddebb2de429,'2:00','4202017',{'Dylan','Elliot'}, 'Big Data is fun');
INSERT INTO tweets (id, created_at, date, hashtags, status) VALUES (4214783a-f687-45ff-b370-5ddebb2de429,'3:00','4202017',{'Dylan'}, 'Big Data is not fun');
INSERT INTO tweets (id, created_at, date, hashtags, status) VALUES (4214783a-f687-47ff-c370-5ddebb2de429,'4:00','4202017',{'Evan','Peter'}, 'The Green Gopher strikes again!');
INSERT INTO tweets (id, created_at, date, hashtags, status) VALUES (4214783a-f787-46ff-b370-5ddebb2de429,'5:00','4202017',{'Evan','Elliot'}, 'Class is lit');
INSERT INTO tweets (id, created_at, date, hashtags, status) VALUES (4214783a-f687-47ff-b370-5ddebb2de429,'6:00','4202017',{'Dylan'}, 'Mumford and Sons rock');
INSERT INTO tweets (id, created_at, date, hashtags, status) VALUES (4214783a-f687-47ff-b372-5ddebb2de429,'7:00','4202017',{'Peter','Elliot'}, 'Karate is fun');
INSERT INTO tweets (id, created_at, date, hashtags, status) VALUES (4214783a-f687-47ff-c370-5ddebb2de429,'8:00','4202017',{'Evan','Peter','Dylan','Elliot'}, 'The tap is not open');
INSERT INTO tweets (id, created_at, date, hashtags, status) VALUES (4214783a-f687-41ff-b370-5ddebb2de429,'9:00','4202017',{'Peter','Dylan'}, 'We got beer');
INSERT INTO tweets (id, created_at, date, hashtags, status) VALUES (4214783a-f687-42ff-b370-5dhebb2de429,'8:00','4202017',{'Evan', 'Elliot'}, 'Pearl is empty');
INSERT INTO tweets (id, created_at, date, hashtags, status) VALUES (4214783a-f687-48ff-b370-5djebb2de429,'10:00','4202017',{'Peter','Dylan','Elliot'}, 'Pearl is not empty');
INSERT INTO tweets (id, created_at, date, hashtags, status) VALUES (4214783a-f687-47df-b370-5deebb2de429,'13:00','4202017',{'Peter','Dylan','Elliot'}, 'Evan is not in this tweet');
INSERT INTO tweets (id, created_at, date, hashtags, status) VALUES (4214783a-f687-47af-b370-5ddebb2de429,'15:00','4202017',{'Dylan','Elliot'}, 'trash can is on fire');

---
## Dependency Information
Cassandra v3.10
Kafka v2.10.0
