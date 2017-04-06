from pysblgnt import morphgnt_rows


def rows_for_verse(book_num, chapter_num, verse_num):
    rows = []

    for row in morphgnt_rows(book_num):
        chapter = int(row["bcv"][2:4])
        verse = int(row["bcv"][4:6])

        if chapter == chapter_num and verse == verse_num:
            rows.append(row)

    return rows


def rows_by_verses_for_chapter(book_num, chapter_num):
    last_verse = 0
    verses = []
    rows = None

    for row in morphgnt_rows(book_num):
        chapter = int(row["bcv"][2:4])
        verse = int(row["bcv"][4:6])

        if chapter == chapter_num:
            if verse != last_verse:

                if rows:
                    verses.append(rows)
                rows = (verse, [])
                last_verse = verse

            rows[1].append(row)

    verses.append(rows)

    return verses


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
