import os

from pysblgnt import morphgnt_rows


def generate(book_title, book_num, output_filename):

    with open(output_filename, "w") as output:
        print(f"""<html>
  <head>
    <meta charset="utf-8">
    <title>Online Reader</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha512-dTfge/zgoMYpP7QbHy4gWMEGsbsdZeCXz7irItjcC3sPUFtf0kuFbDz/ixG7ArTxmDjLXDmezHubeNikyKGVyQ==" crossorigin="anonymous">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=PT+Sans">
    <link rel="stylesheet" href="skolar.css">
    <link rel="stylesheet" href="reader.css">
  </head>
  <body>
    <div class="container">
      <div class="row">
        <div class="col-md-2">
        """, file=output)
        print(f"""<div class="toggles">
            <span class="toggle" data-target="show-verses"><span class="show-verses">&#x25CF;</span>&nbsp;show verse numbers</span>
            <hr>
            <span class="toggle" data-target="larger-text"><span class="larger-text">&#x25CF;</span>&nbsp;larger text</span>
            <span class="toggle" data-target="extra-line-height"><span class="extra-line-height">&#x25CF;</span>&nbsp;extra line height</span>
            <span class="toggle" data-target="extra-word-spacing"><span class="extra-word-spacing">&#x25CF;</span>&nbsp;extra word spacing</span>
            <hr>
            <span class="toggle" data-target="case-N"><span class="case-N">&#x25CF;</span>&nbsp;nominative</span>
            <span class="toggle" data-target="case-G"><span class="case-G">&#x25CF;</span>&nbsp;genitive</span>
            <span class="toggle" data-target="case-D"><span class="case-D">&#x25CF;</span>&nbsp;dative</span>
            <span class="toggle" data-target="case-A"><span class="case-A">&#x25CF;</span>&nbsp;accusative</span>
            <hr>
            <span class="toggle" data-target="ind"><span class="pos-V- mood-I">&#x25CF;</span>&nbsp;indicative</span>
            <span class="toggle" data-target="part"><span class="pos-V- mood-P">&#x25CF;</span>&nbsp;participle</span>
            <span class="toggle" data-target="inf"><span class="pos-V- mood-N">&#x25CF;</span>&nbsp;infinitive</span>
            <hr>
            <span class="toggle" data-target="pos-D"><span class="pos-D-">&#x25CF;</span>&nbsp;adverb</span>
            <span class="toggle" data-target="pos-C"><span class="pos-C-">&#x25CF;</span>&nbsp;conjunction</span>
          </div>
        </div>
        <div class="col-md-10">
          <div class="text">
        """, file=output)

        last_verse = 0

        for row in morphgnt_rows(book_num):
            verse = int(row["bcv"][4:])

            print("<span>", file=output)

            if verse != last_verse:
                print(f"""<span class="verse">{verse}&nbsp;</span>""", file=output)
                last_verse = verse

            word = row["word"]
            text = row["text"]
            pos = row["ccat-pos"]
            mood = row["ccat-parse"][3]
            case = row["ccat-parse"][4]
            before, after = text[:text.index(word)], text[text.index(word) + len(word):]
            print(f"""{before}<span class="pos-{pos} mood-{mood} case-{case}">{word}</span>{after}""", file=output)

            print("</span>", file=output)

        print(f"""</div>
        </div>
      </div>
    </div>
    <script src="http://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script src="reader.js"></script>
  </body>
</html>
        """, file=output)


if not os.path.exists("output"):
    os.makedirs("output")
    print("created directory")


generate("2 John", 24, "output/2john.html")
