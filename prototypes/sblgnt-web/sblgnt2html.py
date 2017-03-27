#!/usr/bin/env python

from pysblgnt import morphgnt_rows


def generate(book_title, book_num, output_filename, chapter_count):

    with open(output_filename, "w") as output:

        print(f"""
        <!doctype html>
        <html>
        <head>
        <title>{book_title}</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="sblgnt.css">
        </head>
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

        for row in morphgnt_rows(book_num):
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
            }[row["ccat-pos"]]
            person, tense, voice, mood, case, number, gender, degree = row["ccat-parse"]
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
            parse = " ".join(parse).strip()
            chapter = int(row["bcv"][2:4])
            verse = int(row["bcv"][4:])
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
            text, form, lemma = row["text"], row["norm"], row["lemma"]
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


generate("Matthew", 1, "matthew.html", 28)
generate("Mark", 2, "mark.html", 16)
generate("Luke", 3, "luke.html", 24)
generate("John", 4, "john.html", 21)
generate("Acts", 5, "acts.html", 28)
generate("Romans", 6, "romans.html", 16)
generate("1 Corinthians", 7, "1corinthians.html", 16)
generate("2 Corinthians", 8, "2corinthians.html", 13)
generate("Galatians", 9, "galatians.html", 6)
generate("Ephesians", 10, "ephesians.html", 6)
generate("Philippians", 11, "philippians.html", 4)
generate("Colossians", 12, "colossians.html", 4)
generate("1 Thessalonians", 13, "1thessalonians.html", 5)
generate("2 Thessalonians", 14, "2thessalonians.html", 3)
generate("1 Timothy", 15, "1timothy.html", 6)
generate("2 Timothy", 16, "2timothy.html", 4)
generate("Titus", 17, "titus.html", 3)
generate("Philemon", 18, "philemon.html", 1)
generate("Hebrews", 19, "hebrews.html", 13)
generate("James", 20, "james.html", 5)
generate("1 Peter", 21, "1peter.html", 5)
generate("2 Peter", 22, "2peter.html", 3)
generate("1 John", 23, "1john.html", 5)
generate("2 John", 24, "2john.html", 1)
generate("3 John", 25, "3john.html", 1)
generate("Jude", 26, "jude.html", 1)
generate("Revelation", 27, "revelation.html", 22)
