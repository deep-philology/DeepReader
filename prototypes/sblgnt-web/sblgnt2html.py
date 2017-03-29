#!/usr/bin/env python

import os
import shutil

from jinja2 import Environment, FileSystemLoader

from render_parse_codes import render_pos, render_parse
from utils import rows_by_verses_by_chapters_for_book


env = Environment(
    loader=FileSystemLoader("."),
)
book_template = env.get_template("template.html")


def generate(book_title, book_num, output_filename):

    book_content = rows_by_verses_by_chapters_for_book(book_num)

    with open(output_filename, "w") as output:
        print(book_template.render(
            book_title=book_title,
            book_content=book_content,
            render_pos=render_pos,
            render_parse=render_parse,
        ), file=output)


OUTPUT_DIR = "output"

BOOK_NAMES = [
    "Matthew", "Mark", "Luke", "John", "Acts", "Romans", "1 Corinthians",
    "2 Corinthians", "Galatians", "Ephesians", "Philippians", "Colossians",
    "1 Thessalonians", "2 Thessalonians", "1 Timothy", "2 Timothy", "Titus",
    "Philemon", "Hebrews", "James", "1 Peter", "2 Peter", "1 John", "2 John",
    "3 John", "Jude", "Revelation"
]


if __name__ == "__main__":
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"created {OUTPUT_DIR}")

    for i, book_name in enumerate(BOOK_NAMES):
        output_filename = os.path.join(
            OUTPUT_DIR, f"{book_name.replace(' ', '').lower()}.html")
        generate(book_name, i + 1, output_filename)
        print(f"wrote {output_filename}")

    for filename in ["sblgnt.css", "sblgnt.js", "index.html"]:
        output_filename = os.path.join(OUTPUT_DIR, filename)
        shutil.copy(filename, output_filename)
        print(f"copied {output_filename}")
