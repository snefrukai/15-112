#################################################
# hw6b: One-Dimensional Connect Four
# name:
# andrew id:
#
# collaborator(s) names and andrew ids:
# 
#################################################

import cs112_s21_week6_linter
from cmu_112_graphics import *
import random, string, math, time

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7): #helper-fn
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d): #helper-fn
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# main app
#################################################

def appStarted(app):
    pass

def mousePressed(app, event):
    pass

def keyPressed(app, event):
    pass

def redrawAll(app, canvas):
    drawTitle(app, canvas)
    drawInstructions(app, canvas)
    drawCurrentPlayerAndMessage(app, canvas)
    drawBoard(app, canvas)
    drawRules(app, canvas)

def drawTitle(app, canvas):
    pass

def drawInstructions(app, canvas):
    messages = ['See rules below.',
                'Click interior piece to select center of 3-piece block.',
                'Click end piece to move that block to that end.',
                'Change board size (and then restart) with arrow keys.',
                'For debugging, press c to set the color of selected block.',
                'For debugging, press p to change the current player.',
                'Press r to restart.',
               ]

def drawRules(app, canvas):
    messages = [
  "The Rules of One-Dimensional Connect Four:",
  "Arrange N (10 by default) pieces in a row of alternating colors.",
  "Players take turns to move three pieces at a time, where:",
  "      The pieces must be in the interior (not on either end)",
  "      The pieces must be adjacent (next to each other).",
  "      At least one moved piece must be the player's color.",
  "The three pieces must be moved in the same order to either end of the row.",
  "The gap must be closed by sliding the remaining pieces together.",
  "The first player to get four (or more) adjacent pieces of their color wins!",
               ]

def drawCurrentPlayerAndMessage(app, canvas):
    pass

def drawPlayerPiece(app, canvas, player, cx, cy, r):
    pass

def drawBoard(app, canvas):
    pass

def main():
    cs112_s21_week6_linter.lint()
    runApp(width=650, height=550)

if __name__ == '__main__':
    main()