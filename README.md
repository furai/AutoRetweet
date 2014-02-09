AutoRetweet
===========

Retweet script written in python, because we can.

Installation
======

* Install python, supervisor and pip
* Install virtualenv `sudo pip install virtualenv`
* Clone this repository `git clone https://github.com/lucasgrzegorczyk/AutoRetweet.git`
* cd into AutoRetweet folder and create virtualenv `virtualenv --no-site-packages retweetenv`
* Activate virtualenv `source retweetenv/bin/activate`
* Install pip requirements `pip install -r requirements.txt`
* Copy settingy.py.example to settings.py and edit it
* Run retweet for the first time `python retweet.py`
* Follow instructions and copy oath keys to settings
* Copy retweet_supervisor.conf to your supervisor conf folder (probably /etc/supervisor/conf.d) and fix paths in it
* Reload supervisor