import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from models import setup_db, db , Shelter , Pet
from .auth.auth import AuthError, requires_auth

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
  @requires_auth('get:shelters')
  def get_shelters(jwt):
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
  @requires_auth('get:shelters')
  def get_shelter_details(jwt,id):

    shelter = Shelter.query.filter(Shelter.id == id).one_or_none()
    
    #checking if the shelter exists , if not return an appropriate error
    if (shelter is None):
      abort(404)
    
    return jsonify({
      "success": True,
      "shelter": shelter.format()
    }) , 200

  @app.route('/shelters/search', methods=['POST'])  
  @requires_auth('search:shelters')
  def shelter_search(jwt):
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
  @requires_auth('get:pets')
  def get_pets(jwt):
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
  @requires_auth('get:pets')
  def get_pet_details(jwt, id):

    pet = Pet.query.filter(Pet.id == id).one_or_none()
    
    #checking if the pet exists , if not return an appropriate error
    if (pet is None):
      abort(404)
    
    return jsonify({
      "success": True,
      "pet": pet.format()
    }) , 200

  @app.route('/pets/search', methods=['POST'])  
  @requires_auth('search:pets')
  def pet_search(jwt):
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
  @requires_auth('post:pets')
  def add_pet(jwt):
    body = request.get_json()
    if not body:
      abort(400)

    pet_name = body.get("name", None)
    pet_type = body.get("type", None)
    pet_breed = body.get("breed", None)
    pet_sex = body.get("sex", None)
    pet_age = body.get("age", None)
    pet_behaviour = body.get("behaviour", None)

    if(pet_name is None or
      pet_type is None or
      pet_sex is None or
      pet_age is None):
        abort(400)

    pet = Pet(name=pet_name,type=pet_type,breed=pet_breed,sex=pet_sex,age=pet_age,behaviour=pet_behaviour)
    # pet = Pet(name=pet_name,
    #           type=pet_type,
    #           breed=pet_breed,
    #           sex=pet_sex,
    #           age=pet_age,
    #           behaviour=pet_behaviour)
    pet.insert()

    return jsonify({
        'success': True
    })

  @app.route('/pets/<id>' , methods=['DELETE'])
  @requires_auth('delete:pets')
  def delete_pet(jwt,id):

    pet = Pet.query.filter(Pet.id == id).one_or_none()
    
    #checking if the pet exists , if not return an appropriate error
    if (pet is None):
      abort(404)
    else:
      pet.delete()

      return jsonify({
        "success": True,
        "pet deleted": pet.format()
      }) , 200
  
  @app.route('/pets/<id>' , methods=['PATCH'])
  @requires_auth('edit:pets')
  def edit_pet(jwt,id):
    pet = Pet.query.filter(Pet.id == id).one_or_none()
    
    #checking if the pet exists , if not return an appropriate error
    if (pet is None):
      abort(404)
    else:
      body = request.get_json()
    if not body:
      abort(400)
    
    #getting the values
    pet_name = body.get("name", None)
    pet_type = body.get("type", None)
    pet_breed = body.get("breed", None)
    pet_sex = body.get("sex", None)
    pet_age = body.get("age", None)
    pet_behaviour = body.get("behaviour", None)

    #Assigning the new values
    pet.name=pet_name
    pet.type=pet_type
    pet.breed=pet_breed
    pet.sex=pet_sex
    pet.age=pet_age
    pet.behaviour=pet_behaviour

    #using the update method to update it in the db 
    pet.update()

    return jsonify({
        "success": True,
        "pet edited": pet.format()
      }) , 200


  #----------------------------------------------------------------------------#
  # Error handling.
  #----------------------------------------------------------------------------#


  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422

  @app.errorhandler(404)
  def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'resource not found'
        }), 404

  @app.errorhandler(400)
  def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'bad request'
        }), 400

  @app.errorhandler(401)
  def unauthorized(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "unauthorized"
    }), 401        

  @app.errorhandler(AuthError)
  def Auth_error(error):
    auth = jsonify(error.error)
    auth.status_code = error.status_code
    return auth


  




  return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)