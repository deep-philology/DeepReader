#!/usr/bin/env python3

import os

from reader import fs, templates, morphgnt, ref


OUTPUT_DIR = "output"

template = templates.load("template.html")


def generate(verse, output_filename):

    rows = [
        {**row, "pos": morphgnt.pos(row), "parse": morphgnt.parse(row)}
        for row in morphgnt.rows_for_verse(verse)
    ]

    with open(output_filename, "w") as output:
        print(template.render(
            title=verse.title,
            rows=rows,
        ), file=output)


if __name__ == "__main__":
    fs.create_dir(OUTPUT_DIR)

    verse = ref.verse("John 3.16")

    output_filename = os.path.join(OUTPUT_DIR, f"{verse.bcv}.html")
    generate(verse, output_filename)
    print(f"wrote {output_filename}")

    fs.copy_css(["interlinear.css", "skolar.css"], OUTPUT_DIR)
    fs.copy_js(["toggle.js"], OUTPUT_DIR)
