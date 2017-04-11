import collections
import csv
import operator


def bcv(ref):
    """
    converts their Verse reference (column 8) to a six-character BBCCVV
    """
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


class BereanInterlinear:

    def __init__(self, filename):
        self.filename = filename
        self.entries = []
        self.strongs_count = collections.defaultdict(int)  # for frequency

    def load(self):
        with open(self.filename, newline="") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                if row[1]:
                    self.entries.append({
                        "sort": int(row[1]),
                        "bcv": bcv(row[7]),
                        "verse_num": int(row[8]),
                        "greek": row[12].strip(),
                        "english": row[14].strip(),
                        "strongs": int(row[19]),
                    })
                    self.strongs_count[int(row[19])] += 1

    def get_verse(self, verse):
        bcv = verse.bcv
        return sorted(
            [
                {**entry, "frequency": self.strongs_count[entry["strongs"]]}
                for entry in self.entries
                if entry["bcv"] == bcv
            ],
            key=operator.itemgetter("sort")
        )
