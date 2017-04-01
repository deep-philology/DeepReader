#!/usr/bin/env python3

import os
import shutil

from jinja2 import Environment, FileSystemLoader
from pysblgnt import morphgnt_rows


env = Environment(
    loader=FileSystemLoader("templates"),
)
template = env.get_template("template.html")


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

    for filename in ["interlinear.css", "skolar.css"]:
        input_filename = os.path.join("css", filename)
        output_filename = os.path.join(OUTPUT_DIR, filename)
        shutil.copy(input_filename, output_filename)
        print(f"copied {output_filename}")
