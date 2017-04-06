#!/usr/bin/env python3

import os

from reader import fs, templates, morphgnt


OUTPUT_DIR = "output"

template = templates.load("template.html")


if __name__ == "__main__":
    fs.create_dir(OUTPUT_DIR)

    book_name = "John"
    book_num = 4
    chapter_num = 3

    verses = morphgnt.rows_by_verses_for_chapter(book_num, chapter_num)

    for i, (verse_num, rows) in enumerate(verses):
        output_filename = os.path.join(OUTPUT_DIR, f"{verse_num}.html")

        if i > 0:
            prev_file = os.path.join(OUTPUT_DIR, f"{verses[i - 1][0]}.html")
        else:
            prev_file = None

        if i < len(verses) - 1:
            next_file = os.path.join(OUTPUT_DIR, f"{verses[i + 1][0]}.html")
        else:
            next_file = None

        with open(output_filename, "w") as output:
            print(template.render(
                title=f"{book_name} {chapter_num}.{verse_num}",
                rows=[
                    {**row, "pos": morphgnt.pos(row), "parse": morphgnt.parse(row)}
                    for row in rows
                ],
                prev_file=prev_file,
                next_file=next_file,
            ), file=output)
        print(f"wrote {output_filename}")

    fs.copy_css(["interlinear.css", "pagination.css", "skolar.css"], OUTPUT_DIR)
    fs.copy_js(["toggle.js"], OUTPUT_DIR)
