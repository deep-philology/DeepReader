#!/usr/bin/env python3

from berean import load_interlinear, get_verse

def output(title, bcv):
    print(f"""
<html>
<head>
<title>{title}</title>
<meta http-equiv="Content-type" content='text/html; charset="utf-8"' />
    """)
    print("""
<style>
div.unit {
 float: left;
 margin-bottom: 1em;
 color: black;
}
p.gk {
 font-size: 16pt;
 margin: 0em;
 padding: 0em 0.5em;
}
p.en {
 font-size: 10pt;
 font-family: sans-serif;
 color: gray;
 margin: 0em;
 padding: 0em 1em;
}
</style>
    """)
    print(f"""
</head>
<body>
<h1>{title}</h1>
    """)

    entries = load_interlinear()
    for row in get_verse(entries, bcv):
        greek = row["greek"]
        english = row["english"]
        print(f"""<div class="unit"><p class="gk">{greek}</p><p class="en">{english}</p></div>""")

    print("""
    </body>
    </html>
    """)


output("John 3.16", "040316")
