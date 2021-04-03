import math


def integerSquareRoot(v):
    if type(v) != int:
        return None
    if v < 0:
        return None
    N = int(v)
    M = 0
    # 24.5 24
    while M**2 <= N:
        M = M + 1
    return M - 1


'''print(integerSquareRoot(0))
print(integerSquareRoot(24))
print(integerSquareRoot(25))
print(integerSquareRoot(35))
print(integerSquareRoot(36))
print(integerSquareRoot(37))
print(integerSquareRoot(123**2))'''
assert (integerSquareRoot(0) == 0)
assert (integerSquareRoot(1) == 1)
assert (integerSquareRoot(2) == 1)
assert (integerSquareRoot(3) == 1)
assert (integerSquareRoot(4) == 2)
assert (integerSquareRoot(5) == 2)
assert (integerSquareRoot(99) == 9)
assert (integerSquareRoot(123**2) == 123)
assert (integerSquareRoot(123**2 - 1) == 122)
assert (integerSquareRoot(2.4) == None)
assert (integerSquareRoot(-5) == None)
assert (integerSquareRoot('Do not crash here!') == None)


def alternatesEvenOdd(n):
    c = n % 10
    b = n // 10 % 10
    a = n // 100 % 10
    # abc
    # True: EOE OEO
    EOE = a % 2 == 0 and b % 2 != 0 and c % 2 == 0
    OEO = a % 2 != 0 and b % 2 == 0 and c % 2 != 0
    noCons = EOE or OEO
    if noCons: return True
    else: return False
    #print(a,b,c)


#print(alternatesEvenOdd(147))
#print(alternatesEvenOdd(478))
assert (alternatesEvenOdd(147) == True)
assert (alternatesEvenOdd(478) == True)
assert (alternatesEvenOdd(124) == False)
assert (alternatesEvenOdd(235) == False)
assert (alternatesEvenOdd(777) == False)
assert (alternatesEvenOdd(222) == False)
assert (alternatesEvenOdd(787) == True)
assert (alternatesEvenOdd(878) == True)
assert (alternatesEvenOdd(943) == True)
assert (alternatesEvenOdd(652) == True)
assert (alternatesEvenOdd(692) == True)

### 1. Code Tracing


def ct1(n):
    print(1 + 2 * n - 3 * 4, n // 4, n / 4, (n % 4)**3)
    x = (n + 2) % n
    y = (n - 2) % n
    return 10 * x + y


# print(ct1(10))  # prints 5 total values (on 2 lines)


def ct2(x, y):
    x *= 2
    # print(float(y), pow(min(x, int(x)), abs(y - 8)), bool(x / y), bool(1 // y))


# print(ct2(2.8, 5))  # prints 5 total values (on 2 lines)


# h(x,y) is used by ct3()
def h(x, y):
    if (y > x):
        if (x < 5):
            return 2
        elif (x >= 3) and (y < 10):
            return 4
    else:
        return 6
    return x


def ct3(x):
    y = 10 * h(x, 10) + h(3, x)
    z = 10 * h(x, 5) + h(x, x + 1)
    return y + z / 100


# print(ct3(5))

### 2. True/False [10 points; 2 points each
#1 / 0

# ============================================================================ #
# quiz2
# ============================================================================ #


def snarf_prime_digit(n):
    while n > 9:
        if n % 10 % 2 + n // 10 % 10 % 2 != 1:
            return False
        n //= 10
    # n = str(n)
    # for i in range(len(n) - 1):
    #     foo = int(n[i]) % 2 + int(n[i + 1]) % 2
    #     if foo != 1: return False
    return True


def isPrime(n):
    factor = math.ceil(math.sqrt(n))
    if n % 2 == 0 or n % 3 == 0: return False
    for i in range(3, factor + 1, 2):
        # print(n, i)
        if n % i == 0: return False
    return True


def nthSnarfPrime(n):
    found, guess = 0, 10

    while found < n + 1:
        guess += 1
        cond = snarf_prime_digit(guess) and isPrime(guess)
        if cond: found += 1
    return guess


# ============================================================================ #
# test
# ============================================================================ #


def test_snarf_prime_digit():
    print('test_snarf_prime_digit ', end='')
    # print(snarf_prime_digit(984))
    # print(snarf_prime_digit(983))
    # print(snarf_prime_digit(895))
    print('Passed!')


def test_isPrime():
    # print(isPrime(25))
    # print(isPrime(55))
    # print(isPrime(69))
    print('Passed!')


def testNthSnarfPrime():
    print('Testing nthSnarfPrime()...', end='')
    # print(nthSnarfPrime(0))
    # print(nthSnarfPrime(1))
    # print(nthSnarfPrime(29))
    # print(nthSnarfPrime(61))
    # print(nthSnarfPrime(101))
    assert (nthSnarfPrime(0) == 23)
    assert (nthSnarfPrime(1) == 29)
    assert (nthSnarfPrime(5) == 61)
    assert (nthSnarfPrime(9) == 101)
    print('Passed!')


def test_all():
    test_snarf_prime_digit()
    test_isPrime()
    testNthSnarfPrime()


test_all()