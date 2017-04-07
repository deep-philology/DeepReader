#!/usr/bin/env python

import os

from reader import fs, templates, morphgnt

from render_parse_codes import render_pos, render_parse


book_template = templates.load("template.html")


def generate(book_title, book_num, output_filename):

    book_content = morphgnt.rows_by_verses_by_chapters_for_book(book_num)

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
    fs.create_dir(OUTPUT_DIR)

    for i, book_name in enumerate(BOOK_NAMES):
        output_filename = os.path.join(
            OUTPUT_DIR, f"{book_name.replace(' ', '').lower()}.html")
        generate(book_name, i + 1, output_filename)
        print(f"wrote {output_filename}")

    fs.copy_files(["sblgnt.css", "sblgnt.js", "index.html"], os.curdir, OUTPUT_DIR)
