#################################################
# extra_practice1ab.py
#################################################

import math, decimal

import cs112_s21_week1_linter

#################################################
# Helper functions
#################################################


def almostEqual(d1, d2, epsilon=10**-7):  # helper-fn
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)


def roundHalfUp(d):  # helper-fn
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))


#################################################
# functions for you to write
#################################################

# ============================================================================ #
# Previous Quizzes


# F20
def isDoubly(n):
    # the left two digits match the right two digits in the same order
    # 1212
    if type(n) != int: return "not an int"
    n = abs(n)
    if n >= 10000: return "too many digits"
    elif 0 < n < 1000: return "not enough digits"

    step = 100
    n_left = n // step
    n_right = n % step
    return n_left == n_right


# S20
def splitPower(x, n):
    if type(x) != int or type(n) != int: return "not int"
    sign = x
    x = abs(x)

    step = 10**n
    left = x // step
    right = x % step
    new = left**right
    return -new if sign < 0 and right % 2 != 0 else new


# F19
def largestPerfectSquare(n):
    return (int(n**0.5))**2


# ============================================================================ #
#


def distance(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


def circlesIntersect(x1, y1, r1, x2, y2, r2):
    dist = distance(x1, y1, x2, y2)
    return dist <= r1 + r2


def getInRange(x, bound1, bound2):
    n_min, n_max = min(bound1, bound2), max(bound1, bound2)
    if x > n_max: return n_max
    elif x < n_min: return n_min
    else: return x


def isFactor(f, n):
    if type(f) != int or type(n) != int: return False
    if n == 0: return True
    else:
        if f == 0: return False
        return n % f == 0


def isFactorish(n):  # n as abc
    if type(n) != int or abs(n) > 1000: return False
    n = abs(n)
    c = n % 10
    b = n // 10 % 10
    a = n // 100 % 10

    no_dupli = (a != b != c)
    all_factor = (a != 0 and n % a == 0) and\
                 (b != 0 and n % b == 0) and\
                 (c != 0 and n % c == 0)
    return True if (no_dupli and all_factor) else False


def isMultiple(m, n):
    if type(m) != int or type(n) != int: return False
    if n == 0:
        if m == 0: return True
        else: return False
    return m % n == 0


def isLegalTriangle(s1, s2, s3):
    if not (s1 > 0 and s2 > 0 and s3 > 0): return False
    s_max = max(s1, s2, s3)
    return s1 + s2 + s3 > s_max * 2  # s_min + s_mid > s_max


def isRightTriangle(x1, y1, x2, y2, x3, y3):
    ab = distance(x1, y1, x2, y2)
    ac = distance(x1, y1, x3, y3)
    bc = distance(x2, y2, x3, y3)
    s_max, s_min = max(ab, ac, bc), min(ab, ac, bc)
    s_mid = (ab + ac + bc) - s_min - s_max
    return almostEqual(s_min**2 + s_mid**2, s_max**2)


def eggCartons(eggs):
    # return math.ceil(eggs / 12)
    return eggs // 12 if eggs % 12 == 0 else eggs // 12 + 1


def isEvenPositiveInt(x):
    if type(x) != int or x <= 0: return False
    return x % 2 == 0


def nthFibonacciNumber(nth):
    Phi = (1 + 5**0.5) / 2  # Binet's Fibonacci Number Formula
    #Binet = ((1+math.sqrt(5))**n-(1-math.sqrt(5))**n)/(2**n*math.sqrt(5))
    nth += 1
    Binet = int((Phi**nth - (-Phi)**-nth) / 5**0.5)
    return Binet


def isPerfectSquare(n):
    if type(n) != int or n < 0: return False
    return n**0.5 == int(n**0.5)


def nearestOdd(n):
    floor, ceil = math.floor(n), math.ceil(n)  # 3.5, 4.5
    if n % 2 == 0: return n - 1
    else: return floor if floor % 2 != 0 else ceil


def getKthDigit(n, kth):
    n = abs(n)
    return (n // 10**kth) % 10


def setKthDigit(n, k, d):
    n_temp = abs(n)
    rem = getKthDigit(n_temp, k) * 10**k
    n_new = d * 10**k + (n_temp - rem)
    return n_new if n >= 0 else -n_new


#################################################
# Test Functions
#################################################


def test_isDoubly():
    # print(isDoubly(1.212))  # not an int
    # print(isDoubly('wow'))  # also not an int
    # print(isDoubly(66666))  # too many digits
    # print(isDoubly(333))   # not enough digits
    # print(isDoubly(-424))  # not enough digits
    # print(isDoubly(1212))
    # print(isDoubly(3838))
    # print(isDoubly(9999))
    # print(isDoubly(-4242))  # negatives are ok
    # print(isDoubly(1221))  # 12 != 21
    # print(isDoubly(1122))  # 11 != 22
    pass


def test_splitPower():
    assert (splitPower(23, 1)) == 8  # 2**3
    assert (splitPower(123, 2)) == 1  # 1**24
    assert (splitPower(-902, 2)) == 81  # (-9)**2


def test_largestPerfectSquare():
    assert (largestPerfectSquare(24) == 16)
    assert (largestPerfectSquare(25) == 25)
    assert (largestPerfectSquare(26) == 25)


# ============================================================================ #
#


def testDistance():
    print('Testing distance()... ', end='')
    assert (almostEqual(distance(0, 0, 3, 4), 5))
    assert (almostEqual(distance(-1, -2, 3, 1), 5))
    assert (almostEqual(distance(-.5, .5, .5, -.5), 2**0.5))
    print('Passed.')


def testCirclesIntersect():
    print('Testing circlesIntersect()... ', end='')
    assert (circlesIntersect(0, 0, 2, 3, 0, 2) == True)
    assert (circlesIntersect(0, 0, 2, 4, 0, 2) == True)
    assert (circlesIntersect(0, 0, 2, 5, 0, 2) == False)
    assert (circlesIntersect(3, 3, 3, 3, -3, 3) == True)
    assert (circlesIntersect(3, 3, 3, 3, -3, 2.99) == False)
    print('Passed.')


def testGetInRange():
    print('Testing getInRange()... ', end='')
    assert (getInRange(5, 1, 10) == 5)
    assert (getInRange(5, 5, 10) == 5)
    assert (getInRange(5, 9, 10) == 9)
    assert (getInRange(5, 10, 10) == 10)
    assert (getInRange(5, 10, 1) == 5)
    assert (getInRange(5, 10, 5) == 5)
    assert (getInRange(5, 10, 9) == 9)
    assert (getInRange(0, -20, -30) == -20)
    assert (almostEqual(getInRange(0, -20.25, -30.33), -20.25))
    print('Passed.')


def testIsFactor():
    print('Testing isFactor()... ', end='')
    assert (isFactor(1, 1) == True)
    assert (isFactor(2, 10) == True)
    assert (isFactor(-5, 25) == True)
    assert (isFactor(5, 0) == True)
    assert (isFactor(0, 0) == True)
    assert (isFactor(2, 11) == False)
    assert (isFactor(10, 2) == False)
    assert (isFactor(0, 5) == False)
    print('Passed.')


def testIsFactorish():
    print('Testing isFactorish()...', end='')
    assert (isFactorish(412) == True)  # 4, 1, and 2 are all factors of 412
    assert (isFactorish(-412) == True)  # Must work for negative numbers!
    assert (isFactorish(4128) == False)  # has more than 3 digits
    assert (isFactorish(112) == False)  # has duplicates digits (two 1's)
    assert (isFactorish(420) == False)  # has a 0 (no 0's allowed)
    assert (isFactorish(42) == False)  # has a leading 0 (no 0's allowed)
    assert (isFactorish(1.0) == False)  # floats are not factorish
    assert (isFactorish('nope!') == False)  # don't crash on strings
    print('Passed!')


def testIsMultiple():
    print('Testing isMultiple()... ', end='')
    assert (isMultiple(1, 1) == True)
    assert (isMultiple(2, 10) == False)
    assert (isMultiple(-5, 25) == False)
    assert (isMultiple(5, 0) == False)
    assert (isMultiple(0, 0) == True)
    assert (isMultiple(2, 11) == False)
    assert (isMultiple(10, 2) == True)
    assert (isMultiple(0, 5) == True)
    assert (isMultiple(25, -5) == True)
    print('Passed.')


def testIsLegalTriangle():
    print('Testing isLegalTriangle()... ', end='')
    assert (isLegalTriangle(3, 4, 5) == True)
    assert (isLegalTriangle(5, 4, 3) == True)
    assert (isLegalTriangle(3, 5, 4) == True)
    assert (isLegalTriangle(0.3, 0.4, 0.5) == True)
    assert (isLegalTriangle(3, 4, 7) == False)
    assert (isLegalTriangle(7, 4, 3) == False)
    assert (isLegalTriangle(3, 7, 4) == False)
    assert (isLegalTriangle(5, -3, 1) == False)
    assert (isLegalTriangle(-3, -4, -5) == False)
    print('Passed.')


def testIsRightTriangle():
    print('Testing isRightTriangle()... ', end='')
    assert (isRightTriangle(0, 0, 0, 3, 4, 0) == True)
    assert (isRightTriangle(1, 1.3, 1.4, 1, 1, 1) == True)
    assert (isRightTriangle(9, 9.12, 8.95, 9, 9, 9) == True)
    assert (isRightTriangle(0, 0, 0, math.pi, math.e, 0) == True)
    assert (isRightTriangle(0, 0, 1, 1, 2, 0) == True)
    assert (isRightTriangle(0, 0, 1, 2, 2, 0) == False)
    assert (isRightTriangle(1, 0, 0, 3, 4, 0) == False)
    print('Passed.')


def testEggCartons():
    print('Testing eggCartons()... ', end='')
    assert (eggCartons(0) == 0)
    assert (eggCartons(1) == 1)
    assert (eggCartons(12) == 1)
    assert (eggCartons(13) == 2)
    assert (eggCartons(24) == 2)
    assert (eggCartons(25) == 3)
    print('Passed.')


def testIsEvenPositiveInt():
    print('Testing isEvenPositiveInt()... ', end='')
    assert (isEvenPositiveInt(809) == False)
    assert (isEvenPositiveInt(810) == True)
    assert (isEvenPositiveInt(2389238001) == False)
    assert (isEvenPositiveInt(2389238000) == True)
    assert (isEvenPositiveInt(-2389238000) == False)
    assert (isEvenPositiveInt(0) == False)
    assert (isEvenPositiveInt('do not crash here!') == False)
    print('Passed.')


def testNthFibonacciNumber():
    print('Testing nthFibonacciNumber()... ', end='')
    assert (nthFibonacciNumber(0) == 1)
    assert (nthFibonacciNumber(1) == 1)
    assert (nthFibonacciNumber(2) == 2)
    assert (nthFibonacciNumber(3) == 3)
    assert (nthFibonacciNumber(4) == 5)
    assert (nthFibonacciNumber(5) == 8)
    assert (nthFibonacciNumber(6) == 13)
    print('Passed.')


def testIsPerfectSquare():
    print('Testing isPerfectSquare()... ', end='')
    assert (isPerfectSquare(0) == True)
    assert (isPerfectSquare(1) == True)
    assert (isPerfectSquare(16) == True)
    assert (isPerfectSquare(1234**2) == True)
    assert (isPerfectSquare(15) == False)
    assert (isPerfectSquare(17) == False)
    assert (isPerfectSquare(-16) == False)
    assert (isPerfectSquare(1234**2 + 1) == False)
    assert (isPerfectSquare(1234**2 - 1) == False)
    assert (isPerfectSquare(4.0000001) == False)
    assert (isPerfectSquare('Do not crash here!') == False)
    print('Passed.')


def testNearestOdd():
    print('Testing nearestOdd()... ', end='')
    assert (nearestOdd(13.0) == 13)
    assert (nearestOdd(12.001) == 13)
    assert (nearestOdd(12) == 11)
    assert (nearestOdd(11.999) == 11)
    assert (nearestOdd(-13) == -13)
    assert (nearestOdd(-12.001) == -13)
    assert (nearestOdd(-12) == -13)
    assert (nearestOdd(-11.999) == -11)
    # results must be int's not floats
    assert (isinstance(nearestOdd(13.0), int))
    assert (isinstance(nearestOdd(11.999), int))
    print('Passed.')


def testGetKthDigit():
    print('Testing getKthDigit()... ', end='')
    assert (getKthDigit(809, 0) == 9)
    assert (getKthDigit(809, 1) == 0)
    assert (getKthDigit(809, 2) == 8)
    assert (getKthDigit(809, 3) == 0)
    assert (getKthDigit(0, 100) == 0)
    assert (getKthDigit(-809, 0) == 9)
    print('Passed.')


def testSetKthDigit():
    print('Testing setKthDigit()... ', end='')
    #print(getKthDigit(321, 0))
    #print(getKthDigit(321, 5))
    #print(getKthDigit(-321, 5))
    #print(setKthDigit(468, 0, 1))
    #print(setKthDigit(468, 1, 1))
    #print(setKthDigit(468, 2, 1))
    #print(setKthDigit(468, 3, 1))
    assert (setKthDigit(809, 0, 7) == 807)
    assert (setKthDigit(809, 1, 7) == 879)
    assert (setKthDigit(809, 2, 7) == 709)
    assert (setKthDigit(809, 3, 7) == 7809)
    assert (setKthDigit(0, 4, 7) == 70000)
    assert (setKthDigit(-809, 0, 7) == -807)
    print('Passed.')


#################################################
# testAll and main
#################################################


def testAll():
    # Previous Quizzes
    test_isDoubly()
    test_splitPower()
    test_largestPerfectSquare()

    # 2021
    testDistance()
    testCirclesIntersect()
    testGetInRange()
    testIsFactor()
    testIsFactorish()
    testIsMultiple()
    testIsLegalTriangle()
    testIsRightTriangle()
    testEggCartons()
    testIsEvenPositiveInt()
    testNthFibonacciNumber()
    testIsPerfectSquare()
    testNearestOdd()
    testGetKthDigit()
    testSetKthDigit()


def main():
    cs112_s21_week1_linter.lint()
    testAll()


if __name__ == '__main__':
    main()
