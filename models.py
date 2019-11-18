from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from marshmallow_sqlalchemy import ModelSchema

from config import db
from datetime import datetime

Base = declarative_base()

class Person(Base):
	__tablename__ = 'test_people'
	id = Column(Integer, primary_key = True)
	fname = Column(String)
	lname = Column(String)
	timestamp = Column(DateTime, default = datetime.utcnow, onupdate=datetime.utcnow)


class PersonSchema(ModelSchema):
    class Meta:
        model = Person
        sqla_session = db.session
