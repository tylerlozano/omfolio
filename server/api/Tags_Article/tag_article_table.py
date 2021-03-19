from api import db

tag_article = db.Table(
    "tag_article",
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id_"), primary_key=True),
    db.Column("article_id", db.Integer, db.ForeignKey("article.id_"), primary_key=True),
)