#!/usr/bin/env python

import os
import shutil

from jinja2 import Environment, FileSystemLoader
from pysblgnt import morphgnt_rows


def render_pos(row):
    return {
        "RA": "article",
        "A-": "adjective",
        "N-": "noun",
        "C-": "conjunction",
        "RP": "personal pronoun",
        "RR": "relative pronoun",
        "V-": "verb",
        "P-": "preposition",
        "D-": "adverb",
        "RD": "demonstrative",
        "RI": "interogative/indefinite pronoun",
        "X-": "particle",
        "I-": "interjection",
    }[row["ccat-pos"]]


def render_parse(row):
    pos = row["ccat-pos"]
    person, tense, voice, mood, case, number, gender, degree = row["ccat-parse"]
    parse = []
    if pos == "V-":
        if mood == "P":
            parse.append({
                "P": "present",
                "A": "aorist",
                "X": "perfect",
                "F": "future",
            }[tense])
            parse.append({
                "A": "active",
                "M": "middle",
                "P": "passive",
            }[voice])
            parse.append("participle")
            parse.append({
                "N": "nominative",
                "A": "accusative",
                "G": "genitive",
                "D": "dative",
                "V": "vocative",
                "-": "",
            }[case])
            parse.append({
                "S": "singular",
                "P": "plural",
                "-": "",
            }[number])
            parse.append({
                "M": "masculine",
                "F": "feminine",
                "N": "neuter",
                "-": "",
            }[gender])
        elif mood == "N":
            parse.append({
                "P": "present",
                "A": "aorist",
                "X": "perfect",
                "F": "future",
            }[tense])
            parse.append({
                "A": "active",
                "M": "middle",
                "P": "passive",
            }[voice])
            parse.append("infinitive")
        else:
            parse.append({
                "P": "present",
                "F": "future",
                "A": "aorist",
                "X": "perfect",
                "Y": "pluperfect",
                "I": "imperfect",
            }[tense])
            parse.append({
                "A": "active",
                "M": "middle",
                "P": "passive",
            }[voice])
            parse.append({
                "I": "indicative",
                "S": "subjunctive",
                "D": "imperative",
                "O": "optative",
            }[mood])
            parse.append({
                "1": "1st person",
                "2": "2nd person",
                "3": "3rd person",
            }[person])
            parse.append({
                "S": "singular",
                "P": "plural",
                "-": "",
            }[number])
    else:
        parse.append({
            "N": "nominative",
            "A": "accusative",
            "G": "genitive",
            "D": "dative",
            "V": "vocative",
            "-": "",
        }[case])
        parse.append({
            "S": "singular",
            "P": "plural",
            "-": "",
        }[number])
        parse.append({
            "M": "masculine",
            "F": "feminine",
            "N": "neuter",
            "-": "",
        }[gender])
        parse.append({
            "C": "comparative",
            "S": "superlative",
            "-": "",
        }[degree])

    return " ".join(parse).strip()


env = Environment(
    loader=FileSystemLoader("."),
)


def rows_by_verses_by_chapters_for_book(book_num):

    last_chapter = 0
    chapters = []
    verses = None
    rows = None

    for row in morphgnt_rows(book_num):
        chapter = int(row["bcv"][2:4])
        verse = int(row["bcv"][4:6])

        if chapter != last_chapter:

            if verses:
                verses[1].append(rows)
                chapters.append(verses)

            verses = (chapter, [])
            rows = None
            last_chapter = chapter
            last_verse = 0

        if verse != last_verse:
            if rows:
                verses[1].append(rows)
            rows = (verse, [])
            last_verse = verse

        rows[1].append(row)

    verses[1].append(rows)
    chapters.append(verses)

    return chapters


def generate(book_title, book_num, output_filename, chapter_count):

    with open(output_filename, "w") as output:
        template = env.get_template("template.html")
        print(template.render(
            book_title=book_title,
            chapter_count=chapter_count,
            book=rows_by_verses_by_chapters_for_book(book_num),
            render_pos=render_pos,
            render_parse=render_parse,
        ), file=output)

    print(f"wrote {output_filename}")


if not os.path.exists("output"):
    os.makedirs("output")
    print("created directory")

generate("Matthew", 1, "output/matthew.html", 28)
generate("Mark", 2, "output/mark.html", 16)
generate("Luke", 3, "output/luke.html", 24)
generate("John", 4, "output/john.html", 21)
generate("Acts", 5, "output/acts.html", 28)
generate("Romans", 6, "output/romans.html", 16)
generate("1 Corinthians", 7, "output/1corinthians.html", 16)
generate("2 Corinthians", 8, "output/2corinthians.html", 13)
generate("Galatians", 9, "output/galatians.html", 6)
generate("Ephesians", 10, "output/ephesians.html", 6)
generate("Philippians", 11, "output/philippians.html", 4)
generate("Colossians", 12, "output/colossians.html", 4)
generate("1 Thessalonians", 13, "output/1thessalonians.html", 5)
generate("2 Thessalonians", 14, "output/2thessalonians.html", 3)
generate("1 Timothy", 15, "output/1timothy.html", 6)
generate("2 Timothy", 16, "output/2timothy.html", 4)
generate("Titus", 17, "output/titus.html", 3)
generate("Philemon", 18, "output/philemon.html", 1)
generate("Hebrews", 19, "output/hebrews.html", 13)
generate("James", 20, "output/james.html", 5)
generate("1 Peter", 21, "output/1peter.html", 5)
generate("2 Peter", 22, "output/2peter.html", 3)
generate("1 John", 23, "output/1john.html", 5)
generate("2 John", 24, "output/2john.html", 1)
generate("3 John", 25, "output/3john.html", 1)
generate("Jude", 26, "output/jude.html", 1)
generate("Revelation", 27, "output/revelation.html", 22)

shutil.copy("sblgnt.css", "output/sblgnt.css")
shutil.copy("sblgnt.js", "output/sblgnt.js")
shutil.copy("index.html", "output/index.html")
