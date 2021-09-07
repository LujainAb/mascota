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

  @app.route('/shelters/search', methods=['POST'])  
  def shelter_search():
    body = request.get_json()
    # to check if the json body is submitted or not
    if not body:
      abort(400)

    searchTerm = body.get('searchTerm', None)
    # to check if the search term is submitted or not
    if (searchTerm is None):
      abort(400)  
    
    shelters_query = Shelter.query.filter(Shelter.name.ilike('%{}%'.format(searchTerm)))

    shelters = [shelter.format() for shelter in shelters_query]

    return jsonify({
        "success": True,
        "shelters": shelters
    }) , 200

  #----------------------------------------------------------------------------#
  # Pet endpoints.
  #----------------------------------------------------------------------------#
  
  @app.route('/pets' , methods=['GET'])
  def get_pets():
    #querying all pets avalible 
    pets_query = Pet.query.all()
    #checkign if the returned result from the query is empty or not , if yes return an appropriate error
    if len(pets_query) == 0:
        abort(404)
    #fortmatting the pets data representation 
    pets = [pet.format() for pet in pets_query]

    return jsonify({
        "success": True,
        "pets": pets
    }) , 200
  
  @app.route('/pets/<id>' , methods=['GET'])
  def get_pet_details(id):

    pet = Pet.query.filter(Pet.id == id).one_or_none()
    
    #checking if the pet exists , if not return an appropriate error
    if (pet is None):
      abort(404)
    
    return jsonify({
      "success": True,
      "pet": pet.format()
    }) , 200

  @app.route('/pets/search', methods=['POST'])  
  def pet_search():
    body = request.get_json()
    # to check if the json body is submitted or not
    if not body:
      abort(400)

    searchTerm = body.get('searchTerm', None)
    # to check if the search term is submitted or not
    if (searchTerm is None):
      abort(400)  
    
    pets_query = Pet.query.filter(Pet.type.ilike('%{}%'.format(searchTerm)))

    pets = [pet.format() for pet in pets_query]

    return jsonify({
        "success": True,
        "pets": pets
    }) , 200

  @app.route('/pets', methods=['POST'])
  def add_pet():
    body = request.get_json()
    if not body:
      abort(400)

    name = body.get('name', None)
    type = body.get('type', None)
    breed = body.get('breed', None)
    sex = body.get('sex', None)
    age = body.get('age', None)
    behaviour = body.get('behaviour', None)

    if(name is None or
      type is None or
      sex is None or
      age is None):
        abort(400)

    try:
      pet = Pet(name=name,
                type=type,
                breed=breed,
                sex=sex,
                age=age,
                behaviour=behaviour)
      Pet.insert()
      return jsonify({
        'success': True
      })
    except:
      abort(422)



  return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)