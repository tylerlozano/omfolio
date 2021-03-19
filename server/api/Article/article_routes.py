from flask import Blueprint
import logging
from flask_jwt_extended import jwt_required
from api.Article.article_logic import (
    get_all_articles,
    get_all_blogs,
    get_all_notes,
    get_all_projects,
    get_single_article,
)


articles = Blueprint("articles", __name__)

LOG = logging.getLogger(__name__)


@articles.route("/api/articles", methods=["GET"])
@jwt_required
def _get_all_articles():
    return get_all_articles(), 200


@articles.route("/api/projects", methods=["GET"])
def _get_all_projects():
    return get_all_projects(), 200


@articles.route("/api/blogs", methods=["GET"])
def _get_all_blogs():
    return get_all_blogs(), 200


@articles.route("/api/notes", methods=["GET"])
def _get_all_notes():
    return get_all_notes(), 200


@articles.route("/api/article/<id_>", methods=["GET"])
def _get_single_article(id_):
    return get_single_article(id_), 200
