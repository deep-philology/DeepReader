#!/usr/bin/env python3

from lxml import etree


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
