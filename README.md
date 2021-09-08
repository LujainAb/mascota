Welcome To Mascota! a place where you can adopt a furry family member ♡

Mascota is a pet shop that connects shelters with adopters. it lets shelters post their pets so future adopters can know about them and know where they are located.

# API Reference
### Getting Started
* Hosted URL: http://mascotashop.herokuapp.com/ 
* Authentication: Auth0 information for authentication can be found in `setup.sh`.

# Running tests
running the API tests using Postman by importing the collection `Mascota tests.postman_collection.json`.

### Error Handling
Errors are returned as JSON objects, in the format of:
```
{
     "success": False,
     "error": 404,
     "message": "resource not found"
}
```
The API may return only 3 types of errors:
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

