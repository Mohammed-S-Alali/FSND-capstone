import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json


# database_name = "casting_agency"
# database_path = "postgresql://{}:{}@{}/{}".format('postgres','M159','localhost:5432',database_name)

database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

'''
Movie

'''

class Movie(db.Model):
  __tablename__ = 'Movies'

  id = Column(Integer, primary_key=True)
  title = Column(String)
  release_date = Column(db.DateTime, nullable=False)

  def __init__(self, title, release_date):
    self.title = title
    self.release_date = release_date

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'release date': self.release_date,
    }    

'''
Actor

'''

class Actor(db.Model):
  __tablename__ = 'Actors'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  age = Column(String(3))
  gender = Column(String(6))

  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'age': self.age,
      'gender': self.gender
    }