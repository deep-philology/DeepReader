#!/usr/bin/env python3

import os

from jinja2 import Environment, FileSystemLoader

from berean import load_interlinear, get_verse


env = Environment(
    loader=FileSystemLoader("."),
)
template = env.get_template("template.html")


def generate(title, bcv, output_filename):

    entries = load_interlinear()
    rows = get_verse(entries, bcv)

    with open(output_filename, "w") as output:
        print(template.render(
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

    output_filename = os.path.join(OUTPUT_DIR, f"{bcv}.html")
    generate(title, bcv, output_filename)
    print(f"wrote {output_filename}")
