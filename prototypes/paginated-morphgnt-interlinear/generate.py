#!/usr/bin/env python3

import os

from reader import fs, templates, morphgnt, ref


OUTPUT_DIR = "output"

template = templates.load("template.html")


def verse_filename(verse):
    if verse:
        return os.path.join(OUTPUT_DIR, f"{verse.verse_num}.html")


def generate(verse, rows, prev_verse, next_verse, output_filename):
    with open(output_filename, "w") as output:
        print(template.render(
            title=verse.title,
            rows=[
                {**row, "pos": morphgnt.pos(row), "parse": morphgnt.parse(row)}
                for row in rows
            ],
            prev_file=verse_filename(prev_verse),
            next_file=verse_filename(next_verse),
        ), file=output)


if __name__ == "__main__":
    fs.create_dir(OUTPUT_DIR)

    chapter = ref.chapter("John 2")

    verses = morphgnt.rows_by_verses_for_chapter(chapter)

    for i, (verse, rows) in enumerate(verses):

        prev_verse = verses[i - 1][0] if i > 0 else None
        next_verse = verses[i + 1][0] if i < len(verses) - 1 else None

        output_filename = verse_filename(verse)
        generate(verse, rows, prev_verse, next_verse, output_filename)
        print(f"wrote {output_filename}")

    fs.copy_css(["interlinear.css", "pagination.css", "skolar.css"], OUTPUT_DIR)
    fs.copy_js(["toggle.js"], OUTPUT_DIR)
