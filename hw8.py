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


def makeMagicSquare(n):
    return 42


def playTetris():
    print('Replace this with your Tetris game!')


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
    # testMakeMagicSquare()


#################################################
#* main
#################################################


def main():
    cs112_s21_week8_linter.lint()
    testAll()
    playTetris()


if __name__ == '__main__':
    main()
