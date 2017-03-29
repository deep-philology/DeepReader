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


def render_person(row):
    return {
        "1": "1st person",
        "2": "2nd person",
        "3": "3rd person",
    }[row["ccat-parse"][0]]


def render_tense(row):
    return {
        "P": "present",
        "F": "future",
        "A": "aorist",
        "X": "perfect",
        "Y": "pluperfect",
        "I": "imperfect",
    }[row["ccat-parse"][1]]


def render_voice(row):
    return {
        "A": "active",
        "M": "middle",
        "P": "passive",
    }[row["ccat-parse"][2]]


def render_mood(row):
    return {
        "I": "indicative",
        "S": "subjunctive",
        "D": "imperative",
        "O": "optative",
    }[row["ccat-parse"][3]]


def render_case(row):
    return {
        "N": "nominative",
        "A": "accusative",
        "G": "genitive",
        "D": "dative",
        "V": "vocative",
        "-": "",
    }[row["ccat-parse"][4]]


def render_number(row):
    return {
        "S": "singular",
        "P": "plural",
        "-": "",
    }[row["ccat-parse"][5]]


def render_gender(row):
    return {
        "M": "masculine",
        "F": "feminine",
        "N": "neuter",
        "-": "",
    }[row["ccat-parse"][6]]


def render_degree(row):
    return {
        "C": "comparative",
        "S": "superlative",
        "-": "",
    }[row["ccat-parse"][7]]


def render_parse(row):
    parse = []
    if row["ccat-pos"] == "V-":
        if row["ccat-parse"][3] == "P":
            parse.append(render_tense(row))
            parse.append(render_voice(row))
            parse.append("participle")
            parse.append(render_case(row))
            parse.append(render_number(row))
            parse.append(render_gender(row))
        elif row["ccat-parse"][3] == "N":
            parse.append(render_tense(row))
            parse.append(render_voice(row))
            parse.append("infinitive")
        else:
            parse.append(render_tense(row))
            parse.append(render_voice(row))
            parse.append(render_mood(row))
            parse.append(render_person(row))
            parse.append(render_number(row))
    else:
        parse.append(render_case(row))
        parse.append(render_number(row))
        parse.append(render_gender(row))
        parse.append(render_degree(row))

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
    output_filename = os.path.join(
        OUTPUT_DIR, f"{book_name.replace(' ', '').lower()}.html")
    generate(book_name, i + 1, output_filename)
    print(f"wrote {output_filename}")

for filename in ["sblgnt.css", "sblgnt.js", "index.html"]:
    output_filename = os.path.join(OUTPUT_DIR, filename)
    shutil.copy(filename, output_filename)
    print(f"copied {output_filename}")
