# ============================================================================ #
# file des
# ============================================================================ #

import math, copy, random
# import decimal
# from cmu_112_graphics import *
from icecream import ic
from hw3 import test_unexpected

import cs112_s21_week8_linter
from extra_practice5 import dotProduct

# ============================================================================ #
#* helper fun
# ============================================================================ #


def get_2d_list_cols(list):
    l = []
    cols = len(list[0])
    for i in range(cols):
        l += [rows[i] for rows in list],
    # l = [[rows[i] for rows in board] for i in range(len(board[0]))]
    return l


# ============================================================================ #
#* standard func
# ============================================================================ #


def hasDuplicates(l):
    l_check = []
    for row in l:
        for col in row:
            if col in l_check:
                return False
            l_check += [col]
    return True


# ============================================================================ #
#
def isLatinSquare_count_is_1(l):
    row_1 = l[0]
    for row in l:  # in each row
        for v in row_1:
            if row.count(v) != 1:
                return False
    return True


def list_2d_check_row_col(l, f):
    l_rows = l
    l_cols = get_2d_list_cols(l)
    for list in [l_rows, l_cols]:
        for row in list:
            if f(row) == False:
                return False
    return True


def isLatinSquare(l):
    row_1 = l[0]

    def f(row):
        for val in row_1:
            if row.count(val) != 1:
                return False

    return list_2d_check_row_col(l, f)


# ============================================================================ #
#
def matrixMultiply(l1, l2):
    # m*n * n*p = m*p
    n1 = len(l1[0])  # if isinstance(m1[0], list) else len(m1)  # col of m1
    n2 = len(l2)  # if isinstance(m2[0], list) else 1  # row of m2
    if n1 != n2: return None

    l = []
    l_p = get_2d_list_cols(l2)
    for m in l1:  #? can the nested loop be extracted, w op func
        row = [dotProduct(m, p) for p in l_p]
        l += [row]  # as 2d
    return l


# ============================================================================ #
#


def isKnightsTour_get_board(s):
    for v in [' ', '\n']:
        s = s.strip(v)
    l = s.split("\n")
    for i in range(len(l)):
        l[i] = l[i].split()  # 2d list
        for k in range(len(l[i])):
            l[i][k] = int(l[i][k])
    return l


def isKnightsTour_get_posn(board, i):
    for row in range(len(board)):
        if i in board[row]:
            return [row, board[row].index(i)]


def isKnightsTour_check_legal(l1, l2):  # 'L' shape direction
    l = [abs(l1[i] - l2[i]) for i in range(2)]
    return l in [[2, 1], [1, 2]]


def isKnightsTour(board):
    if isinstance(board, str): board = isKnightsTour_get_board(board)
    n_max = len(board)**2

    l_temp = [v for row in board for v in row]
    if sorted(l_temp) != [i for i in range(n_max)]:  # check number sequence
        return False

    for i in range(n_max - 1):
        posn_now = isKnightsTour_get_posn(board, i)
        posn_next = isKnightsTour_get_posn(board, i + 1)
        # ic(posn_i, posn_next)
        if not isKnightsTour_check_legal(posn_now, posn_next):
            return False
    return True


# ============================================================================ #
#
def nQueensChecker(board):
    def f(v):
        # ic(v)
        if v.count(1) != 1:
            return False

    return list_2d_check_row_col(board, f)


# ============================================================================ #
# * test func
# ============================================================================ #


def test_hasDuplicates():
    parm = [
        [
            [1, 2, 3, 4],
            [2, 3, 4, 1],
        ],
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
        ],
    ]
    soln = [
        False,
        True,
    ]
    for i, (l) in enumerate(parm):
        expect, output = soln[i], hasDuplicates(l)
        # ic(output)
        test_unexpected(output, expect)
        assert output == expect


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


def test_isKnightsTour():
    board = '''

    0  59  38  33  30  17   8   63
37  34  31  60   9  62  29   16
58   1  36  39  32  27  18    7
35  48  41  26  61  10  15   28
42  57   2  49  40  23   6  19
47  50  45  54  25  20  11  14
56  43  52   3  22  13  24   5
51  46  55  44  53   4  21  12

    '''
    board_wrong_numb = '''

    1  2  38  33  30  17   8   63
37  34  31  60   9  62  29   16
58   0  36  39  32  27  18    7
35  48  41  26  61  10  15   28
42  57   2  49  40  23   6  19
47  50  45  54  25  20  11  14
56  43  52   3  22  13  24   5
51  46  55  44  53   4  21  12

    '''
    board_wrong_seq = '''

    1  59  38  33  30  17   8   63
37  34  31  60   9  62  29   16
58   0  36  39  32  27  18    7
35  48  41  26  61  10  15   28
42  57   2  49  40  23   6  19
47  50  45  54  25  20  11  14
56  43  52   3  22  13  24   5
51  46  55  44  53   4  21  12

    '''
    assert (isKnightsTour(board_wrong_numb)) == False
    assert (isKnightsTour(board_wrong_seq)) == False

    # ic(isKnightsTour_check_legal([4, 2], [6, 4]))
    assert (isKnightsTour_check_legal([4, 2], [6, 3])) == True
    assert (isKnightsTour_check_legal([4, 2], [6, 4])) == False


def test_nQueensChecker():
    parm = [
        [
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [1, 0, 0, 0],
            [0, 0, 1, 0],
        ],
        [
            [0, 1, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 1, 0],
        ],
    ]
    soln = [
        True,
        False,
    ]
    for i, (l) in enumerate(parm):
        expect, output = soln[i], nQueensChecker(l)
        # ic(output)
        test_unexpected(output, expect)
        assert output == expect


# ============================================================================ #
#


def testAll():
    print('Tesing all...')

    test_hasDuplicates()
    test_isLatinSquare()
    test_matrixMultiply()
    test_isKnightsTour()
    test_nQueensChecker()

    print('All passed')


# ============================================================================ #
#* main
# ============================================================================ #


def main():
    cs112_s21_week8_linter.lint()
    testAll()


if __name__ == '__main__':
    main()
