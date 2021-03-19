from renderer import md_renderer
from flask import Blueprint
from api.Article.article_logic import (
    create_article,
    update_article,
    exists,
    get_all_articles,
)
import os
from config import Config
import click

render = Blueprint("db", __name__)


class RequiredArgument(Exception):
    pass


@click.argument("path", required=False)
@render.cli.command("process_content")  # @click.argument('name')
def process_content(path=None):
    """processes markdown into html in content directory with assumed structure
    (set in config.py or pass as param) -- see readme.md

    Parameters
    ----------
    path : path of content directory"""
    if not path:
        path = Config.CONTENT_PATH

    for (root, dirs, files) in os.walk(path):

        for article in files:
            if article[-3:] != ".md":
                continue
            print(f"processing {article} in {root}")
            _root = root.split("/")
            # grab first letter of parent folder
            type = _root[-1][0]
            mdr = md_renderer.MDRenderer()
            html_string, front_matter, anchor_pairs, image_path = mdr.process_md(
                f"{root}/{article}"
            )
            # TODO: fix bug with description rendering, if  multiline format and only 1 line is used will bug
            # if not front_matter.get("title", None):
            #     raise RequiredArgument(
            #         msg="Markdown file missing required 'title' in front matter"
            #     )

            #  front_matter_defaults = {'description': "", 'feature_image': 'default.jpg', 'published', 'link', 'tags'}
            # for k in front_matter_keys:
            #     if not front_matter.get(k, None):

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