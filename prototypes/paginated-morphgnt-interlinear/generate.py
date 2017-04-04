#!/usr/bin/env python3

import os
import shutil

from jinja2 import Environment, FileSystemLoader
from utils import rows_by_verses_by_chapters_for_book


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


COMMONS_DIR = "../../commons"
OUTPUT_DIR = "output"


if __name__ == "__main__":
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"created {OUTPUT_DIR}")

    book_name = "John"
    book_num = 4

    chapters = rows_by_verses_by_chapters_for_book(book_num)

    chapter_num, verses = chapters[2]

    for i in range(len(verses)):
        verse_num, rows = verses[i]
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
                    {**row, "pos": pos(row), "parse": parse(row)}
                    for row in rows
                ],
                prev_file=prev_file,
                next_file=next_file,
            ), file=output)
        print(f"wrote {output_filename}")

    for filename in ["interlinear.css", "pagination.css", "skolar.css"]:
        input_filename = os.path.join(COMMONS_DIR, "css", filename)
        output_filename = os.path.join(OUTPUT_DIR, filename)
        shutil.copy(input_filename, output_filename)
        print(f"copied {output_filename}")
