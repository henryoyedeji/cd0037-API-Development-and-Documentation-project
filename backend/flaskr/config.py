import os

DB_NAME = "trivia"
DB_NAME_TEST = "trivia_test"
DB_USERNAME = "postgres"
DB_PASSWORD = "Overflow"


class Config(object):
    SECRET_KEY = os.urandom(32)
    # Grabs the folder where the script runs.
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Enable debug mode.
    os.environ["FLASK_DEBUG"] = "True"

    # SQLALCHEMY_TRACK_MODIFICATIONS
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Connect to the database

    # DATABASE URL
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@localhost:5432/{DB_NAME}"


class TestConfig(object):
    TESTING = (True,)
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@localhost:5432/{DB_NAME_TEST}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
