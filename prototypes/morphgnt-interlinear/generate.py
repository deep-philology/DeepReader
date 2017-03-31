#!/usr/bin/env python3

import os
# import shutil

from jinja2 import Environment, FileSystemLoader
from pysblgnt import morphgnt_rows


env = Environment(
    loader=FileSystemLoader("."),
)
template = env.get_template("template.html")


def generate(title, book_num, bcv, output_filename):

    rows = [row for row in morphgnt_rows(book_num) if row["bcv"] == bcv]

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
    generate(title, book_num, bcv, output_filename)
    print(f"wrote {output_filename}")

    # for filename in ["skolar.css", "reader.css", "reader.js"]:
    #     output_filename = os.path.join(OUTPUT_DIR, filename)
    #     shutil.copy(filename, output_filename)
    #     print(f"copied {output_filename}")
