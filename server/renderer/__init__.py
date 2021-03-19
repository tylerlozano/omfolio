from renderer import md_render
from flask import Blueprint
from api.Article.article_logic import (
    create_article,
    update_article,
    exists,
    get_all_articles,
)
import os
from configmodule import Config

cmd = Blueprint("db", __name__)


@cmd.cli.command("process_content")
def process_content():
    # if not path:
    path = Config.CONTENT_PATH
    for (root, dirs, files) in os.walk(path):
        for article in files:
            if article[-3:] != ".md":
                continue
            _root = root.split("/")
            type = _root[-1][0]
            mdr = md_render.MDRender()
            html_string, front_matter, anchor_pairs, image_path = mdr.process_md(
                f"{root}/{article}"
            )

            feature_image = f'/media/{front_matter.pop("feature_image")}'
            if exists(article, type):
                update_article(
                    article,
                    type,
                    html_string,
                    **front_matter,
                    feature_image=feature_image,
                    anchor_pairs=anchor_pairs,
                )
            else:
                create_article(
                    article,
                    type,
                    html_string,
                    **front_matter,
                    feature_image=feature_image,
                    anchor_pairs=anchor_pairs,
                )