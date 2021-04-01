import pyperclip

toc = """
Introduction
Chapter 1: Started 
test line
"""
start = "chapter", "Chapter", "Introduction", "introduction", "intro:", "Intro:", "preface", "Preface", "Forward", "forward"

toc = pyperclip.paste()
foo = "TOC s\r\n"

for line in toc.splitlines():
    if (line.startswith(start)):
        foo += line + "\r\n"

pyperclip.copy(foo)
print(foo)
