#!/usr/bin/env python3

import os

from reader import fs, templates, morphgnt, ref


OUTPUT_DIR = "output"

template = templates.load("template.html")


if __name__ == "__main__":
    fs.create_dir(OUTPUT_DIR)

    chapter = ref.chapter("John 2")

    verses = morphgnt.rows_by_verses_for_chapter(chapter)

    for i, (verse, rows) in enumerate(verses):
        output_filename = os.path.join(OUTPUT_DIR, f"{verse.verse_num}.html")

        if i > 0:
            prev_file = os.path.join(OUTPUT_DIR, f"{verses[i - 1][0].verse_num}.html")
        else:
            prev_file = None

        if i < len(verses) - 1:
            next_file = os.path.join(OUTPUT_DIR, f"{verses[i + 1][0].verse_num}.html")
        else:
            next_file = None

        with open(output_filename, "w") as output:
            print(template.render(
                title=verse.title,
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
