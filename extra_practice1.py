#################################################
# extra_practice1ab.py
#################################################

import decimal
import cs112_s21_week1_linter
import math

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


def distance(x1, y1, x2, y2):
    foo = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return foo


def circlesIntersect(x1, y1, r1, x2, y2, r2):
    dist = distance(x1, y1, x2, y2)
    r = r1 + r2
    if dist <= r:
        return True
    else:
        return False


def getInRange(x, bound1, bound2):
    foo = min(bound1, bound2)
    bar = max(bound1, bound2)
    #print(x, "in", foo, bar)
    if x > bar:
        return bar
    elif x < foo:
        return foo
    else:
        return x


def isFactor(f, n):
    if type(f) != int or type(n) != int:
        return False
    if n == 0:
        return True
    elif f == 0:
        return False
    else:
        foo = n / f
        bar = n // f
        paz = n % f
        # if foo - bar == 0: return True
        #print(foo, bar, "|", paz)
        if paz == 0:
            return True
        else:
            return False


def isFactorish(n):
    # n as abc
    if type(n) != int or abs(n) > 1000:
        return False
    foo = abs(n)
    c = foo % 10
    foo = foo // 10
    b = foo % 10
    foo = foo // 10
    a = foo % 10
    #print(a, b, c)
    if a == 0 or b == 0 or c == 0:
        return False
    if a != b and a != c and b != c:
        return True
    else:
        return False


def isMultiple(m, n):
    if type(m) != int or type(n) != int:
        return False
    if n == 0:
        if m == 0:
            return True
        else:
            return False
    #foo = (m/n)%1
    foo = (m % n)
    if foo == 0:
        return True
    else:
        return False


def isLegalTriangle(s1, s2, s3):
    if s1 <= 0 or s2 <= 0 or s3 <= 0:
        return False
    c = max(s1, s2, s3)
    if s1 + s2 + s3 - c > c:
        return True
    else:
        return False


def getdistance(x1, y1, x2, y2):
    return 42


def isRightTriangle(x1, y1, x2, y2, x3, y3):
    ab = distance(x1, y1, x2, y2)
    ac = distance(x1, y1, x3, y3)
    bc = distance(x2, y2, x3, y3)
    c = max(ab, ac, bc)
    a = min(ab, ac, bc)
    b = ab + ac + bc - a - c
    #print(a, b, c)
    if almostEqual(a**2 + b**2, c**2):
        return True
    else:
        return False


def eggCartons(eggs):
    foo = math.ceil(eggs / 12)
    # print(foo)
    return foo


def isEvenPositiveInt(x):
    if type(x) != int:
        return False
    if x <= 0:
        return False
    elif x % 2 == 0:
        return True
    else:
        return False


def nthFibonacciNumber(n):
    Phi = (1 + math.sqrt(5)) / 2
    #Binet = ((1+math.sqrt(5))**n-(1-math.sqrt(5))**n)/(2**n*math.sqrt(5))
    n += 1
    Binet = (Phi**n - (-Phi)**-n) / math.sqrt(5)
    Binet = math.floor(Binet)
    return Binet


def isPerfectSquare(n):
    if type(n) != int or n < 0:
        return False
    foo = math.sqrt(n)
    #bar = int(foo)-foo
    bar = math.ceil(foo) - math.floor(foo)
    if bar == 0:
        return True
    else:
        return False


def nearestOdd(n):
    foo = math.floor(n)
    bar = math.ceil(n)
    #print(n, end=": ")
    if n % 2 == 0:
        n = n - 1
    if foo % 2 != 0:
        n = foo
    if bar % 2 != 0:
        n = bar
    #print(foo, bar)
    return n


def getKthDigit(n, k):
    n = abs(n)
    return n // 10**k % 10


def setKthDigit(n, k, d):
    negative = n < 0
    n = abs(n)
    rem = getKthDigit(n, k) * 10**k
    foo = d * 10**k + n - rem
    if negative:
        foo = -foo
    return foo


#################################################
# quiz older
#################################################
# fall-20/15-112/notes/quiz1a.html


def isDoubly(n):
    if type(n) != int:
        return "not an int"
    n = abs(n)
    if n >= 10000:
        return "too many digits"
    if 0 < n < 1000:
        return "not enough digits"
    foo = n // 100
    bar = n - foo * 100
    cond = foo == bar
    #print(foo, bar, cond)
    if cond:
        return True
    elif not cond:
        return False


# spring-20/15-112/notes/quiz1a.pdf


def splitPower(x, n):
    negative = x < 0
    x = abs(x)
    x // 10
    # base =
    # pow =
    # return 42


#################################################
# Test Functions
#################################################


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
    # comment out the tests you do not wish to run!
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
    #print(getKthDigit(321, 0))
    #print(getKthDigit(321, 5))
    #print(getKthDigit(-321, 5))
    #print(setKthDigit(468, 0, 1))
    #print(setKthDigit(468, 1, 1))
    #print(setKthDigit(468, 2, 1))
    #print(setKthDigit(468, 3, 1))
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
    # print(splitPower(23, 1)) # 2**3 == 8
    # print(splitPower(123, 2)) # 1**23 == 1
    # print(splitPower(-902, 2)) # (-9)**2 == 81


if __name__ == '__main__':
    main()
