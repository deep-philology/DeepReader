from pysblgnt import morphgnt_rows

from . import ref


def rows_for_verse(verse):
    book_num, chapter_num, verse_num = verse.tup

    rows = []

    for row in morphgnt_rows(book_num):
        c = int(row["bcv"][2:4])
        v = int(row["bcv"][4:6])

        if (c, v) == (chapter_num, verse_num):
            rows.append(row)

    return rows


def rows_by_verses_for_chapter(chapter):
    book_num, chapter_num = chapter.tup

    last_verse = 0
    verses = []
    rows = None

    for row in morphgnt_rows(book_num):
        c = int(row["bcv"][2:4])
        v = int(row["bcv"][4:6])

        if c == chapter_num:
            if v != last_verse:

                if rows:
                    verses.append(rows)
                rows = (chapter.verse(v), [])
                last_verse = v

            rows[1].append(row)

    verses.append(rows)

    return verses


def rows_by_verses_by_chapters_for_book(book_num):

    last_chapter = 0
    chapters = []
    verses = None
    rows = None

    for row in morphgnt_rows(book_num):
        c = int(row["bcv"][2:4])
        v = int(row["bcv"][4:6])

        if c != last_chapter:

            if verses:
                verses[1].append(rows)
                chapters.append(verses)

            chapter = ref.Chapter(book_num, c)
            verses = (chapter, [])
            rows = None
            last_chapter = c
            last_verse = 0

        if v != last_verse:
            if rows:
                verses[1].append(rows)
            rows = (chapter.verse(v), [])
            last_verse = v

        rows[1].append(row)

    verses[1].append(rows)
    chapters.append(verses)

    return chapters


def pos(row):
    return row["ccat-pos"].strip("-")


def parse(row):
    if row["ccat-parse"][3] == "-":
        return row["ccat-parse"][4:].strip("-")
    elif row["ccat-parse"][3] == "N":
        return row["ccat-parse"][1:4]
    elif row["ccat-parse"][3] == "P":
        return row["ccat-parse"][1:4] + "." + row["ccat-parse"][4:7]
    elif row["ccat-parse"][3] in "DISO":
        return row["ccat-parse"][1:4] + "." + row["ccat-parse"][0] + row["ccat-parse"][5]


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
