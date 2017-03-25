#!/usr/bin/env python


def generate(book_title, input_filename, output_filename, chapter_count):

    with open(output_filename, "w") as output:

        print(f"""
        <!doctype html>
        <html>
            <head>
                <title>{book_title}</title>
        """, file=output)

        print("""
                <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
                <style>
                    body {
                        font-family: sans-serif;
                        margin: 0;
                    }
                    h1 {
                        margin-top: 50px;
                        margin-left: 210px;
                    }
                    .header {
                        margin: 0;
                        position: fixed;
                        top: 0px;
                    }
                    .book {
                        padding: 5px 10px;
                        font-size: 12pt;
                        font-weight: bold;
                    }
                    .nav {
                        margin: 0;
                        padding: 0;
                        list-style: none;
                        width: 160px;
                        font-weight: 100;
                        font-size: 10pt;
                        text-align: right;
                    }
                    .nav li.active a {
                        background: #EEE;
                        font-weight: bold;
                    }
                    .nav a {
                        padding: 5px 10px;
                        display: block;
                        text-decoration: none;
                        color: black;
                    }
                    .nav a:hover {
                        font-weight: bold;
                    }
                    .text {
                        width: 450px;
                        margin: 0 250px;
                    }
                    .gk {
                        font-size: 16pt;
                        color: #444;
                        line-height: 32pt;
                        font-family: sans-serif;
                    }
                    .word {
                        text-decoration: none;
                        color: inherit;
                    }
                    .lowlight {
                        color: #999;
                    }
                    .highlight {
                        color: black;
                    }
                    .verse_num {
                        color: #999;
                        font-size: 10pt;
                        position: absolute;
                        left: 200px;
                        padding: 0 20px;
                        text-decoration: none;
                    }
                    .verse_num:hover {
                        color: #000;
                    }

                    .verse:target {
                        background: #FF6;
                    }
                    .analysis {
                        color: black;
                        min-width: 200px;
                        position: absolute;
                        left: 750px;
                        background: #F7F7F7;
                        padding: 4px 8px;
                    }
                    .analysis .form {
                        font-weight: bold;
                        font-size: 16pt;
                        line-height: 16pt;
                    }
                    .analysis .pos {
                        color: #999;
                        font-size: 10pt;
                        line-height: 10pt;
                    }
                    .analysis .parse {
                        color: #999;
                        font-size: 10pt;
                        line-height: 10pt;
                        font-style: italic;
                    }
                    .analysis .lemma {
                        font-size: 12pt;
                        line-height: 16pt;
                    }
                    .word:hover {
                        background: #FF6;
                        color: black;
                    }
                    .book_title {
                        font-weight: bold;
                    }
                    .site_title {
                        margin-top: 20px;
                        text-align: right;
                    }
                    .site_title a {
                        text-decoration: none;
                        color: black;
                        font-weight: bold;
                    }
                    .site_title a:hover {
                        color: #666;
                    }
                </style>
            </head>
        """, file=output)

        print(f"""
            <body>
                <div id="chapter-nav" class="header">
                    <div class="site_title"><a href="./">MorphGNT SBLGNT</a></div>
                    <ul class="nav">
                    <li class="book_title">{book_title}</li>
        """, file=output)

        for chapter in range(1, chapter_count + 1):
            print(f"""<li><a href="#chapter-{chapter}">{chapter}</a></li>""", file=output)

        print(f"""
                    </ul>
                </div>
                <h1>{book_title}</h1>
                <div class="text gk" id="text">
        """, file=output)

        last_verse = 0
        last_chapter = 0

        for line in open(input_filename):
            bcv, pos, parse, text, norm, form, lemma = line.strip().split()
            pos = {
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
                "RI": "interoggative/indefinite pronoun",
                "X-": "particle",
                "I-": "interjection",
            }[pos]
            person, tense, voice, mood, case, number, gender, degree = parse
            parse = []
            if pos == "verb":
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
            parse = " ".join(parse)
            chapter = int(bcv[2:4])
            verse = int(bcv[4:])
            cv = f"{chapter}-{verse}"
            if chapter != last_chapter:
                if last_chapter:
                    print("""</span>""", file=output)
                    print("""</div>""", file=output)
                print(f"""<div id="chapter-{chapter}" class="chapter">""", file=output)
                last_chapter = chapter
                last_verse = 0
            if verse != last_verse:
                if last_verse:
                    print("""</span>""", file=output)
                print(f"""<a href="#verse-{cv}" class="verse_num" data-verse="{cv}">{verse}</a>""", file=output)
                last_verse = verse
                print(f"""<span class="verse" id="verse-{cv}">""", file=output)
            print(f"""<a href="#" class="word" data-form="{form}" data-pos="{pos}" data-parse="{parse}" data-lemma="{lemma}">{text}</a>""", file=output)

        print("""
                    </span>
                    </div>
                </div>
                <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>
                <script>
                    $(function() {
                        var positions = [];
                        $(".chapter").each(function(i, e) {
                            positions[positions.length] = {
                                start: $(e).offset().top,
                                end: $(e).offset().top + $(e).height(),
                                id: $(e).attr("id"),
                                selected: null
                            }
                        });
                        function update() {
                            var window_start = $(window).scrollTop();
                            var window_end = window_start + $(window).height();

                            for (var i=0; i<positions.length; i++) {
                                if (window_start < positions[i].end && window_end > positions[i].start) {
                                    if (!positions[i].selected) {
                                        $("a[href=#" + positions[i].id + "]").parent().addClass("active");
                                        positions[i].selected = true;
                                    }
                                } else {
                                    if (positions[i].selected) {
                                        $("a[href=#" + positions[i].id + "]").parent().removeClass("active");
                                        positions[i].selected = false;
                                    }
                                }
                            }
                        }
                        $(window).bind("scroll", update);
                        $(window).bind("resize", update);
                        update();
                        $(".verse_num").hover(
                            function() {
                                $("#text").addClass("lowlight");
                                var verse = $(this).data("verse");
                                $("#verse-" + verse).addClass("highlight");
                            },
                            function() {
                                $("#text").removeClass("lowlight");
                                var verse = $(this).data("verse");
                                $("#verse-" + verse).removeClass("highlight");
                            }
                        );
                        $(".word").hover(
                            function() {
                                var form = $(this).data("form");
                                var pos = $(this).data("pos")
                                var parse = $(this).data("parse");
                                var lemma = $(this).data("lemma");
                                $(this).after('<span class="analysis"><div class="form">' + form + '</div><div class="pos">' + pos + '</div><div class="parse">' + parse + '</div><div class="lemma">' + lemma + '</div></span>');
                            },
                            function() {
                                $(".analysis").remove();
                            }
                        )
                    });
                </script>
            </body>
        </html>
        """, file=output)

    assert chapter == chapter_count, chapter


# generate("Matthew", "../../../../morphgnt/sblgnt/61-Mt-morphgnt.txt", "matthew.html", 28)
# generate("Mark", "../../../../morphgnt/sblgnt/62-Mk-morphgnt.txt", "mark.html", 16)
# generate("Luke", "../../../../morphgnt/sblgnt/63-Lk-morphgnt.txt", "luke.html", 24)
generate("John", "../../../../morphgnt/sblgnt/64-Jn-morphgnt.txt", "john.html", 21)
# generate("Acts", "../../../../morphgnt/sblgnt/65-Ac-morphgnt.txt", "acts.html", 28)
# generate("Romans", "../../../../morphgnt/sblgnt/66-Ro-morphgnt.txt", "romans.html", 16)
# generate("1 Corinthians", "../../../../morphgnt/sblgnt/67-1Co-morphgnt.txt", "1corinthians.html", 16)
# generate("2 Corinthians", "../../../../morphgnt/sblgnt/68-2Co-morphgnt.txt", "2corinthians.html", 13)
# generate("Galatians", "../../../../morphgnt/sblgnt/69-Ga-morphgnt.txt", "galatians.html", 6)
# generate("Ephesians", "../../../../morphgnt/sblgnt/70-Eph-morphgnt.txt", "ephesians.html", 6)
# generate("Philippians", "../../../../morphgnt/sblgnt/71-Php-morphgnt.txt", "philippians.html", 4)
# generate("Colossians", "../../../../morphgnt/sblgnt/72-Col-morphgnt.txt", "colossians.html", 4)
# generate("1 Thessalonians", "../../../../morphgnt/sblgnt/73-1Th-morphgnt.txt", "1thessalonians.html", 5)
# generate("2 Thessalonians", "../../../../morphgnt/sblgnt/74-2Th-morphgnt.txt", "2thessalonians.html", 3)
# generate("1 Timothy", "../../../../morphgnt/sblgnt/75-1Ti-morphgnt.txt", "1timothy.html", 6)
# generate("2 Timothy", "../../../../morphgnt/sblgnt/76-2Ti-morphgnt.txt", "2timothy.html", 4)
# generate("Titus", "../../../../morphgnt/sblgnt/77-Tit-morphgnt.txt", "titus.html", 3)
# generate("Philemon", "../../../../morphgnt/sblgnt/78-Phm-morphgnt.txt", "philemon.html", 1)
# generate("Hebrews", "../../../../morphgnt/sblgnt/79-Heb-morphgnt.txt", "hebrews.html", 13)
# generate("James", "../../../../morphgnt/sblgnt/80-Jas-morphgnt.txt", "james.html", 5)
# generate("1 Peter", "../../../../morphgnt/sblgnt/81-1Pe-morphgnt.txt", "1peter.html", 5)
# generate("2 Peter", "../../../../morphgnt/sblgnt/82-2Pe-morphgnt.txt", "2peter.html", 3)
# generate("1 John", "../../../../morphgnt/sblgnt/83-1Jn-morphgnt.txt", "1john.html", 5)
# generate("2 John", "../../../../morphgnt/sblgnt/84-2Jn-morphgnt.txt", "2john.html", 1)
# generate("3 John", "../../../../morphgnt/sblgnt/85-3Jn-morphgnt.txt", "3john.html", 1)
# generate("Jude", "../../../../morphgnt/sblgnt/86-Jud-morphgnt.txt", "jude.html", 1)
# generate("Revelation", "../../../../morphgnt/sblgnt/87-Re-morphgnt.txt", "revelation.html", 22)
