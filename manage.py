import argparse
from api import db

parser = argparse.ArgumentParser(description="Showws deployment script")
parser.add_argument('createdb')
args = parser.parse_args()

if vars(args).has_key('createdb'):
    print "Creating database and tables..."
    db.create_all()

