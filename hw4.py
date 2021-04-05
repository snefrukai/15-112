#################################################
# hw4.py
#
# Your name:
# Your andrew id:
#################################################

import cs112_s21_week4_linter
from cmu_112_graphics import *
import random, string, math, time

# ============================================================================ #
# course case rewrite

# def appStarted(app):
#     app.cx = app.width / 2
#     app.cy = app.height / 2
#     app.r = 40
#     app.paused = False

# def timerFired(app):
#     if app.paused: doStep(app)

# def doStep(app):
#     app.cx -= 10
#     if app.cx + app.r < 0: app.cx = app.width

# def keyPressed(app, event):
#     if event.key == 'Left': app.cx -= 10
#     elif event.key == 'Right': app.cx += 10

#     if event.key == 'p':
#         app.paused = not app.paused  # why cant use True? cuz it's toggle
#     elif not app.paused and event.key == 's':  # stepping
#         doStep(app)

# def mousePressed(app, event):
#     app.cx = event.x
#     app.cy = event.y

# def redrawAll(app, canvas):
#     canvas.create_oval(app.cx - app.r, app.cy - app.r, app.cx + app.r,
#                        app.cy + app.r)

# runApp(width=400, height=400)

# From here: https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO

# Note: Tkinter uses event.keysym for some keys, and event.char
# for others, and it can be confusing how to use these properly.
# Instead, cmu_112_graphics replaces both of these with event.key,
# which simply works as expected in all cases.

# This version moves in both x and y dimensions.


def readFile(path):
    with open(path, "rt") as f:
        return f.read()


def appStarted(app):
    pass


def mousePressed(app, event):
    pass


def keyPressed(app, event):
    pass


def timerFired(app):
    pass


#########################################
# redrawAll and drawing helper functions:
#########################################


def drawTitle(app, canvas):
    pass


def drawDisplayWord(app, canvas):
    pass


def drawGuesses(app, canvas):
    pass


def drawGuessCount(app, canvas):
    pass


def drawElapsedTime(app, canvas):
    pass


def drawMessage(app, canvas):
    pass


# def redrawAll(app, canvas):
#     drawTitle(app, canvas)
#     drawDisplayWord(app, canvas)
#     drawGuesses(app, canvas)
#     drawGuessCount(app, canvas)
#     drawElapsedTime(app, canvas)
#     drawMessage(app, canvas)


def main():
    cs112_s21_week4_linter.lint()
    # runApp(width=600, height=400)


if __name__ == '__main__':
    main()