import os

from jinja2 import Environment, ChoiceLoader, FileSystemLoader

from . import fs


def load(template_name, extra_dirs=None):
    extra_dirs = extra_dirs or []
    env = Environment(
        loader=ChoiceLoader([
            *[FileSystemLoader(dirname) for dirname in extra_dirs],
            FileSystemLoader("templates"),
            FileSystemLoader(os.path.join(fs.COMMONS_DIR, "templates")),
        ])
    )
    return env.get_template(template_name)
