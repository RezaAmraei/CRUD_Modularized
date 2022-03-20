# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.f_name = data['f_name']
        self.l_name = data['l_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('crud_modularized').query_db(query)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of users with cls.
        for user in results:
            users.append( cls(user) )
        return users
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (f_name, l_name, email, created_at, updated_at) VALUES (%(f_name)s, %(l_name)s, %(email)s, NOW(), NOW());"
        return connectToMySQL('CRUD_MODULARIZED').query_db(query, data)

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM users WHERE id = %(id)s;"
        print(query)
        result = connectToMySQL('CRUD_MODULARIZED').query_db(query,data)
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE users SET f_name = %(f_name)s, l_name = %(l_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"

        return connectToMySQL('CRUD_MODULARIZED').query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('CRUD_MODULARIZED').query_db(query,data)