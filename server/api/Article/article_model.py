from flask_sqlalchemy import event
from datetime import datetime
from api.Tags_Article.tag_article_table import tag_article
from api.Tag.tag_model import Tag
from api import db
import json


class Article(db.Model):
    id_ = db.Column(db.String, primary_key=True)
    type = db.Column(db.String(1), nullable=False)
    published = db.Column(db.Boolean, nullable=False, default=False)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String, nullable=False)
    link = db.Column(db.Boolean, nullable=False, default=False)
    content = db.Column(db.String, nullable=False)
    feature_image = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow())
    tags = db.relationship(
        "Tag",
        secondary=tag_article,
        backref=db.backref("articles_associated", lazy="dynamic"),
    )
    anchor_pairs = db.Column(db.String, nullable=False)  # list in json form

    # ENUM for sqllite
    @staticmethod
    def before_set_type(target, value, oldvalue, initiator):
        if value not in ["b", "p", "n"]:  # blog, project, note
            raise ValueError('Type has to be one of "b", "p", or "n"')

    # TODO: use timedelta
    def formatUpdatedAt(self):
        days = (datetime.utcnow() - self.updated_at).days
        updated = ""
        if days >= 356:
            pass

        elif days >= 89:
            updated = f"{days//29} Months Ago"

        elif days >= 28:
            updated = f"{days//7} Weeks Ago"

        elif days >= 1:
            updated = f"{days} Days Ago"

        else:
            updated = "Today"
        return updated

    @property
    def serialize(self):
        return {
            "id": self.id_,
            "type": self.type,
            "published": json.dumps(self.published),
            "title": self.title,
            "slug": "-".join(self.title.lower().split()),
            "description": self.description,
            "link": json.dumps(self.link),
            "content": self.content,
            "feature_image": self.feature_image,
            "anchor_pairs": self.anchor_pairs,
            "tags": json.dumps([f"{tag.name}" for tag in self.tags]),
            "created_at": self.created_at.strftime("%b %d %Y"),
            "updated_at": self.formatUpdatedAt(),
        }


event.listen(Article.type, "set", Article.before_set_type)