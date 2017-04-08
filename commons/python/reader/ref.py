import re

BOOK_NAMES = [
    # sblgnt file, paratext, osis, full
    ("Mt", "MAT", "Matt", "Matthew"),
    ("Mk", "MRK", "Mark", "Mark"),
    ("Lk", "LUK", "Mark", "Mark"),
    ("Jn", "JHN", "John", "John"),
    ("Ac", "ACT", "Acts", "Acts"),
    ("Ro", "ROM", "Rom", "Romans"),
    ("1Co", "1CO", "1Cor", "1 Corinthians"),
    ("2Co", "2CO", "2Cor", "2 Corinthians"),
    ("Ga", "GAL", "Gal", "Galatians"),
    ("Eph", "EPH", "Eph", "Ephesians"),
    ("Php", "PHP", "Phil", "Philippians"),
    ("Col", "COL", "Col", "Colossians"),
    ("1Th", "1TH", "1Thess", "1 Thessalonians"),
    ("2Th", "2TH", "2Thess", "2 Thessalonians"),
    ("1Ti", "1TI", "1Tim", "1 Timothy"),
    ("2Ti", "2TI", "2Tim", "2 Timothy"),
    ("Tit", "TIT", "Titus", "Titus"),
    ("Phm", "PHM", "Phlm", "Philemon"),
    ("Heb", "HEB", "Heb", "Hebrews"),
    ("Jas", "JAS", "Jas", "James"),
    ("1Pe", "1PE", "1Pet", "1 Peter"),
    ("2Pe", "2PE", "2Pet", "2 Peter"),
    ("1Jn", "1JN", "1John", "1 John"),
    ("2Jn", "2JN", "2John", "2 John"),
    ("3Jn", "3JN", "3John", "3 John"),
    ("Jud", "JUD", "Jude", "Jude"),
    ("Re", "REV", "Rev", "Revelation"),
]

BOOK_NAME_MAPPINGS = {
    name: i
    for i, name_set in enumerate(BOOK_NAMES, 1)
    for name in set(name_set)
}

BOOK_NAME_RE = "|".join(BOOK_NAME_MAPPINGS)

OSIS_NAME = [None, *[row[2] for row in BOOK_NAMES]]
FULL_NAME = [None, *[row[3] for row in BOOK_NAMES]]


class Verse:
    def __init__(self, book_num, chapter_num, verse_num):
        self.book_num = book_num
        self.chapter_num = chapter_num
        self.verse_num = verse_num

    @property
    def bcv(self):
        "returns a BBCCVV string for the verse"
        return f"{self.book_num:02d}{self.chapter_num:02d}{self.verse_num:02d}"

    @property
    def tup(self):
        "returns a (B, C, V) tuple of integers for the verse"
        return (self.book_num, self.chapter_num, self.verse_num)

    @property
    def title(self):
        "returns {FULL_NAME} {CHAPTER}.{VERSE} for the verse"
        book_name = FULL_NAME[self.book_num]
        return f"{book_name} {self.chapter_num}.{self.verse_num}"


VERSE_REF_RE = re.compile(
    rf"(?P<book>({BOOK_NAME_RE}))\s(?P<chapter>\d+)(:|.)(?P<verse>\d+)$"
)


def verse(txt):
    m = VERSE_REF_RE.match(txt)
    if not m:
        raise ValueError("can't parse verse reference")

    return Verse(
        BOOK_NAME_MAPPINGS[m["book"]],
        int(m["chapter"]),
        int(m["verse"])
    )


class Chapter:
    def __init__(self, book_num, chapter_num):
        self.book_num = book_num
        self.chapter_num = chapter_num

    @property
    def bc(self):
        "returns a BBCC string for the chapter"
        return f"{self.book_num:02d}{self.chapter_num:02d}"

    @property
    def tup(self):
        "returns a (B, C) tuple of integers for the chapter"
        return (self.book_num, self.chapter_num)

    @property
    def title(self):
        "returns {FULL_NAME} {CHAPTER} for the chapter"
        book_name = FULL_NAME[self.book_num]
        return f"{book_name} {self.chapter_num}"

    @property
    def filename(self):
        "returns filename-compatible string for chapter"
        book_name = OSIS_NAME[self.book_num]
        return book_name.replace(" ", "").lower() + f"_{self.chapter_num:02d}"

    def verse(self, verse_num):
        return Verse(self.book_num, self.chapter_num, verse_num)


CHAPTER_REF_RE = re.compile(
    rf"(?P<book>({BOOK_NAME_RE}))\s(?P<chapter>\d+)$"
)


def chapter(txt):
    m = CHAPTER_REF_RE.match(txt)
    if not m:
        raise ValueError("can't parse chapter reference")

    return Chapter(
        BOOK_NAME_MAPPINGS[m["book"]],
        int(m["chapter"])
    )


class Book:
    def __init__(self, num, osis, title):
        self.num = num
        self.osis = osis
        self.title = title

    @property
    def filename(self):
        "returns filename-compatible string for book"
        return self.osis.replace(" ", "").lower()


NT_BOOKS = [
    Book(index, osis, full)
    for index, (sblgnt, paratext, osis, full) in enumerate(BOOK_NAMES, 1)
]
