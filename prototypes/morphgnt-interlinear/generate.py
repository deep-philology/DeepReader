#!/usr/bin/env python3

import os

from reader import fs, templates, morphgnt


OUTPUT_DIR = "output"

template = templates.load("template.html")


def generate(title, book_num, chapter_num, verse_num, output_filename):

    rows = [
        {**row, "pos": morphgnt.pos(row), "parse": morphgnt.parse(row)}
        for row in morphgnt.rows_for_verse(book_num, chapter_num, verse_num)
    ]

    with open(output_filename, "w") as output:
        print(template.render(
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

    output_filename = os.path.join(OUTPUT_DIR, f"{book_num:02d}{chapter_num:02d}{verse_num:02d}.html")
    generate(title, book_num, chapter_num, verse_num, output_filename)
    print(f"wrote {output_filename}")

    fs.copy_css(["interlinear.css", "skolar.css"], OUTPUT_DIR)
    fs.copy_js(["toggle.js"], OUTPUT_DIR)
