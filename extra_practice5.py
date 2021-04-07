#################################################
# extra-practice5.py
#################################################

import math, string
from icecream import ic

#################################################
# Helper functions
#################################################


# ============================================================================ #
# Worked Examples
# ============================================================================ #
def locker_problem(n):
    #* loop
    # l_lockers = [True] * n
    # for i in range(n):
    #     if (i + 1) % 2 == 0: l_lockers[i] = not l_lockers[i]
    # # ic(l)

    # for i in range(2, n):
    #     k = 1
    #     while (i + 1) * k - 1 < len(l_lockers):
    #         i_new = (i + 1) * k - 1
    #         l_lockers[i_new] = not l_lockers[i_new]
    #         k += 1

    # l_new = []
    # for i in range(n):
    #     if l_lockers[i]: l_new += (i + 1, )

    #* mathematical
    l = [i + 1 for i in range(n)]
    l_new = []

    for i in range(len(l)):
        root = l[i]**0.5
        if root == int(root): l_new += (l[i], )

    return l_new


# ============================================================================ #
#

#################################################
# ep5-functions
#################################################

#################################################
# Test Functions
#################################################


def test_locker_problem():
    # ic(locker_problem(4))
    # ic(locker_problem(6))
    # ic(locker_problem(9))

    assert locker_problem(16) == [1, 4, 9, 16]
    assert locker_problem(2000) == [
        1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256,
        289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900,
        961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764,
        1849, 1936
    ]


#################################################
# testAll and main
#################################################


def testAll():
    test_locker_problem()


def main():
    # cs112_s21_week3_linter.lint()
    testAll()


if __name__ == '__main__':
    main()
