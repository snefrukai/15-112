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


#################################################
#* hw8
#################################################


def isRectangular(L):
    return 42


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


def testIsRectangular():
    print('Testing isRectangular()...', end='')
    assert (isRectangular([[1, 2], [3, 4]]) == True)
    assert (isRectangular([[1, 2], [3, 4, 5]]) == False)
    assert (isRectangular([[1], [2]]) == True)
    assert (isRectangular([[], []]) == True)
    assert (isRectangular([]) == False)
    assert (isRectangular(["this", "is", "silly"]) == False)
    assert (isRectangular([["this"], "is", "silly"]) == False)
    assert (isRectangular([["this"], ["is"], ["fine"]]) == True)
    assert (isRectangular([[1], [2, 3], [4]]) == False)
    assert (isRectangular([[1, 2], [3], [4]]) == False)
    assert (isRectangular([12, [3], [4]]) == False)
    assert (isRectangular(["abc", [1, 2, 3]]) == False)
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


def testAll():
    test_list_2d_edit()

    # testIsRectangular()
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