#!/usr/bin/env python3

import os

from jinja2 import Environment, ChoiceLoader, FileSystemLoader

from reader.berean import BereanInterlinear
from reader import fs


OUTPUT_DIR = "output"

templates = {
    name: Environment(
        loader=ChoiceLoader([
            FileSystemLoader(os.path.join("templates", name)),
            FileSystemLoader(os.path.join("templates")),
            FileSystemLoader(os.path.join(fs.COMMONS_DIR, "templates")),
        ])
    ).get_template("template.html")
    for name in ["plain", "hover", "toggle", "frequency"]
}


def generate(title, rows, template_type, output_filename):

    with open(output_filename, "w") as output:
        print(templates[template_type].render(
            title=title,
            rows=rows,
        ), file=output)


if __name__ == "__main__":
    fs.create_dir(OUTPUT_DIR)

    book_name = "John"
    book_num = 4
    chapter_num = 3
    verse_num = 16

    title = f"{book_name} {chapter_num}.{verse_num}"
    bcv = f"{book_num:02d}{chapter_num:02d}{verse_num:02d}"

    interlinear = BereanInterlinear(os.path.join("data", "berean_tables.csv"))
    interlinear.load()

    rows = interlinear.get_verse(bcv)

    for template_type in ["plain", "hover", "toggle", "frequency"]:
        output_filename = os.path.join(OUTPUT_DIR, f"{template_type}_{bcv}.html")
        generate(title, rows, template_type, output_filename)
        print(f"wrote {output_filename}")

    fs.copy_css(["interlinear.css", "skolar.css"], OUTPUT_DIR)
    fs.copy_js(["toggle.js", "frequency.js"], OUTPUT_DIR)
