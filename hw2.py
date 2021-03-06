#################################################
# hw2.py
# name:
# andrew id:
#################################################

import decimal, math
from sys import prefix, setprofile
from icecream import ic

import cs112_s21_week2_linter
from extra_practice1 import getKthDigit
from extra_practice1 import setKthDigit

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
# hw2-standard-functions
#################################################


def longestDigitRun(n):
    if 0 <= n < 10: return n
    n = abs(n)
    digit_max = 0
    digit = 0
    run_max = 1
    run = 1

    while (n >= 10):
        digit = n % 10
        if digit == n // 10 % 10:
            run += 1
        else:
            digit_max = digit if run > run_max else min(digit, digit_max)
            run_max = run
            run = 1
        n //= 10

    if run > 1 and digit_max == 0: return digit  # 22222, 1000001
    else: return digit_max


# ============================================================================ #
#


def isPrime(n):
    factor = int(n**0.5)
    if n == 2 or n == 3: return True
    elif n < 2 or n % 2 == 0 or n % 3 == 0 or n**0.5 == factor: return False

    for i in range(5, factor + 1, 6):
        if n % i == 0 or n % (i + 2) == 0: return False
    return True


def circular_prime(n):  # all rotates are prime(n):
    n = abs(n)

    def check_digit(n):
        while n >= 10:  # not have [0, 5, 2, 4, 6, 8]
            digit = n % 10
            if digit == 0 or digit % 2 == 0 or digit % 5 == 0: return False
            n //= 10  # when n < 10, return...?
        return True

    def check_rotate(n):
        if (n <= 11): return True
        count = digit_count(n)
        for i in range(1, count):
            n = n % 10 * 10**(count - 1) + n // 10
            if not isPrime(n): return False
        return True

    return (check_digit(n) and isPrime(n) and check_rotate(n))


def nthCircularPrime(nth):
    def f(n):
        return circular_prime(n)

    return counter_int_positive(nth, f)


def counter_int_positive(nth, f):
    found = 0
    guess = 0
    while (found <= nth):
        guess += 1
        if f(guess): found += 1
    return guess


# ============================================================================ #
#


def digit_count(n):
    n = abs(n)
    count = 1
    while n >= 10:
        n //= 10
        count += 1
    return count


def palindromic_prime(n):
    def check_palindro(n):
        if n > 10:
            count = digit_count(n)
            for i in range(int(count / 2)):
                # a = getKthDigit(n, count - 1 - i)  # a = n[i]
                # z = getKthDigit(n, i)  # z = n[-1 - i]
                a = n // 10**(count - 1 - i) % 10
                z = n // 10**i % 10
                if a != z: return False
        return True

    return isPrime(n) and check_palindro(n)


def nthPalindromicPrime(nth):
    def f(n):
        return palindromic_prime(n)

    return counter_int_positive(nth, f)


#################################################
# hw2-spicy-function
# you can do this instead of the hw2-standard
# functions if you prefer.  Otherwise, you can
# skip the hw2-spicy function.  Either way,
# you should continue on to the hw2-required
# functions below.
#################################################


def makeBoard(n):
    board = 0
    for i in range(n):
        board += 8 * 10**i
    return board


def getLeftmostDigit(n):
    len = digit_count(n)
    return getKthDigit(n, len - 1)


def clearLeftmostDigit(n):
    len = digit_count(n)
    return setKthDigit(n, len - 1, 0)  # n % 10**(len - 1)


def makeMove(board, posn, move):
    len = digit_count(board)
    if move != 1 and move != 2:
        return "move must be 1 or 2!"
    elif posn > len:
        return "offboard!"
    elif getKthDigit(board, len - posn) != 8:
        return "occupied!"
    else:
        return setKthDigit(board, len - posn, move)


def hasDigits(n, d):
    len_d = digit_count(d)
    while n >= 10**(len_d - 1):
        if n % 10**(len_d) == d: return True
        # ic(n, d)
        n //= 10
    return False


def isWin(n):
    return hasDigits(n, 112)


def isFull(n):
    return not hasDigits(n, 8)


def play112(game):
    board = makeBoard(getLeftmostDigit(game))
    moves = clearLeftmostDigit(game)
    len = digit_count(moves)
    player = 1 if (len / 2) % 2 != 0 else 2
    # ic(moves)

    for i in range(int(len / 2)):
        posn = getKthDigit(moves, len - 1 - i * 2)
        move = getKthDigit(moves, len - 2 - i * 2)
        # ic(i, player, posn, move)
        board_temp = board
        board = makeMove(board, posn, move)

    msgPlayer = "Player " + str(player)
    if not isinstance(board, int):
        return str(board_temp) + ": " + msgPlayer + ": " + board
    else:
        msgBoard = str(board) + ": "
        if isWin(board):
            return msgBoard + msgPlayer + " wins!"
        if not isFull(board):
            return msgBoard + "Unfinished!"
        else:
            return msgBoard + "Tie!"


#################################################
# hw2-required-functions
#################################################


def carrylessAdd(x1, x2):
    count_x1 = digit_count(x1)
    count_x2 = digit_count(x2)
    count_min = min(count_x1, count_x2)
    n_max = max(x1, x2)
    n = 0
    for i in range(count_min):
        rem = (x1 % 10 + x2 % 10) % 10
        n += rem * 10**i
        x1 //= 10
        x2 //= 10
    if count_x1 != count_x2:
        step = 10**count_min
        n += (n_max // step) * step  # leftmost digit
    return n


# ============================================================================ #
#


def findZeroWithBisection(f, x0, x1, epsilon):
    xmid = (x0 + x1) / 2
    while x1 - x0 >= epsilon:
        a, z = f(x0), f(x1)
        mid = f(xmid)
        if a * z > 0:
            return None
        elif mid != 0:
            if a * mid > 0: x0 = xmid
            elif z * mid > 0: x1 = xmid
            xmid = (x0 + x1) / 2  # new mid
        # print(x0, "..", xmid,"..", x1)
        elif mid == 0:
            return None
    return xmid


# ============================================================================ #
#


def checkKaprekar(n):
    if n == 1: return True
    n_origin = n
    n = n**2
    count = digit_count(n)

    for i in range(count):
        step = 10**(count - 1 - i)
        left = n // step
        right = n % step
        if right != 0 and n_origin == left + right: return True
    return False


def nthKaprekarNumber(nth):
    def f(n):
        return checkKaprekar(n)

    return counter_int_positive(nth, f)


#################################################
# hw2-bonus-functions
# these are optional
#################################################


def carrylessMultiply(x1, x2):
    count1 = digit_count(x1)
    count2 = digit_count(x2)
    n = 0

    for i in range(count2):
        d2 = getKthDigit(x2, i)
        n_temp = 0
        for k in range(count1):
            d1 = getKthDigit(x1, k)
            n_temp += ((d1 * d2) % 10 * 10**k) * 10**i
        n = carrylessAdd(n, n_temp)
    return n


def nearestKaprekarNumber(n):
    if n < 1: return 1
    elif checkKaprekar(n): return n

    def get_part(n, part, count_max):
        count = 0
        while n > 0:
            n += 1 if part == 1 else -1
            count += 1
            if count_max != 0 and count > count_max + 1:  # +1 incase of float
                # count current > count previous
                return None, 0
            elif checkKaprekar(n):
                return n, count

    n_temp = int(n)
    count_max = 0
    if checkKaprekar(n_temp):
        left = n_temp
    else:
        left, count_max = get_part(n_temp, 0, count_max)
    right, count_max = get_part(n_temp, 1, count_max)
    # ic(left, right)

    if right == None:
        return left
    else:
        return right if (right - n < n - left) else left


############################
# integerDataStructures
############################


def intCat(n, m):  # to nm
    return n * 10**digit_count(m) + m


def lengthEncode(n):
    sign = 2 if n < 0 else 1
    n_encode = abs(n)
    count = digit_count(n)
    count_of_count = digit_count(count)

    n_encode = intCat(count, n_encode)
    n_encode = intCat(count_of_count, n_encode)
    n_encode = intCat(sign, n_encode)
    return n_encode


def lengthDecode(encoding):
    count_encoding = digit_count(encoding)

    sign = getKthDigit(encoding, count_encoding - 1)
    count_of_count = getKthDigit(encoding, count_encoding - 2)

    len_prefix = 2 + count_of_count  # break parts
    prefix = encoding // 10**(count_encoding - len_prefix)
    count = prefix % 10**(len_prefix - 2)  #* use mod
    decode = encoding % 10**count

    # count = 0
    # for i in range(count_of_count): #* use concatenation
    #     digit = getKthDigit(encoding, count_encoding - 3 - i)
    #     count = intCat(count, digit)
    # ic(count_of_count, count)

    # ic(prefix, sign, count_of_count, count, decode)
    return -decode if sign == 2 else decode


def lengthDecodeLeftmost_split(encoding):
    count = digit_count(encoding)
    p1_count_of_count = encoding // 10**(count - 1 - 2) % 10
    p1_len = 3 + p1_count_of_count
    # ic(count, p1_len)

    step = 10**(count - 1 - (p1_len - 1))  # break parts
    p1 = encoding // step
    p_rem = encoding % step
    return p1, p_rem


def lengthDecodeLeftmostValue(encoding):
    p1, p_rem = lengthDecodeLeftmost_split(encoding)
    return lengthDecode(p1), p_rem


# ============================================================================ #
#


def newIntList():
    return lengthEncode(0)


def intListLen(l):  # len-l[0]-l[1], so leftmost part
    p1_decode, p_rem = lengthDecodeLeftmostValue(l)
    return p1_decode


def intList_check_range(l, i):
    len, p_rem = lengthDecodeLeftmostValue(l)
    if not 0 <= i < len: return 'index out of range'


def intListGet(l, i):  # start from 0 (1st is len)
    check_range = intList_check_range(l, i)
    if check_range != None: return check_range

    for k in range(i + 1 + 1):  # one more loop to move posn to p1
        p1, l = lengthDecodeLeftmost_split(l)  #
    # ic(p1, l)
    return lengthDecode(p1)


def intListAppend(l, val):
    len, p_rem = lengthDecodeLeftmostValue(l)
    p_len = lengthEncode(len + 1)
    p_rem = intCat(p_rem, lengthEncode(val))
    return intCat(p_len, p_rem)


def intList_split_i(l, i):
    p_left = 0
    nth = 0
    while nth < i + 1:
        p1, l = lengthDecodeLeftmost_split(l)
        p_left = intCat(p_left, p1)
        nth += 1
    return p_left, l


def intListSet(l, i, val):
    check_range = intList_check_range(l, i)
    if check_range != None: return check_range
    p_left, p_rem = intList_split_i(l, i)
    p_i, p_rem = lengthDecodeLeftmost_split(p_rem)  # pop and replace p_i

    p_set = lengthEncode(val)
    p_rem = intCat(p_set, p_rem) if p_rem != 0 else p_set
    # ic(p_left, p_set, p_rem)
    return intCat(p_left, p_rem)


def intListPop_i(l, i):
    check_range = intList_check_range(l, i)
    if check_range != None: return check_range

    p_left, p_rem = intList_split_i(l, i)
    p_i, p_rem = lengthDecodeLeftmost_split(p_rem)  # pop and replace p_i
    p_new = intCat(p_left, p_rem) if p_rem != 0 else p_left
    # ic(p_left, p_rem)

    p_len, p_rem = lengthDecodeLeftmostValue(p_new)  # minus len
    p_len_encode = lengthEncode(p_len - 1)
    p_new = intCat(p_len_encode, p_rem) if p_rem != 0 else p_len_encode
    return p_new, lengthDecode(p_i)


def intListPop(l):  # pop -1
    i = intListLen(l) - 1
    return intListPop_i(l, i)


# ============================================================================ #
#


def newIntSet():
    return newIntList()


def intSetAdd(intSet, val):
    len, p_rem = lengthDecodeLeftmostValue(intSet)
    if intSetContains(intSet, val):
        return intSet
    else:
        return intListAppend(intSet, val)


def intSetContains(intSet, val):
    len, p_rem = lengthDecodeLeftmostValue(intSet)

    for i in range(len):
        p1, p_rem = lengthDecodeLeftmostValue(p_rem)
        # ic(p1, p_rem)
        if p1 == val: return True
    return False


# ============================================================================ #
#


def newIntMap():
    return newIntList()


def intMapGet(l, key):
    if not intMapContains(l, key): return 'no such key'
    i = intMap_get_key_i(l, key)
    return intListGet(l, i + 1)


def intMap_get_key_i(l, key):
    len, p_rem = lengthDecodeLeftmostValue(l)
    i = 0
    while i < len:
        key_test = intListGet(l, i)
        #* ?????? index ?????????????????? f() ????????????
        if key_test == key: return i
        i += 2
    return None


def intMapContains(l, key):  # fixed range, len-key-val
    i = intMap_get_key_i(l, key)
    return i != None


def intMapSet(l, key, val):
    if not intMapContains(l, key):
        l_new = intListAppend(l, key)
        l_new = intListAppend(l_new, val)
    else:
        i = intMap_get_key_i(l, key)
        l_new = intListSet(l, i + 1, val)
    return l_new


# ============================================================================ #
#


def newIntFSM():
    pass


def isAcceptingState(fsm, state):
    pass


def addAcceptingState(fsm, state):
    pass


def setTransition(fsm, fromState, digit, toState):
    pass


def getTransition(fsm, fromState, digit):
    pass


def accepts(fsm, inputValue):
    pass


def states(fsm, inputValue):
    pass


# ============================================================================ #
#
def encode_char(c):
    return intListAppend(newIntList(), ord(c))


def encodeString(s):
    l = newIntList()
    for c in s:
        val = ord(c)
        l = intListAppend(l, val)
        # ic(c, val, l)
    return l


def decodeString(l):
    len, p_rem = lengthDecodeLeftmostValue(l)

    s = ''
    for i in range(len):
        p1, p_rem = lengthDecodeLeftmostValue(p_rem)
        s += chr(p1)
        # ic(i, p1, s, p_rem)
    return s


#################################################
# Test Functions
#################################################


def testLongestDigitRun():
    print('Testing longestDigitRun()... ', end='')
    assert (longestDigitRun(117773732) == 7)
    assert (longestDigitRun(-677886) == 7)
    assert (longestDigitRun(5544) == 4)
    assert (longestDigitRun(1) == 1)
    assert (longestDigitRun(0) == 0)
    assert (longestDigitRun(22222) == 2)
    assert (longestDigitRun(111222111) == 1)
    assert (longestDigitRun(1000001) == 0)  # my extreme test
    '''print(longestDigitRun(117773732) )
    print(longestDigitRun(-677886))
    print(longestDigitRun(5544) )
    print(longestDigitRun(1))
    print(longestDigitRun(0))
    print(longestDigitRun(22222) )
    print(longestDigitRun(111222111) )'''
    print('Passed.')


def test_isPrime():
    assert (isPrime(3)) == True
    assert (isPrime(5)) == True
    assert (isPrime(17)) == True
    assert (isPrime(83)) == True
    assert (isPrime(173)) == True
    assert (isPrime(509)) == True
    assert (isPrime(511)) == False
    assert (isPrime(1373731)) == False

    # print("prime:",isPrime(149345643266432421))
    # testNumb = 13173
    # print(testNumb, isPrime(testNumb) and circular_p_rotate(testNumb))


def test_circular_prime():
    # print(circular_p_rotate(3))
    # print(circular_p_rotate(5))
    # print( circular_p_rotate(19))
    # print( circular_p_rotate(23))
    # print(circular_p_rotate(173))
    # print(circular_p_rotate(709))  # 097 970
    # print(circular_p_rotate(590))
    # print( circular_p_rotate(7937))
    pass


def testNthCircularPrime():
    print('Testing nthCircularPrime()...', end='')
    test_isPrime()
    test_circular_prime()

    # [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113,
    #  131, 197, 199, 311, 337, 373, 719, 733, 919, 971, 991, 1193, ...]
    assert (nthCircularPrime(0) == 2)
    assert (nthCircularPrime(5) == 13)
    assert (nthCircularPrime(10) == 73)
    assert (nthCircularPrime(15) == 197)
    assert (nthCircularPrime(20) == 719)
    assert (nthCircularPrime(25) == 1193)
    # print(nthCircularPrime(0), end="?2 ")
    # print(nthCircularPrime(1), end="?3 ")
    # print(nthCircularPrime(2), end="?5 ")
    # print(nthCircularPrime(3), end="?7 ")
    # print(nthCircularPrime(4), end="?11 ")
    # print(nthCircularPrime(5), end="?13 ")
    # print(nthCircularPrime(6), end="?17 ")
    # print(nthCircularPrime(7), end="?31 ") #91
    # print(nthCircularPrime(9), end="?71 ")
    # print(nthCircularPrime(10), end="?73 ")
    # print(nthCircularPrime(11), end="?79 ")
    # print(nthCircularPrime(12), end="?97 ")
    # print(nthCircularPrime(13), end="?113 ") #bug
    # print(nthCircularPrime(14), end=" ")
    # print(nthCircularPrime(15), end="?197 ")
    # print(nthCircularPrime(16), end=" ")
    # print(nthCircularPrime(20), end="?719 ")
    # print(nthCircularPrime(25), end="?1193 ")
    # print(nthCircularPrime(30), end="? ")
    print('Passed!')


def test_palindromic_prime():
    # print(palindromic_digit(54321))
    # print(palindromic_digit(9))
    # print(palindromic_digit(121))
    # print(palindromic_digit(3021))
    # print(palindromic_digit(1011))
    # print(palindromic_digit2(10201))
    # print(palindromic_digit(102201))
    pass


def testNthPalindromicPrime():
    print('Testing nthPalindromicPrime()...', end='')
    test_palindromic_prime()

    assert nthPalindromicPrime(0) == 2
    assert nthPalindromicPrime(4) == 11
    assert nthPalindromicPrime(10) == 313
    assert nthPalindromicPrime(15) == 757
    assert nthPalindromicPrime(20) == 10301

    # print(nthPalindromicPrime(5))
    # print(nthPalindromicPrime(20))  # 10301
    print('Passed.')


def testPlay112():
    print("Testing play112()... ", end="")
    assert (makeMove(8, 1, 1) == 1)
    assert (makeMove(888888, 1, 1) == 188888)
    assert (makeMove(888888, 2, 1) == 818888)
    assert (makeMove(888888, 5, 2) == 888828)
    assert (makeMove(888888, 6, 2) == 888882)
    assert (makeMove(888888, 6, 3) == "move must be 1 or 2!")
    assert (makeMove(888888, 7, 1) == "offboard!")
    assert (makeMove(888881, 6, 1) == "occupied!")

    assert (isWin(888888) == False)
    assert (isWin(112888) == True)
    assert (isWin(811288) == True)
    assert (isWin(888112) == True)
    assert (isWin(211222) == True)
    assert (isWin(212212) == False)
    assert (isFull(888888) == False)
    assert (isFull(121888) == False)
    assert (isFull(812188) == False)
    assert (isFull(888121) == False)
    assert (isFull(212122) == True)
    assert (isFull(212212) == True)

    assert (hasDigits(112888, 112)) == True
    assert (hasDigits(113888, 112)) == False
    assert (hasDigits(112811, 8)) == True
    assert (hasDigits(812111, 8)) == True
    assert (hasDigits(112118, 8)) == True
    assert (hasDigits(112111, 8)) == False
    ic(getKthDigit(2112, 4))

    assert (play112(5) == "88888: Unfinished!")
    assert (play112(521) == "81888: Unfinished!")
    assert (play112(52112) == "21888: Unfinished!")
    assert (play112(5211231) == "21188: Unfinished!")
    assert (play112(521123142) == "21128: Player 2 wins!")
    assert (play112(521123151) == "21181: Unfinished!")
    assert (play112(52112315142) == "21121: Player 1 wins!")
    assert (play112(523) == "88888: Player 1: move must be 1 or 2!")
    assert (play112(51223) == "28888: Player 2: move must be 1 or 2!")
    assert (play112(51211) == "28888: Player 2: occupied!")
    assert (play112(5122221) == "22888: Player 1: occupied!")
    assert (play112(51261) == "28888: Player 2: offboard!")
    assert (play112(51122324152) == "12212: Tie!")
    print("Passed!")


def testCarrylessAdd():
    print('Testing carrylessAdd()... ', end='')
    assert (carrylessAdd(785, 376) == 51)
    assert (carrylessAdd(0, 376) == 376)
    assert (carrylessAdd(785, 0) == 785)
    assert (carrylessAdd(30, 376) == 306)
    assert (carrylessAdd(785, 30) == 715)
    assert (carrylessAdd(12345678900, 38984034003) == 40229602903)
    # print(carrylessAdd(720085, 76))
    # print(carrylessAdd(785, 376))
    # print(carrylessAdd(30, 376))
    print('Passed.')


# helper test functions for testFindZeroWithBisection():


def f1(x):
    return x * x - 2  # root at x=sqrt(2)


def f2(x):
    return x**2 - (x + 1)  # root at x=phi


def f3(x):
    return x**5 - 2**x  # f(1)<0, f(2)>0


def testFindZeroWithBisection():
    print('Testing findZeroWithBisection()... ', end='')
    # print(findZeroWithBisection(f1, 0, 2, 0.000000001))  # 1.41421356192
    # print(findZeroWithBisection(f2, 0, 2, 0.000000001))  # 1.61803398887
    # print(findZeroWithBisection(f3, 1, 2, 0.000000001))  # 17727855081

    x = findZeroWithBisection(f1, 0, 2, 0.000000001)
    assert (almostEqual(x, 1.41421356192))
    x = findZeroWithBisection(f2, 0, 2, 0.000000001)
    assert (almostEqual(x, 1.61803398887))
    x = findZeroWithBisection(f3, 1, 2, 0.000000001)
    assert (almostEqual(x, 1.17727855081))

    print('Passed.')


# nthKaprekarNumber


def test_checkKaprekar():
    # print(checkKaprekar(1))
    # print(checkKaprekar(230))
    # print(checkKaprekar(297))
    # print(checkKaprekar(703))
    # print(checkKaprekar(999))
    # print(checkKaprekar(2223))
    # print(checkKaprekar(2728))
    # print(checkKaprekar(2729))
    # print(checkKaprekar(100))
    assert (checkKaprekar(5292)) == True
    assert (checkKaprekar(5293)) == False


def testNthKaprekarNumber():
    print('Testing nthKaprekarNumber()...', end='')
    test_checkKaprekar()

    assert (nthKaprekarNumber(0) == 1)
    assert (nthKaprekarNumber(1) == 9)
    assert (nthKaprekarNumber(2) == 45)
    assert (nthKaprekarNumber(3) == 55)
    assert (nthKaprekarNumber(4) == 99)
    assert (nthKaprekarNumber(5) == 297)
    assert (nthKaprekarNumber(6) == 703)
    assert (nthKaprekarNumber(7) == 999)
    assert (nthKaprekarNumber(8) == 2223)
    assert (nthKaprekarNumber(9) == 2728)
    # ic(nthKaprekarNumber(2))
    # ic(nthKaprekarNumber(10))
    # ic(nthKaprekarNumber(11))
    # ic(nthKaprekarNumber(12))
    print('Passed.')


def testCarrylessMultiply():
    print("Testing carrylessMultiply()...", end="")
    # ic(carrylessMultiply(643, 59))  # == 417

    assert (carrylessMultiply(643, 59) == 417)
    assert (carrylessMultiply(6412, 387) == 807234)
    print("Passed!")


def testNearestKaprekarNumber():
    print("Testing nearestKaprekarNumber()...", end="")
    # ic(nearestKaprekarNumber(4.99999999))  # == 1
    # ic(nearestKaprekarNumber(2475.51))  # == 1

    assert (nearestKaprekarNumber(-1) == 1)
    assert (nearestKaprekarNumber(-2) == 1)
    assert (nearestKaprekarNumber(-12345) == 1)
    assert (nearestKaprekarNumber(0) == 1)
    assert (nearestKaprekarNumber(1) == 1)
    assert (nearestKaprekarNumber(1.234) == 1)
    assert (nearestKaprekarNumber(5) == 1)
    assert (nearestKaprekarNumber(4.99999999) == 1)
    assert (nearestKaprekarNumber(5.00000001) == 9)
    assert (nearestKaprekarNumber(27) == 9)
    assert (nearestKaprekarNumber(28) == 45)
    assert (nearestKaprekarNumber(45) == 45)
    assert (nearestKaprekarNumber(50) == 45)
    assert (nearestKaprekarNumber(51) == 55)
    assert (nearestKaprekarNumber(1611) == 999)
    assert (nearestKaprekarNumber(1612) == 2223)
    assert (nearestKaprekarNumber(2475.4) == 2223)
    assert (nearestKaprekarNumber(2475.5) == 2223)
    assert (nearestKaprekarNumber(2475.51) == 2728)
    assert (nearestKaprekarNumber(2475.6) == 2728)

    # kaps = [1, 9, 45, 55, 99, 297, 703, 999, 2223, 2728]
    # bigKaps = [994708, 999999]
    assert (nearestKaprekarNumber(995123) == 994708)
    assert (nearestKaprekarNumber(9376543) == 9372385)
    # assert (nearestKaprekarNumber(13641234) == 13641364)
    print("Passed!")


# Integer Data Structures


def test_intCat():
    assert (intCat(12, 34)) == 1234
    assert (intCat(2, 34)) == 234
    assert (intCat(0, 34)) == 34
    assert (intCat(0, 0)) == 0
    assert (intCat(1, 0)) == 10


def testLengthEncode():
    print('Testing lengthEncode()...', end='')
    test_intCat()

    # ic(lengthEncode(-789))  # == 213789)

    assert (lengthEncode(789) == 113789)
    assert (lengthEncode(-789) == 213789)
    assert (lengthEncode(1234512345) == 12101234512345)
    assert (lengthEncode(-1234512345) == 22101234512345)
    assert (lengthEncode(0) == 1110)
    print('Passed!')


def testLengthDecodeLeftmostValue():
    print('Testing lengthDecodeLeftmostValue()...', end='')
    # ic(lengthDecodeLeftmostValue(11101110))  # == (0, 1110))
    # ic(lengthDecodeLeftmostValue(212341115))  # 2-1-2-34

    assert (lengthDecodeLeftmostValue(212341115)) == (-34, 1115)
    assert (lengthDecodeLeftmostValue(111211131114) == (2, 11131114))
    assert (lengthDecodeLeftmostValue(112341115) == (34, 1115))
    assert (lengthDecodeLeftmostValue(111211101110) == (2, 11101110))
    assert (lengthDecodeLeftmostValue(11101110) == (0, 1110))
    print('Passed!')


def testLengthDecode():
    print('Testing lengthDecode()...', end='')
    # ic(lengthDecode(213789))  #
    # ic(lengthDecode(12101234512345))  # 1234512345

    assert (lengthDecode(113789) == 789)
    assert (lengthDecode(213789) == -789)
    assert (lengthDecode(12101234512345) == 1234512345)
    assert (lengthDecode(22101234512345) == -1234512345)
    assert (lengthDecode(1110) == 0)
    print('Passed!')


def testIntList():
    print('Testing intList functions...', end='')
    a1 = newIntList()
    assert (a1 == 1110)  # length = 0, list = []
    assert (intListLen(a1) == 0)
    assert (intListGet(a1, 0) == 'index out of range')

    # a1 = 111211191148888
    # # ic(intListLen(a1))  # == 0
    # assert (intListGet(a1, 0)) == 9
    # assert (intListGet(a1, 1)) == 8888

    a1 = intListAppend(a1, 42)  # 0,42
    assert (a1 == 111111242)  # length = 1, list = [42]
    assert (intListLen(a1) == 1)
    # ic(intListGet(a1, 0))
    assert (intListGet(a1, 0) == 42)
    assert (intListGet(a1, 1) == 'index out of range')
    assert (intListSet(a1, 1, 99) == 'index out of range')

    a1 = intListSet(a1, 0, 567)
    assert (a1 == 1111113567)  # length = 1, list = [567]
    assert (intListLen(a1) == 1)
    assert (intListGet(a1, 0) == 567)

    a1 = intListAppend(a1, 8888)
    a1 = intListSet(a1, 0, 9)
    assert (a1 == 111211191148888)  # length = 2, list = [9, 8888]
    assert (intListLen(a1) == 2)
    # ic(intListGet(a1, 0))
    assert (intListGet(a1, 0) == 9)
    assert (intListGet(a1, 1) == 8888)

    # ic(intListPop_i(111211191148888, 2))
    assert (intListPop_i(111211191148888, 0)) == (11111148888, 9)
    assert (intListPop_i(11111119, 0)) == (1110, 9)

    # ic(intListPop(a1))
    a1, poppedValue = intListPop(a1)
    assert (poppedValue == 8888)
    assert (a1 == 11111119)  # length = 1, list = [9]
    assert (intListLen(a1) == 1)
    assert (intListGet(a1, 0) == 9)
    assert (intListGet(a1, 1) == 'index out of range')
    # ic(a1)

    a2 = newIntList()
    a2 = intListAppend(a2, 0)
    assert (a2 == 11111110)
    a2 = intListAppend(a2, 0)
    assert (a2 == 111211101110)
    print('Passed!')


def testIntSet():
    print('Testing intSet functions...', end='')
    assert (intSetContains(111211191148888, 42)) == False
    assert (intSetContains(111211191148888, 8888)) == True
    # ic(intSetAdd(111211191148888, 9))
    # ic(intSetAdd(111211191148888, 2))

    s = newIntSet()
    assert (s == 1110)  # length = 0
    assert (intSetContains(s, 42) == False)
    s = intSetAdd(s, 42)
    assert (s == 111111242)  # length = 1, set = [42]
    assert (intSetContains(s, 42) == True)
    s = intSetAdd(s, 42)  # multiple adds --> still just one
    assert (s == 111111242)  # length = 1, set = [42]
    assert (intSetContains(s, 42) == True)
    print('Passed!')


def testIntMap():
    print('Testing intMap functions...', end='')
    assert (intMapContains(11121124211273, 42)) == True
    assert (intMapContains(11121127311242, 42)) == False
    # ic(intMapContains(11141124211598765112991110, 99))
    # ic(intMapContains(11121127311242, 42))
    assert (intMapContains(11141124211598765112991110, 42)) == True  # 42,99
    assert (intMapContains(11141124211598765112991110, 99)) == True

    assert (intMapGet(11121127311242, 42)) == 'no such key'
    # ic(intMapGet(11121124211273, 42))  # 73
    # ic(intMapGet(11141124211598765112991110, 42))  # 98765

    m = newIntMap()
    assert (m == 1110)  # length = 0
    assert (intMapContains(m, 42) == False)
    assert (intMapGet(m, 42) == 'no such key')

    # ic(intMapSet(1110, 42, 73))  # 11121124211273
    # ic(intMapSet(11121124211273, 42, 12))
    m = intMapSet(m, 42, 73)
    assert (m == 11121124211273)  # length = 2, map = [42, 73]
    assert (intMapContains(m, 42) == True)
    assert (intMapGet(m, 42) == 73)

    m = intMapSet(m, 42, 98765)
    assert (m == 11121124211598765)  # length = 2, map = [42, 98765]
    assert (intMapGet(m, 42) == 98765)

    m = intMapSet(m, 99, 0)
    assert (m == 11141124211598765112991110)  # length = 4,
    # map = [42, 98765, 99, 0]
    assert (intMapGet(m, 42) == 98765)
    assert (intMapGet(m, 99) == 0)
    print('Passed!')


def testIntFSM():
    print('Testing intFSM functions...', end='')

    # fsm = newIntFSM()
    # assert (fsm == 111211411101141110)  # length = 2,
    # # [empty stateMap, empty startStateSet]
    # assert (isAcceptingState(fsm, 1) == False)

    # fsm = addAcceptingState(fsm, 1)
    # assert (fsm == 1112114111011811111111)
    # assert (isAcceptingState(fsm, 1) == True)

    # assert (getTransition(fsm, 0, 8) == 'no such transition')
    # fsm = setTransition(fsm, 4, 5, 6)
    # # map[5] = 6: 111211151116
    # # map[4] = (map[5] = 6):  111211141212111211151116
    # assert (fsm == 1112122411121114121211121115111611811111111)
    # assert (getTransition(fsm, 4, 5) == 6)

    # fsm = setTransition(fsm, 4, 7, 8)
    # fsm = setTransition(fsm, 5, 7, 9)
    # assert (getTransition(fsm, 4, 5) == 6)
    # assert (getTransition(fsm, 4, 7) == 8)
    # assert (getTransition(fsm, 5, 7) == 9)

    # fsm = newIntFSM()
    # assert (fsm == 111211411101141110)  # length = 2,
    # # [empty stateMap, empty startStateSet]
    # fsm = setTransition(fsm, 0, 5, 6)
    # # map[5] = 6: 111211151116
    # # map[0] = (map[5] = 6):  111211101212111211151116
    # assert (fsm == 111212241112111012121112111511161141110)
    # assert (getTransition(fsm, 0, 5) == 6)

    print('Passed!')


def testAccepts():
    print('Testing accepts()...', end='')
    fsm = newIntFSM()
    # fsm accepts 6*7+8
    fsm = addAcceptingState(fsm, 3)
    fsm = setTransition(fsm, 1, 6, 1)  # At state 1, receive 6, move to state 1
    fsm = setTransition(fsm, 1, 7, 2)  # At state 1, receive 7, move to state 2
    fsm = setTransition(fsm, 2, 7, 2)  # At state 1, receive 7, move to state 2
    fsm = setTransition(fsm, 2, 8, 3)  # At state 1, receive 8, move to state 3
    assert (accepts(fsm, 78) == True)
    assert (states(fsm, 78) == 1113111111121113)  # length = 3, list = [1,2,3]
    assert (accepts(fsm, 678) == True)
    assert (states(fsm, 678) == 11141111111111121113)  # length = 4,
    # list = [1,1,2,3]

    assert (accepts(fsm, 5) == False)
    assert (accepts(fsm, 788) == False)
    assert (accepts(fsm, 67) == False)
    assert (accepts(fsm, 666678) == True)
    assert (accepts(fsm, 66667777777777778) == True)
    assert (accepts(fsm, 7777777777778) == True)
    assert (accepts(fsm, 666677777777777788) == False)
    assert (accepts(fsm, 77777777777788) == False)
    assert (accepts(fsm, 7777777777778) == True)
    assert (accepts(fsm, 67777777777778) == True)
    print('Passed!')


def testEncodeDecodeStrings():
    print('Testing encodeString and decodeString...', end='')
    # ic(encodeString('Af3!'))

    assert (encodeString('A') == 111111265)  # length = 1, str = [65]
    assert (encodeString('f') == 1111113102)  # length = 1, str = [102]
    assert (encodeString('3') == 111111251)  # length = 1, str = [51]
    assert (encodeString('!') == 111111233)  # length = 1, str = [33]
    assert (encodeString('Af3!') == 1114112651131021125111233)  # length = 4,

    # ic(decodeString(1114112651131021125111233))  # == 'Af3!')
    # str = [65,102,51,33]
    assert (decodeString(111111265) == 'A')
    assert (decodeString(1114112651131021125111233) == 'Af3!')
    assert (decodeString(encodeString('WOW!!!')) == 'WOW!!!')
    print('Passed!')


def testIntegerDataStructures():
    testLengthEncode()
    testLengthDecode()
    testLengthDecodeLeftmostValue()
    testIntList()
    testIntSet()
    testIntMap()
    testIntFSM()
    # testAccepts()
    testEncodeDecodeStrings()


#################################################
# testAll and main
#################################################


def testAll():
    # comment out the tests you do not wish to run!
    # hw2-standard
    testLongestDigitRun()
    testNthCircularPrime()
    testNthPalindromicPrime()

    # hw2-spicy
    testPlay112()

    # hw2-required
    testCarrylessAdd()
    testFindZeroWithBisection()
    testNthKaprekarNumber()

    # hw2-bonus
    testCarrylessMultiply()
    testNearestKaprekarNumber()

    # hw2-spicy-bonus
    testIntegerDataStructures()


def main():
    cs112_s21_week2_linter.lint()
    testAll()


if __name__ == '__main__':
    main()
