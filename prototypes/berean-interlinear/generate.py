#!/usr/bin/env python3

import os

from reader.berean import BereanInterlinear
from reader import fs, templates, ref


OUTPUT_DIR = "output"

templates = {
    name: templates.load("template.html", extra_dirs=[os.path.join("templates", name)])
    for name in ["plain", "hover", "toggle", "frequency"]
}


def generate(title, rows, template_type, output_filename):

    with open(output_filename, "w") as output:
        print(templates[template_type].render(
            title=title,
            rows=rows,
        ), file=output)


if __name__ == "__main__":
    fs.create_dir(OUTPUT_DIR)

    verse = ref.verse("John 3.16")

    interlinear = BereanInterlinear(os.path.join("data", "berean_tables.csv"))
    interlinear.load()

    rows = interlinear.get_verse(verse)

    for template_type in ["plain", "hover", "toggle", "frequency"]:
        output_filename = os.path.join(OUTPUT_DIR, f"{template_type}_{verse.bcv}.html")
        generate(verse.title, rows, template_type, output_filename)
        print(f"wrote {output_filename}")

    fs.copy_css(["interlinear.css", "skolar.css"], OUTPUT_DIR)
    fs.copy_js(["toggle.js", "frequency.js"], OUTPUT_DIR)
