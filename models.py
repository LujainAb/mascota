from sqlalchemy import Column, String, create_engine , Integer
from flask_sqlalchemy import SQLAlchemy
import json
import os

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


'''
Person
Have title and release year
'''
class Person(db.Model):  
  __tablename__ = 'People'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  catchphrase = Column(String)

  def __init__(self, name, catchphrase=""):
    self.name = name
    self.catchphrase = catchphrase

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'catchphrase': self.catchphrase}


#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Pet(db.Model):
    __tablename_ = 'Pet'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    type = db.Column(db.String)
    breed = db.Column(db.String)
    sex = db.Column(db.Character)
    age = db.Column(db.Integer)
    behavior = db.Column(db.String)
    owner = db.Column()



class Owner(db.Model):
    __tablename_ = 'Owner'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

