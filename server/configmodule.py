import os


class Config(object):
    """Base config, uses staging database server."""

    CONTENT_PATH = f"{os.path.abspath(os.path.dirname(__file__))}/../content"
    MEDIA_FOLDER = "/media/"
    DEFAULT_IMAGE = "omfolio.svg"
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///flaskdatabase.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    """Uses production database server."""
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
