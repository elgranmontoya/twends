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