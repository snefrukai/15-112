# ============================================================================ #
# file des
# ============================================================================ #

import math, copy, random
# import decimal
# from cmu_112_graphics import *
from icecream import ic

import cs112_s21_week8_linter
from hw3 import test_unexpected
from extra_practice5 import dotProduct

# ============================================================================ #
#* helper fun
# ============================================================================ #


def make_2d_list_cols(board):
    l = []
    for i in range(len(board[0])):  # numb of cols
        l += [rows[i] for rows in board],
    # ic(l)
    return l


# ============================================================================ #
#* standard func
# ============================================================================ #


def isLatinSquare_count_is_1(l):
    for val in l[0]:
        for i in range(len(l)):
            if l[i].count(val) != 1: return False
    return True


def isLatinSquare(l):
    l_row = l
    l_col = make_2d_list_cols(l)
    for val in [l_row, l_col]:
        if not isLatinSquare_count_is_1(val): return False
    return True


# ============================================================================ #
#


def matrixMultiply(m1, m2):
    # m*n * n*p = m*p
    n1 = len(m1[0])  # if isinstance(m1[0], list) else len(m1)  # col of m1
    n2 = len(m2)  # if isinstance(m2[0], list) else 1  # row of m2
    if n1 != n2: return None

    l_cols_2 = make_2d_list_cols(m2)
    # ic(l_col_2)
    l = []
    for k in range(len(m1)):  #? can the nested loop be extracted, w op func
        l_temp = []
        for i in range(len(l_cols_2)):
            l_temp += [dotProduct(m1[k], l_cols_2[i])]
        l += [l_temp]  # as 2d
    return l


# ============================================================================ #
# * test func
# ============================================================================ #


def test_isLatinSquare():
    parm = [
        [
            [1, 2, 3, 4],
            [2, 3, 4, 1],
            [3, 4, 1, 2],
            [4, 1, 2, 3],
        ],
        [
            [1, 2, 3, 4],
            [2, 3, 4, 1],
            [3, 4, 1, 2],
            [3, 1, 2, 3],
        ],
    ]
    soln = [
        True,
        False,
    ]
    for i, (l) in enumerate(parm):
        expect, output = soln[i], isLatinSquare(l)
        # ic(output)
        test_unexpected(output, expect)
        assert output == expect


def test_matrixMultiply():
    parm = [
        ([
            [3, 4, 2],
        ], [
            [13, 9, 7],
            [8, 7, 4],
        ]),  # F
        ([
            [3, 4, 2],
        ], [
            [13, 9, 7],
        ]),  # F
        ([
            [3, 4, 2],
        ], [
            [13],
            [8],
            [6],
        ]),
        ([
            [3, 4, 2],
        ], [
            [13, 9, 7, 15],
            [8, 7, 4, 6],
            [6, 4, 0, 3],
        ]),
        ([
            [1, 2, 3],
            [4, 5, 6],
        ], [[7, 8], [9, 10], [11, 12]]),
    ]
    soln = [
        None, None, [
            [83],
        ], [
            [83, 63, 37, 75],
        ], [
            [58, 64],
            [139, 154],
        ]
    ]
    for i, (m1, m2) in enumerate(parm):
        expect, output = soln[i], matrixMultiply(m1, m2)
        # ic(output)
        test_unexpected(output, expect)
        assert output == expect


# ============================================================================ #
#


def testAll():
    print('Tesing all...')

    test_isLatinSquare()
    test_matrixMultiply()

    print('All passed')


# ============================================================================ #
#* main
# ============================================================================ #


def main():
    cs112_s21_week8_linter.lint()
    testAll()


if __name__ == '__main__':
    main()
