import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
# DEBUG = True
# Doing through command line since running with 'flask run'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = '<Put your local database url>'
