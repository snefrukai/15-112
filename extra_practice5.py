#################################################
# extra-practice5.py
#################################################

import math, string, time
from icecream import ic
from hw3 import test_unexpected
import operator

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
    # l = [
    #     False if i > 3 and (i % 2 == 0 or i % 3 == 0 or i % 5 == 0) else True
    #     for i in range(n + 1)
    # ]
    # ic(l)
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


def alternatingSum(l):
    if len(l) == 0: return False
    sum = 0
    if l[0] >= 0: foo = 2
    else: foo = 2 + 1

    for i in range(len(l)):
        sign = (-1)**(i + foo)
        sum += l[i] * sign
        # ic(i, sign)
    return sum


# ============================================================================ #
#
def median(l):
    if len(l) == 0: return None
    l_new = sorted(l)
    mid_nth = len(l) / 2

    if int(mid_nth) != mid_nth:
        mid_nth = math.floor(mid_nth)
        n = l_new[mid_nth]
    else:
        mid_nth = int(mid_nth)
        n = (l_new[mid_nth] + l_new[mid_nth - 1]) / 2
    # ic(l_new, mid_nth, mid)
    return n


# ============================================================================ #
#
def isSorted(l):
    order_asc = None
    if l[0] != min(l) and l[0] != max(l): return False
    elif l[0] == min(l): order_asc = True
    elif l[0] == max(l): order_asc = False

    while len(l) > 1:
        l = l[1:]
        if order_asc and l[0] != min(l): return False
        elif not order_asc and l[0] != max(l): return False

    # ic(l, order_asc)
    return True


# ============================================================================ #
#
def smallestDifference(l):
    if len(l) == 0: return -1
    l_dif = []
    l.sort()

    for i in range(len(l) - 1):
        dif = abs(l[i] - l[i + 1])
        l_dif += [dif]
    # ic(l, l_dif)
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
        elif l[i] != l[i - 1]:  # end of equal seq
            l_new += [(count, l[i - 1])]
            count = 1
        if i == len(l) - 1:  # end of list
            l_new += [(count, l[i])]
        # ic(len(l), i, count, l[i], l[i + 1])

    return l_new


def inverseLookAndSay(l):
    if l == []: return []
    l_new = []

    for item in l:
        l_new += [item[1]] * item[0]
        # for i in range(item[0]):
        #     l_new += [item[1]]
    return l_new


# ============================================================================ #
#
def nondestructiveRemoveRepeats(l):
    l_new = []
    for i in range(len(l)):
        if l[i] not in l_new: l_new += [l[i]]
        # ic(i, l[i], l_new[-1])
    return l_new


def destructiveRemoveRepeats(l):
    l_new = []
    i = 0

    while i < len(l):
        if l[i] not in l_new:
            l_new += [l[i]]
            i += 1
        else:
            l.pop(i)
        # ic(i, len(l))


# ============================================================================ #
#


def isPalindromicList(l):
    if l == []: return False
    for i in range(int(len(l) / 2)):
        if l[i] != l[-1 - i]: return False
    return True


# ============================================================================ #
#


def reverse(l):
    for i in range(len(l)):
        # ic(i, l, l[-1])
        l.insert(i, l[-1])
        l.pop()


# ============================================================================ #
#


def l_op_two(l1, l2, f):
    l_new = []
    l_len = min(len(l1), len(l2))
    for i in range(l_len):
        l_new += [f(l1[i], l2[i])]
        #     l_new += [l1[i] + l2[i]]  #* non-dest
        #     # l1[i] = l1[i] + l2[i] #* dest
        # return l1 + l2
        # ic(l_new)
    return l_new


def vectorSum(l1, l2):
    # l = l_op_two(l1, l2, lambda l1, l2: l1 + l2)
    l = l_op_two(l1, l2, lambda *args: sum(args))
    return l


def dotProduct(l1, l2):
    l = l_op_two(l1, l2, lambda l1, l2: l1 * l2)
    return sum(l)


# ============================================================================ #
#
def moveToBack_hit(l_hit, n):
    for i in range(len(l_hit)):
        if n == l_hit[i][0]: l_hit[i][1] += 1


def moveToBack(l1, l2):
    l_hits = [0] * len(l2)

    for i in range(len(l2)):
        n = l2[i]
        if n in l1:
            l_hits[i] = l1.count(n)
            while n in l1:
                l1.remove(n)
    # ic(l1, l2, l_hits)

    for i in range(len(l2)):
        if l_hits[i] != 0:
            l1 += [l2[i]] * l_hits[i]
    # ic(l1)


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
        if i == 0:
            s = s[i + 1:]
            continue
        l += [s[:i]]
        s = s[i + 1:]
        # ic(s)
    if s != '': l += [s]
    return l


def join(l, delimiter):
    s = ''
    for d in l:

        s += delimiter + d
    s = s.replace(delimiter, '', 1)
    return s


# ============================================================================ #
#
def repeatingPattern(l):
    for k in range(2, int(len(l) / 2) + 1):
        foo = len(l) / k
        # ic(k, foo, l[:k])
        if foo != int(foo): continue
        elif l[:k] * int(foo) == l: return True
    return False


# ============================================================================ #
#
def s_sort_alpha(s):
    return "".join(sorted(list(s)))


def l_first_hit(l, d, f):
    if any(f(d) in i for i in l):
        # ic(f(d), l, d)
        # ic(f(d) in (2, 'act'))
        return d


def mostAnagrams(l):
    l_temp = l[:]
    for i in range(len(l_temp)):
        l_temp[i] = s_sort_alpha(l_temp[i])

    l_anag = lookAndSay(sorted(l_temp))
    l_anag_most = l_most_get(l_anag)

    for d in l:
        foo = l_first_hit(l_anag_most, d, lambda x: s_sort_alpha(x))
        if foo != None: return foo
    # if any(s_sort_alpha(d) in i for i in l_most_anag):
    #     return d


# a = [('fox', 5), ('cat', 4), ('dog', 5)]
# a = sorted(a, key=operator.itemgetter(1))
# a = sorted(a, key=lambda x: x[1])
# foo = max([i[0] for i in l_anag])
# ic(a)

# ============================================================================ #
#


def mul2(x):
    return x * 2


def plus3(x):
    return x + 3


def map(f, l):
    for i in range(len(l)):
        l[i] = f(l[i])
    return l


# ============================================================================ #
#
def firstNEvenFibonacciNumbers(n):
    l = [0, 1]
    l_even = []

    i = 2
    while len(l_even) < n:
        foo = l[i - 2] + l[i - 1]
        if foo % 2 == 0: l_even += [foo]
        l += [foo]
        i += 1
    # ic(l, l_even)
    return l_even


# ============================================================================ #
#
def l_most_get(l):
    l_new = sorted(l, reverse=True)

    count_max = l_new[0][0]
    for i in range(1, len(l_new)):
        if l_new[i][0] < count_max:
            l_new = l_new[:i]
            break
    l_new.sort()
    return l_new


def mostCommonName(l):
    if l == []: return None
    l.sort()

    l_name_most = l_most_get(lookAndSay(l))
    for i in range(len(l_name_most)):
        l_name_most[i] = l_name_most[i][1]
    return l_name_most


# ============================================================================ #
#
def histogram_format(val):
    if val < 10: return '10-- '
    elif val >= 90: return '90++ '
    else:
        foo = str(val // 10)
        return foo + '0-' + foo + '9'


def histogram(l):
    l_check = [histogram_format(i * 10) for i in range(10)]
    l_temp = l[:]
    for i in range(len(l_temp)):
        foo = l_temp[i]
        l_temp[i] = histogram_format(foo)
    l_temp.sort()
    l_input_count = lookAndSay(l_temp)

    l_input = []
    l_input_range = []
    for d in l_input_count:
        l_input += d[1],
        l_input_range += l_check.index(d[1]),
    # ic(l_input_count)
    # ic(l_input_range)

    l_output = []
    for i in range(min(l_input_range), max(l_input_range) + 1):
        bar = ''
        for d in l_input_count:
            if d[1] == l_check[i]:
                bar = ' ' + '*' * d[0]
                break
        l_output += [l_check[i] + ':' + bar]
    # ic(l_output)
    l_output = "\n".join(l_output)
    # ic(len(l_output))

    return l_output


# ============================================================================ #
#
def nearestWords_match_pop(s_long, s_short):
    for c in s_long:
        if c not in s_short:
            s_long = s_long.replace(c, '')
            break
    return s_long


def nearestWords_match(word, s):
    if word == s: print("!: word and s should not be euqal")

    elif len(word) - 1 == len(s):  # add
        if s in word: return True
        word = nearestWords_match_pop(word, s)
        if word == s: return True

    elif len(word) == len(s):  # change
        count_mismatch = 0
        for i in range(len(word)):
            if word[i] != s[i]: count_mismatch += 1
        if count_mismatch == 1: return True

    elif len(word) + 1 == len(s):  # del
        if word in s: return True
        for i in range(len(s)):
            if s[i] != word[i]:
                i_mismatch = i
                break
        s = s[:i_mismatch] + s[i_mismatch + 1:]
        if word == s: return True
        # ic(s_sub)

    return False


def nearestWords(l, s):
    if s in l: return s
    l_new = []

    for word in l:
        if nearestWords_match(word, s):
            l_new += [word]
        # ic(s, d)
    if l_new == []: return None
    else: return l_new


# ============================================================================ #
#
def bowlingScore(l):
    n_score, i, n_frame = 0, 0, 0

    while i + 1 < len(l):
        # ic(i, len(l), k, l[i])
        strike = l[i] == 10
        spare = l[i] + l[i + 1] == 10

        n_score += l[i] + l[i + 1]
        if strike or spare:
            n_score += l[i + 2]
        if spare or not (strike or spare):
            i += 1

        i += 1
        n_frame += 1
        if n_frame == 10: break
        # ic(n_score)
    return n_score


# ============================================================================ #
#
def polynomialToString(l):
    s = ''
    for i in range(len(l)):
        sign = ''
        if l[i] == 0: continue
        elif l[i] > 0 and i > 0: sign = ' + '
        elif l[i] < 0: sign = ' - '

        if i == len(l) - 1: exponentation = ''
        else: exponentation = 'n^' + str(len(l) - 1 - i)

        s += sign + str(abs(l[i])) + exponentation

    if s[:3] == ' + ': s = s[3:]
    return s


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

    # ic(sieve_eratos(10))
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
    parm = [[1, 3, 2], [1, 2, 2], [5, 3, 4, 2], [2, 3, 4, 5],
            [1, 2, 3, 3, 2, 1]]
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
        # ic(i)
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
    # assert (L == [1, 3, 5, 2, 7])  # destructive!
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
        assert l == expect
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
    ]
    soln = [
        32,
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
        ([2, 3, 3, 4, 1, 5, 3, 2], [3, 2]),
        ([2, 3, 3, 4, 1, 5], [3, 0]),
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
        test_unexpected(l1, expect)
        assert (l1 == expect)

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
        [1, 2, 1, 2, 1, 2],
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
        # assert output == expect
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
        ('hat', 'yhat'),
        ('hat', 'hayt'),
        ('hat', 'htay'),  # del
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
        True,
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


def main():
    # cs112_s21_week3_linter.lint()
    testAll()


if __name__ == '__main__':
    main()
