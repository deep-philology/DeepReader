#!/usr/bin/env python3

import os
import shutil

from jinja2 import Environment, FileSystemLoader

from berean import BereanInterlinear


env = Environment(
    loader=FileSystemLoader("templates"),
)

templates = {
    name: env.get_template(f"{name}.html")
    for name in ["plain", "hover", "toggle", "frequency"]
}


def generate(title, rows, template_type, output_filename):

    with open(output_filename, "w") as output:
        print(templates[template_type].render(
            title=title,
            rows=rows,
        ), file=output)


OUTPUT_DIR = "output"


if __name__ == "__main__":
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"created {OUTPUT_DIR}")

    book_name = "John"
    book_num = 4
    chapter_num = 3
    verse_num = 16

    title = f"{book_name} {chapter_num}.{verse_num}"
    bcv = f"{book_num:02d}{chapter_num:02d}{verse_num:02d}"

    interlinear = BereanInterlinear()
    interlinear.load()

    rows = interlinear.get_verse(bcv)

    for template_type in ["plain", "hover", "toggle", "frequency"]:
        output_filename = os.path.join(OUTPUT_DIR, f"{template_type}_{bcv}.html")
        generate(title, rows, template_type, output_filename)
        print(f"wrote {output_filename}")

    for filename in ["interlinear.css", "skolar.css"]:
        output_filename = os.path.join(OUTPUT_DIR, filename)
        shutil.copy(filename, output_filename)
        print(f"copied {output_filename}")
