#!/usr/bin/env python3

import os

from pysblgnt import morphgnt_rows

from reader import fs, templates


OUTPUT_DIR = "output"

template = templates.load("template.html")


def pos(row):
    return row["ccat-pos"].strip("-")


def parse(row):
    if row["ccat-parse"][3] == "-":
        return row["ccat-parse"][4:].strip("-")
    elif row["ccat-parse"][3] == "N":
        return row["ccat-parse"][1:4]
    elif row["ccat-parse"][3] == "P":
        return row["ccat-parse"][1:4] + "." + row["ccat-parse"][4:7]
    elif row["ccat-parse"][3] in "DISO":
        return row["ccat-parse"][1:4] + "." + row["ccat-parse"][0] + row["ccat-parse"][5]


def generate(title, book_num, bcv, output_filename):

    rows = [
        {**row, "pos": pos(row), "parse": parse(row)}
        for row in morphgnt_rows(book_num)
        if row["bcv"] == bcv
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
    bcv = f"{book_num:02d}{chapter_num:02d}{verse_num:02d}"

    output_filename = os.path.join(OUTPUT_DIR, f"{bcv}.html")
    generate(title, book_num, bcv, output_filename)
    print(f"wrote {output_filename}")

    fs.copy_css(["interlinear.css", "skolar.css"], OUTPUT_DIR)
    fs.copy_js(["toggle.js"], OUTPUT_DIR)
