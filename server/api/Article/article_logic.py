from flask import jsonify
import logging
from werkzeug.exceptions import BadRequest, UnprocessableEntity
from datetime import datetime
from api import db
from api.Article.article_model import Article
from api.Tag.tag_model import Tag
from api.Tags_Article.tag_article_table import tag_article
import json

LOG = logging.getLogger(__name__)

type_names = {"b": "blog", "p": "project", "n": "note"}


def make_id(article_name, type):
    return f"{type}-{article_name}"


def exists(article_name, type):
    id_ = make_id(article_name, type)
    return Article.query.filter_by(id_=id_).first() is not None


def create_article(
    article_name,
    type,
    content,
    title="",
    description="",
    feature_image=DEFAULT_IMAGE,
    published=False,
    link=False,
    tags=[],
    anchor_pairs=[],
):
    id_ = make_id(article_name, type)
    if Article.query.filter_by(id_=id_).first():
        LOG.debug(f"{type} with id_ {id_} already exists.")
        e = UnprocessableEntity("Input payload validation failed.")
        e.data = {"errors": {"msg": f"{type} with id_ {id_} already exists."}}
        raise e
    new_article = Article(
        id_=id_,
        type=type,
        published=published,
        title=title,
        description=description,
        link=link,
        content=content,
        feature_image=feature_image,
        anchor_pairs=json.dumps(anchor_pairs),
    )

    if tags:
        tags = json.loads(tags)
        for tag in tags:
            present_tag = Tag.query.filter_by(name=tag).first()
            if present_tag:
                present_tag.articles_associated.append(new_article)
            else:
                new_tag = Tag(name=tag)
                new_tag.articles_associated.append(new_article)
                db.session.add(new_tag)

    db.session.add(new_article)
    db.session.commit()

    article_id = getattr(new_article, "id_")
    return jsonify({"id": article_id})


def _get_all_articles(type):
    articles = (
        Article.query.filter_by(type=type)
        .order_by(db.desc(Article.created_at))
        .order_by(db.desc(Article.title))
    )
    serialized_data = []
    for article in articles:
        keys_to_extract = [
            "created_at",
            "updated_at",
            "description",
            "slug",
            "feature_image",
            "id",
            "published",
            "title",
            "tags",
        ]
        data = article.serialize
        serialized_article = {key: data[key] for key in keys_to_extract}
        serialized_data.append(serialized_article)

    return jsonify({f"all_{type_names[type]}s": serialized_data})


def get_all_articles():
    return jsonify({get_all_blogs(), get_all_projects(), get_all_notes()})


def get_all_projects():
    return _get_all_articles("p")


def get_all_blogs():
    return _get_all_articles("b")


def get_all_notes():
    return _get_all_articles("n")


def get_single_article(id_):
    article = Article.query.filter_by(id_=id_).first()
    serialized_article = article.serialize
    serialized_article["tags"] = []

    for tag in article.tags:
        serialized_article["tags"].append(tag.serialize)

    return jsonify(serialized_article)


def update_article(
    article_name,
    type,
    content,
    title="",
    description="",
    feature_image=DEFAULT_IMAGE,
    published=False,
    link=False,
    tags=[],
    anchor_pairs=[],
):
    id_ = make_id(article_name, type)
    article = Article.query.filter_by(id_=id_).first()

    article.published = published
    article.title = title
    article.description = description
    article.link = link
    article.content = content
    article.feature_image = feature_image
    article.anchor_pairs = json.dumps(anchor_pairs)
    article.updated_at = datetime.utcnow()

    db.session.commit()
    return jsonify({"article_id": article.id_})


def hide_article(id_):
    article = Article.query.filter_by(id_=id_).first()
    article.published = False
    db.session.commit()

    return jsonify("article was unpublished"), 200


def delete_article(id_):
    article = Article.query.filter_by(id_=id_).first()
    db.session.delete(article)
    db.session.commit()

    return jsonify("article was deleted"), 200