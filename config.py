# config.py
import os

# Base directory of the application
basedir = os.path.abspath(os.path.dirname(__file__))

# MySQL database configurations
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@localhost/druidot_assign'
SQLALCHEMY_TRACK_MODIFICATIONS = False
