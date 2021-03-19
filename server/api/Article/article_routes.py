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


# @articles.route("/add_article", methods=["POST"])
# @jwt_required  # Bearer ‘YOUR_JWT_TOKEN‘ : ADD TO HEADER
# def _create_article():
#     # if not request.is_json:
#     #     LOG.debug(f"Invalid json request.")
#     #     e = BadRequest("Input payload validation failed.")
#     #     e.data = {"errors": {"msg": "Missing JSON in request"}}
#     #     raise e

#     data = request.get_json(force=True)
#     create_article(data)


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


# @articles.route("/update_article/<int:id>", methods=["PUT"])
# @jwt_required
# def _update_article(id_):
#     # TODO: update by type-title or some onother unique combination in frontmatter
#     if not request.is_json:
#         LOG.debug(f"Invalid json request.")
#         e = BadRequest("Input payload validation failed.")
#         e.data = {"errors": {"msg": "Missing JSON in request"}}
#         raise e

#     data = request.get_json()
#     return update_article(id_, data)


# @articles.route("/hide_article/<int:id>", methods=["PUT"])
# @jwt_required
# def _hide_article(id_):
#     return hide_article(id_)


# @articles.route("/delete_article/<int:id>", methods=["DELETE"])
# @jwt_required
# def _delete_article(id_):
#     return delete_article(id_)

# curl --header -H 'Accept: application/json' -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MTAzNTExODAsIm5iZiI6MTYxMDM1MTE4MCwianRpIjoiNDI4NDlkMmEtMDA3NC00OGU0LWFiMjQtMmM0MDg5NzlhNjdmIiwiZXhwIjoxNjEwMzU4MzgwLCJpZGVudGl0eSI6InR5bGVyLm0ubG96YW5vQGdtYWlsLmNvbSIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.fvcsiiSF9MZMXLL-l2X99Z4UJfJIYI5pTW8nKv5CzoY" --data "published=false&title=example+title&body=some+content+here&description=disc&feature_image=boobs.jpg" http://127.0.0.1:5000/add_article
