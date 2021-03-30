toc = """
intro: asd
Chapter 7: Getting Modular: Modules, methods, classes, and objects](zotero://open-pdf/0_MJMVS3VW/331)
test line
"""

start = "chapter", "Chapter", "Introduction", "introduction", "intro:", "Intro:", "preface", "Preface", "Forward", "forward"

for line in toc.splitlines():
    if (line.startswith(start)):
        print(line)