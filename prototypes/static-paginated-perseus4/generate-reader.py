#!/usr/bin/env python3

import os
import shutil

from jinja2 import Environment, FileSystemLoader

from parse_tei2 import tei_chapters

env = Environment(
    loader=FileSystemLoader("."),
)
template = env.get_template("chapter.html")


OUTPUT_DIR = "output"


if __name__ == "__main__":
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"created {OUTPUT_DIR}")

    chapters = list(tei_chapters("histories2.xml"))

    for i in range(len(chapters)):
        chapter_num, chapter_content = chapters[i]
        output_filename = os.path.join(OUTPUT_DIR, f"{chapter_num}.html")

        if i > 0:
            prev_file = os.path.join(OUTPUT_DIR, f"{chapters[i - 1][0]}.html")
        else:
            prev_file = None

        if i < len(chapters) - 1:
            next_file = os.path.join(OUTPUT_DIR, f"{chapters[i + 1][0]}.html")
        else:
            next_file = None

        with open(output_filename, "w") as output:
            print(template.render(
                title=f"Histories 2.{chapter_num}",
                content=chapter_content,
                prev_file=prev_file,
                next_file=next_file,
            ), file=output)
        print(f"wrote {output_filename}")

    for filename in ["reader.css"]:
        output_filename = os.path.join(OUTPUT_DIR, filename)
        shutil.copy(filename, output_filename)
        print(f"copied {output_filename}")
