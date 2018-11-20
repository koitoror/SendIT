import os
# from run import app

import psycopg2
import psycopg2.extras
import urllib.parse as urlparse
# from instance import create_app


# app = create_app(config_name=os.getenv("FLASK_CONFIG"))

class Database(object):
    """Class for creating the database
    schema and establishing connection.
    """
    def __init__(self, testing=None):
        # with app.app_context():
        self.connection = self.connect(testing=testing)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        self.dict_cursor = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def connect(self, testing=None):
        # db_uri = os.getenv("TEST_DB_URL") if testing else os.getenv("DATABASE_URL")
        db_uri = os.getenv("DATABASE_URL")
        result = urlparse.urlparse(db_uri)    
        host = result.hostname
        role = result.username
        pwd = result.password
        database = result.path[1:]

        return psycopg2.connect(
            database="deu75mlooshddr", 
            user="gneferakfbnran", 
            password="c08024e49203b31e0584237f938f0bc310ca010431c31cefcb0cade0e69e4e37", 
            host="ec2-54-83-27-162.compute-1.amazonaws.com", 
            port="5432",
        )

    #     return psycopg2.connect(
    #         database=database,
    #         user=role,
    #         host=host,
    #         password=pwd,
        # )


    # def connect_db(self):
    #     """Method for creating db connection."""
    #     try:
    #         self.connection = psycopg2.connect(database="store_manager", user="postgres", password="123456", host="localhost", port="5432")
    #         self.connection.autocommit = True
    #         self.cursor = self.connection.cursor()
    #         self.dict_cursor = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    #     except Exception as e:
    #         return {"message": str(e)}

    # def connect_db(self, testing=None):
    #     """Method for creating db connection."""
    #     try:
    #         self.connection = psycopg2.connect(database="d4501hveeam6gl", user="hpwkkcsgckkgvk", password="2e5282386e7f2a3e1faef5558102a71b67019dc02844d1b16a5374b8e354be7a", host="ec2-107-22-189-136.compute-1.amazonaws.com", port="5432")
    #         self.connection.autocommit = True
    #         self.cursor = self.connection.cursor()
    #         self.dict_cursor = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    #     except Exception as e:
    #         return {"message": str(e)}



if __name__=="__main__":
    db = Database()
    # db.connect_db()
    # db.create_tables()
    # db.drop_all()