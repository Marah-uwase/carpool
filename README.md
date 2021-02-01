# Carpool
## Description
This application allows users to book space and share rides with others by finding a driver near their location who has space in their car and is headed their desired destination.
### User Stories
1. Sign in to the application to start using.
2. Set up a profile about me and a general location.
3. Find a list of drivers near me.
4. View a map with the location of all pickup points.
5. Review a driver and also be reviewed by the driver.
6. View the current space left in a driver’s car and get to book It.
## Technologies Used
- Python 3.6
- Django MVC framework
- HTML, CSS and Bootstrap
- JavaScript
- Postgressql
- Heroku
### Prerequisite
This project requires a prerequisite understanding of the following:
- Django Framework
- Python3.6
- Postgres
- Python virtualenv
## Setup and installation
#### Clone the Repository
####  Activate virtual environment
Create and activate virtual environment using python3.6 as default handler
    `python3.6 -m venv virtual && source virtual/bin/activate`
####  Install dependancies
Install dependancies that will create an environment for the app to run `pip3 install -r requirements.txt`
####  Create the Database
    - psql
    - CREATE DATABASE karpool;
#### Run initial Migration
python3.6 manage.py makemigrations app
python3.6 manage.py makemigrations carpool
python3.6 manage.py migrate
#### Run the app
python3.6 manage.py runserver
Open terminal on localhost:8000
## Support and contact details
Incase you come across errors, have any questions, ideas ,concerns, or want to contribute to the application, please contact:
1. maranahuwase12@gmail.com
2. arisodee@gmail.com
### License
* LICENSED UNDER  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](license/MIT)
