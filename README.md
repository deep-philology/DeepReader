# online-reader

At the moment, this is mostly an attempt to generalise one-off prototypes of Greek New Testament reading environments I've previously built over the last 11 years or so into code for generating those prototypes with arbitrary text (appropriately annotated).

There are, however, also early experiments with vue.js for more dynamic, modular readers.

The best place to start is the various prototypes that statically generate HTML, demos of which are linked to below.

The goal is for this project to be the basis for lots of different types of online and mobile reading environments with multiple technology architectures. This ranges in feature scope from basic ebook-style reading to a rich, modular platform for parallel texts, linguistic annotation, and integrated language learning tools.

I'm working, in particular, with texts and annotations from https://github.com/biblicalhumanities and https://github.com/perseusdl but this project is potentially much more general than that, and I'm interested in collaborating with anyone interested in online reading environments.

## Statically-generated prototypes

These are all programmatically generated so, even though the demos are sometimes only for a single verse, chapter, or book, they can be run on arbitrary texts with appropriate annotation.


### Interlinears for arbitrary verse using Berean interlinear

**Demo** (John 3.16): [plain](https://jtauber.github.io/online-reader/berean-interlinear/plain_040316.html) [hover](https://jtauber.github.io/online-reader/berean-interlinear/hover_040316.html) [toggle](https://jtauber.github.io/online-reader/berean-interlinear/toggle_040316.html) [frequency](https://jtauber.github.io/online-reader/berean-interlinear/frequency_040316.html)

**Code**: [/prototypes/berean-interlinear/](https://github.com/jtauber/online-reader/tree/master/prototypes/berean-interlinear/)

### Paginated verses of MorphGNT with toggled interlinear analysis

**Demo**: [John 2.1](https://jtauber.github.io/online-reader/paginated-morphgnt-interlinear/1.html)

**Code**: [/prototypes/paginated-morphgnt-interlinear/](https://github.com/jtauber/online-reader/tree/master/prototypes/paginated-morphgnt-interlinear/)


### Complete MorphGNT SBLGNT with analysis, one page per book with chapter nav

**Demo**: [MorphGNT SBLGNT](https://jtauber.github.io/online-reader/sblgnt-web/)

**Code**: [/prototypes/sblgnt-web/](https://github.com/jtauber/online-reader/tree/master/prototypes/sblgnt-web/)

### Paginated Perseus 4 (alternative pagination styling; no additional annotation)

**Demo**: [Herodotus Book 2](https://jtauber.github.io/online-reader/static-paginated-perseus4/1.html)

**Code**: [/prototypes/static-paginated-perseus4/](https://github.com/jtauber/online-reader/tree/master/prototypes/static-paginated-perseus4/)

### Toggle controls to change styling of text and morphology-based colouring

**Demo**: [2 John](https://jtauber.github.io/online-reader/toggle-controls/2john_01.html)

**Code**: [/prototypes/toggle-controls/](https://github.com/jtauber/online-reader/tree/master/prototypes/toggle-controls/)
