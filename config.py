import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.  Must run with "python app.py" for this to be picked up
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Connect to the database
# toy password for assignment (Windows required it), not real world best practice!
SQLALCHEMY_DATABASE_URI = 'postgres://postgres:a@localhost:5432/fyyur_app'