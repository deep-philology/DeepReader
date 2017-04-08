#!/usr/bin/env python3

import os

from reader import fs, templates
from reader.pagination import paginate

from parse_tei2 import tei_chapters


OUTPUT_DIR = "output"

template = templates.load("chapter.html")


def chapter_filename(num_content):
    "takes tuple of (chapter_num, chapter_content)"
    if num_content:
        return os.path.join(OUTPUT_DIR, f"{num_content[0]}.html")


def generate(chapter, prev, nxt, output_filename):
    chapter_num, chapter_contents = chapter
    with open(output_filename, "w") as output:
        print(template.render(
            title=f"Histories 2.{chapter_num}",
            content=chapter_contents,
            prev_file=chapter_filename(prev),
            next_file=chapter_filename(nxt),
        ), file=output)


if __name__ == "__main__":
    fs.create_dir(OUTPUT_DIR)

    chapters = tei_chapters(os.path.join("data", "histories2.xml"))

    for prev, item, nxt in paginate(chapters):
        output_filename = chapter_filename(item)
        generate(item, prev, nxt, output_filename)
        print(f"wrote {output_filename}")

    fs.copy_files(["reader.css"], "css", OUTPUT_DIR)
