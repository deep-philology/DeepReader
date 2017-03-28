import csv
import operator


def bcv(ref):
    if ref.count("|") == 2:
        book1, book2, cv = ref.split("|")
        book = book1 + book2
    else:
        book, cv = ref.split("|")
    c, v = cv.split(":")
    c = int(c)
    v = int(v)
    b = {
        "matthew": 1,
        "mark": 2,
        "luke": 3,
        "john": 4,
        "acts": 5,
        "romans": 6,
        "1corinthians": 7,
        "2corinthians": 8,
        "galatians": 9,
        "ephesians": 10,
        "philippians": 11,
        "colossians": 12,
        "1thessalonians": 13,
        "2thessalonians": 14,
        "1timothy": 15,
        "2timothy": 16,
        "titus": 17,
        "philemon": 18,
        "hebrews": 19,
        "james": 20,
        "1peter": 21,
        "2peter": 22,
        "1john": 23,
        "2john": 24,
        "3john": 25,
        "jude": 26,
        "revelation": 27,
    }[book.lower()]
    return f"{b:02d}{c:02d}{v:02d}"


def load_interlinear():

    entries = []
    with open("berean_tables.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            if row[1]:
                entries.append({
                    "sort": int(row[1]),
                    "bcv": bcv(row[7]),
                    "verse_num": int(row[8]),
                    "greek": row[12].strip(),
                    "english": row[14].strip(),
                })
    return entries


def get_verse(entries, bcv):
    return sorted(
        [entry for entry in load_interlinear() if entry["bcv"] == bcv],
        key=operator.itemgetter("sort")
    )
