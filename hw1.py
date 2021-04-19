#################################################
# hw1.py
# name:
# andrew id:
#################################################

import cs112_s21_week1_linter
import math

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


#################################################
# hw1-standard-functions
#################################################


def fabricYards(inches):
    return math.ceil(inches / 36)


def fabricExcess(inches):
    return fabricYards(inches) * 36 - inches


def nearestBusStop(street):
    dist = street / 8 - street // 8
    step = 0 if dist <= 0.5 else 1
    return (street // 8 + step) * 8


def numberOfPoolBalls(rows):
    return rows * (1 + rows) / 2


def numberOfPoolBallRows(balls):
    a, b = 1, 1
    c = -2 * balls
    x = a * (-b + (b**2 - 4 * a * c)**0.5) / 2  # ((8*balls+1)**0.5-1)/2
    return math.ceil(x)


#################################################
# hw1-spicy-functions
# you can do these instead of the hw1-standard
# functions if you prefer.  Otherwise, you can
# skip the hw1-spicy functions.  Either way,
# you should continue on to the hw1-required
# functions below.
#################################################


def handToDice(hand):  # 123
    c = hand % 10
    b = hand // 10 % 10
    a = hand // 100 % 10
    return a, b, c


def diceToOrderedHand(a, b, c):
    foo = max(a, b, c) * 100 + min(a, b, c)
    mid = a + b + c - max(a, b, c) - min(a, b, c)
    return foo + mid * 10


def playStep2(hand, dice):
    dice1 = dice % 10
    dice2 = dice // 10 % 10
    a, b, c = handToDice(hand)
    match2 = a == b or a == c or b == c

    if match2:
        if a == b: c = dice1
        elif a == c: b = dice1
        else: a = dice1
        dice //= 10
    if not match2:
        a = max(a, b, c)
        b = dice1
        c = dice2
        dice //= 100
    hand = diceToOrderedHand(a, b, c)
    #print(a, b, c, hand, dice)
    return hand, dice


def score(hand):
    a, b, c = handToDice(hand)
    if a == b and b == c:
        foo = 20 + a * 3
    elif a == b or a == c:
        foo = 10 + a * 2
    elif b == c:
        foo = 10 + b * 2
    else:
        foo = max(a, b, c)
    #print(foo)
    return foo


def playThreeDiceYahtzee(dice):
    a, b, c = handToDice(dice)
    hand = diceToOrderedHand(a, b, c)
    dice //= 1000
    if a == b and b == c: return hand, score(hand)

    hand, dice = playStep2(hand, dice)  #s21
    hand, dice = playStep2(hand, dice)  #s22
    return hand, score(hand)


#################################################
# hw1-required-functions
#################################################


def rectanglesOverlap(x1, y1, w1, h1, x2, y2, w2, h2):
    r1 = x1 + w1
    b1 = y1 + h1
    r2 = x2 + w2
    b2 = y2 + h2
    cond1 = r1 < x2
    cond2 = x1 > r2
    cond3 = b1 < y2
    cond4 = y1 > b2
    overlap = not (cond1 or cond2 or cond3 or cond4)
    #print("re:", overlap)
    return overlap


def getIntersect(a1, c1, a2, c2):
    # parameter用别的var就不容易乱了
    #x = (b1-b2)/(m2-m1)
    #y = m1*x+b1
    #a1*x+b1*y+c1 = 0
    b1 = -1
    b2 = -1
    x = (b1 * c2 - b2 * c1) / (a1 * b2 - a2 * b1)
    #y = (a2*c1-a1*c2)/(a1*b2-a2*b1)
    #y = m1*x + b1
    y = a1 * x + c1
    #print(x, y)
    return x, y


def getDistance(x1, y1, x2, y2):
    foo = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return foo


def threeLinesArea(m1, b1, m2, b2, m3, b3):
    #y = m1*x + b1
    x1, y1 = getIntersect(m1, b1, m2, b2)
    x2, y2 = getIntersect(m1, b1, m3, b3)
    x3, y3 = getIntersect(m2, b2, m3, b3)
    #print("tuple:", x1, y1, x2, y2, x3, y3)
    a = getDistance(x1, y1, x2, y2)
    b = getDistance(x1, y1, x3, y3)
    c = getDistance(x2, y2, x3, y3)
    #print(a, b, c)
    #x12 = (b1-b2)/(m2-m1)
    #y12 = m1*x12 + b1
    #x13 = (b1-b3)/(m3-m1)
    #y13 = m1*x13 + b1
    #x23 = (b2-b3)/(m3-m2)
    #y23 = m2*x23 + b2

    #a = math.sqrt((x12-x13)**2+(y12-y13)**2)
    #b = math.sqrt((x13-x23)**2+(y13-y23)**2)
    #c = math.sqrt((x12-x23)**2+(y12-y23)**2)
    #print("wid:", a)
    #print("wid:", c)
    #print("wid:", b)
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    #print("area:", area)
    return area


#################################################
# hw1-bonus-functions
# these are optional
#################################################


def colorBlender(rgb1, rgb2, midpoints, n):
    return 42


def findIntRootsOfCubic(a, b, c, d):
    return 42


#################################################
# Test Functions
#################################################


def testFabricYards():
    print('Testing fabricYards()... ', end='')
    assert (fabricYards(0) == 0)
    assert (fabricYards(1) == 1)
    assert (fabricYards(35) == 1)
    assert (fabricYards(36) == 1)
    assert (fabricYards(37) == 2)
    assert (fabricYards(72) == 2)
    assert (fabricYards(73) == 3)
    assert (fabricYards(108) == 3)
    assert (fabricYards(109) == 4)
    print('Passed.')


def testFabricExcess():
    print('Testing fabricExcess()... ', end='')
    assert (fabricExcess(0) == 0)
    assert (fabricExcess(1) == 35)
    assert (fabricExcess(35) == 1)
    assert (fabricExcess(36) == 0)
    assert (fabricExcess(37) == 35)
    assert (fabricExcess(72) == 0)
    assert (fabricExcess(73) == 35)
    assert (fabricExcess(108) == 0)
    assert (fabricExcess(109) == 35)
    print('Passed.')


def testNearestBusStop():
    print('Testing nearestBusStop()... ', end='')
    assert (nearestBusStop(0) == 0)
    assert (nearestBusStop(4) == 0)
    assert (nearestBusStop(5) == 8)
    assert (nearestBusStop(12) == 8)
    assert (nearestBusStop(13) == 16)
    assert (nearestBusStop(20) == 16)
    assert (nearestBusStop(21) == 24)
    print('Passed.')


def testNumberOfPoolBalls():
    print('Testing numberOfPoolBalls()... ', end='')
    assert (numberOfPoolBalls(0) == 0)
    assert (numberOfPoolBalls(1) == 1)
    assert (numberOfPoolBalls(2) == 3)  # 1+2 == 3
    assert (numberOfPoolBalls(3) == 6)  # 1+2+3 == 6
    assert (numberOfPoolBalls(10) == 55)  # 1+2+...+10 == 55
    print('Passed.')


def testNumberOfPoolBallRows():
    print('Testing numberOfPoolBallRows()... ', end='')
    assert (numberOfPoolBallRows(0) == 0)
    assert (numberOfPoolBallRows(1) == 1)
    assert (numberOfPoolBallRows(2) == 2)
    assert (numberOfPoolBallRows(3) == 2)
    assert (numberOfPoolBallRows(4) == 3)
    assert (numberOfPoolBallRows(6) == 3)
    assert (numberOfPoolBallRows(7) == 4)
    assert (numberOfPoolBallRows(10) == 4)
    assert (numberOfPoolBallRows(11) == 5)
    assert (numberOfPoolBallRows(55) == 10)
    assert (numberOfPoolBallRows(56) == 11)
    print('Passed.')


def testPlayThreeDiceYahtzee():
    print('Testing playThreeDiceYahtzee()...', end='')
    assert (handToDice(123) == (1, 2, 3))
    assert (handToDice(214) == (2, 1, 4))
    assert (handToDice(422) == (4, 2, 2))
    assert (diceToOrderedHand(1, 2, 3) == 321)
    assert (diceToOrderedHand(6, 5, 4) == 654)
    assert (diceToOrderedHand(1, 4, 2) == 421)
    assert (diceToOrderedHand(6, 5, 6) == 665)
    assert (diceToOrderedHand(2, 2, 2) == 222)
    assert (playStep2(413, 2312) == (421, 23))
    assert (playStep2(421, 23) == (432, 0))
    assert (playStep2(413, 2345) == (544, 23))
    assert (playStep2(544, 23) == (443, 2))
    assert (playStep2(544, 456) == (644, 45))
    assert (score(432) == 4)
    assert (score(532) == 5)
    assert (score(443) == 10 + 4 + 4)
    assert (score(633) == 10 + 3 + 3)
    assert (score(333) == 20 + 3 + 3 + 3)
    assert (score(555) == 20 + 5 + 5 + 5)
    assert (playThreeDiceYahtzee(2312413) == (432, 4))
    assert (playThreeDiceYahtzee(2315413) == (532, 5))
    assert (playThreeDiceYahtzee(2345413) == (443, 18))
    assert (playThreeDiceYahtzee(2633413) == (633, 16))
    assert (playThreeDiceYahtzee(2333413) == (333, 29))
    assert (playThreeDiceYahtzee(2333555) == (555, 35))
    print('Passed!')


def testRectanglesOverlap():
    print('Testing rectanglesOverlap()...', end='')
    assert (rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 2) == True)
    assert (rectanglesOverlap(1, 1, 2, 2, -2, -2, 6, 6) == True)
    assert (rectanglesOverlap(1, 1, 2, 2, 3, 3, 1, 1) == True)
    assert (rectanglesOverlap(1, 1, 2, 2, 3.1, 3, 1, 1) == False)
    assert (rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 1.9) == False)
    assert (rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 2) == True)
    assert (rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 6) == True)
    assert (rectanglesOverlap(1, 1, 2, 2, 3, 4, 5, 6) == False)
    print('Passed.')


def testThreeLinesArea():
    print('Testing threeLinesArea()... ', end='')
    assert (almostEqual(threeLinesArea(1, 2, 3, 4, 5, 6), 0))
    assert (almostEqual(threeLinesArea(0, 7, 1, 0, -1, 2), 36))
    assert (almostEqual(threeLinesArea(0, 3, -.5, -5, 1, 3),
                        42.66666666666666))
    assert (almostEqual(threeLinesArea(1, -5, 0, -2, 2, 2), 25))
    assert (almostEqual(threeLinesArea(0, -9.75, -6, 2.25, 1, -4.75), 21))
    assert (almostEqual(threeLinesArea(1, -5, 0, -2, 2, 25), 272.25))
    print('Passed.')


def testColorBlender():
    print('Testing colorBlender()... ', end='')
    # http://meyerweb.com/eric/tools/color-blend/#Ddice43C:BDFCC9:3:rgbd
    assert (colorBlender(220020060, 189252201, 3, -1) == None)
    assert (colorBlender(220020060, 189252201, 3, 0) == 220020060)
    assert (colorBlender(220020060, 189252201, 3, 1) == 212078095)
    assert (colorBlender(220020060, 189252201, 3, 2) == 205136131)
    assert (colorBlender(220020060, 189252201, 3, 3) == 197194166)
    assert (colorBlender(220020060, 189252201, 3, 4) == 189252201)
    assert (colorBlender(220020060, 189252201, 3, 5) == None)
    # http://meyerweb.com/eric/tools/color-blend/#0100FF:FF0280:2:rgbd
    assert (colorBlender(1000255, 255002128, 2, -1) == None)
    assert (colorBlender(1000255, 255002128, 2, 0) == 1000255)
    assert (colorBlender(1000255, 255002128, 2, 1) == 86001213)
    assert (colorBlender(1000255, 255002128, 2, 2) == 170001170)
    assert (colorBlender(1000255, 255002128, 2, 3) == 255002128)
    print('Passed.')


def getCubicCoeffs(k, root1, root2, root3):  #helper-fn
    # helper function for testFindIntRootsOfCubic
    # Given roots e,f,g and vertical scale k, we can find
    # the coefficients a,b,c,d as such:
    # k(x-e)(x-f)(x-g) =
    # k(x-e)(x^2 - (f+g)x + fg)
    # kx^3 - k(e+f+g)x^2 + k(ef+fg+eg)x - kefg
    e, f, g = root1, root2, root3
    return k, -k * (e + f + g), k * (e * f + f * g + e * g), -k * e * f * g


def testFindIntRootsOfCubicCase(k, z1, z2, z3):  #helper-fn
    # helper function for testFindIntRootsOfCubic
    a, b, c, d = getCubicCoeffs(k, z1, z2, z3)
    result1, result2, result3 = findIntRootsOfCubic(a, b, c, d)
    m1 = min(z1, z2, z3)
    m3 = max(z1, z2, z3)
    m2 = (z1 + z2 + z3) - (m1 + m3)
    actual = (m1, m2, m3)
    assert (almostEqual(m1, result1))
    assert (almostEqual(m2, result2))
    assert (almostEqual(m3, result3))


def testFindIntRootsOfCubic():
    print('Testing findIntRootsOfCubic()...', end='')
    testFindIntRootsOfCubicCase(5, 1, 3, 2)  #helper-fn
    testFindIntRootsOfCubicCase(2, 5, 33, 7)  #helper-fn
    testFindIntRootsOfCubicCase(-18, 24, 3, -8)  #helper-fn
    testFindIntRootsOfCubicCase(1, 2, 3, 4)  #helper-fn
    print('Passed.')


#################################################
# testAll and main
#################################################


def testAll():
    # comment out the tests you do not wish to run!
    testFabricYards()
    testFabricExcess()
    testNearestBusStop()
    testNumberOfPoolBalls()
    testNumberOfPoolBallRows()
    testPlayThreeDiceYahtzee()
    testRectanglesOverlap()
    testThreeLinesArea()
    #testColorBlender()
    #testFindIntRootsOfCubic()


def main():
    cs112_s21_week1_linter.lint()
    testAll()


if __name__ == '__main__':
    main()
