# ============================================================================ #
# file des
# ============================================================================ #

import math, copy, random
# import decimal
# from cmu_112_graphics import *
from icecream import ic

# ============================================================================ #
#* standard func
# ============================================================================ #

# ============================================================================ #
#


def isLatinSquare_count_is_1(l):
    for val in l[0]:
        for i in range(len(l)):
            if l[i].count(val) != 1: return False
    return True


def isLatinSquare(l):
    l_row = l
    l_col = []
    for i in range(len(l[0])):
        l_col += [rows[i] for rows in l],

    for val in [l_row, l_col]:
        if not isLatinSquare_count_is_1(val): return False
    return True


# ============================================================================ #
# * test func
# ============================================================================ #


def test_isLatinSquare():
    l = [
        [1, 2, 3, 4],
        [2, 3, 4, 1],
        [3, 4, 1, 2],
        [4, 1, 2, 3],
    ]
    l1 = [
        [1, 2, 3, 4],
        [2, 3, 4, 1],
        [3, 4, 1, 2],
        [3, 1, 2, 3],
    ]
    assert (isLatinSquare(l)) == True
    assert (isLatinSquare(l1)) == False


# ============================================================================ #
#


def testAll():
    print('Tesing all...')

    test_isLatinSquare()

    print('All passed')


# ============================================================================ #
#* main
# ============================================================================ #


def main():
    # linter
    testAll()


if __name__ == '__main__':
    main()
