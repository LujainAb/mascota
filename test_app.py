import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Shelter, Pet


class MascotaTestCase(unittest.TestCase):
    """This class represents the Mascota test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "mascota_test"
        self.database_path = "postgresql://postgres:123@localhost:5432/" + self.database_name  # noqa
        self.shelterToken = os.environ.get('shelterToken')
        self.adopterToken = os.environ.get('adopterToken')
        setup_db(self.app, self.database_path)

        self.validAddPet = {
                "name": "Cody",
                "type": "Dog",
                "breed": "German shepard",
                "sex": "male",
                "age": 3,
                "behaviour": "very quite"}

        self.invalidAddPet = {
                "name": "Cody",
                "breed": "German shepard",
                "age": 3,
                "behaviour": "very quite"}

        self.editPet = {
                "name": "Cody edit",
                "type": "Dog",
                "breed": "German shepard",
                "sex": "male",
                "age": 3,
                "behaviour": "very quite"}

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

# ----------------------------------------------------------------------------#
# testing endpoints.
# ----------------------------------------------------------------------------#

    def test_get_shelters(self):
        res = self.client().get('/shelters', headers={
            'Authorization': "Bearer {}".format(self.shelterToken)
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['shelters'])
        self.assertTrue(len(data['shelters']))

    def test_without_token_get_shelters(self):
        res = self.client().get('/shelters')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)

    def test_get_pets(self):
        res = self.client().get('/pets', headers={
            'Authorization': "Bearer {}".format(self.adopterToken)
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['pets'])
        self.assertTrue(len(data['pets']))

    def test_without_token_get_pets(self):
        res = self.client().get('/pets')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)

    def test_get_shelter_details(self):
        res = self.client().get('/shelters/1', headers={
            'Authorization': "Bearer {}".format(self.shelterToken)
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['shelter'])

    def test_invalid_id_get_shelter_details(self):
        res = self.client().get('/shelters/1000', headers={
            'Authorization': "Bearer {}".format(self.shelterToken)
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_get_pet_details(self):
        res = self.client().get('/pets/1', headers={
            'Authorization': "Bearer {}".format(self.adopterToken)
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['pet'])

    def test_invalid_id_get_pet_details(self):
        res = self.client().get('/pets/1000', headers={
            'Authorization': "Bearer {}".format(self.adopterToken)
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_search_shelter(self):
        res = self.client().post('/shelters/search', headers={
            'Authorization': "Bearer {}".format(self.shelterToken)
        }, json={"searchTerm": "hub"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_search_shelter_with_invalid_searchterm(self):
        res = self.client().post('/shelters/search', headers={
            'Authorization': "Bearer {}".format(self.shelterToken)
        }, json={"searchTerm": "zzz"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['shelters']) == 0)  # will return empty array

    def test_search_pet(self):
        res = self.client().post('/pets/search', headers={
            'Authorization': "Bearer {}".format(self.shelterToken)
        }, json={"searchTerm": "cat"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_search_shelter_with_invalid_searchterm(self):
        res = self.client().post('/pets/search', headers={
            'Authorization': "Bearer {}".format(self.shelterToken)
        }, json={"searchTerm": "giraffe"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['pets']) == 0)  # will return an empty array

    def test_add_pet(self):
        res = self.client().post('/pets', headers={
             'Content-Type': 'application/json',
             'Authorization': "Bearer {}".format(self.shelterToken)
            }, data=json.dumps(self.validAddPet))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_add_invalid_pet(self):
        res = self.client().post('/pets', headers={
            'Content-Type': 'application/json',
            'Authorization': "Bearer {}".format(self.shelterToken)
        }, data=json.dumps(self.invalidAddPet))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)

    def test_edit_pet(self):
        res = self.client().patch('/pets/3', headers={
            'Content-Type': 'application/json',
            'Authorization': "Bearer {}".format(self.shelterToken)
        }, data=json.dumps(self.editPet))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['pet edited'])

    def test_edit_invalid_id_pet(self):
        res = self.client().patch('/pets/546674', headers={
            'Content-Type': 'application/json',
            'Authorization': "Bearer {}".format(self.shelterToken)
        }, data=json.dumps(self.editPet))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_delete_pet(self):
        p = Pet(name=self.validAddPet['name'], type=self.validAddPet['type'],
            breed=self.validAddPet['breed'], sex=self.validAddPet['sex'], age=self.validAddPet['age'], behaviour=self.validAddPet['behaviour'])
        p.insert()

        res = self.client().delete('/pets/'+str(p.id), headers={
            'Authorization': "Bearer {}".format(self.shelterToken)
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['pet deleted'])

    def test_delete_with_invalid_id_pet(self):
        res = self.client().delete('/pets/43434', headers={
            'Authorization': "Bearer {}".format(self.shelterToken)
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

# ----------------------------------------------------------------------------#
# testing roles.
# ----------------------------------------------------------------------------#

# Shelter role with avaliable permissions get:shelter (Shelter role has all permissions)

    def test_get_shelters(self):
        res = self.client().get('/shelters', headers={
            'Authorization': "Bearer {}".format(self.shelterToken)
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['shelters'])
        self.assertTrue(len(data['shelters']))


# Adopter role with avaliable permissions get:shelter
    def test_get_shelters(self):
        res = self.client().get('/shelters', headers={
            'Authorization': "Bearer {}".format(self.adopterToken)
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['shelters'])
        self.assertTrue(len(data['shelters']))

# Shelter role with avaliable permissions edit:pet (Shelter role has all permissions)

    def test_edit_pet(self):
        res = self.client().patch('/pets/3', headers={
            'Content-Type': 'application/json',
            'Authorization': "Bearer {}".format(self.shelterToken)
        }, data=json.dumps(self.editPet))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['pet edited'])

# Adopter role has NO permissions edit:pet to edit pet
    def test_edit_pet(self):
        res = self.client().patch('/pets/3', headers={
            'Content-Type': 'application/json',
            'Authorization': "Bearer {}".format(self.adopterToken)
        }, data=json.dumps(self.editPet))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)  # not allowed
        self.assertEqual(data['description'], "Permission not found.")


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
