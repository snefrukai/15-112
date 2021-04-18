#################################################
# hw8.py: 2d Lists + Tetris!
#
# Your name:
# Your andrew id:
#
# Your partner's name:
# Your partner's andrew id:
#################################################

import cs112_s21_week8_linter
import math, copy, random
from icecream import ic

from cmu_112_graphics import *

#################################################
#* Helper functions
#################################################


def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)


import decimal


def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))


def plus(x, n):
    return x + n


def list_2d_edit(l, n):
    rows, cols = len(l), len(l[0])
    for row in range(rows):
        for col in range(cols):
            l[row][col] = plus(l[row][col], n)
    return l


# ============================================================================ #
#* case study
# ============================================================================ #

# ============================================================================ #
# wordSearch


def wordSearch(l_board, s_word):
    rows, cols = len(l_board), len(l_board[0])
    for i_row in range(rows):
        for i_col in range(cols):
            s_hit_dir = wordSearch_dir(l_board, s_word, i_row, i_col)
            if s_hit_dir != None:
                return (s_word, (i_row, i_col), s_hit_dir)


def wordSearch_dir(l_board, s_word, row_start, col_start):
    # l_dir_row = l_dir_col = [-1, 0, 1]
    l_dir_names = [
        "up-left", "up", "up-right",\
        "left", "right",\
        "down-left", "down", "down-right",
    ]
    l_dir = [ (-1, -1), (-1, 0), (-1, +1),\
             ( 0, -1),          ( 0, +1),\
             (+1, -1), (+1, 0), (+1, +1) ]

    for i in range(len(l_dir)):
        hit = wordSearch_dir_hit(l_board, s_word, row_start, col_start,
                                 l_dir[i])
        if hit: return l_dir_names[i]

    # l_dir_names = [
    #     ["up-left", "up", "up-right"],
    #     ["left", "", "right"],
    #     ["down-left", "down", "down-right"],
    # ]
    # for i in range(len(l_dir_row)):
    #     for k in range(len(l_dir_col)):
    #         if (l_dir_row[i], l_dir_col[k]) != (0, 0):
    #             # ic(dir_row[i], dir_col[k], dir_names[i][k])
    #             hit = wordSearch_dir_hit(l_board, s_word, row_start,\
    #  col_start,  l_dir_row[i], l_dir_col[k])
    #             if hit: return l_dir_names[i][k]


def wordSearch_dir_hit(l_board, s_word, row_start, col_start, l_dir):
    for i in range(len(s_word)):
        row = row_start + i * l_dir[0]
        col = col_start + i * l_dir[1]
        # ic(row, col)
        in_range = 0 <= row < len(l_board) and 0 <= col < len(l_board[0])
        if not in_range or l_board[row][col] != s_word[i]:
            return False
    return True


# ============================================================================ #
# connect4
# A simple game of connect4 with a text interface
# based on the wordSearch code written in class.


def playConnect4():
    rows, cols = 6, 7
    count_move = 0
    board = [['-'] * cols for row in range(rows)]
    printBoard(board)

    while (count_move < rows * cols):
        player = 'X' if count_move % 2 == 0 else 'O'
        moveCol = getMoveCol(board, player)
        moveRow = getMoveRow(board, moveCol)
        board[moveRow][moveCol] = player
        printBoard(board)
        if checkForWin(board, player):
            print(f'*** Player {player} Wins!!! ***')
            return
        count_move += 1

    print('*** Tie Game!!! ***')


def getMoveCol(board, player):
    cols = len(board[0])
    while True:
        response = input(f"Enter player {player}'s move (column number): ")
        try:
            moveCol = int(response) - 1  # int('26.6'), ValueError
            if moveCol not in range(cols):
                print(f'Columns must be between 1 and {cols}.')
            elif board[0][moveCol] != '-':
                print('That column is full!')
            else:
                return moveCol
        except:
            print('Columns must be integer values!')
    print('Please try again.')


def getMoveRow(board, moveCol):
    # find first open row from bottom
    for row in range(len(board) - 1, -1, -1):
        if board[row][moveCol] == '-': return row

    # should never get here!
    assert False


def checkForWin(board, player):
    s_win = player * 4
    return wordSearch(board, s_win) != None


def printBoard(board):
    rows, cols = len(board), len(board[0])
    width = 5

    # first print the column headers
    for i in range(cols):
        print(str(i + 1).center(width), end='')
    print()

    # then print the board
    for i_row in range(rows):
        for i_col in range(cols):
            print(board[i_row][i_col].center(width), end='')
        print()


# ============================================================================ #
# othello

#################################################
#* hw8
#################################################


def isRectangular(l):
    if not len(l) > 1: return False
    for i in range(len(l)):
        if not isinstance(l[i], list): return False
        if i > 0 and len(l[i]) != len(l[i - 1]): return False
        for val in l[i]:
            if isinstance(val, list): return False

    return True


# ============================================================================ #
#


def makeMagicSquare(n):
    if n % 2 == 0 or n < 0: return None
    pesudo = '/'
    l = [[pesudo] * n for i in range(n)]

    row, col = 0, int(n / 2)
    for i in range(1, n * n + 1):
        if i > 1:
            row_temp, col_temp = row, col
            row = (row - 1) % n
            col = (col + 1) % n
            # ic(i, row, col)
            if l[row][col] != pesudo:
                row = row_temp + 1  #? why this not out of range
                col = col_temp
        l[row][col] = i
        # ic(l)
    return l


# ============================================================================ #
#* Tetris
# ============================================================================ #

# ============================================================================ #
# helper
# ============================================================================ #


def loop_each_cell(l, f):
    rows, cols = len(l), len(l[0])
    for row in range(rows):
        for col in range(cols):
            # f(l, row, col)  #? how to return bool
            bool = f(l, row, col)
            if bool != None: return bool


# ============================================================================ #
# model
# ============================================================================ #


def newFallingPiece(app):
    i = random.randint(0, len(app.tetrisPieces) - 1)
    l_i = [v[i] for v in [app.tetrisPieces, app.tetrisPieceColors]]
    app.fallingPiece, app.fallingPieceColor = l_i[0], l_i[1]
    app.fallingPieceRow = 0
    app.fallingPieceCol = app.cols // 2 - len(app.fallingPiece[0]) // 2
    # 10//2 - 3//2 = 5 -1 = 4


def appStarted(app):
    # set board
    app.rows, app.cols, app.cellSize, app.margin = gameDimensions()
    app.emptyColor = 'blue'
    app.board = [[app.emptyColor] * app.cols for row in range(app.rows)]
    # ic(app.board)

    # pre-load a few cells with known colors for testing purposes
    app.board[0][0] = "red"  # top-left is red
    app.board[0][app.cols - 1] = "white"  # top-right is white
    app.board[app.rows - 1][0] = "green"  # bottom-left is green
    app.board[app.rows - 1][app.cols - 1] = "gray"  # bottom-right is gray

    # Seven "standard" pieces (tetrominoes)
    iPiece = [[True, True, True, True]]
    jPiece = [
        [True, False, False],
        [True, True, True],
    ]
    lPiece = [
        [False, False, True],
        [True, True, True],
    ]
    oPiece = [
        [True, True],
        [True, True],
    ]
    sPiece = [
        [False, True, True],
        [True, True, False],
    ]
    tPiece = [
        [False, True, False],
        [True, True, True],
    ]
    zPiece = [
        [True, True, False],
        [False, True, True],
    ]
    app.tetrisPieces = [iPiece, jPiece, lPiece, oPiece, sPiece, tPiece, zPiece]
    app.tetrisPieceColors = [
        "red", "yellow", "magenta", "pink", "cyan", "green", "orange"
    ]
    newFallingPiece(app)


# ============================================================================ #
# controller
# ============================================================================ #


def fallingPieceIsLegal(app):
    def f(l, row, col):
        if l[row][col] == True:
            x = app.fallingPieceRow + row
            y = app.fallingPieceCol + col
            onBoard = x in range(app.rows) and y in range(app.cols)
            # ic(app.fallingPieceRow, row, app.fallingPieceCol, col)
            if not onBoard:
                return False
            elif app.board[x][y] != app.emptyColor:
                return False

    bool = loop_each_cell(app.fallingPiece, f)
    if bool == False: return False
    else: return True


def moveFallingPiece(app, key):
    l_temp = [app.fallingPieceRow, app.fallingPieceCol]
    if key == 'Down': app.fallingPieceRow += 1  # ['Down', 'Right', 'Left']
    else: app.fallingPieceCol += 1 if key == 'Right' else -1

    # ic(fallingPieceIsLegal(app))
    if not fallingPieceIsLegal(app):
        app.fallingPieceRow, app.fallingPieceCol = l_temp[0], l_temp[1]


# ============================================================================ #
#


def keyPressed(app, event):
    # test code for newFallingPiece
    if event.key == 'n': newFallingPiece(app)

    # move piece
    if event.key in ['Right', 'Left', 'Down']:
        moveFallingPiece(app, event.key)


# ============================================================================ #
# view
# ============================================================================ #


def drawCell(app, canvas, row, col, color):
    l0 = [app.margin + app.cellSize * v for v in [row, col]]
    x0, y0 = l0[1], l0[0]
    l1 = [v + app.cellSize for v in [x0, y0]]
    x1, y1 = l1[0], l1[1]
    canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=3)


def drawBoard(app, canvas):
    def f(l, row, col):
        drawCell(app, canvas, row, col, app.board[row][col])

    loop_each_cell(app.board, f)


def drawFallingPiece(app, canvas):
    def f(l, row, col):
        if l[row][col] == True:
            drawCell(app, canvas, app.fallingPieceRow + row,
                     app.fallingPieceCol + col, app.fallingPieceColor)

    loop_each_cell(app.fallingPiece, f)


# def drawBoard(app, canvas):
#     l = app.board
#     rows, cols = len(l), len(l[0])
#     for row in range(rows):
#         for col in range(cols):
#             drawCell(app, canvas, row, col, app.board[row][col])

# def drawFallingPiece(app, canvas):
#     l = app.fallingPiece
#     rows, cols = len(l), len(l[0])
#     for row in range(rows):
#         for col in range(cols):
#             if l[row][col] == True:
#                 drawCell(app, canvas, app.fallingPieceRow + row,
#                          app.fallingPieceCol + col, app.fallingPieceColor)

# ============================================================================ #
#


def redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill='orange')

    drawBoard(app, canvas)
    drawFallingPiece(app, canvas)


# ============================================================================ #
# setup
# ============================================================================ #


def gameDimensions():
    rows, cols = 15, 10
    # rows, cols = 4, 4
    cellSize = 20
    margin = 25
    return (rows, cols, cellSize, margin)


def playTetris():
    (rows, cols, cellSize, margin) = gameDimensions()
    l_len = [margin * 2 + cellSize * n for n in [rows, cols]]
    width, height = l_len[1], l_len[0]
    runApp(width=width, height=height)  # start app


#################################################
#* Test Functions
#################################################


def test_list_2d_edit():
    l = [[2, 3, 5], [1, 4, 7]]
    # print(list_2d_edit(l, 1))


# ============================================================================ #
# case study


def test_wordSearch_dir(board):
    assert (wordSearch_dir(board, 'dog', 0, 0) == 'right')
    assert (wordSearch_dir(board, 'cat', 1, 2) == 'left')
    # ic(wordSearch_dir(board, 'dog', 0, 0))


def testWordSearch():
    board = [
        ['d', 'o', 'g'],
        ['t', 'a', 'c'],
        ['o', 'a', 't'],
        ['u', 'r', 'k'],
    ]
    test_wordSearch_dir(board)

    assert (wordSearch(board, "dog")) == ('dog', (0, 0), 'right')
    assert (wordSearch(board, "cat")) == ('cat', (1, 2), 'left')
    assert (wordSearch(board, "tad")) == ('tad', (2, 2), 'up-left')
    assert (wordSearch(board, "cow")) == None


def test_playConnect4():
    # playConnect4()
    getMoveCol('-', 'X')


# ============================================================================ #
# hw8


def testIsRectangular():
    print('Testing isRectangular()...', end='')
    assert (isRectangular([[], []]) == True)
    assert (isRectangular([]) == False)
    assert (isRectangular([[1, 2], [3, 4]]) == True)
    assert (isRectangular([[1, 2], [3, 4, 5]]) == False)
    assert (isRectangular([[1], [2]]) == True)
    assert (isRectangular(["this", "is", "silly"]) == False)
    assert (isRectangular([["this"], "is", "silly"]) == False)
    assert (isRectangular([["this"], ["is"], ["fine"]]) == True)
    assert (isRectangular([[1], [2, 3], [4]]) == False)
    assert (isRectangular([[1, 2], [3], [4]]) == False)
    assert (isRectangular([12, [3], [4]]) == False)
    assert (isRectangular(["abc", [1, 2, 3]]) == False)
    assert (isRectangular([[1, 1], [2, [5, 5]], [3, 3]]) == False)  # 3d lsit
    print('Passed!')


def testMakeMagicSquare():
    print('Testing makeMagicSquare()...', end='')
    # ic(makeMagicSquare(1))

    L1 = [[1]]
    L3 = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
    L5 = [[17, 24, 1, 8, 15], [23, 5, 7, 14, 16], [4, 6, 13, 20, 22],
          [10, 12, 19, 21, 3], [11, 18, 25, 2, 9]]
    L9 = [[47, 58, 69, 80, 1, 12, 23, 34, 45],
          [57, 68, 79, 9, 11, 22, 33, 44, 46],
          [67, 78, 8, 10, 21, 32, 43, 54, 56],
          [77, 7, 18, 20, 31, 42, 53, 55, 66],
          [6, 17, 19, 30, 41, 52, 63, 65, 76],
          [16, 27, 29, 40, 51, 62, 64, 75, 5],
          [26, 28, 39, 50, 61, 72, 74, 4, 15],
          [36, 38, 49, 60, 71, 73, 3, 14, 25],
          [37, 48, 59, 70, 81, 2, 13, 24, 35]]
    assert (makeMagicSquare(1) == L1)
    assert (makeMagicSquare(3) == L3)
    assert (makeMagicSquare(5) == L5)
    assert (makeMagicSquare(9) == L9)
    assert (makeMagicSquare(0) == None)
    assert (makeMagicSquare(2) == None)
    assert (makeMagicSquare(4) == None)
    assert (makeMagicSquare(-3) == None)
    print('Passed!')


# ============================================================================ #
#


def testAll():
    test_list_2d_edit()

    # case study
    testWordSearch()
    # test_playConnect4()
    # playConnect4()

    # hw8
    testIsRectangular()
    testMakeMagicSquare()


#################################################
#* main
#################################################


def main():
    cs112_s21_week8_linter.lint()
    testAll()
    playTetris()


if __name__ == '__main__':
    main()
