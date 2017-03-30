#!/usr/bin/env python3

import os

from jinja2 import Environment, FileSystemLoader
from lxml import etree

env = Environment(
    loader=FileSystemLoader("."),
)
template = env.get_template("chapter.html")


def tei_chapters(filename):
    with open(filename) as f:
        tree = etree.parse(f)
        for book in tree.xpath("/TEI.2/text/body/div1[@type='Book']"):
            chapter_num = None
            chapter_content = []
            for child in book.xpath("p")[0]:  # hack?
                if child.tag == "milestone":
                    if child.attrib["unit"] == "chapter":
                        if chapter_content:
                            yield chapter_num, "".join(chapter_content).strip()
                            chapter_content = []
                        chapter_num = child.attrib["n"]
                    elif child.attrib["unit"] == "section":
                        chapter_content.append(f"""<p><span class="section">{child.attrib["n"]}</span> """)
                    else:
                        pass
                    if child.tail:
                        chapter_content.append(child.tail)
                elif child.tag == "note":
                    if child.tail:
                        chapter_content.append(child.tail)
                else:
                    chapter_content.append(etree.tostring(child, encoding="unicode", method="text"))
        yield chapter_num, "".join(chapter_content).strip()


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
