#!/usr/bin/env python3

import os

from reader import fs, templates

from parse_tei2 import tei_chapters


OUTPUT_DIR = "output"

template = templates.load("chapter.html")


if __name__ == "__main__":
    fs.create_dir(OUTPUT_DIR)

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

    fs.copy_files(["reader.css"], os.curdir, OUTPUT_DIR)
