Welcome To Mascota! a place where you can adopt a furry family member ♡

Mascota is a pet shop that connects shelters with adopters. it lets shelters post their pets so future adopters can know about them and know where they are located.

# API Reference
### Getting Started
* Hosted URL: http://mascotashop.herokuapp.com/ 
* Authentication: Auth0 information for authentication can be found in `setup.sh`.


### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### PIP Dependencies

run the following to install all necessary dependencies:

```
pip3 install -r requirements.txt
```

This will install all of the required packages.

##### Key Dependencies

Stack/tools used:

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Running the server

To run the server, execute:
```
python3 app.py
```
We can now also open the application via Heroku using the URL:
http://mascotashop.herokuapp.com/ 

The live application can only be used to generate tokens via Auth0, the endpoints have to be tested using curl or Postman 
using the token since I did not build a frontend for the application.

# Running tests
running the API tests using Postman by importing the collection `Mascota tests.postman_collection.json`. 

Or by running test_app.py. To run this file use:
```
dropdb mascota_test
createdb mascota_test
psql mascota_test < mascota_test.sql
python test_app.py
```

### Error Handling
Errors are returned as JSON objects, in the format of:
```
{
     "success": False,
     "error": 404,
     "message": "resource not found"
}
```
The API may return only 4 types of errors:
* 400: Bad Request
* 404: Resource Not Found
* 401: unauthorized
* 422: Not processable

# Endpoints

## Endpoints documentation 
endpoint documentation can be found in  https://documenter.getpostman.com/view/16709336/U16jLQjy .

_____________________

`GET '/'` 

Adopter role : 

`GET '/shelters'`

`GET '/pets'`

`GET '/shelters/<int:id>'`

`GET '/pets/<int:id>'`

`POST '/shelters/search'`

`POST '/pets/search'`

Shelter manager role. same permissions as adopter and:

`POST '/pets'`

`PATCH '/pets/<int:id>'`

`DELETE '/pets/<int:id>'`

