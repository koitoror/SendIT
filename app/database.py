import os
# from run import app

import psycopg2
import psycopg2.extras
from flask_bcrypt import Bcrypt


class Database(object):
    """Class for creating the database
    schema and establishing connection.
    """

    def __init__(self, testing=None):
        # with app.app_context():
        self.connection = self.connect(testing=testing)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        self.dict_cursor = self.connection.cursor(
            cursor_factory=psycopg2.extras.DictCursor)

    def connect(self, testing=None):
        # db_uri = os.getenv("TEST_DB_URL") if testing else os.getenv("DATABASE_URL")

        # if testing:
        #     db_uri = os.getenv("TEST_DB_URL")
        # else:
        #     db_uri = os.getenv("DATABASE_URL")

        db_uri = os.getenv("DATABASE_URL")

        return psycopg2.connect(db_uri)



    def create_tables(self):
        tables = (
            """
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                date_registered TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                admin BOOLEAN NOT NULL DEFAULT False

            )
            """,
            """
            CREATE TABLE IF NOT EXISTS parcels (
                parcel_id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL,
                parcel_name VARCHAR(255) NOT NULL,
                date_ordered TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                date_modified TIMESTAMP WITH TIME ZONE,
                price INTEGER NOT NULL,
                pickup_location text,
                present_location text,
                destination_location text,
                status text,
                cancel_order BOOLEAN NOT NULL DEFAULT False,
                FOREIGN KEY (user_id)
                    REFERENCES users (id)
                    ON UPDATE CASCADE ON DELETE CASCADE
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS blacklist(
                tokens VARCHAR(200) NOT NULL
            )
            """
        )
        for table in tables:
            self.cursor.execute(table)


    def add_admin(self):
        new_admin = ("adm", "adm@gmail.com", Bcrypt().generate_password_hash("123456").decode(), "True")
        add_admin_user_command = "INSERT INTO users(username, email, password, admin) VALUES('" + new_admin[0] + "','" + new_admin[1] + "','" + new_admin[2] + "','" + new_admin[3] + "')"
        self.cursor.execute(add_admin_user_command)


    def drop_all(self):
        tables = (
            """
            DROP TABLE IF EXISTS users CASCADE
            """,
            """
            DROP TABLE IF EXISTS parcels CASCADE
            """,
            """
            DROP TABLE IF EXISTS blacklist CASCADE
            """
        )
        for table in tables:
            self.cursor.execute(table)


if __name__ == "__main__":
    db = Database()
    # db.connect_db()  
    db.create_tables()
    db.add_admin()
    # db.drop_all()
