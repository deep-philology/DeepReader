#!/usr/bin/env python

import os

from reader import fs, templates, morphgnt, ref


OUTPUT_DIR = "output"

template = templates.load("template.html")


def generate(chapter, output_filename):

    verses = morphgnt.rows_by_verses_for_chapter(chapter)

    with open(output_filename, "w") as output:
        print(template.render(
            verses=[
                (v, [
                    {
                        **row,
                        "before": morphgnt.before(row),
                        "after": morphgnt.after(row)
                    } for row in rows
                ]) for (v, rows) in verses
            ]), file=output)


if __name__ == "__main__":
    fs.create_dir(OUTPUT_DIR)

    chapter = ref.chapter("2 John 1")

    output_filename = os.path.join(OUTPUT_DIR, f"{chapter.filename}.html")
    generate(chapter, output_filename)
    print(f"wrote {output_filename}")

    fs.copy_css(["skolar.css"], OUTPUT_DIR)
    fs.copy_files(["reader.css"], "css", OUTPUT_DIR)
    fs.copy_files(["reader.js"], "js", OUTPUT_DIR)
