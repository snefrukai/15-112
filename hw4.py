#################################################
# hw4.py
#
# Your name:
# Your andrew id:
#################################################

import cs112_s21_week4_linter
from cmu_112_graphics import *
import random, string, math, time

# From here: https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
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

def redrawAll(app, canvas):
    drawTitle(app, canvas)
    drawDisplayWord(app, canvas)
    drawGuesses(app, canvas)
    drawGuessCount(app, canvas)
    drawElapsedTime(app, canvas)
    drawMessage(app, canvas)

def main():
    cs112_s21_week4_linter.lint()
    runApp(width=600, height=400)

if __name__ == '__main__':
    main()