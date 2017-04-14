#!/usr/bin/env python

import os

from reader import fs, templates, morphgnt, ref


OUTPUT_DIR = "output"

index_template = templates.load("index.html")
book_template = templates.load("template.html")


def generate(book, output_filename):

    chapters = morphgnt.rows_by_verses_by_chapters_for_book(book.num)

    with open(output_filename, "w") as output:
        print(book_template.render(
            book_title=book.title,
            chapters=chapters,
            render_pos=morphgnt.render_pos,
            render_parse=morphgnt.render_parse,
        ), file=output)


if __name__ == "__main__":
    fs.create_dir(OUTPUT_DIR)

    index_filename = os.path.join(OUTPUT_DIR, "index.html")
    with open(index_filename, "w") as output:
        print(index_template.render(books=ref.NT_BOOKS), file=output)
    print(f"wrote {index_filename}")

    for book in ref.NT_BOOKS:
        output_filename = os.path.join(OUTPUT_DIR, f"{book.filename}.html")
        generate(book, output_filename)
        print(f"wrote {output_filename}")

    fs.copy_files(["sblgnt.css"], "css", OUTPUT_DIR)
    fs.copy_files(["sblgnt.js"], "js", OUTPUT_DIR)
