#################################################
# hw6a.py
#
# name:
# andrew id:
#################################################

import cs112_s21_week6_linter
import math, copy, string

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


# ============================================================================ #
# Part 2: Case Studies
# ============================================================================ #

# ============================================================================ #
# Example: Grids
from cmu_112_graphics import *


def appStarted(app):  # set margin, row, col, selection
    app.margin = 50
    app.cols = 8
    app.rows = 4
    app.selection = (-1, -1)

    app.grid_w = int((app.width - app.margin * 2) / app.cols)
    app.grid_h = int((app.height - app.margin * 2) / app.rows)


def mousePressed(app, event):  # select this (row, col) unless it is selected
    select_row = int((event.y - app.margin) / app.grid_h)
    select_col = int((event.x - app.margin) / app.grid_w)
    app.selection = (select_row, select_col)
    print(app.selection)


def redrawAll(app, canvas):  # draw grid of cells
    for row in range(app.rows):
        for col in range(app.cols):
            x0 = app.margin + app.grid_w * col
            y0 = app.margin + +app.grid_h * row
            x1 = x0 + app.grid_w
            y1 = y0 + app.grid_h
            fill = "orange" if app.selection == (row, col) else "cyan"
            canvas.create_rectangle(x0, y0, x1, y1, fill=fill)


# runApp(width=400, height=400)

# ============================================================================ #
# Optional Example: Pong!

#################################################
# hw6-standard functions
#################################################


def destructiveRemoveEvens(L):
    return 42


def nondestructiveRemoveEvens(L):
    return 42


def areaOfPolygon(L):
    return 42


def evalPolynomial(coeffs, x):
    return 42


def multiplyPolynomials(p1, p2):
    return 42


def solvesCryptarithm(puzzle, solution):
    return 42


def bestScrabbleScore(dictionary, letterScores, hand):
    return 42


#################################################
# hw6-bonus functions
#################################################


def runSimpleProgram(program, args):
    return 42


def allSublists(L):
    return 42


def solveSubsetSum(L):
    return 42


def heapsAlgorithmForPermutations(L):
    # from https://en.wikipedia.org/wiki/Heap%27s_algorithm
    return 42


def formatCryptarithmSolution(puzzle, solution):
    return 42


def solveCryptarithmWithMaxDigit(puzzle, maxDigit):
    return 42


def countCryptarithmsWithMaxDigit(puzzle, maxDigit):
    return 42


def getAllSingletonCryptarithmsWithMaxDigit(words, maxDigit):
    return 42


#################################################
# Test Functions
#################################################


def _destructiveRemoveEvens(L):
    destructiveRemoveEvens(L)
    return L


def testDestructiveRemoveEvens():
    print("Testing destructiveRemoveEvens()...", end="")
    assert (_destructiveRemoveEvens([1, 2, 3, 4]) == [1, 3])
    assert (_destructiveRemoveEvens([1, 3, 5, 7, 3]) == [1, 3, 5, 7, 3])
    assert (_destructiveRemoveEvens([2, 4, 2, 4, 6]) == [])
    assert (_destructiveRemoveEvens([2, 4, 1, 2, 4, 6]) == [1])
    print("Passed!")


def _verifyRemoveEvensIsNondestructive():
    a = [1, 2, 3]
    b = copy.copy(a)
    nondestructiveRemoveEvens(a)  # ignore result, just check if destructive
    return (a == b)


def testNondestructiveRemoveEvens():
    print("Testing nondestructiveRemoveEvens()...", end='')
    assert (_verifyRemoveEvensIsNondestructive())
    assert (nondestructiveRemoveEvens([1, 2, 3, 4]) == [1, 3])
    assert (nondestructiveRemoveEvens([1, 3, 5, 7, 3]) == [1, 3, 5, 7, 3])
    assert (nondestructiveRemoveEvens([2, 4, 2, 4, 6]) == [])
    assert (nondestructiveRemoveEvens([2, 4, 1, 2, 4, 6]) == [1])
    print("Passed!")


def _verifyAreaOfPolygonIsNondestructive():
    a = [(4, 10), (9, 7), (11, 2), (2, 2)]
    b = copy.deepcopy(a)
    # ignore result, just checking for destructiveness here
    areaOfPolygon(a)
    return (a == b)


def testAreaOfPolygon():
    print("Testing areaOfPolygon()...", end="")
    assert (_verifyAreaOfPolygonIsNondestructive())
    assert (almostEqual(areaOfPolygon([(4, 10), (9, 7), (11, 2), (2, 2)]),
                        45.5))
    assert (almostEqual(areaOfPolygon([(9, 7), (11, 2), (2, 2), (4, 10)]),
                        45.5))
    assert (almostEqual(areaOfPolygon([(0, 0), (0.5, 1), (1, 0)]), 0.5))
    assert (almostEqual(areaOfPolygon([(0, 10), (0.5, 11), (1, 10)]), 0.5))
    assert (almostEqual(areaOfPolygon([(-0.5, 10), (0, -11), (0.5, 10)]),
                        10.5))
    print("Passed!")


def _verifyEvalPolynomialIsNondestructive():
    a = [2, 3, 0, 4]
    b = copy.copy(a)
    # ignore result, just checking for destructiveness here
    evalPolynomial(a, 4)
    return (a == b)


def testEvalPolynomial():
    print("Testing evalPolynomial()...", end="")
    assert (_verifyEvalPolynomialIsNondestructive())
    # f(x) = 2x^3 + 3x^2 + 4, f(4) = 180
    assert (evalPolynomial([2, 3, 0, 4], 4) == 180)
    # f(x) = 6, f(42) = 6
    assert (evalPolynomial([6], 42) == 6)
    # f(x) = 6x^2 -2x - 20, f(-1) = -12
    assert (evalPolynomial([6, -2, -20], -1) == -12)
    # f(x) = 6x^5-8x^3-8x, f(2) = 112, f(1) = -10, f(0) = 0
    assert (evalPolynomial([6, 0, -8, 0, -8, 0], 2) == 112)
    assert (evalPolynomial([6, 0, -8, 0, -8, 0], 1) == -10)
    assert (evalPolynomial([6, 0, -8, 0, -8, 0], 0) == 0)
    print("Passed.")


def _verifyMultiplyPolynomialsIsNondestructive():
    a, b = [2], [3]
    c, d = copy.copy(a), copy.copy(b)
    # ignore result, just checking for destructiveness here
    multiplyPolynomials(a, b)
    return (a == c) and (b == d)


def testMultiplyPolynomials():
    print("Testing multiplyPolynomials()...", end="")
    _verifyMultiplyPolynomialsIsNondestructive()
    # (2)*(3) == 6
    assert (multiplyPolynomials([2], [3]) == [6])
    # (2x-4)*(3x+5) == 6x^2 -2x - 20
    assert (multiplyPolynomials([2, -4], [3, 5]) == [6, -2, -20])
    # (2x^2-4)*(3x^3+2x) == (6x^5-8x^3-8x)
    assert (multiplyPolynomials([2, 0, -4],
                                [3, 0, 2, 0]) == [6, 0, -8, 0, -8, 0])
    print("Passed!")


def testSolvesCryptarithm():
    print("Testing solvesCryptarithm()...", end="")
    assert (solvesCryptarithm("SEND + MORE = MONEY", "OMY--ENDRS") == True)
    # from http://www.cryptarithms.com/default.asp?pg=1
    assert (solvesCryptarithm("NUMBER + NUMBER = PUZZLE",
                              "UMNZP-BLER") == True)
    assert (solvesCryptarithm("TILES + PUZZLES = PICTURE",
                              "UISPELCZRT") == True)
    assert (solvesCryptarithm("COCA + COLA = OASIS", "LOS---A-CI") == True)
    assert (solvesCryptarithm("CROSS + ROADS = DANGER", "-DOSEARGNC") == True)

    assert (solvesCryptarithm("SEND + MORE = MONEY", "OMY--ENDR-") == False)
    assert (solvesCryptarithm("SEND + MORE = MONEY", "OMY-ENDRS") == False)
    assert (solvesCryptarithm("SEND + MORE = MONY", "OMY--ENDRS") == False)
    assert (solvesCryptarithm("SEND + MORE = MONEY", "MOY--ENDRS") == False)
    print("Passed!")


def _verifyBestScrabbleScoresIsNondestructive():
    a = ["a", "b", "c"]
    b = [1] * 26
    c = ['b']
    d, e, f = copy.copy(a), copy.copy(b), copy.copy(c)
    bestScrabbleScore(a, b, c)
    return (a == d) and (b == e) and (c == f)


def testBestScrabbleScore():
    print("Testing bestScrabbleScore()...", end="")
    _verifyBestScrabbleScoresIsNondestructive()

    def dictionary1():
        return ["a", "b", "c"]

    def letterScores1():
        return [1] * 26

    def dictionary2():
        return ["xyz", "zxy", "zzy", "yy", "yx", "wow"]

    def letterScores2():
        return [1 + (i % 5) for i in range(26)]

    assert (bestScrabbleScore(dictionary1(), letterScores1(),
                              list("b")) == ("b", 1))
    assert (bestScrabbleScore(dictionary1(), letterScores1(),
                              list("ace")) == (["a", "c"], 1))
    assert (bestScrabbleScore(dictionary1(), letterScores1(),
                              list("b")) == ("b", 1))
    assert (bestScrabbleScore(dictionary1(), letterScores1(),
                              list("z")) == None)
    # x = 4, y = 5, z = 1
    # ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
    #    10     10     7     10    9      -
    assert (bestScrabbleScore(dictionary2(), letterScores2(),
                              list("xyz")) == (["xyz", "zxy"], 10))
    assert (bestScrabbleScore(dictionary2(), letterScores2(),
                              list("xyzy")) == (["xyz", "zxy", "yy"], 10))
    assert (bestScrabbleScore(dictionary2(), letterScores2(),
                              list("xyq")) == ("yx", 9))
    assert (bestScrabbleScore(dictionary2(), letterScores2(),
                              list("yzz")) == ("zzy", 7))
    assert (bestScrabbleScore(dictionary2(), letterScores2(),
                              list("wxz")) == None)
    print("Passed!")


def testRunSimpleProgram():
    print("Testing runSimpleProgram()...", end="")
    largest = """! largest: Returns max(A0, A1)
                   L0 - A0 A1
                   JMP+ L0 a0
                   RTN A1
                   a0:
                   RTN A0"""
    assert (runSimpleProgram(largest, [5, 6]) == 6)
    assert (runSimpleProgram(largest, [6, 5]) == 6)

    sumToN = """! SumToN: Returns 1 + ... + A0
                ! L0 is a counter, L1 is the result
                L0 0
                L1 0
                loop:
                L2 - L0 A0
                JMP0 L2 done
                L0 + L0 1
                L1 + L1 L0
                JMP loop
                done:
                RTN L1"""
    assert (runSimpleProgram(sumToN, [5]) == 1 + 2 + 3 + 4 + 5)
    assert (runSimpleProgram(sumToN, [10]) == 10 * 11 // 2)
    print("Passed!")


def testAllSublists():
    print('  Testing allSublists()...', end='')

    def f():
        yield 42

    assert (type(allSublists([1, 2, 3])) == type(f()))  # generator
    assert (sorted(allSublists([1])) == [[], [1]])
    assert (sorted(allSublists([3, 5])) == [[], [3], [3, 5], [5]])
    assert (sorted(allSublists([6, 7, 8])) == [[], [6], [6, 7], [6, 7, 8],
                                               [6, 8], [7], [7, 8], [8]])
    print('Passed!')


def testSolveSubsetSum():
    def checkSubsetSum(L):
        solution = solveSubsetSum(L)
        for v in solution:
            assert (solution.count(v) <= L.count(v))
        assert (sum(solution) == 0)

    print('  Testing solveSubsetSum()...', end='')
    assert (solveSubsetSum([5, 2, 3, -4]) == None)
    checkSubsetSum([-1, 5, 2, 3, -4])
    checkSubsetSum([8, 19, 31, 27, 52, -70, 4])
    print('Passed!')


def testHeapsAlgorithmForPermutations():
    print('  Testing heapsAlgorithmForPermutations()...', end='')

    def f():
        yield 42

    assert (type(heapsAlgorithmForPermutations([1])) == type(f()))  # generator
    assert (sorted(heapsAlgorithmForPermutations([1])) == [[1]])
    assert (sorted(heapsAlgorithmForPermutations([1, 2])) == [[1, 2], [2, 1]])
    assert (sorted(heapsAlgorithmForPermutations([3, 1, 2])) == [[1, 2, 3],
                                                                 [1, 3, 2],
                                                                 [2, 1, 3],
                                                                 [2, 3, 1],
                                                                 [3, 1, 2],
                                                                 [3, 2, 1]])
    print('Passed!')


def testSolveCryptarithmWithMaxDigit():
    print('  Testing solveCryptarithmWithMaxDigit()...', end='')
    assert (solveCryptarithmWithMaxDigit('RAM + RAT = ANT', 4) == '''\
RAM + RAT = ANT
120 + 123 = 243''')
    assert (solveCryptarithmWithMaxDigit('ANT + CAT = EEL', 4) == None)
    assert (solveCryptarithmWithMaxDigit('ANT + CAT = EEL', 5) == '''\
ANT + CAT = EEL
125 + 315 = 440''')
    print('Passed!')


def testGetAllSingletonCryptarithmsWithMaxDigit():
    print('  Testing getAllSingletonCryptarithmsWithMaxDigit()...', end='')
    words = ['EEL', 'RAM', 'CAT', 'BEE', 'FLY', 'HEN', 'RAT', 'DOG', 'ANT']
    assert (getAllSingletonCryptarithmsWithMaxDigit(words, 3) == '')
    assert (getAllSingletonCryptarithmsWithMaxDigit(words, 4) == '''\
RAM + RAT = ANT
120 + 123 = 243''')
    assert (getAllSingletonCryptarithmsWithMaxDigit(words, 5) == '''\
ANT + CAT = EEL
125 + 315 = 440
ANT + CAT = HEN
105 + 315 = 420
ANT + RAT = EEL
125 + 315 = 440
ANT + RAT = HEN
105 + 315 = 420
BEE + EEL = FLY
411 + 112 = 523''')

    words = [
        'DEER', 'BEAR', 'GOAT', 'MULE', 'PUMA', 'COLT', 'ORCA', 'IBEX', 'LION',
        'WOLF'
    ]
    assert (getAllSingletonCryptarithmsWithMaxDigit(words, 5) == '')
    assert (getAllSingletonCryptarithmsWithMaxDigit(words, 6) == '''\
BEAR + DEER = IBEX
4203 + 1223 = 5426
COLT + GOAT = ORCA
4635 + 1605 = 6240''')
    print('Passed!')


def testBonusCombinatoricsProblems():
    print('Testing bonus combinatorics problems...')
    testAllSublists()
    testSolveSubsetSum()
    testHeapsAlgorithmForPermutations()
    testSolveCryptarithmWithMaxDigit()
    testGetAllSingletonCryptarithmsWithMaxDigit()
    print('Passed!')


#################################################
# testAll and main
#################################################


def testAll():
    # comment out the tests you do not wish to run!
    # testDestructiveRemoveEvens()
    # testNondestructiveRemoveEvens()
    # testAreaOfPolygon()
    # testEvalPolynomial()
    # testMultiplyPolynomials()
    # testSolvesCryptarithm()
    # testBestScrabbleScore()

    # bonus
    # testRunSimpleProgram()
    # testBonusCombinatoricsProblems()
    pass


def main():
    cs112_s21_week6_linter.lint()
    testAll()


if __name__ == '__main__':
    main()
