import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from models import setup_db, db , Shelter , Pet

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  CORS(app)
  migrate = Migrate(app,db)
  setup_db(app)
  

  @app.route('/')
  def Welcome():
    return "Welcome To Mascota! a place where you can adopt a furry family member ♡"
  #----------------------------------------------------------------------------#
  # Shelter endpoints.
  #----------------------------------------------------------------------------#
  
  @app.route('/shelters' , methods=['GET'])
  def get_shelters():
    #querying all shelters avalible 
    shelters_query = Shelter.query.all()
    #checkign if the returned result from the query is empty or not , if yes return an appropriate error
    if len(shelters_query) == 0:
        abort(404)
    #fortmatting the shelters data representation 
    shelters = [shelter.format() for shelter in shelters_query]

    return jsonify({
        "success": True,
        "shelters": shelters
    }) , 200


  @app.route('/shelters/<id>' , methods=['GET'])
  def get_shelter_details(id):

    shelter = Shelter.query.filter(Shelter.id == id).one_or_none()
    
    #checking if the shelter exists , if not return an appropriate error
    if (shelter is None):
      abort(404)
    
    return jsonify({
      "success": True,
      "shelter": shelter.format()
    }) , 200




  return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)