# Codename: Green Gopher

## Team Members
* Dylan Ahearn
* Peter Wang
* Elliot Whitehead
* Evan Yin

## About
Mappiness is a scalable big data application which analyzes sentiment from geo-tagged tweets in the United States. Users can view this information overlaid on an interactive map.

## Installation
1. Install pip (if needed)
  * Ubuntu: `apt-get update; apt-get -y install python-pip`
  * MacOS: `sudo easy_install pip`
2. Install [virtualenv](https://virtualenv.pypa.io/en/stable/): `sudo pip install virtualenv`
3. Create a new virtualenv environment to isolate dependancies: `virtualenv venv`
4. Activate your new virtual environment (Must be done every time to run the codebase): `source venv/bin/activate`
  * To deactivate the virtual environment, simply run `deactivate` (or kill terminal session)
5. Install project dependencies: `pip install -r requirements.txt`
6. To start the Django app server, run `python mappiness/manage.py runserver`
7. Visit [http://localhost:8000](https://goo.gl/H8y9c7) to see your running Django app!