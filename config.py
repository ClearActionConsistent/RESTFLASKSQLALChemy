import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

# Create the connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get the underlying Flask app instance
app = connex_app.app

# Build the Sqlite ULR for SqlAlchemy
#postgres_url = 'postgresql://postgres:admin@localhost/telusko'
postgres_url = 'postgresql://postgres:adminadmin@testdatabase.cni4eoms02tt.us-west-2.rds.amazonaws.com:5432/testdatabase'

# Configure the SqlAlchemy part of the app instance
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = postgres_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create the SqlAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)