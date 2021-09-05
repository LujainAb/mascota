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
# class Person(db.Model):  
#   __tablename__ = 'People'

#   id = Column(Integer, primary_key=True)
#   name = Column(String)
#   catchphrase = Column(String)

#   def __init__(self, name, catchphrase=""):
#     self.name = name
#     self.catchphrase = catchphrase

#   def format(self):
#     return {
#       'id': self.id,
#       'name': self.name,
#       'catchphrase': self.catchphrase}


#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Pet(db.Model):
    __tablename_ = 'Pet'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    breed = Column(String)
    sex = Column(String)
    age = Column(Integer)
    shelter_id = Column(Integer, db.ForeignKey('Shelter.id'))
    



class Shelter(db.Model):
    __tablename_ = 'Shelter'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String)
    shelter_pet = db.relationship('Pet', backref='Shelter')

    def __repr__(self):
      return f'<Shelter {self.id} {self.name}>'

