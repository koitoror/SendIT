# import os
# from run import app

import psycopg2
import psycopg2.extras
# import urllib.parse as urlparse


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
        # # db_uri = os.getenv("TEST_DB_URL") if testing else os.getenv("DATABASE_URL")
        # db_uri = os.getenv("DATABASE_URL")
        # result = urlparse.urlparse(db_uri)
        # host = result.hostname
        # role = result.username
        # pwd = result.password
        # database = result.path[1:]

        return psycopg2.connect(
            database="dfdao6n5c3ldv0",
            user="lvyhayqrcwomlj",
            password="10030c356eb6d7f42f498a9b83cc66e050056e840e8164a0ff3ba99376612ae7",
            host="ec2-54-197-249-140.compute-1.amazonaws.com",
            port="5432"
        )

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

    def drop_all(self):
        tables = (
            """
            DROP TABLE IF EXISTS users CASCADE
            """,
            """
            DROP TABLE IF EXISTS parcels CASCADE
            """
        )
        for table in tables:
            self.cursor.execute(table)


if __name__ == "__main__":
    db = Database()
    # db.connect_db()
    db.create_tables()
    # db.drop_all()
