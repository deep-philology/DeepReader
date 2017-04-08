#!/usr/bin/env python3

import os

from reader import fs, templates, morphgnt, ref
from reader.pagination import paginate


OUTPUT_DIR = "output"

template = templates.load("template.html")


def verse_filename(verse_rows):
    "takes tuple of (verse, rows)"
    if verse_rows:
        return os.path.join(OUTPUT_DIR, f"{verse_rows[0].verse_num}.html")


def generate(item, prev, nxt, output_filename):
    with open(output_filename, "w") as output:
        print(template.render(
            title=item[0].title,
            rows=[
                {**row, "pos": morphgnt.pos(row), "parse": morphgnt.parse(row)}
                for row in item[1]
            ],
            prev_file=verse_filename(prev),
            next_file=verse_filename(nxt),
        ), file=output)


if __name__ == "__main__":
    fs.create_dir(OUTPUT_DIR)

    chapter = ref.chapter("John 2")

    verses = morphgnt.rows_by_verses_for_chapter(chapter)

    for prev, item, nxt in paginate(verses):
        output_filename = verse_filename(item)
        generate(item, prev, nxt, output_filename)
        print(f"wrote {output_filename}")

    fs.copy_css(["interlinear.css", "pagination.css", "skolar.css"], OUTPUT_DIR)
    fs.copy_js(["toggle.js"], OUTPUT_DIR)
