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


def almostEqual(d1, d2, epsilon=10**-7):  #helper-fn
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)


import decimal


def roundHalfUp(d):  #helper-fn
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))


#################################################
# model
#################################################


def appStarted(app):
    app.cx = app.width / 2
    app.cy = app.height / 2
    app.board_len_half = 5

    appRestart(app)
    sizeChanged(app)


def appRestart(app):
    l = [1, 2]
    random.shuffle(l)
    app.board = l * app.board_len_half
    app.step = app.width / len(app.board)
    app.player_current = app.board[0]

    app.selection_i = []
    app.selection_legal = True
    app.win_i = []

    app.gameOver = False
    app.message = 'Select your 3-piece block'


def sizeChanged(app):
    app.cx = app.width / 2
    app.cy = app.height / 2
    app.step = app.width / len(app.board)

    app.font_1 = f'Arial {app.width // 30} bold'
    app.font_2 = f'Arial {app.width // 50} '
    app.font_3 = f'Arial {app.width // 50} '


# ============================================================================ #
# controller
# ============================================================================ #
def getPieceIndex(app, x, y):
    i = int(x // app.step)
    (cx, cy, r) = getPieceCenterAndRadius(app, i)
    if y - app.cy < r * 1.5: return i  # 到中线的距离


def getSelection(app, i_piece):
    app.selection_i = [i_piece - 1, i_piece, i_piece + 1]

    if 1 < i_piece < len(app.board) - 2:
        app.selection_legal = True
        app.message = 'Select your 3-piece block'
    else:  # in [1, -2]
        app.selection_legal = False
        app.message = 'End cannot be in block'

    # print(app.selection_i, app.selection_legal)


def moveSelection(app, moveToLeftEnd):
    start = app.selection_i[0]
    end = app.selection_i[-1] + 1
    pop = app.board[start:end]

    app.board = app.board[:start] + app.board[end:]
    if moveToLeftEnd:
        app.board = pop + app.board
    else:
        app.board = app.board + pop

    # print('pop', pop)
    check_win(app)
    app.selection_i = []
    if not app.gameOver:
        app.player_current += 1
        check_player(app)


def check_player(app):
    if app.player_current % 2 != 0:
        app.player_current = 1


def check_win(app):
    k = 1
    for i in range(1, len(app.board)):
        if app.board[i] == app.board[i - 1]: k += 1
        else: k = 1
        if k == 4:
            app.gameOver = True
            app.message = 'Game Over!!!!!'
            app.win_i = i
            print(i)


# ============================================================================ #
#


def mousePressed(app, event):
    if not app.gameOver:
        i = getPieceIndex(app, event.x, event.y)
        # print(i)

        i_at_end = i in [0, len(app.board) - 1]
        if i != None:  # in clickable area
            if not i_at_end:
                if app.board[i] != app.player_current:
                    app.message = 'Block must contain current player'
                else:
                    getSelection(app, i)
                    app.message = 'Select end to move block'
            elif i_at_end and app.selection_i != []:
                if app.selection_legal:  # 先写正常，后写报错？
                    # moveSelection(app, True if i == 0 else False)
                    moveSelection(app, i == 0)
                else:
                    app.message = 'Cannot move illegal selection'

            # app.message = ' move ' if i_at_end else 'def'


# ============================================================================ #
#


def keyPressed(app, event):
    # Debugging features: c and p
    if event.key == 'r':
        appRestart(app)
    elif not app.gameOver:
        if event.key == 'Up' and app.board_len_half < 10:
            app.board_len_half += 1
            appRestart(app)
        elif event.key == 'Down' and app.board_len_half > 3:
            app.board_len_half -= 1
            appRestart(app)
        elif event.key == 'c':
            for d in app.selection_i:
                app.board[d] = app.player_current
        elif event.key == 'p':
            app.player_current += 1
            check_player(app)


# ============================================================================ #
# view
# ============================================================================ #


def redrawAll(app, canvas):
    drawTitle(app, canvas)
    drawInstructions(app, canvas)

    drawCurrentPlayerAndMessage(app, canvas)
    drawBoard(app, canvas)

    drawRules(app, canvas)


def drawTitle(app, canvas):
    canvas.create_text(app.cx,
                       30,
                       text='One-Dimensional Connect Four!',
                       font='Arial 26 bold ')


def drawInstructions(app, canvas):
    messages = [
        'See rules below.',
        'Click interior piece to select center of 3-piece block.',
        'Click end piece to move that block to that end.',
        'Change board size (and then restart) with arrow keys.',
        'For debugging, press c to set the color of selected block.',
        'For debugging, press p to change the current player.',
        'Press r to restart.',
    ]
    f_size = 13
    for i in range(len(messages)):
        canvas.create_text(
            app.cx,
            60 + i * f_size * 1.5,
            #    anchor='w',
            text=messages[i],
            font=f'Arial {f_size} ')


# ============================================================================ #
#


def getPieceCenterAndRadius(app, pieceIndex):
    cx = app.step * pieceIndex + app.step / 2
    cy = app.height / 2
    r = app.step / 2 * 0.8
    return (cx, cy, r)


def drawCurrentPlayerAndMessage(app, canvas):
    # y = app.cy - app.step
    y = 210
    font = 'Arial 13 bold'
    fill = 'lightBlue' if app.player_current == 1 else 'lightGreen'
    outline = "blue" if app.player_current == 1 else 'green'
    r = 14
    canvas.create_text(app.cx - r * 2 - 2,
                       y,
                       text='Current Player:',
                       font=font,
                       fill=outline,
                       anchor='e')
    drawPlayerPiece(app, canvas, app.player_current, app.cx, y, r)
    canvas.create_text(app.cx + r * 2 - 2,
                       y,
                       text=app.message,
                       font=font,
                       fill=outline,
                       anchor='w')


def drawPlayerPiece(app, canvas, player, cx, cy, r):
    # p1 'lightBlue' with a 'blue' outline
    # p2 'lightGreen' with a 'green' outline
    fill = 'lightBlue' if player == 1 else 'lightGreen'
    outline = "blue" if player == 1 else 'green'
    canvas.create_oval(cx - r,
                       cy - r,
                       cx + r,
                       cy + r,
                       fill=fill,
                       outline=outline,
                       width=4)


def drawBoard(app, canvas):
    if app.selection_i != []:  #selection box
        (x0, y0, r) = getPieceCenterAndRadius(app, app.selection_i[0])
        (x1, y1, r) = getPieceCenterAndRadius(app, app.selection_i[-1])
        margin = 5
        #'orange' and 'pink' for the selection box
        fill = 'orange' if app.selection_legal else 'pink'
        canvas.create_rectangle(x0 - r - margin,
                                y0 - r - margin,
                                x1 + r + margin,
                                y1 + r + margin,
                                fill=fill,
                                width=0)

    for i in range(len(app.board)):  # board
        (cx, cy, r) = getPieceCenterAndRadius(app, i)
        drawPlayerPiece(app, canvas, app.board[i], cx, cy, r)

    if app.gameOver:
        (x3, y3, r) = getPieceCenterAndRadius(app, app.win_i - 3)
        (x4, y4, r) = getPieceCenterAndRadius(app, app.win_i)
        canvas.create_line(x3, y3, x4, y4, width=3)


# ============================================================================ #
#


def drawRules(app, canvas):
    messages = [
        "The Rules of One-Dimensional Connect Four:",
        "Arrange N (10 by default) pieces in a row of alternating colors.",
        "Players take turns to move three pieces at a time, where:",
        "      The pieces must be in the interior (not on either end)",
        "      The pieces must be adjacent (next to each other).",
        "      At least one moved piece must be the player's color.",
        "The three pieces must be moved in the same order to\
either end of the row.",
        "The gap must be closed by sliding the remaining pieces together.",
        "The first player to get four (or more) adjacent pieces of\
their color wins!",
    ]
    f_size = 13
    for i in range(len(messages)):
        canvas.create_text(10,
                           360 + i * f_size * 1.5,
                           anchor='nw',
                           text=messages[i],
                           font=f'Arial {f_size} ')


# ============================================================================ #
# main
# ============================================================================ #


def main():
    cs112_s21_week6_linter.lint()
    runApp(width=650, height=550)


if __name__ == '__main__':
    main()
