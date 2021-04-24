#################################################
# extra-practice5.py
#################################################

import math, string, time
from starter import name
from icecream import ic
import operator

import cs112_s21_week8_linter
from hw3 import test_unexpected

#################################################
# Helper functions
#################################################

import decimal


def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))


# ============================================================================ #
#* Worked Examples
# ============================================================================ #


def locker_problem(n):
    #* loop
    l_bool = [True if i % 2 != 0 else False for i in range(n + 1)]
    student = n
    for student in range(3, student + 1):
        for i in range(student, n + 1, student):
            l_bool[i] = not l_bool[i]

    l_lockers = [i for i in range(1, n + 1) if l_bool[i]]

    # #* mathematical
    # l = [i + 1 for i in range(n)]
    # l_new = []

    # for i in range(len(l)):
    #     root = l[i]**0.5
    #     if root == int(root):
    #         l_new += [l[i]]

    return l_lockers


# ============================================================================ #
#


def prime_wheel_basis(n):
    newvariable406 = n != 2 and n != 3
    has_factor = n % 2 == 0 or n % 3 == 0 or n**0.5 == int(n**0.5)
    return has_factor and newvariable406
    # return has_factor


def isPrime(n):
    if n == 2 or n == 3: return True
    elif n < 2 or prime_wheel_basis(n): return False

    for i in range(5, int(n**0.5), 6):
        if n % i == 0 or n % (i + 2) == 0: return False
        #* range has already skip multis of n in wheel
        # if not prime_wheel_basis(i) and (n % i == 0 or n % (i + 5) == 0):
    return True


def nthPrime(nth):
    found, guess = 0, 0
    while (found <= nth):
        guess += 2 if guess >= 3 else 1
        if (isPrime(guess)): found += 1
    return guess


def sieve_eratos_des(n):  #* des
    # l = [2, 3] + [i for i in range(n) if not (prime_wheel_basis(i))]
    l = [i for i in range(n) if not (prime_wheel_basis(i))]
    # ic(l)

    for p in l:
        for i in range(p**2, n + 1, p * 2):  # while p * i <= n
            if i in l: l.remove(i)
    return l


def sieve_eratos(n):  #* non-des
    l = [False if (i > 3 and i % 2 == 0) else True for i in range(n + 1)]
    # l = [True] * (n + 1) #* about the same speed
    l[0] = l[1] = False

    # for i in range(4, len(l)): #* dont need to pre edit
    #     if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:  # or i**0.5 == int(i**0.5)
    #         l[i] = False

    l_primes = [2]
    for p in range(3, n + 1, 2):
        if l[p] == True:
            l_primes += [p]
            for i in range(p**2, n + 1, p * 2):  # p ood, p*p+p = p*(p+1) even
                l[i] = False
    return l_primes


def sieve_course(n):  #* course method
    l = [True] * (n + 1)  # assume all are prime to start
    l[0] = l[1] = False  # except 0 and 1, of course
    l_primes = []
    for prime in range(n + 1):
        if (l[prime] == True):
            # we found a prime, so add it to our result
            l_primes.append(prime)
            # and mark all its multiples as not prime
            for multiple in range(2 * prime, n + 1, prime):
                l[multiple] = False
    return l_primes


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


def alternatingSum(l):
    if l == []: return 0

    n = 0
    pow = 2 if l[0] >= 0 else 3
    for i in range(len(l)):
        sign = (-1)**(i + pow)
        n += sign * l[i]
        # ic(i, sign)
    return n


# ============================================================================ #
#
def median(l):
    if len(l) == 0: return None

    l_new = sorted(l)
    i = len(l) / 2
    if int(i) != i:
        i = math.floor(i)
        return l_new[i]
    else:
        i = int(i)
        return (l_new[i] + l_new[i - 1]) / 2


# ============================================================================ #
#
def isSorted(l):
    if l[0] != min(l) and l[0] != max(l): return False

    # while len(l) > 1: #* des
    #     l = l[1:]
    #     cond1 = l[0] == min(l) and l[0] != min(l)
    #     cond2 = l[0] == max(l) and l[0] != max(l)
    #     if cond1 or cond2: return False

    i = 1  #* non-des
    while i < len(l) - 1:
        cond1 = l[0] == min(l) and l[i] > l[i + 1]
        cond2 = l[0] == max(l) and l[i] < l[i + 1]
        if cond1 or cond2:
            return False
        i += 1
    return True


# ============================================================================ #
#
def smallestDifference(l):
    if len(l) == 0: return -1
    l.sort()
    l_dif = [abs(l[i] - l[i + 1]) for i in range(len(l) - 1)]
    return min(l_dif)


# ============================================================================ #
#
def lookAndSay(l):
    if l == []: return []

    l_new = []
    i, count = 0, 1
    for i in range(1, len(l)):
        if l[i] == l[i - 1]:
            count += 1
        else:  # end of equal seq
            l_new += [(count, l[i - 1])]
            count = 1
        if i == len(l) - 1:  # end of list
            l_new += [(count, l[i])]
    return l_new


def inverseLookAndSay(l):
    if l == []: return []

    l_new = []
    for v in l:
        l_new += [v[1]] * v[0]
    # l_new = [[v[1]] * v[0] for v in l]
    return l_new


# ============================================================================ #
#
def nondestructiveRemoveRepeats(l):
    # l_new = [v for v in l if v not in l_new]
    l_new = []
    for v in l:
        if v not in l_new:
            l_new += [v]
    return l_new


def destructiveRemoveRepeats(l):
    i = 0
    while i < len(l):
        while l.count(l[i]) > 1:
            k = l.index(l[i], i + 1)
            l.pop(k)
        # while l[i] in l[i + 1:]:
        #     k = l[i + 1:].index(l[i])
        #     l.pop(i + 1 + k)
        i += 1


# ============================================================================ #
#
def isPalindromicList(l):
    if l == []:
        return False
    for i in range(int(len(l) / 2)):
        if l[i] != l[-1 - i]:
            return False
    return True


# ============================================================================ #
#
def reverse(l):
    for i in range(len(l) - 1):
        # ic(i, l, l[-1])
        l.insert(i, l[-1])
        l.pop()


# ============================================================================ #
#
def list_2_op_each_val(l1, l2, f):
    l = [f(l1[i], l2[i]) for i in range(min(len(l1), len(l2)))]
    return l


def vectorSum(l1, l2):
    def f(n1, n2):
        return n1 + n2

    # l = l_op_two(l1, l2, lambda l1, l2: l1 + l2)
    return list_2_op_each_val(l1, l2, f)


def dotProduct(l1, l2):
    def f(n1, n2):
        return n1 * n2

    # l = l_op_two(l1, l2, lambda l1, l2: l1 * l2)
    l = list_2_op_each_val(l1, l2, f)
    return sum(l)


# ============================================================================ #
#


def moveToBack(l1, l2):
    # l_hits = [0] * len(l2) #* create l of hit
    # for i in range(len(l2)):
    #     n = l2[i]
    #     if n in l1:
    #         l_hits[i] = l1.count(n)
    #         while n in l1:
    #             l1.remove(n)
    # for i in range(len(l2)):
    #     if l_hits[i] != 0:
    #         l1 += [l2[i]] * l_hits[i]

    for c in l2:
        count = l1.count(c)
        for _ in range(count):
            l1.remove(c)
        l1 += [c] * count
        # ic(c, count, l1)


# ============================================================================ #
#
def binaryListToDecimal(l):
    n = 0
    for i in range(len(l)):
        if l[i] != 0:
            n += 2**(len(l) - 1 - i)
        # ic(n, len(l) - 1 - i)
    return n


# ============================================================================ #
#
def split(s, delimiter):
    l = []
    while delimiter in s:
        i = s.find(delimiter)
        if i != 0:
            l += [s[:i]]
        s = s[i + 1:]
    # if s != '': l += [s]
    # return l
    return l if s == '' else l + [s]


def join(l, delimiter):
    s = ''
    for d in l:
        s += d if s == '' else delimiter + d
    return s


# ============================================================================ #
#
def repeatingPattern(l):  # True if l == l0*k
    if len(l) % 2 != 0: return False
    for k in range(2, int(len(l) / 2) + 1):
        if l[:k] * int(len(l) / k) == l:
            return True
    return False


# ============================================================================ #
#
def s_sort_alpha(s):
    return "".join(sorted(s))


def mostAnagrams(l):
    l_temp = [s_sort_alpha(c) for c in l]
    l_anag = lookAndSay(sorted(l_temp))
    # a = [('fox', 5), ('cat', 4), ('dog', 5)]
    # a = sorted(a, key=operator.itemgetter(1))
    # a = sorted(a, key=lambda x: x[1])
    # foo = max([i[0] for i in l_anag])
    # ic(a)
    # l_anag = sorted(l_anag, key=operator.itemgetter(0), reverse=True)
    # ic(l_anag)

    l_anag_most = l_get_most(l_anag)
    for d in l:
        if any(s_sort_alpha(d) in v for v in l_anag_most):
            return d  # sublist


# ============================================================================ #
#
def mul2(x):
    return x * 2


def plus3(x):
    return x + 3


def map(f, l):
    return [f(v) for v in l]


# ============================================================================ #
#
def firstNEvenFibonacciNumbers(n):
    l = [0, 1]
    l_even = []

    while len(l_even) < n:
        m = l[-2] + l[-1]
        if m % 2 == 0:
            l_even += [m]
        l += [m]
    return l_even


# ============================================================================ #
#
def l_get_most(l):
    l_new = sorted(l, reverse=True)
    for i in range(1, len(l_new)):
        if l_new[i][0] < l_new[0][0]:
            l_new = l_new[:i]
            break
    return sorted(l_new)


def mostCommonName(l):
    if l == []: return None
    l_name = lookAndSay(sorted(l))
    l_name_most = l_get_most(l_name)
    l_new = [v[1] for v in l_name_most]
    return l_new


# ============================================================================ #
#
def histogram(l):
    def change_to_key(val):
        if val < 10: return '10-- '
        elif val >= 90: return '90++ '
        else:
            s = str(val // 10)
            return s + '0-' + s + '9'

    l_input = [change_to_key(v) for v in l]
    l_input_count = lookAndSay(sorted(l_input))  # [(1, '10-- '), (1, '80-89')]
    # ic(l_input_count)

    l_keys = [change_to_key(i * 10) for i in range(10)]
    l_input_range = [l_keys.index(d[1]) for d in l_input_count]  # [0, 8]
    # ic(l_input_range)

    l_output = []
    for i in range(min(l_input_range), max(l_input_range) + 1):
        bar = ''
        for d in l_input_count:
            if d[1] == l_keys[i]:
                bar = ' ' + '*' * d[0]
                break
        l_output += [l_keys[i] + ':' + bar]
    s = "\n".join(l_output)
    return s


# ============================================================================ #
#
def nearestWords_match(word, s):
    def pop_mismatch_digit(word, s):
        # for c in word:
        #     if c not in s: return word.replace(c, '')
        for i in range(len(word)):
            if word[i] != s[i]: return word[:i] + word[i + 1:]

    def count_mismatches(word, s):
        count = 0
        for i in range(len(word)):
            if word[i] != s[i]:
                count += 1
        return count

    if word == s:
        print("!: word and s should not be euqal")
    elif len(word) - 1 == len(s):  # add
        if s in word or (pop_mismatch_digit(word, s) == s):
            return True
    elif len(word) == len(s):  # change
        if count_mismatches(word, s) == 1:
            return True
    elif len(word) + 1 == len(s):  # del
        if word in s or (pop_mismatch_digit(s, word) == word):
            return True
    return False


def nearestWords(l, s):
    if s in l: return s
    l_new = [word for word in l if nearestWords_match(word, s)]
    return l_new if l_new != [] else None


# ============================================================================ #
#
def bowlingScore(l):
    n, i, frame = 0, 0, 0
    while i + 1 < len(l) and frame < 10:
        strike, spare = (l[i] == 10), (l[i] + l[i + 1] == 10)
        n += l[i] + l[i + 1]
        if strike or spare:
            n += l[i + 2]
        if spare or not (strike or spare):  # 2 scores in 1 frame
            i += 1
        i += 1
        frame += 1
    return n


# ============================================================================ #
#
def polynomialToString(l):
    s = ''
    for i in range(len(l)):
        if l[i] == 0: continue
        sign = ' + ' if l[i] > 0 else ' - '
        expo = 'n^' + str(len(l) - 1 - i) if i != len(l) - 1 else ''
        s += sign + str(abs(l[i])) + expo
    # if s[:3] == ' + ':         s = s[3:]
    # return s
    return s if s[:3] != ' + ' else s[3:]


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
    assert (isPrime(121)) == False
    assert (isPrime(173)) == True
    assert (isPrime(509)) == True
    assert (isPrime(511)) == False
    assert (isPrime(1373731)) == False


def test_sieve_eratos():
    n = 1000
    assert (sieve_eratos_des(n) == sieve_eratos(n))
    # ic(sieve_eratos_des(10))
    # ic(sieve_eratos_des(50))
    # ic(sieve_eratos(50))

    # ic(sieve_eratos(10))
    # ic(sieve_eratos(100))
    # ic(sieve_eratos(500))
    # ic(sieve_eratos(1000))
    n = 40000
    nth = 50
    # ic(sieve_eratos(1000)[nth])
    sieve_eratos(n)[nth] == nthPrime(nth)
    # test_time(sieve_eratos, n)
    # test_time(sieve_course, n)
    # test_time(sieve_eratos_des, n)


def test_time(func_name, parag):
    time0 = time.time()
    times = 10
    for i in range(times):
        func_name(parag)
    dist = roundHalfUp((time.time() - time0) * 1000 / times, 2)
    print(f"Timing in {times} times, n =", parag, ":", dist, "ms")


# ============================================================================ #
#
def test_alternatingSum():
    parm = [
        [],
        [1, 1],
        [1, 1, 1],
        [-2, 1, 1],
    ]
    soln = [
        0,
        0,
        1,
        2,
    ]
    for i, l in enumerate(parm):
        expect = soln[i]
        output = alternatingSum(l)
        # ic(output)
        test_unexpected(output, expect)
        assert (output == expect)


def test_median():
    parm = [
        [],
        [1],
        [1, 2],
        [3, 2, 1],
        [3, 4, 2, 1],
        [3, 4, 5, 2, 1],
        [3.5, 4, 5, 2, 1],
        [6, 3.5, 4, 5, 2, 1],
    ]
    soln = [None, 1, 1.5, 2, 2.5, 3, 3.5, 3.75]
    for i, l in enumerate(parm):
        expect = soln[i]
        output = median(l)
        # ic(output)
        test_unexpected(output, expect)
        assert (output == expect)


def test_isSorted():
    parm = [
        [1, 3, 2],
        [1, 2, 2],
        [5, 3, 4, 2],
        [2, 3, 4, 5],
        [1, 2, 3, 3, 2, 1],
    ]
    soln = [
        False,
        True,
        False,
        True,
        False,
    ]
    for i, l in enumerate(parm):
        expect = soln[i]
        output = isSorted(l)
        # ic(output)
        test_unexpected(output, expect)
        assert (output == expect)


def test_smallestDifference():
    parm = [
        [],
        [19, 2, 83, 6, 27],
        [19, -12, 83, -10, 27],
        [0, 1],
        [0, 2, 99, 97, -1, -2],
    ]
    soln = [
        -1,
        4,
        2,
        1,
        1,
    ]
    for i, l in enumerate(parm):
        expect = soln[i]
        output = smallestDifference(l)
        # ic(output)
        test_unexpected(output, expect)
        assert (output == expect)


def test_lookAndSay():
    parm = [
        [],
        [1, 1, 1],
        [1, 2, 2, 3],
        [1, 1, 2, 3],
        [3, 3, 8, -10, -10, -10],
        [3, 3, 8, 3, 3, 3, 3],
    ]
    soln = [
        [],
        [(3, 1)],
        [(1, 1), (2, 2), (1, 3)],
        [(2, 1), (1, 2), (1, 3)],
        [(2, 3), (1, 8), (3, -10)],
        [(2, 3), (1, 8), (4, 3)],
    ]
    for i, l in enumerate(parm):
        expect = soln[i]
        output = lookAndSay(l)
        # ic(output)
        test_unexpected(output, expect)
        assert (output == expect)

    i = 4
    # ic(inverseLookAndSay(soln[i]))
    assert inverseLookAndSay(soln[i]) == parm[i]


def test_nondestructiveRemoveRepeats():
    parm = [
        [1, 1, 1],
        [1, 3, 5, 3, 3, 2, 1, 7, 5],
    ]
    soln = [
        [1],
        [1, 3, 5, 2, 7],
    ]
    for i, l in enumerate(parm):
        expect = soln[i]
        output = nondestructiveRemoveRepeats(l)
        # ic(output)
        test_unexpected(output, expect)
        assert (output == expect)

    L = [1, 3, 5, 3, 3, 2, 1, 7, 5]
    assert (nondestructiveRemoveRepeats(L) == [1, 3, 5, 2, 7])
    assert (L == [1, 3, 5, 3, 3, 2, 1, 7, 5])  # nondestructive!

    destructiveRemoveRepeats(L)
    assert (L == [1, 3, 5, 2, 7])  # destructive!
    # ic(L)


def test_isPalindromicList():
    parm = [
        [],
        [1, 2, 1],
        [1, 2, 3, 2, 1],
        [1, 2, 3, 3, 1],
        ['a', 'b', 'a', 'b'],
        [(1, 1), (1, 2), (1, 1)],
        [(1, 1), (1, 2), (2, 1)],
    ]
    soln = [
        False,
        True,
        True,
        False,
        False,
        True,
        False,
    ]
    for i, l in enumerate(parm):
        expect = soln[i]
        output = isPalindromicList(l)
        # ic(output)
        test_unexpected(output, expect)
        assert (output == expect)


def test_reverse():
    parm = [
        [1, 2, 3],
        [1, 1, 3],
        [4, 3, 2, 1],
    ]
    soln = [
        [3, 2, 1],
        [3, 1, 1],
        [1, 2, 3, 4],
    ]
    for i, l in enumerate(parm):
        expect = soln[i]
        output = reverse(l)
        # ic(l)
        # assert l == expect
        # test_unexpected(output, expect)
        # assert (output == expect)


def test_vectorSum():
    parm = [
        ([2, 4], [20, 30]),
        ([1, 2, 3], [1, 2, 3]),
    ]
    soln = [
        [22, 34],
        [2, 4, 6],
    ]
    for i, (l1, l2) in enumerate(parm):
        expect = soln[i]
        output = vectorSum(l1, l2)
        # ic(output)
        test_unexpected(output, expect)
        assert (output == expect)


def test_dotProduct():
    parm = [
        ([1, 2, 3], [4, 5, 6]),
        ([2, 2, 3], [4, 5, 6]),
        ([2, 2, 3], [4, 5, 6, 7]),
    ]
    soln = [
        32,
        36,
        36,
    ]
    for i, (l1, l2) in enumerate(parm):
        expect = soln[i]
        output = dotProduct(l1, l2)
        # ic(output)
        test_unexpected(output, expect)
        assert (output == expect)


def test_moveToBack():
    parm = [
        ([2, 3, 3, 4, 1, 5], [3, 2]),
        # ([2, 3, 3, 4, 1, 5, 3, 2], [3, 2]),
        # ([2, 3, 3, 4, 1, 5], [3, 0]),
    ]
    soln = [
        [4, 1, 5, 3, 3, 2],
        [4, 1, 5, 3, 3, 3, 2, 2],
        [2, 4, 1, 5, 3, 3],
    ]
    for i, (l1, l2) in enumerate(parm):
        expect = soln[i]
        output = moveToBack(l1, l2)
        # ic(output)
        # test_unexpected(l1, expect)
        # assert (l1 == expect)

    # l_hit = [3, 0], [2, 0]
    # moveToBack_hit(l_hit, 3)
    # moveToBack_hit(l_hit, 2)
    # ic(l_hit)


def test_binaryListToDecimal():
    parm = [
        [1, 0],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
    ]
    soln = [
        2,
        11,
        13,
    ]
    for i, l in enumerate(parm):
        expect = soln[i]
        output = binaryListToDecimal(l)
        # ic(output)
        test_unexpected(output, expect)
        assert (output == expect)


def test_split():
    parm = [
        ("ab,cd,efg", ","),
        ("ab,cd,efg,", ","),
        (",ab,cd,efg,", ","),
        (", ab ,cd,efg,", ","),
    ]
    soln = [
        ["ab", "cd", "efg"],
        ["ab", "cd", "efg"],
        ["ab", "cd", "efg"],
        [" ab ", "cd", "efg"],
    ]
    for i, (s, d) in enumerate(parm):
        expect = soln[i]
        output = split(s, d)
        # ic(output)
        test_unexpected(output, expect)
        assert output == expect


def test_join():
    parm = [
        (["ab", "cd", "efg"], ","),
        (["ab ", "c d", "e g"], "-"),
    ]
    soln = [
        "ab,cd,efg",
        "ab -c d-e g",
    ]
    for i, (l, d) in enumerate(parm):
        expect = soln[i]
        output = join(l, d)
        # ic(output)
        test_unexpected(output, expect)
        assert output == expect


def test_repeatingPattern():
    parm = [
        [1, 2, 3, 1, 2, 3],  # True (b==[1,2,3] and k=2)
        [1, 2, 3, 1, 2],
        [1, 2, 1, 2, 1, 2],  # [1,2]
    ]
    soln = [
        True,
        False,
        True,
    ]
    for i, (l) in enumerate(parm):
        expect = soln[i]
        output = repeatingPattern(l)
        # ic(output)
        test_unexpected(output, expect)
        assert output == expect


def test_mostAnagrams():
    parm = [
        ['zoo', 'cat', 'hot', 'act', 'tho', 'cool'],
        ['cat', 'hot', 'tho', 'cool'],
        ['hot', 'tho'],
        # ['cat','hot','act','tho','mach','cham','hamc'],
    ]
    soln = [
        'cat',
        'hot',
        'hot',
    ]
    for i, (l) in enumerate(parm):
        expect = soln[i]
        output = mostAnagrams(l)
        # ic(output)
        test_unexpected(output, expect)
        assert output == expect


def test_map():
    parm = [
        (plus3, [2, 4, 7]),
        (mul2, [2, 4, 7]),
    ]
    soln = [
        [5, 7, 10],
        [4, 8, 14],
    ]
    for i, (f, l) in enumerate(parm):
        expect = soln[i]
        output = map(f, l)
        # ic(output)
        test_unexpected(output, expect)
        assert output == expect


def test_firstNEvenFibonacciNumbers():
    parm = [
        4,
        5,
    ]
    soln = [
        [2, 8, 34, 144],
        [2, 8, 34, 144, 610],
    ]
    for i, n in enumerate(parm):
        expect = soln[i]
        output = firstNEvenFibonacciNumbers(n)
        # ic(output)
        test_unexpected(output, expect)
        assert output == expect


def test_mostCommonName():
    parm = [
        ['Jane', 'Aaron', 'Jane', 'Cindy', 'Aaron'],
        ['Jane', 'Aaron', 'jane', 'Cindy', 'Aaron'],
    ]
    soln = [
        ['Aaron', 'Jane'],
        ['Aaron'],
    ]
    for i, n in enumerate(parm):
        expect = soln[i]
        output = mostCommonName(n)
        # ic(output)
        test_unexpected(output, expect)
        assert output == expect


def test_histogram():
    parm = [
        [73, 62, 91, 74, 100, 77],
        [86, 5],
        [97, 86, 5],
        [73, 62, 91, 74, 100, 77, 5],
    ]
    soln = [
        ('''\
60-69: *
70-79: ***
80-89:
90++ : **\
'''),
        ('''\
10-- : *
10-19:
20-29:
30-39:
40-49:
50-59:
60-69:
70-79:
80-89: *\
'''),
        ('''\
10-- : *
10-19:
20-29:
30-39:
40-49:
50-59:
60-69:
70-79:
80-89: *
90++ : *\
'''),
        ('''\
10-- : *
10-19:
20-29:
30-39:
40-49:
50-59:
60-69: *
70-79: ***
80-89:
90++ : **\
'''),
    ]
    for i, n in enumerate(parm):
        expect = soln[i]
        output = histogram(n)
        # ic(output)
        test_unexpected(output, expect)
        assert output == expect
    l = [
        '10-- : *', '10-19:', '20-29:', '30-39:', '40-49:', '50-59:', '60-69:',
        '70-79:', '80-89: *', '90++ : *'
    ]
    l = "\n".join(l)
    # print(l)


def test_nearestWords_match():
    parm = [
        ('cat', 'at'),
        ('hat', 'ht'),
        ('hat', 'xt'),  # add 
        ('cat', 'yat'),
        ('cat', 'cyt'),
        ('cat', 'yct'),  # change
        ('hat', 'haty'),
        ('hat', 'htat'),
        ('hat', 'yhat'),  # del, in
        ('hat', 'haat'),  # del, del
        ('hat', 'htay'),
    ]
    soln = [
        True,
        True,
        False,  # add
        True,
        True,
        False,  # change
        True,
        True,
        True,  # del
        True,
        False,
    ]
    for i, (s, s1) in enumerate(parm):
        expect = soln[i]
        output = nearestWords_match(s, s1)
        # ic(output)
        test_unexpected(output, expect)
        assert output == expect


def test_nearestWords():
    test_nearestWords_match()

    parm = [
        (['cat', 'hat'], 'at'),
        (['cat', 'hat'], 'ct'),  # add
        (['cat', 'hat'], 'bat'),
        (['cat', 'hat'], 'cab'),  # change
        (['cat', 'hat'], 'htat'),
        (['hat', 'cat'], 'hcat'),  # del
        (['cat', 'hat'], 'ab'),
        (['hat', 'cat'], 'cat'),
    ]
    soln = [
        ['cat', 'hat'],
        ['cat'],  # add
        ['cat', 'hat'],
        ['cat'],  # change
        ['hat'],
        ['hat', 'cat'],  # del
        None,
        'cat'
    ]
    for i, (l, s) in enumerate(parm):
        expect = soln[i]
        output = nearestWords(l, s)
        # ic(output)
        test_unexpected(output, expect)
        assert output == expect


def test_bowlingScore():
    parm = [
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 1],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 1, 10],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 1, 5],
        [1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 6, 4, 7, 3, 8, 2, 9, 1, 5, 5, 6],
        [1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 6, 4, 7, 3, 8, 2, 9, 1, 10, 10, 6],
        [1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 6, 4, 7, 3, 8, 2, 9, 1, 4, 4],
        [1, 2, 2, 2, 3, 2, 4, 2, 5, 2, 6, 2, 7, 2, 8, 0, 9, 0, 1, 0],
        [10, 2, 1, 3, 7, 10, 5, 5, 10, 7, 1, 8, 2, 9, 1, 1, 9, 5],
    ]
    soln = [
        300,
        289,
        279,
        274,
        155,
        170,
        146,
        60,
        147,
    ]
    for i, (l) in enumerate(parm):
        expect = soln[i]
        output = bowlingScore(l)
        # ic(output)
        test_unexpected(output, expect)
        assert output == expect


def test_polynomialToString():
    parm = [
        [2, -3, 0, 4],
        [2, -3, 0, 0],
        [0, -3, 0, 4],
        [5, 2, -3, 0, 4],
        [0, 2, -3, 0, 4],
        [0, 0, -3, 0, 0],
    ]
    soln = [
        "2n^3 - 3n^2 + 4",
        "2n^3 - 3n^2",
        " - 3n^2 + 4",
        "5n^4 + 2n^3 - 3n^2 + 4",
        "2n^3 - 3n^2 + 4",
        " - 3n^2",
    ]
    for i, (l) in enumerate(parm):
        expect = soln[i]
        output = polynomialToString(l)
        # ic(output)
        test_unexpected(output, expect)
        assert output == expect


#################################################

# testAll and main
#################################################


def testAll():
    print('testing all...', end='')
    test_rc2()

    test_locker_problem()
    test_isPrime()
    test_sieve_eratos()

    test_alternatingSum()
    test_median()
    test_isSorted()
    test_smallestDifference()
    test_lookAndSay()
    test_nondestructiveRemoveRepeats()
    test_isPalindromicList()
    test_reverse()
    test_vectorSum()
    test_dotProduct()
    test_moveToBack()
    test_binaryListToDecimal()
    test_split()
    test_join()
    test_mostAnagrams()
    test_map()
    test_firstNEvenFibonacciNumbers()
    test_mostCommonName()
    test_histogram()
    test_nearestWords()
    test_bowlingScore()
    test_polynomialToString()
    print('all passed')


def main():
    cs112_s21_week8_linter.lint()
    testAll()


if __name__ == '__main__':
    main()
