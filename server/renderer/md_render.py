from markdown_it import MarkdownIt
from mdit_py_plugins.front_matter import front_matter_plugin
from mdit_py_plugins.footnote import footnote_plugin
from mdit_py_plugins.anchors import anchors_plugin
from mdit_py_plugins.deflist import deflist_plugin
from mdit_py_plugins.texmath import texmath_plugin
import json
from subprocess import PIPE, run

from markdown_it.renderer import RendererHTML
from configmodule import Config


def render_math_inline(self, tokens, idx, options, env):
    content = tokens[idx].content
    displayMode = "false"
    command = [
        "node",
        "scripts/render-math.js",
        content,
        displayMode,
    ]
    result = run(command, stdout=PIPE, stderr=PIPE, text=True)
    return result.stdout


def math_block(self, tokens, idx, options, env):
    content = tokens[idx].content
    displayMode = "true"
    command = ["node", "scripts/render-math.js", content, displayMode]
    result = run(command, stdout=PIPE, stderr=PIPE, text=True).stdout
    tokens[idx].content = result
    return result


class MDRender:
    full_path = None
    image_path = None

    @classmethod
    def process_md(cls, md_file_path):
        # plugins and options
        md = (
            MarkdownIt("commonmark", renderer_cls=MDRender.MyRenderer)
            .use(front_matter_plugin)
            .use(footnote_plugin)
            .use(deflist_plugin)
            .use(texmath_plugin)
            .use(anchors_plugin, max_level=5)
            .enable("image")
            .enable("table")
        )
        # rendering for inline tokens, non-inline defined in MyRenderer
        md.add_render_rule("math_inline", render_math_inline)
        md.add_render_rule("math_block", math_block)
        md.add_render_rule("math_block_eqno", math_block)

        cls.full_path = md_file_path
        cls.image_path = Config.MEDIA_FOLDER
        # print(md.get_active_rules())
        html_string = md.render(cls._get_md_string(md_file_path))

        return (
            html_string,
            md.renderer._front_matter,
            md.renderer.anchor_pairs,
            cls.image_path,
        )

    # @classmethod
    # def _set_path(cls, post_type, post_id):
    #     options = {
    #         "blog": cls.BLOG_PATH,
    #         "note": cls.NOTES_PATH,
    #         "project": cls.PORTFOLIO_PATH,
    #     }
    #     cls.full_path = f"{cls.ABS_PATH}{options[post_type]}{post_id}/"

    @classmethod
    def _get_md_string(cls, md_file_path):
        with open(md_file_path, "r") as reader:
            md_string = reader.read()
        return md_string

    class MyRenderer(RendererHTML):
        def __init__(self, *args, **kwargs):
            self._front_matter = None
            self.anchor_pairs = []
            super().__init__(*args, **kwargs)

        def fence(self, tokens, idx, options, env):
            tkn = tokens[idx]
            language = tkn.info.strip()
            code = tkn.content
            command = ["node", "scripts/render-code.js", language, code]
            result = run(command, stdout=PIPE, stderr=PIPE, text=True)
            resultString = (
                f'<pre><code class="language-{language}">{result.stdout}</code></pre>'
            )
            return resultString

        def front_matter(self, tokens, idx, options, env):
            if tokens[idx].content:
                _front_matter = tokens[idx].content.splitlines()
                # try split on ":" for multiline values
            d = {}
            for i in range(len(_front_matter)):
                s = _front_matter[i]
                if ":" in s:
                    x, y = s.split(":")
                    x = x.strip()
                    if x == "tags":
                        d[x] = json.dumps([f"{t.strip()}" for t in y.split(",")])

                    else:
                        # add to description string multiple lines withous ":"
                        if x == "description":
                            i += 1
                            while ":" not in _front_matter[i]:
                                y = f"{y} {_front_matter[i]}"
                                i += 1
                            d[x] = y.strip()
                            continue

                        if x == "published" or x == "link":
                            d[x] = json.loads(y.strip())
                            continue

                        y = f'"{y.strip()}"'
                        d[x] = json.loads(y)

            self._front_matter = d
            return self.renderToken(tokens, idx, options, env)

        def heading_open(self, tokens, idx, options, env):
            IDindex = tokens[idx].attrIndex("id")
            if IDindex >= 0:
                _id = tokens[idx].attrs[IDindex][1]
                title = tokens[idx + 1].content
                tag_num = tokens[idx].tag[1]
                self.anchor_pairs.append([tag_num, title, _id])
            return self.renderToken(tokens, idx, options, env)

        def math_block_eqno(self, tokens, idx, options, env):
            content = tokens[idx].content
            displayMode = "true"
            command = ["node", "scripts/render-math.js", content, displayMode]
            tokens[idx].content = run(command, stdout=PIPE, stderr=PIPE, text=True)
            return self.renderToken(tokens, idx + 1, options, env)

        def math_block(self, tokens, idx, options, env):
            print("HERE TOO")
            return self.renderToken(tokens, idx, options, env)

        def image(self, tokens, idx, options, env):
            aIndex = tokens[idx].attrIndex("src")
            if aIndex < 0:
                # link to default?
                pass
            else:
                tokens[idx].attrs[aIndex][1] = (
                    MDRender.image_path + tokens[idx].attrs[aIndex][1]
                )

            return self.renderToken(tokens, idx, options, env)

        def link_open(self, tokens, idx, options, env):
            aIndex = tokens[idx].attrIndex("target")
            if aIndex < 0:
                tokens[idx].attrPush(["target", "_blank"])  # add new attribute
            else:
                tokens[idx].attrs[aIndex][
                    1
                ] = "_blank"  # replace value of existing attr

            # pass token to default renderer.
            return self.renderToken(tokens, idx, options, env)


# {'code_block': <bound method RendererHTML.code_block of <server.md_render.MDRender.MyRenderer object at 0x1058b83d0>>, 'code_inline': <bound method RendererHTML.code_inline of <server.md_render.MDRender.MyRenderer object at 0x1058b83d0>>, 'fence': <bound method MDRender.MyRenderer.fence of <server.md_render.MDRender.MyRenderer object at 0x1058b83d0>>, 'front_matter': <bound method MDRender.MyRenderer.front_matter of <server.md_render.MDRender.MyRenderer object at 0x1058b83d0>>, 'hardbreak': <bound method RendererHTML.hardbreak of <server.md_render.MDRender.MyRenderer object at 0x1058b83d0>>, 'heading_open': <bound method MDRender.MyRenderer.heading_open of <server.md_render.MDRender.MyRenderer object at 0x1058b83d0>>, 'html_block': <bound method RendererHTML.html_block of <server.md_render.MDRender.MyRenderer object at 0x1058b83d0>>, 'html_inline': <bound method RendererHTML.html_inline of <server.md_render.MDRender.MyRenderer object at 0x1058b83d0>>, 'image': <bound method MDRender.MyRenderer.image of <server.md_render.MDRender.MyRenderer object at 0x1058b83d0>>, 'link_open': <bound method MDRender.MyRenderer.link_open of <server.md_render.MDRender.MyRenderer object at 0x1058b83d0>>, 'math_block': <bound method texmath_plugin.<locals>.render_math_block of <server.md_render.MDRender.MyRenderer object at 0x1058b83d0>>, 'softbreak': <bound method RendererHTML.softbreak of <server.md_render.MDRender.MyRenderer object at 0x1058b83d0>>, 'text': <bound method RendererHTML.text of <server.md_render.MDRender.MyRenderer object at 0x1058b83d0>>, 'footnote_ref': <bound method render_footnote_ref of <server.md_render.MDRender.MyRenderer object at 0x1058b83d0>>, 'footnote_block_open': <bound method render_footnote_block_open of <server.md_render.MDRender.MyRenderer object at 0x1058b83d0>>, 'footnote_block_close': <bound method render_footnote_block_close of <server.md_render.MDRender.MyRenderer object at 0x1058b83d0>>, 'footnote_open': <bound method render_footnote_open of <server.md_render.MDRender.MyRenderer object at 0x1058b83d0>>, 'footnote_close': <bound method render_footnote_close of <server.md_render.MDRender.MyRenderer object at 0x1058b83d0>>, 'footnote_anchor': <bound method render_footnote_anchor of <server.md_render.MDRender.MyRenderer object at 0x1058b83d0>>, 'footnote_caption': <bound method render_footnote_caption of <server.md_render.MDRender.MyRenderer object at 0x1058b83d0>>, 'footnote_anchor_name': <bound method render_footnote_anchor_name of <server.md_render.MDRender.MyRenderer object at 0x1058b83d0>>, 'math_inline': <bound method render_math_inline of <server.md_render.MDRender.MyRenderer object at 0x1058b83d0>>, 'math_single': <bound method texmath_plugin.<locals>.render_math_inline of <server.md_render.MDRender.MyRenderer object at 0x1058b83d0>>, 'math_block_eqno': <bound method texmath_plugin.<locals>.render_math_block of <server.md_render.MDRender.MyRenderer object at 0x1058b83d0>>}

# mdr = MDRender()
# html_string, fm, ap = mdr.process_md(
#     "/Users/tylerlozano/Documents/workspace/projects/vue/lozano-ai/server/server/content/blog/0/post.md"
# )
# print(html_string)
# print(fm)
# print(ap)