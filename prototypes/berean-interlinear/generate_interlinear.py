#!/usr/bin/env python3

from berean import load_interlinear, get_verse


from jinja2 import Environment, FileSystemLoader


env = Environment(
    loader=FileSystemLoader("."),
)
template = env.get_template("template.html")


def output(title, bcv):
    entries = load_interlinear()
    print(template.render(
        title=title,
        rows=get_verse(entries, bcv),
    ))


if __name__ == "__main__":
    output("John 3.16", "040316")
