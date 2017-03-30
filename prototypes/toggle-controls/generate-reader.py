#!/usr/bin/env python

import os
import shutil

from jinja2 import Environment, FileSystemLoader

from utils import rows_by_verses_by_chapters_for_book


env = Environment(
    loader=FileSystemLoader("."),
)
template = env.get_template("template.html")


def before(row):
    word = row["word"]
    text = row["text"]
    return text[:text.index(word)]


def after(row):
    word = row["word"]
    text = row["text"]
    return text[text.index(word) + len(word):]


def generate(book_num, chapter_num, output_filename):

    book_content = rows_by_verses_by_chapters_for_book(book_num)
    verses = book_content[chapter_num - 1][1]

    with open(output_filename, "w") as output:
        print(template.render(
            verses=verses,
            before=before,
            after=after,
        ), file=output)


OUTPUT_DIR = "output"


if __name__ == "__main__":
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"created {OUTPUT_DIR}")

    book_name = "2 John"
    book_num = 24
    chapter_num = 1

    output_filename = os.path.join(
        OUTPUT_DIR, f"{book_name.replace(' ', '').lower()}_{chapter_num:02d}.html")
    generate(book_num, chapter_num, output_filename)
    print(f"wrote {output_filename}")

    for filename in ["skolar.css", "reader.css", "reader.js"]:
        output_filename = os.path.join(OUTPUT_DIR, filename)
        shutil.copy(filename, output_filename)
        print(f"copied {output_filename}")
