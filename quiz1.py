import math
from icecream import ic
from cmu_112_graphics import *
import time

# ============================================================================ #
#* quiz1
# ============================================================================ #


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
#* quiz2
# ============================================================================ #


# ============================================================================ #
# CT
def ct1(x, y):
    for i in range(x):
        for j in range(i, y):
            if (i + j) % 3 == 0:
                print(j)
        if i < 2:
            print(112)
            if (i + j > 4):
                break


# ct1(3, 5)
def ct2(a, b, c):
    n = 0
    while n < 1234:
        print(n)
        n += c
        n *= a
        b, c = c, b
    return n


# print(ct2(10, 7, 2))


def rc1(x):
    if not isinstance(x, int):
        return False
    elif (x < 1000) or (5000 < x):
        return False

    t = 0
    while x > 0:
        t *= 100
        a = x % 10
        b = (x % 100) - a
        x = x // 100
        t += 10 * a + b // 10
    return t == 2021


# ============================================================================ #
# FR


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
#* quiz3
# ============================================================================ #
def averageGrade(student, gradebook):
    student = student.lower()
    gradebook = gradebook.lower()
    for line in gradebook.splitlines():
        name = None
        score = count = 0
        for entry in line.split(','):
            # ic(entry)
            if (name == None):
                name = entry
            elif entry != '--':  # wrong: name != None
                score += int(entry)
                count += 1
        # ic(score)
        if (name == student):
            if (count == 0):
                return None
            else:
                return int(score / count)  # wrong: score
    return None


def ct1(s):
    t = s.upper()
    s += 'z'
    t *= len(s + t)
    return f's+t{s+t}'


# print(ct1('a'))
def ct2(r, s):
    t = ''
    for i in range(0, len(r), 2):
        t += str(s.find(r[i]))

    result = f'{t}=={eval(t)}'
    return result


# print(ct2('amazing', 'zambia'))


def rc1(s):
    n, c = ord(s[0]), 0
    while s != '':
        assert (ord(s[0]) == n)
        n -= 1
        c += 1
        s = s[1:]
    return (chr(n) == 'B') and (c == 4)


print(rc1('FEDC'))

# ============================================================================ #
#* Quiz5 Version A
# ============================================================================ #

# from cmu_112_graphics import *

# def appStarted(app):
#     appReset(app)

# def appReset(app):
#     app.cx = app.width / 2
#     app.cy = app.height / 2
#     app.r = 50
#     app.step = 5
#     app.gameOver = False
#     app.gamePause = False

# def keyPressed(app, event):
#     if not app.gameOver:
#         if event.key == 'p': app.gamePause = not app.gamePause
#         elif event.key == 's' and not app.gamePause:
#             if app.step > 0: app.step += 2
#             elif app.step < 0: app.step -= 2

# def mousePressed(app, event):
#     foo = ((event.x - app.cx)**2 + (event.y - app.cy)**2)**0.5 <= app.r
#     if not app.gameOver and not app.gamePause:
#         if foo: app.r = app.r / 2
#         else: app.gameOver = True

# def timerFired(app):
#     if not app.gameOver and not app.gamePause:
#         if (app.cx > app.width and app.cy > app.height) or (app.cx < 0
#                                                             and app.cy < 0):
#             app.step = -app.step
#         app.cx += app.step
#         app.cy += app.step

# def redrawAll(app, canvas):
#     canvas.create_oval(app.cx - app.r,
#                        app.cy - app.r,
#                        app.cx + app.r,
#                        app.cy + app.r,
#                        fill='red')
#     if app.gameOver:
#         canvas.create_text(app.width / 2, app.height / 2, text='Game Over')

# runApp(width=400, height=400)

# ============================================================================ #
# *midterm1a
# ============================================================================ #


def isPerfectSquare(n):
    foo = n**0.5
    return foo == int(foo)


def contain_zero(n):
    # while n > 0:
    #     if n % 10 == 0: return True
    #     n = n // 10

    # ic(n, n % 10 == 0)
    if n < 10: return False # recur test
    elif n % 10 == 0: return True
    else: return contain_zero(n // 10)


def isSortOfSquarish(n):
    if n <= 0 or isPerfectSquare(n) or contain_zero(n): return False

    l = []
    while n > 0:
        l += [n % 10]
        n //= 10
    l = sorted(l)

    n_temp = 0
    for i in range(len(l)):
        n_temp += l[i] * 10**(len(l) - 1 - i)
    # ic(n_temp)

    if isPerfectSquare(n_temp): return True
    else: return False


def nthSortOfSquarish(nth):
    l = []
    n = 0
    while len(l) - 1 < nth:
        if isSortOfSquarish(n): l += [n]
        n += 1
    # ic(l)
    return l[nth]


# ============================================================================ #
# Free Response: animation

# def appStarted(app):
#     appReset(app)

# def appReset(app):
#     app.l_dot = []
#     app.time_start = time.time()
#     app.line_i = None

# def nearestDot(app, cx, cy):
#     l_dist = []
#     if len(app.l_dot) > 1:
#         for (x, y) in app.l_dot:
#             l_dist += [((cx - x)**2 + (cy - y)**2)**0.5]
#         l_dist = l_dist[:-1]
#         app.line_i = l_dist.index(min(l_dist))
#         # ic(app.l_dot, app.line_i)

# def mousePressed(app, event):
#     app.cx = event.x
#     app.cy = event.y
#     app.l_dot += [(event.x, event.y)]
#     nearestDot(app, event.x, event.y)

# def timerFired(app):
#     # print(time.time() - app.time_start)
#     if time.time() - app.time_start > 5: appReset(app)

# def keyPressed(app, event):
#     if event.key == 'r': appReset(app)

# def redrawAll(app, canvas):
#     r = 20
#     for (x, y) in app.l_dot:
#         canvas.create_oval(x - r, y - r, x + r, y + r, fill='green')

#     if app.line_i != None:
#         line = app.l_dot[app.line_i]
#         canvas.create_line(app.cx, app.cy, line[0], line[1], width=1)

# runApp(width=500, height=500)

# ============================================================================ #
#* test
# ============================================================================ #


def test_integerSquareRoot():
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


def test_alternatesEvenOdd():
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


# ============================================================================ #
#


def test_snarf_prime_digit():
    # print('test_snarf_prime_digit ', end='')
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
    # print('Testing nthSnarfPrime()...', end='')
    # print(nthSnarfPrime(0))
    # print(nthSnarfPrime(1))
    # print(nthSnarfPrime(29))
    # print(nthSnarfPrime(61))
    # print(nthSnarfPrime(101))
    assert (nthSnarfPrime(0) == 23)
    assert (nthSnarfPrime(1) == 29)
    assert (nthSnarfPrime(5) == 61)
    assert (nthSnarfPrime(9) == 101)
    # print('Passed!')


# ============================================================================ #
#


def tes_averageGrade():
    gradebook = '''\
dan,80,78,--
mae,86,87,88
sue,--,--,--'''

    # ic(averageGrade('dan', gradebook))
    assert (type(averageGrade('dan', gradebook) == int))
    assert (averageGrade('dan', gradebook) == 79)
    assert (averageGrade('mae', gradebook) == 87)
    assert (averageGrade('sue', gradebook) == None)
    assert (averageGrade('max', gradebook) == None)
    assert (averageGrade('DAN', gradebook) == 79)


# ============================================================================ #
# midterm1a


def testIsPerfectSquare():
    # print('Testing isPerfectSquare(n))...', end='')
    assert (isPerfectSquare(4) == True)
    assert (isPerfectSquare(9) == True)
    assert (isPerfectSquare(10) == False)
    assert (isPerfectSquare(225) == True)
    assert (isPerfectSquare(1225) == True)
    assert (isPerfectSquare(1226) == False)
    # print('Passed')


def testIsSortOfSquarish():
    # print('Testing isSortOfSquarish(n))...', end='')
    # ic(contain_zero(1204))
    assert contain_zero(12034) == True
    # ic(isSortOfSquarish(414))  # 144

    assert (isSortOfSquarish(52) == True)
    assert (isSortOfSquarish(16) == False)
    assert (isSortOfSquarish(502) == False)
    assert (isSortOfSquarish(414) == True)
    assert (isSortOfSquarish(5221) == True)
    assert (isSortOfSquarish(6221) == False)
    assert (isSortOfSquarish(-52) == False)
    # print('Passed')


def testNthSortOfSquarish():
    # print('Testing nthSortOfSquarish()...', end='')
    # ic(nthSortOfSquarish(8))
    assert (nthSortOfSquarish(0) == 52)
    assert (nthSortOfSquarish(1) == 61)
    assert (nthSortOfSquarish(2) == 63)
    assert (nthSortOfSquarish(3) == 94)
    assert (nthSortOfSquarish(4) == 252)
    assert (nthSortOfSquarish(8) == 522)
    # print('Passed')


# ============================================================================ #
#


def test_all():
    # quiz1
    test_integerSquareRoot()
    test_alternatesEvenOdd()

    # quiz2
    test_snarf_prime_digit()
    test_isPrime()
    testNthSnarfPrime()
    # print(rc1(1202))

    # quiz3
    tes_averageGrade()

    # midterm1a
    testIsPerfectSquare()
    testIsSortOfSquarish()
    testNthSortOfSquarish()


test_all()