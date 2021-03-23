#################################################
# hw2.py
# name:
# andrew id:
#################################################

import cs112_s21_week2_linter
import math

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7): #helper-fn
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d): #helper-fn
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# hw2-standard-functions
#################################################

def longestDigitRun(n):
    n = abs(n)
    if n < 0: return "negative numb"
    if 0 <= n < 10: return n
    runNew = 1
    run = 1
    valNew = 0
    val = 0
    while (n//10 != 0):
        #print(n%10, "?", n//10%10)
        if n%10 == n//10%10:
            runNew += 1
            valNew = n % 10
            #val = valNew
        elif runNew > run:
            run = runNew
            val = n % 10
            runNew = 1
        elif runNew == run:
            val = min(n % 10, val)
            runNew = 1
        n //= 10
    if runNew > 1 and val == 0:
        return valNew
    else: return val

def nthCircularPrime(n):
    return 42

def nthPalindromicPrime(n):
    return 42

#################################################
# hw2-spicy-function
# you can do this instead of the hw2-standard
# functions if you prefer.  Otherwise, you can
# skip the hw2-spicy function.  Either way,
# you should continue on to the hw2-required
# functions below.
#################################################

def play112(game):
    return 42

#################################################
# hw2-required-functions
#################################################

def carrylessAdd(x1, x2):
    return 42

def findZeroWithBisection(f, x0, x1, epsilon):
    return 42

def nthKaprekarNumber(n):
    return 42

#################################################
# hw2-bonus-functions
# these are optional
#################################################

def carrylessMultiply(x1, x2):
    return 42

def nearestKaprekarNumber(n):
    return 42

############################
# integerDataStructures
############################

def intCat(n, m): pass
def lengthEncode(value): pass
def lengthDecode(encoding): pass
def lengthDecodeLeftmostValue(encoding): pass
def newIntList(): pass
def intListLen(intList): pass
def intListGet(intList, i): pass
def intListSet(intList, i, value): pass
def intListAppend(intList, value): pass
def intListPop(intList): pass
def newIntSet(): pass
def intSetAdd(intSet, value): pass
def intSetContains(intSet, value): pass
def newIntMap(): pass
def intMapGet(intMap, key): pass
def intMapContains(intMap,key): pass
def intMapSet(intMap, key, value): pass
def newIntFSM(): pass
def isAcceptingState(fsm, state): pass
def addAcceptingState(fsm, state): pass
def setTransition(fsm, fromState, digit, toState): pass
def getTransition(fsm, fromState, digit): pass
def accepts(fsm, inputValue): pass
def states(fsm, inputValue): pass
def encodeString(s): pass
def decodeString(intList): pass

#################################################
# Test Functions
#################################################

def testLongestDigitRun():
    print('Testing longestDigitRun()... ', end='')
    assert(longestDigitRun(117773732) == 7)
    assert(longestDigitRun(-677886) == 7)
    assert(longestDigitRun(5544) == 4)
    assert(longestDigitRun(1) == 1)
    assert(longestDigitRun(0) == 0)
    assert(longestDigitRun(22222) == 2)
    assert(longestDigitRun(111222111) == 1)
    assert(longestDigitRun(1000001) == 0) #my extreme test
    '''print(longestDigitRun(117773732) )
    print(longestDigitRun(-677886))
    print(longestDigitRun(5544) )
    print(longestDigitRun(1))
    print(longestDigitRun(0))
    print(longestDigitRun(22222) )
    print(longestDigitRun(111222111) )'''
    print('Passed.')

def testNthCircularPrime():
    print('Testing nthCircularPrime()...', end='')
    # [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113,
    #  131, 197, 199, 311, 337, 373, 719, 733, 919, 971, 991, 1193, ...]
    assert(nthCircularPrime(0) == 2)
    assert(nthCircularPrime(5) == 13)
    assert(nthCircularPrime(10) == 73)
    assert(nthCircularPrime(15) == 197)
    assert(nthCircularPrime(20) == 719)
    assert(nthCircularPrime(25) == 1193)
    print('Passed!')

def testNthPalindromicPrime():
    print('Testing nthPalindromicPrime()...', end='')
    assert nthPalindromicPrime(0) == 2
    assert nthPalindromicPrime(4) == 11
    assert nthPalindromicPrime(10) == 313
    assert nthPalindromicPrime(15) == 757
    assert nthPalindromicPrime(20) == 10301
    print('Passed.')

def testPlay112():
    print("Testing play112()... ", end="")
    assert(play112( 5 ) == "88888: Unfinished!")
    assert(play112( 521 ) == "81888: Unfinished!")
    assert(play112( 52112 ) == "21888: Unfinished!")
    assert(play112( 5211231 ) == "21188: Unfinished!")
    assert(play112( 521123142 ) == "21128: Player 2 wins!")
    assert(play112( 521123151 ) == "21181: Unfinished!")
    assert(play112( 52112315142 ) == "21121: Player 1 wins!")
    assert(play112( 523 ) == "88888: Player 1: move must be 1 or 2!")
    assert(play112( 51223 ) == "28888: Player 2: move must be 1 or 2!")
    assert(play112( 51211 ) == "28888: Player 2: occupied!")
    assert(play112( 5122221 ) == "22888: Player 1: occupied!")
    assert(play112( 51261 ) == "28888: Player 2: offboard!")
    assert(play112( 51122324152 ) == "12212: Tie!")
    print("Passed!")

def testCarrylessAdd():
    print('Testing carrylessAdd()... ', end='')
    assert(carrylessAdd(785, 376) == 51)
    assert(carrylessAdd(0, 376) == 376)
    assert(carrylessAdd(785, 0) == 785)
    assert(carrylessAdd(30, 376) == 306)
    assert(carrylessAdd(785, 30) == 715)
    assert(carrylessAdd(12345678900, 38984034003) == 40229602903)
    print('Passed.')

# helper test functions for testFindZeroWithBisection():
def f1(x): return x*x - 2 # root at x=sqrt(2)
def f2(x): return x**2 - (x + 1)  # root at x=phi
def f3(x): return x**5 - 2**x # f(1)<0, f(2)>0

def testFindZeroWithBisection():
    print('Testing findZeroWithBisection()... ', end='')
    x = findZeroWithBisection(f1, 0, 2, 0.000000001)
    assert(almostEqual(x, 1.41421356192))   
    x = findZeroWithBisection(f2, 0, 2, 0.000000001)
    assert(almostEqual(x, 1.61803398887))
    x = findZeroWithBisection(f3, 1, 2, 0.000000001)
    assert(almostEqual(x, 1.17727855081))
    print('Passed.')

# nthKaprekarNumber

def testNthKaprekarNumber():
    print('Testing nthKaprekarNumber()...', end='')
    assert(nthKaprekarNumber(0) == 1)
    assert(nthKaprekarNumber(1) == 9)
    assert(nthKaprekarNumber(2) == 45)
    assert(nthKaprekarNumber(3) == 55)
    assert(nthKaprekarNumber(4) == 99)
    assert(nthKaprekarNumber(5) == 297)
    assert(nthKaprekarNumber(6) == 703)
    assert(nthKaprekarNumber(7) == 999)
    print('Passed.')

def testCarrylessMultiply():
    print("Testing carrylessMultiply()...", end="")
    assert(carrylessMultiply(643, 59) == 417)
    assert(carrylessMultiply(6412, 387) == 807234)
    print("Passed!")

def testNearestKaprekarNumber():
    print("Testing nearestKaprekarNumber()...", end="")
    assert(nearestKaprekarNumber(1) == 1)
    assert(nearestKaprekarNumber(0) == 1)
    assert(nearestKaprekarNumber(-1) == 1)
    assert(nearestKaprekarNumber(-2) == 1)
    assert(nearestKaprekarNumber(-12345) == 1)
    assert(nearestKaprekarNumber(1.234) == 1)
    assert(nearestKaprekarNumber(4.99999999) == 1)
    assert(nearestKaprekarNumber(5) == 1)
    assert(nearestKaprekarNumber(5.00000001) == 9)
    assert(nearestKaprekarNumber(27) == 9)
    assert(nearestKaprekarNumber(28) == 45)
    assert(nearestKaprekarNumber(45) == 45)
    assert(nearestKaprekarNumber(50) == 45)
    assert(nearestKaprekarNumber(51) == 55)
    assert(nearestKaprekarNumber(1611) == 999)
    assert(nearestKaprekarNumber(1612) == 2223)
    assert(nearestKaprekarNumber(2475.4) == 2223)
    assert(nearestKaprekarNumber(2475.5) == 2223)
    assert(nearestKaprekarNumber(2475.51) == 2728)
    assert(nearestKaprekarNumber(2475.6) == 2728)
    #kaps = [1, 9, 45, 55, 99, 297, 703, 999, 2223, 2728]
    #bigKaps = [994708, 999999]
    assert(nearestKaprekarNumber(995123) == 994708)
    assert(nearestKaprekarNumber(9376543) == 9372385)
    assert(nearestKaprekarNumber(13641234) == 13641364)
    print("Passed!")

# Integer Data Structures

def testLengthEncode():
    print('Testing lengthEncode()...', end='')
    assert(lengthEncode(789) == 113789)
    assert(lengthEncode(-789) == 213789)
    assert(lengthEncode(1234512345) == 12101234512345)
    assert(lengthEncode(-1234512345) == 22101234512345)
    assert(lengthEncode(0) == 1110)
    print('Passed!')

def testLengthDecodeLeftmostValue():
    print('Testing lengthDecodeLeftmostValue()...', end='')
    assert(lengthDecodeLeftmostValue(111211131114) == (2, 11131114))
    assert(lengthDecodeLeftmostValue(112341115) == (34, 1115))
    assert(lengthDecodeLeftmostValue(111211101110) == (2, 11101110))
    assert(lengthDecodeLeftmostValue(11101110) == (0, 1110))
    print('Passed!')

def testLengthDecode():
    print('Testing lengthDecode()...', end='')
    assert(lengthDecode(113789) == 789)
    assert(lengthDecode(213789) == -789)
    assert(lengthDecode(12101234512345) == 1234512345)
    assert(lengthDecode(22101234512345) == -1234512345)
    assert(lengthDecode(1110) == 0)
    print('Passed!')

def testIntList():
    print('Testing intList functions...', end='')
    a1 = newIntList()
    assert(a1 == 1110) # length = 0, list = []
    assert(intListLen(a1) == 0)
    assert(intListGet(a1, 0) == 'index out of range')

    a1 = intListAppend(a1, 42)
    assert(a1 == 111111242) # length = 1, list = [42]
    assert(intListLen(a1) == 1)
    assert(intListGet(a1, 0) == 42)
    assert(intListGet(a1, 1) == 'index out of range')
    assert(intListSet(a1, 1, 99) == 'index out of range')

    a1 = intListSet(a1, 0, 567)
    assert(a1 == 1111113567) # length = 1, list = [567]
    assert(intListLen(a1) == 1)
    assert(intListGet(a1, 0) == 567)

    a1 = intListAppend(a1, 8888)
    a1 = intListSet(a1, 0, 9)
    assert(a1 == 111211191148888) # length = 2, list = [9, 8888]
    assert(intListLen(a1) == 2)
    assert(intListGet(a1, 0) == 9)
    assert(intListGet(a1, 1) == 8888)

    a1, poppedValue = intListPop(a1)
    assert(poppedValue == 8888)
    assert(a1 == 11111119) # length = 1, list = [9]
    assert(intListLen(a1) == 1)
    assert(intListGet(a1, 0) == 9)
    assert(intListGet(a1, 1) == 'index out of range')

    a2 = newIntList()
    a2 = intListAppend(a2, 0)
    assert(a2 == 11111110)
    a2 = intListAppend(a2, 0)
    assert(a2 == 111211101110)
    print('Passed!')

def testIntSet():
    print('Testing intSet functions...', end='')
    s = newIntSet()
    assert(s == 1110) # length = 0
    assert(intSetContains(s, 42) == False)
    s = intSetAdd(s, 42)
    assert(s == 111111242) # length = 1, set = [42]
    assert(intSetContains(s, 42) == True)
    s = intSetAdd(s, 42) # multiple adds --> still just one
    assert(s == 111111242) # length = 1, set = [42]
    assert(intSetContains(s, 42) == True)
    print('Passed!')

def testIntMap():
    print('Testing intMap functions...', end='')
    m = newIntMap()
    assert(m == 1110) # length = 0
    assert(intMapContains(m, 42) == False)
    assert(intMapGet(m, 42) == 'no such key')
    m = intMapSet(m, 42, 73)
    assert(m == 11121124211273) # length = 2, map = [42, 73]
    assert(intMapContains(m, 42) == True)
    assert(intMapGet(m, 42) == 73)
    m = intMapSet(m, 42, 98765)
    assert(m == 11121124211598765) # length = 2, map = [42, 98765]
    assert(intMapGet(m, 42) == 98765)
    m = intMapSet(m, 99, 0)
    assert(m == 11141124211598765112991110) # length = 4, 
                                            # map = [42, 98765, 99, 0]
    assert(intMapGet(m, 42) == 98765)
    assert(intMapGet(m, 99) == 0)
    print('Passed!')

def testIntFSM():
    print('Testing intFSM functions...', end='')
    fsm = newIntFSM()
    assert(fsm == 111211411101141110) # length = 2, 
                                      # [empty stateMap, empty startStateSet]
    assert(isAcceptingState(fsm, 1) == False)

    fsm = addAcceptingState(fsm, 1)
    assert(fsm == 1112114111011811111111)
    assert(isAcceptingState(fsm, 1) == True)

    assert(getTransition(fsm, 0, 8) == 'no such transition')
    fsm = setTransition(fsm, 4, 5, 6)
    # map[5] = 6: 111211151116
    # map[4] = (map[5] = 6):  111211141212111211151116
    assert(fsm == 1112122411121114121211121115111611811111111)
    assert(getTransition(fsm, 4, 5) == 6)

    fsm = setTransition(fsm, 4, 7, 8)
    fsm = setTransition(fsm, 5, 7, 9)
    assert(getTransition(fsm, 4, 5) == 6)
    assert(getTransition(fsm, 4, 7) == 8)
    assert(getTransition(fsm, 5, 7) == 9)

    fsm = newIntFSM()
    assert(fsm == 111211411101141110) # length = 2, 
                                      # [empty stateMap, empty startStateSet]
    fsm = setTransition(fsm, 0, 5, 6)
    # map[5] = 6: 111211151116
    # map[0] = (map[5] = 6):  111211101212111211151116
    assert(fsm == 111212241112111012121112111511161141110)
    assert(getTransition(fsm, 0, 5) == 6)

    print('Passed!')

def testAccepts():
    print('Testing accepts()...', end='')
    fsm = newIntFSM()
    # fsm accepts 6*7+8
    fsm = addAcceptingState(fsm, 3)
    fsm = setTransition(fsm, 1, 6, 1) # At state 1, receive 6, move to state 1
    fsm = setTransition(fsm, 1, 7, 2) # At state 1, receive 7, move to state 2
    fsm = setTransition(fsm, 2, 7, 2) # At state 1, receive 7, move to state 2
    fsm = setTransition(fsm, 2, 8, 3) # At state 1, receive 8, move to state 3
    assert(accepts(fsm, 78) == True)
    assert(states(fsm, 78) == 1113111111121113) # length = 3, list = [1,2,3]
    assert(accepts(fsm, 678) == True)
    assert(states(fsm, 678) == 11141111111111121113) # length = 4, 
                                                     # list = [1,1,2,3]

    assert(accepts(fsm, 5) == False)
    assert(accepts(fsm, 788) == False)
    assert(accepts(fsm, 67) == False)
    assert(accepts(fsm, 666678) == True)
    assert(accepts(fsm, 66667777777777778) == True)
    assert(accepts(fsm, 7777777777778) == True)
    assert(accepts(fsm, 666677777777777788) == False)
    assert(accepts(fsm, 77777777777788) == False)
    assert(accepts(fsm, 7777777777778) == True)
    assert(accepts(fsm, 67777777777778) == True)
    print('Passed!')

def testEncodeDecodeStrings():
    print('Testing encodeString and decodeString...', end='')
    assert(encodeString('A') == 111111265) # length = 1, str = [65]
    assert(encodeString('f') == 1111113102) # length = 1, str = [102]
    assert(encodeString('3') == 111111251) # length = 1, str = [51]
    assert(encodeString('!') == 111111233) # length = 1, str = [33]
    assert(encodeString('Af3!') == 1114112651131021125111233) # length = 4, 
                                                          # str = [65,102,51,33]
    assert(decodeString(111111265) == 'A')
    assert(decodeString(1114112651131021125111233) == 'Af3!')
    assert(decodeString(encodeString('WOW!!!')) == 'WOW!!!')
    print('Passed!')

def testIntegerDataStructures():
    testLengthEncode()
    testLengthDecode()
    testLengthDecodeLeftmostValue()
    testIntList()
    testIntSet()
    testIntMap()
    testIntFSM()
    testAccepts()
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
    #testPlay112()

    # hw2-required
    testCarrylessAdd()
    testFindZeroWithBisection()
    testNthKaprekarNumber()

    # hw2-bonus
    testCarrylessMultiply()
    testNearestKaprekarNumber()

    # hw2-spicy-bonus
    # testIntegerDataStructures()

def main():
    cs112_s21_week2_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
