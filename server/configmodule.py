import os

# app.config["SQLALCHEMY_DATABASE_URI"] =
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config["JWT_SECRET_KEY"] = "YOUR_SECRET_KEY"


class Config(object):
    """Base config, uses staging database server."""

    CONTENT_PATH = f"{os.path.abspath(os.path.dirname(__file__))}/../content"
    MEDIA_FOLDER = "/media/"
    DEFAULT_IMAGE = "omfolio.svg"
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///flaskdatabase.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "YOUR_SECRET_KEY"

    # @property
    # def DATABASE_URI(self):         # Note: all caps
    #     return 'mysql://user@{}/foo'.format(self.DB_SERVER)


class ProductionConfig(Config):
    """Uses production database server."""

    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
