from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import click
from flask.cli import with_appcontext
import logging
from configmodule import *

db = SQLAlchemy()

# set basic logging level
logging.basicConfig(level=logging.DEBUG)


def create_app():
    app = Flask(__name__)
    # change according to deployment, can make script
    app.config.from_object(DevelopmentConfig())
    CORS(app)
    db.init_app(app)

    from api.Article.article_routes import articles

    app.register_blueprint(articles)

    from renderer import cmd

    app.register_blueprint(cmd)

    from api.Tag.tag_model import Tag

    @click.command(name="create_db")
    @with_appcontext
    def create_db():
        db.create_all(app=app)

    @click.command(name="uncreate_db")
    @with_appcontext
    def uncreate_db():
        db.drop_all(app=app)

    app.cli.add_command(create_db)
    app.cli.add_command(uncreate_db)

    return app
