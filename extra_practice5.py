#################################################
# extra-practice5.py
#################################################

import math, string, time
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


def isPrime(n):
    if n == 2 or n == 3 or n == 5: return True  # exclude 2,3,5
    if n < 2 or prime_wheel_basis(n): return False

    for i in range(7, int(n**0.5), 2):  # factor start from 7
        if not prime_wheel_basis((i)) and n % i == 0: return False
    return True


def nthPrime(nth):
    found = 0
    guess = 0
    while (found <= nth):
        guess += 1
        if (isPrime(guess)): found += 1
    return guess


def prime_wheel_basis(n):
    pre = n != 2 and n != 3 and n != 5
    factor = n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n**0.5 == int(n**0.5)
    return pre and factor


def sieve_eratos_des(n):  #* destructive list
    l = [i for i in range(n) if not (prime_wheel_basis(i))]
    ic(l)

    for p in l:
        for i in range(p**2, n + 1, p * 2):  # while p * i <= n
            if i in l and not prime_wheel_basis(i):
                l.remove(i)
    ic(p, i)
    return l


def sieve_eratos(n):  #* non-destructive list
    l = [True] * (n + 1)
    l[0] = l[1] = False
    for i in range(4, len(l)):
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:  # or i**0.5 == int(i**0.5)
            l[i] = False
    l_new = [2, 3, 5]

    for p in range(7, n + 1, 2):
        if l[p] == True:
            # ic(p)
            l_new += (p, )
            for i in range(p**2, n + 1, p * 2):  # p*p+p = p*(p+1) is even
                # ic(i)
                l[i] = False
    return l_new


def sieve_course(n):  #* course method
    isPrime = [True] * (n + 1)  # assume all are prime to start
    isPrime[0] = isPrime[1] = False  # except 0 and 1, of course
    primes = []
    for prime in range(n + 1):
        if (isPrime[prime] == True):
            # we found a prime, so add it to our result
            primes.append(prime)
            # and mark all its multiples as not prime
            for multiple in range(2 * prime, n + 1, prime):
                isPrime[multiple] = False
    return primes


# ============================================================================ #
# ct and roc
# ============================================================================ #


def rc2(L):
    assert ((isinstance(L, list)) and (None not in L))
    i = 0
    while (L[i] != None):
        j = L[i]
        L[i] = None
        i = j
        a = [None] * 2
    return (L == a + [-1] + a)


#################################################
# ep5-functions
#################################################

#################################################
# Test Functions
#################################################


def test_rc2():
    for i in [0, 1, 3, 4]:
        l = [1, 3, -1, 4, i]
        assert rc2(l)


# ============================================================================ #
#


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


def test_isPrime():
    assert (isPrime(3)) == True
    assert (isPrime(5)) == True
    assert (isPrime(17)) == True
    assert (isPrime(83)) == True
    assert (isPrime(173)) == True
    assert (isPrime(509)) == True
    assert (isPrime(511)) == False
    assert (isPrime(1373731)) == False


def test_sieve_eratos():
    # ic(sieve_eratos_des(10))
    # ic(sieve_eratos_des(30))
    # ic(sieve_eratos_des(50))
    # ic(sieve_eratos(100))
    # ic(sieve_eratos(500))
    # ic(sieve_eratos(1000))
    n = 4000
    nth = 50
    # ic(sieve_eratos(1000)[nth])
    sieve_eratos(n)[nth] == nthPrime(nth)
    # test_time(sieve_eratos, n)
    # test_time(sieve_eratos_des, n)
    # test_time(sieve_course, n)


def test_time(func_name, input):
    param = input
    time0 = time.time()
    times = 6
    for i in range(times):
        func_name(param)
        # print(i, end='')
    dist = round((time.time() - time0) * 1000 / times, 2)
    print("Timing sieve_eratos(", param, "):", dist, "ms")


#################################################
# testAll and main
#################################################


def testAll():
    test_rc2()

    test_locker_problem()
    test_isPrime()
    test_sieve_eratos()


def main():
    # cs112_s21_week3_linter.lint()
    testAll()


if __name__ == '__main__':
    main()
