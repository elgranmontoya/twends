# Project: Mappiness
Mappiness is a scalable big data application which analyzes sentiment from geo-tagged tweets in the United States. Users can view this information overlaid on an interactive map.


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
5. Install project dependencies: `pip install -r requirements.txt`
6. To start the Django app server, run `python mappiness/manage.py runserver`
7. Visit [http://localhost:8000](https://goo.gl/H8y9c7) to see your running Django app!
8. install cassandra by debian package by following this link: http://cassandra.apache.org/doc/latest/getting_started/installing.html, In the first step of this guide, make sure the version is version 3.10. 

(note you can also download it via the tarbell method)
 when doing this you will download a file into the downloads(or where ever you have files download to) file on your machine. 
we can make a new directory where ever we want on our machine for the new cassandra db.
something like this. mkdir cassandra
next we can move the file from the download file into the cassandra file (we must cd into the cassandra file before we do the next step)
 mv ~/Download/apache.cassandra.3.10 .
now we can unpack the tar file with this command
tar -xvzf apache-cassandra-3.10-bin.tar.gz
You have now successfully downloaded cassandra
9. 

## Cassandra
*to run cassandra go into the cassandra directory and the apachefile and do.
bin cassandra -f (-f is important because we can then kill the process with [crtl/cmd + c] rather than figuring out what the process id cassandra is running and the kill from there.
*to check the status of the nodes go into the cassandra directory and the apachefile and do.
bin/nodetools status
