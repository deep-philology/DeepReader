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


def generate(book_title, book_num, output_filename):

    book_content = rows_by_verses_by_chapters_for_book(book_num)

    with open(output_filename, "w") as output:
        template = env.get_template("template.html")
        print(template.render(
            book_title=book_title,
            book_content=book_content,
            render_pos=render_pos,
            render_parse=render_parse,
        ), file=output)


OUTPUT_DIR = "output"

BOOK_NAMES = [
    "Matthew", "Mark", "Luke", "John", "Acts", "Romans", "1 Corinthians",
    "2 Corinthians", "Galatians", "Ephesians", "Philippians", "Colossians",
    "1 Thessalonians", "2 Thessalonians", "1 Timothy", "2 Timothy", "Titus",
    "Philemon", "Hebrews", "James", "1 Peter", "2 Peter", "1 John", "2 John",
    "3 John", "Jude", "Revelation"
]

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)
    print(f"created {OUTPUT_DIR}")

for i, book_name in enumerate(BOOK_NAMES):
    output_filename = os.path.join(OUTPUT_DIR, f"{book_name.replace(' ', '').lower()}.html")
    generate(book_name, i + 1, output_filename)
    print(f"wrote {output_filename}")

for filename in ["sblgnt.css", "sblgnt.js", "index.html"]:
    output_filename = os.path.join(OUTPUT_DIR, filename)
    shutil.copy(filename, output_filename)
    print(f"copied {output_filename}")
