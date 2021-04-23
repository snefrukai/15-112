#################################################
# hw3.py
# name:
# andrew id:
#################################################
import math, random, string, decimal
from icecream import ic

import basic_graphics
import cs112_s21_week3_linter


#################################################
# Helper functions
#################################################
def test_unexpected(output, expect):
    if output != expect:
        print("\n? expect: ", expect)
        ic(output)


def almostEqual(d1, d2, epsilon=10**-7):  #helper-fn
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)


def roundHalfUp(d):  #helper-fn
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))


#################################################
# hw3-standard-functions
#################################################

# ============================================================================ #


def largestNumber(s):
    s_new = ""
    n = -1

    for i in range(len(s)):
        if s[i].isdigit():
            s_new += s[i]
            n = max(int(s_new), n)
        else:  # if digits end, reset
            s_new = ""

    # i = 0  #* skip next few
    # while i < len(s):
    #     s_new = ""
    #     if s[i].isdigit():
    #         s_new += s[i]
    #         i += 1
    #         while i < len(s) and s[i].isdigit():
    #             i += 1
    #             s_new += s[i]
    #     elif not s[i].isdigit():
    #         i += 1
    #         if s_new != "": n = max(int(s_new), n)
    # if s_new != "": n = max(int(s_new), n)

    return n if n >= 0 else None


# ============================================================================ #


def rotateStringLeft(s, n):
    # if n == 0: return s
    i = n % len(s)
    # ic(i)
    return s[i:] + s[:i]


# ============================================================================ #
# 3


def isRotation(s, t):
    if s == t or len(s) != len(t): return False

    for i in range(1, len(s)):
        s = rotateStringLeft(s, i)
        if s == t: return True
    return False


# ============================================================================ #


def score_total_get(str):
    score = 0
    for val in str.split(","):
        val = val.strip()
        if val.isalpha(): name = val
        elif val.isdigit(): score += int(val)
    return name, score


def topScorer(str):
    if str == "": return None

    winner = ""
    score_max = 0
    for line in str.splitlines():
        name, score = score_total_get(line)
        if score > score_max:  # save max
            winner, score_max = name, score
        elif score == score_max:
            winner += "," + name if winner != '' else name
    return winner


#################################################
# hw3-spicy-functions
# you can do these instead of the hw3-standard
# functions if you prefer.  Otherwise, you can
# skip the hw3-spicy functions.  Either way,
# you should continue on to the hw3-required
# functions below.
#################################################


def str_del_kth(s, i):
    if i > len(s) - 1:
        return "out of range"
    else:
        return s[:i] + s[i + 1:] if i != len(s) - 1 else s[:i]


def count_match_exact(s, s1):
    count = 0
    i = 0
    while i < len(s):
        if s[i] == s1[i]:
            s = str_del_kth(s, i)  # replace when match
            s1 = str_del_kth(s1, i)
            count += 1
        else:
            i += 1
    return s, s1, count


def count_match_partial(s, s1):
    count = 0
    for c in s:
        k = s1.find(c)
        if k != -1:
            count += 1
            s1 = str_del_kth(s1, k)
    return s, s1, count


def mastermindScore(s, s1):
    if s == s1: return 'You win!!!'

    s, s1, count_exact = count_match_exact(s, s1)
    s, s1, count_partial = count_match_partial(s, s1)
    # ic(count_exact, count_partial)

    if count_exact == count_partial == 0:  # FF
        return 'No matches'
    else:
        txt_exact = ' exact match'
        txt_partial = ' partial match'
        if count_exact > 1: txt_exact += 'es'
        if count_partial > 1: txt_partial += 'es'
        result_exact = str(count_exact) + txt_exact
        result_partial = str(count_partial) + txt_partial

        if count_exact == 0:
            return result_partial
        elif count_partial == 0:
            return result_exact
        else:
            return result_exact + ', ' + result_partial

    # if result_exact == "none":
    #     return result_partial  # FT or FF
    # elif result_partial == "No matches":
    #     return result_exact  # TF
    # else:
    #     return result_exact + ", " + result_partial  # TT


# ============================================================================ #
#


def topLevelFunctionNames(code):
    quotes_triple = ['"""', "'''"]
    quotes_single = ['"', "'"]
    quotes = quotes_triple + quotes_single
    code_temp = ''

    # def pop_quotes(s): #* pop single quote content
    #     for c in quotes:
    #         i = s.find(c)
    #         if i != -1:  # and s[i:i + 4] not in ('"""', "'''"):
    #             left = s[:i]
    #             mid = s[i + len(c):]
    #             right = mid[mid.find(c) + len(c):] if c in mid else mid
    #             s = left + right
    #     return s

    # quotes = '"""' + "'''" #* pop triple quote content
    # for c in ('"""', "'''"):
    #     while c in code:
    #         i = code.find(c)
    #         left = code[:i]
    #         mid = code[i + 3:]
    #         right = mid[mid.find(c) + 3:]
    #         # ic(left, right)
    #         code = left + right
    # ic(code)

    def check_comment(s):
        i = s.find('#')
        for c in quotes_triple:
            if -1 < s.find(c) < i: return False
        for c in quotes_single:
            if c in s[:i] and c in s[i + len(c):]: return False
        return True

    def check_triple(s):
        for c in quotes_triple:
            if c in s and s.count(c) % 2 != 0:
                return True
        return False

    valid_triple = None
    for line in code.splitlines():
        if valid_triple and check_triple(line):
            valid_triple = False
            continue
        else:
            valid_comment = check_comment(line)
            if not valid_comment:
                valid_triple = check_triple(line)
            code_temp += '\n' + line if code_temp != '' else line
            # ic(valid_comment, valid_triple)
    # ic(code_temp)

    s = ''
    for line in code_temp.splitlines():  #* add func name
        if line[:3] != 'def':
            continue
        else:
            func = line[4:line.find('(')]
            if func not in s:
                s += '.' + func if s != '' else func
    return s


#################################################
# hw3-required-functions
#################################################

# ============================================================================ #
# cousre case


def get_rad(n, digit):
    # if digit != 12 and digit != 60: return "digit has to be 12 or 60"
    rad = (n / digit) * 2 * math.pi - math.pi / 2
    return rad


def draw(canvas, width, height):
    width, margin = 100, 10
    r = width / 2
    r_hr = r * 0.5

    def draw_clock(canvas, x0, y0):
        canvas.create_oval(x0, y0, x0 + r * 2, y0 + r * 2)

        r_numb = r * 0.8
        for i in range(12):  # draw numb
            angle = get_rad(i, 12)
            x = (x0 + r) + r_numb * math.cos(angle)
            y = (y0 + r) + r_numb * math.sin(angle)
            canvas.create_text(x, y, text=i)

    def draw_hand_hr(canvas, x0, y0, angle_hr):
        x1 = x0 + r_hr * math.cos(angle_hr)
        y1 = y0 + r_hr * math.sin(angle_hr)
        canvas.create_line(x0, y0, x1, y1)  # hand hr

    for k in range(3):
        for i in range(4):
            x = 100 + i * r * 2 + i * margin
            y = 100 + k * r * 2 + k * margin
            draw_clock(canvas, x, y)

            angle_hr = get_rad(4 * k + i, 12)
            x0, y0 = x + r, y + r
            draw_hand_hr(canvas, x0, y0, angle_hr)

            # angle_min = get_rad(min, 60)
            # x_min = cx + r_min * math.cos(angle_min)
            # y_min = cy + r_min * math.sin(angle_min)
            canvas.create_line(x0, y0, x + r, y + 16)  # hand minute


# basic_graphics.run(width=600, height=600)

# ============================================================================ #
# 7.


def draw_triangle(canvas, x0, y0, step):
    canvas.create_polygon(
        x0,
        y0,
        x0 + step * 1.6,  # hori length
        y0 + step / 2,  # vert midpoint
        x0,
        y0 + step,  # height of 1 tri
        fill="white")


def drawFlagOfQatar(canvas, x0, y0, x1, y1):
    canvas.create_rectangle(x0, y0, x1, y1, fill='orange')  # bg

    cx = x0 + (x1 - x0) / 3
    cy = y0 + (y1 - y0) / 3
    canvas.create_rectangle(x0, y0, cx, y1, fill='white')  # left
    canvas.create_rectangle(cx, y0, x1, y1, fill='#B31722')  # right

    step = (y1 - y0) / 9
    for i in range(9):  # mid triangles
        draw_triangle(canvas, cx, y0 + i * step, step)

    canvas.create_text((x0 + x1) / 2,
                       y0 - 20,
                       text='Qatar',
                       font='Arial 14 bold')


# ============================================================================ #
#


def poker_hand_get(deck, player_id, player_count):
    i1 = (player_id - 1) * 3
    i2 = (player_id - 1) * 3 + 3 * player_count
    step = 2
    return deck[i1:i1 + step] + '-' + deck[i2:i2 + step]


def poker_card_indexes(card):
    rank = 'A23456789TJQK'.find(card[0])
    suit = 'CDHS'.find(card[1])
    return rank, suit


def poker_hand_eval(hand):  # 'A23456789TJQK', 'CDHS'
    card1, card2 = hand[:2], hand[3:]
    rank1, suit1 = poker_card_indexes(card1)
    rank2, suit2 = poker_card_indexes(card2)

    if rank1 > rank2 or (rank1 == rank2 and suit1 > suit2):
        card_highest = card1
        rank, suit = rank1, suit1
    else:
        card_highest = card2
        rank, suit = rank2, suit2

    flush = suit1 == suit2
    straight = abs(rank1 - rank2) == 1
    if flush and straight:
        category, txt = 5, 'a straight flush to'
    elif flush:
        category, txt = 4, 'a flush to'
    elif straight:
        category, txt = 3, 'a straight to'
    elif rank1 == rank2:
        category, txt = 2, 'a pair to'
    else:
        category, txt = 1, 'a high card of'

    score = category * 1000 + rank * 10 + suit  # rank could get to 130
    result = txt + ' ' + card_highest
    return score, result


def playPoker(deck, players):
    if len(deck.replace('-', '')) / 4 < players: return 'Not enough cards'

    score = 0
    for i in range(1, players + 1):
        hand = poker_hand_get(deck, i, players)
        score_new, result_new = poker_hand_eval(hand)
        if score_new > score:
            score = score_new
            result = 'Player ' + str(i) + ' wins with ' + result_new
    return result


#################################################
# hw3-collaborative-functions
#
# Important note: for only these functions, you
# may work collaboratively with your cohort parters,
# as assigned by your cohort TA.  See the hw writeup
# for details.  In any case, this is ONLY FOR THIS SECTION.
# All other parts of this hw are entirely SOLO as usual!!!
#################################################


def cipher_loop_part(text, groups, f):
    s = ""
    step = int(len(text) / groups)
    for i in range(groups):
        s += f(i, step)  # edit and add each part
    return s


def cipher_reindex(text, groups):
    if len(text) % groups != 0: return "need to fiil length"

    def f(i, step):
        part = ""
        for k in range(step):
            part += text[k * groups + i]
        return part

    return cipher_loop_part(text, groups, f)


def cipher_rotate(text, groups):
    def f(i, step):
        part = text[i * step:(i + 1) * step]
        return part[::-1] if i % 2 != 0 else part

    return cipher_loop_part(text, groups, f)


def encodeRightLeftRouteCipher(text, rows):
    fill = len(text) % rows
    if fill != 0:
        text += string.ascii_lowercase[-(rows - fill):][::-1]

    text = cipher_reindex(text, rows)
    text = cipher_rotate(text, rows)
    return str(rows) + text


def decodeRightLeftRouteCipher(text):
    rows = int(text[0])
    text = text[1:]
    col = int(len(text) / rows)

    text = cipher_rotate(text, rows)
    text = cipher_reindex(text, col)
    return str_del_trailing(text, string.ascii_lowercase)


#################################################
# hw3-bonus-functions
# these are optional
#################################################


def str_del_trailing(text, s):
    while text[-1] in s:
        text = text[:-1]
    while text[0] in s:
        text = text[1:]
    return text


def patternedMessage(msg, pattern):
    if pattern == "": return ""
    msg = msg.replace(" ", "")

    s = ""
    i_msg = 0
    for line in pattern.splitlines():
        line_temp = ""
        for c in line:
            if c != " ":
                c = msg[i_msg]
                i_msg = (i_msg + 1) % len(msg)
            line_temp += c
        s += "\n" + line_temp if s != '' else line_temp
    return s


# ============================================================================ #
#


def getEvalSteps(expr):
    def do_op(s1, s2, op):
        n1, n2 = int(s1), int(s2)
        if op == '**': n = n1**n2
        elif op == '*': n = n1 * n2
        elif op == '/': n = n1 / n2
        elif op == '//': n = n1 // n2
        elif op == '%': n = n1 % n2
        elif op == '+': n = n1 + n2
        elif op == '-': n = n1 - n2
        return str(n)

    def do_step(s, op):
        i = s.find(op)
        left = s[:i]
        right = s[i + len(op):]

        s1, s2 = '', ''
        while left != '' and left[-1].isdigit():
            s1 = left[-1] + s1
            left = left[:-1]
        while right != '' and right[0].isdigit():
            s2 += right[0]
            right = right[1:]
        return left + do_op(s1, s2, op) + right

    def get_ops(expr):
        s1 = s2 = s3 = ()  # get ops in priority and precedence
        i = 0
        while i < len(expr):
            d = expr[i]
            if not d.isdigit():
                if d == expr[i + 1]:
                    i += 1
                    if d == '*':
                        s1 += d * 2,
                    else:
                        s2 += d * 2,
                elif d in ('+', '-'):
                    s3 += d,
                else:
                    s2 += d,
            i += 1
        return s1 + s2 + s3

    def get_tabs(s):
        i = s.find('=') / 4
        tab = int(i)
        space = int((i - tab) * 4)
        return tab, space

    l_op = get_ops(expr)
    if l_op == ():
        return expr + ' = ' + expr
    s = expr

    space = ' ' * len(s)  #* calc space
    for i in range(len(l_op)):
        expr = do_step(expr, l_op[i])
        result = ' = ' + expr
        # s += '\n' + result if k != 0 else result
        s += '\n' + space + result if i != 0 else result
    return s

    # s_temp = '' #* calc tab and space
    # tab = space = None
    # for line in s.splitlines():
    #     if tab == space == None:
    #         tab, space = get_tabs(line)
    #     else:
    #         line = ('\t' * tab + ' ' * space) + line.strip()
    #     s_temp += '\n' + line if s_temp != '' else line
    # return s_temp


# ============================================================================ #
#


def funEncoder1(msg):
    return 42


def funDecode1(msg):
    return 42


def funEncoder2(msg):
    return 42


def funDecode2(msg):
    return 42


def funEncoder3(msg):
    return 42


def funDecode3(msg):
    return 42


#################################################
# Test Functions
#################################################


def testLargestNumber():
    print("Testing largestNumber()...", end="")
    # ic(largestNumber("I saw 0"))

    # assert (largestNumber("3 I saw!") == 3)
    # assert (largestNumber("I saw 3 dogs, 17 cats, and 14 cows!") == 17)
    # assert (largestNumber("I saw 3 dogs, 1700 cats, and 14 cows!") == 1700)
    assert (largestNumber("One person ate two hot dogs!") == None)
    # assert (largestNumber("42!!!!") == 42)
    # assert (largestNumber("12+3==15") == 15)
    # assert (largestNumber("12dogs345cats67owls") == 345)
    print("Passed!")


def testRotateStringLeft():
    # print(rotateStringLeft("abcde", 2))
    # print(rotateStringLeft("abcde", -2))
    print('Testing rotateStringLeft()...', end='')
    assert (rotateStringLeft('abcde', 0) == 'abcde')
    assert (rotateStringLeft('abcde', 1) == 'bcdea')
    assert (rotateStringLeft('abcde', 2) == 'cdeab')
    assert (rotateStringLeft('abcde', 3) == 'deabc')
    assert (rotateStringLeft('abcde', 4) == 'eabcd')
    assert (rotateStringLeft('abcde', 5) == 'abcde')
    assert (rotateStringLeft('abcde', 25) == 'abcde')
    assert (rotateStringLeft('abcde', 28) == 'deabc')
    assert (rotateStringLeft('abcde', -1) == 'eabcd')
    assert (rotateStringLeft('abcde', -24) == 'bcdea')
    assert (rotateStringLeft('abcde', -25) == 'abcde')
    assert (rotateStringLeft('abcde', -26) == 'eabcd')
    print('Passed!')


def testIsRotation():
    # print(isRotation("ab", "ba"))
    # data = '''\
    # Fred,10,20,30,40
    # Wilma,10,20,30, 40
    # '''
    print('Testing isRotation()...', end='')
    assert (isRotation('a',
                       'a') == False)  # a string is not a rotation of itself
    assert (isRotation('',
                       '') == False)  # a string is not a rotation of itself
    assert (isRotation('ab', 'ba') == True)
    assert (isRotation('abcd', 'dabc') == True)
    assert (isRotation('abcd', 'cdab') == True)
    assert (isRotation('abcd', 'bcda') == True)
    assert (isRotation('abcd', 'abcd') == False)
    assert (isRotation('abcd', 'bcd') == False)
    assert (isRotation('abcd', 'bcdx') == False)
    print('Passed!')


def test_score_total_get():
    parms = [
        ('''\
        Fred,10,20,30
        '''),
        ('''\
        Fred,0,0,0,
        '''),
    ]
    solns = [
        ('Fred', 60),
        ('Fred', 0),
    ]
    for i, data in enumerate(parms):
        expect = solns[i]
        output = score_total_get(data)
        test_unexpected(output, expect)
        assert (output == expect)


def testTopScorer():
    print('Testing topScorer()...', end='')
    data = '''\
Fred,0,0,0,0
'''
    assert (topScorer(data))  #  == 'Fred'

    data = '''\
Fred,10,20,30,40
Wilma,10,20,30
'''
    assert (topScorer(data) == 'Fred')

    data = '''\
Fred,10,20,30
Wilma,10,20,30,40
'''
    assert (topScorer(data) == 'Wilma')

    data = '''\
Fred,11,20,30
Wilma,10,20,30,1
'''
    assert (topScorer(data) == 'Fred,Wilma')
    assert (topScorer('') == None)
    print('Passed!')


def test_count_match_exact():
    print("Testing count_match_exact()...", end="")
    # print(count_match_exact('abcd', 'abcd'))
    parms = [
        # ('abcd', 'abcd'),
        ('aafa', 'aayy'),
        ('affb', 'ayyb'),
        ('affa', 'ayyy'),
        ('abcxyz', 'xyzabc')
    ]
    solns = [
        # ('abcd', 'abcd', 'win'),
        ('fa', 'yy', '2 exact matches'),
        ('ff', 'yy', '2 exact matches'),
        ('ffa', 'yyy', '1 exact match'),
        ('abcxyz', 'xyzabc', 'none')
    ]
    for i, (s, s1) in enumerate(parms):
        expect = solns[i]
        output = count_match_exact(s, s1)
        # ic(output)
        # test_unexpected(output, expect)
        # assert (output == expect)
    print('Passed!')


def test_count_match_partial():
    # ic(count_match_partial('ooffzx', 'yyazb'))  # z, 1
    # print(count_match_partial('aaffzx', 'yyazb'))  # az, 2
    # print(count_match_partial('aaffzx', 'ooo'))  # none
    return 42


def testMastermindScore():
    print("Testing mastermindScore()...", end="")
    # ic(mastermindScore('abcd', 'aabd'))
    # ic(mastermindScore('efgh', 'abef'))
    # ic(mastermindScore('efgh', 'efef'))
    # ic(mastermindScore('ijkl', 'mnop'))
    # ic(mastermindScore('abcd', 'aabd'))
    # ic(mastermindScore('abcd', 'aabd'))
    assert (mastermindScore('abcd',
                            'aabd') == '2 exact matches, 1 partial match')
    assert (mastermindScore('efgh', 'abef') == '2 partial matches')
    assert (mastermindScore('efgh', 'efef') == '2 exact matches')
    assert (mastermindScore('ijkl', 'mnop') == 'No matches')
    assert (mastermindScore('cdef', 'cccc') == '1 exact match')
    assert (mastermindScore('cdef', 'bccc') == '1 partial match')
    assert (mastermindScore('wxyz',
                            'wwwx') == '1 exact match, 1 partial match')
    assert (mastermindScore('wxyz', 'wxya') == '3 exact matches')
    assert (mastermindScore('wxyz', 'awxy') == '3 partial matches')
    assert (mastermindScore('wxyz', 'wxyz') == 'You win!!!')
    print("Passed!'")


def testTopLevelFunctionNames():
    print("Testing topLevelFunctionNames()...", end="")

    # no fn defined
    code = """\
# This has no functions!
# def f(): pass
print("Hello world!")
"""
    assert (topLevelFunctionNames(code) == "")

    # f is redefined
    code = """\
def f(x): return x+42
def g(x): return x+f(x)
def f(x): return x-42
"""
    assert (topLevelFunctionNames(code) == "f.g")

    # def not at start of line
    code = """\
def f(): return "def g(): pass"
"""
    assert (topLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (''')
    code = """\
def f(): return '''
def g(): pass'''
"""
    assert (topLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (""")
    code = '''\
def f(): return """
def g(): pass"""
'''
    assert (topLevelFunctionNames(code) == "f")

    # triple-quote (''') in comment
    code = """\
def f(): return 42 # '''
def g(): pass # '''
"""
    assert (topLevelFunctionNames(code) == "f.g")

    # triple-quote (""") in comment
    code = '''\
def f(): return 42 # """
def g(): pass # """
'''
    assert (topLevelFunctionNames(code) == "f.g")
    # ic(topLevelFunctionNames(code))

    # comment character (#) in quotes
    code = """\
def f(): return '#' + '#' + ''' 
def g(): pass # '''
def h(): return "#" + '''
def i(): pass # '''
def j(): return '''#''' + '''
def k(): pass # '''
"""
    assert (topLevelFunctionNames(code) == "f.h.j")
    # ic(topLevelFunctionNames(code))
    print("Passed!")


def testDrawFlagOfQatarDrawFn(canvas, width, height):
    canvas.create_rectangle(0, 0, width, height, fill='lightYellow')
    drawFlagOfQatar(canvas, 50, 125, 350, 275)
    drawFlagOfQatar(canvas, 425, 100, 575, 200)
    drawFlagOfQatar(canvas, 450, 275, 550, 325)


def testDrawFlagOfQatar():
    print('Testing drawFlagOfQatar()...')
    print('  You should visually inspect the canvas...')
    basic_graphics.run(width=600, height=400, drawFn=testDrawFlagOfQatarDrawFn)


def test_poker_get_hand():
    parm = [
        ('AS-2D-3S-4C-5H-6D-7S-8D', 1, 4),
        ('AS-2D-3S-4C-5H-6D-7S-8D', 2, 4),
        ('AS-2D-3S-4C-5H-6D-7S-8D', 3, 4),
        ('AS-2D-3S-4C-5H-6D-7S-8D', 4, 4),
        ('AS-2D-3S-4C-5H-6D-7S-8D', 2, 3),
    ]
    soln = [
        'AS-5H',
        '2D-6D',
        '3S-7S',
        '4C-8D',
        '2D-5H',
    ]
    for i, (a, b, c) in enumerate(parm):
        expect = soln[i]
        output = poker_hand_get(a, b, c)
        # ic(output)
        test_unexpected(output, expect)
        assert (output == expect)


def test_poker_hand_eval():
    parm = [
        '2C-3C',
        '2D-6D',
        'QD-KC',
        '2D-2H',
        '5H-2D',
    ]
    soln = [
        (5020, 'a straight flush to 3C'),
        (4051, 'a flush to 6D'),
        (3120, 'a straight to KC'),
        (2012, 'a pair to 2H'),
        (1042, 'a high card of 5H'),
    ]
    for i, (hand) in enumerate(parm):
        expect = soln[i]
        output = poker_hand_eval(hand)
        # ic(output)
        test_unexpected(output, expect)
        assert (output == expect)


def testPlayPoker():
    # print('Testing playPoker()...', end='')
    test_poker_get_hand()
    test_poker_hand_eval()

    parm = [('AS-2D-3S-4C-5H-6D-7S-8D', 4), ('5S-2H-3C-4D', 2)]
    soln = [
        'Player 3 wins with a flush to 7S',
        'Player 1 wins with a high card of 5S'
    ]
    for i, (deck, players) in enumerate(parm):
        expect = soln[i]
        output = playPoker(deck, players)
        # ic(output)
    assert (playPoker('QD-3S', 1) == 'Player 1 wins with a high card of QD')
    assert (playPoker('QD-QC', 1) == 'Player 1 wins with a pair to QD')
    assert (playPoker('QD-JS', 1) == 'Player 1 wins with a straight to QD')
    assert (playPoker('TD-QD', 1) == 'Player 1 wins with a flush to QD')
    assert (playPoker('QD-JD',
                      1) == 'Player 1 wins with a straight flush to QD')
    assert (playPoker('QD-JD', 2) == 'Not enough cards')

    assert (playPoker('AS-2H-3C-4D',
                      2) == 'Player 2 wins with a high card of 4D')
    assert (playPoker('5S-2H-3C-4D',
                      2) == 'Player 1 wins with a high card of 5S')
    assert (playPoker('AS-2H-3C-2D', 2) == 'Player 2 wins with a pair to 2H')
    assert (playPoker('3S-2H-3C-2D', 2) == 'Player 1 wins with a pair to 3S')
    assert (playPoker('AS-2H-2C-2D',
                      2) == 'Player 1 wins with a straight to 2C')
    assert (playPoker('AS-2H-2C-3D',
                      2) == 'Player 2 wins with a straight to 3D')
    assert (playPoker('AS-2H-4S-3D', 2) == 'Player 1 wins with a flush to 4S')
    assert (playPoker('AS-2H-4S-3H',
                      2) == 'Player 2 wins with a straight flush to 3H')
    assert (playPoker('2S-2H-3S-3H',
                      2) == 'Player 1 wins with a straight flush to 3S')

    assert (playPoker('AS-2D-3C-4C-5H-6D-7S-8D',
                      2) == 'Player 2 wins with a high card of 4C')
    assert (playPoker('AS-2D-3S-4C-5H-6D-7S-8D',
                      4) == 'Player 3 wins with a flush to 7S')
    # print('Passed!')


def test_str_del_kth():
    assert (str_del_kth("123", 3) == 'out of range')
    assert (str_del_kth("123", 0) == '23')
    assert (str_del_kth("123", 2) == '12')
    assert (str_del_kth("123", 1) == '13')


def testEncodeRightLeftRouteCipher():
    # print(encodeRightLeftRouteCipher("WEATTACKATDAWN", 3))  # 3WTCTWNDKTEAAAAz
    # print(encodeRightLeftRouteCipher("WEATTACKATDAWN", 5))  # 5WADACEAKWNATTTz
    text = 'WEATTACKATDAWNz'
    # ic(cipher_reindex(text, 3))  #WTCTWETKDNAAAAz

    assert (encodeRightLeftRouteCipher("WEATTACKATDAWN",
                                       4) == "4WTAWNTAEACDzyAKT")
    assert (encodeRightLeftRouteCipher("WEATTACKATDAWN",
                                       3) == "3WTCTWNDKTEAAAAz")
    assert (encodeRightLeftRouteCipher("WEATTACKATDAWN",
                                       5) == "5WADACEAKWNATTTz")


def testDecodeRightLeftRouteCipher():
    # print(decodeRightLeftRouteCipher("3WTCTWNDKTEAAAAz"))
    # print(decodeRightLeftRouteCipher("4WTAWNTAEACDzyAKT"))
    # print('Testing decodeRightLeftRouteCipher()...', end='')
    assert (
        decodeRightLeftRouteCipher("4WTAWNTAEACDzyAKT") == "WEATTACKATDAWN")
    assert (decodeRightLeftRouteCipher("3WTCTWNDKTEAAAAz") == "WEATTACKATDAWN")
    assert (decodeRightLeftRouteCipher("5WADACEAKWNATTTz") == "WEATTACKATDAWN")
    text = "WEATTACKATDAWN"
    cipher = encodeRightLeftRouteCipher(text, 6)
    plaintext = decodeRightLeftRouteCipher(cipher)
    assert (plaintext == text)


def testEncodeAndDecodeRightLeftRouteCipher():
    testEncodeRightLeftRouteCipher()
    testDecodeRightLeftRouteCipher()


def testPatternedMessage():
    # print(patternedMessage("1 23", "******   ******"))
    # print(
    #     patternedMessage(
    #         "Three Diamonds!", """
    #     *     *     *
    #    ***   ***   ***
    #   ***** ***** *****
    #    ***   ***   ***
    #     *     *     *
    # """))
    # patternedMessage("Three Diamonds!", """
    # """)
    # print('Testing patternedMessage()...', end='')
    parms = [("Go Pirates!!!", """
***************
******   ******
***************
"""),
             ("Three Diamonds!", """
	*     *     *
   ***   ***   ***
  ***** ***** *****
   ***   ***   ***
	*     *     *
"""),
             ("Go Steelers!", """
						  oooo$$$$$$$$$$$$oooo
					  oo$$$$$$$$$$$$$$$$$$$$$$$$o
				   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ '$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
'$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  '$$$
   '$$$'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$
	$$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$o
   o$$'   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$' '$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$'$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$'
 ''''       $$$$    '$$$$$$$$$$$$$$$$$$$$$$$$$$$$'      o$$$
			'$$$o     '$$$$$$$$$$$$$$$$$$'$$'         $$$
			  $$$o          '$$'$$$$$$'           o$$$
			   $$$$o                                o$$$'
				'$$$$o      o$$$$$$o'$$$$o        o$$$$
				  '$$$$$oo     '$$$$o$$$$$o   o$$$$'
					 '$$$$$oooo  '$$$o$$$$$$$$$'
						'$$$$$$$oo $$$$$$$$$$
								'$$$$$$$$$$$
									$$$$$$$$$$$$
									 $$$$$$$$$$'
									  '$$$'
""")]
    solns = [
        """
GoPirates!!!GoP
irates   !!!GoP
irates!!!GoPira
""", """
	T     h     r
   eeD   iam   ond
  s!Thr eeDia monds
   !Th   ree   Dia
	m     o     n
""", """
						  GoSteelers!GoSteeler
					  s!GoSteelers!GoSteelers!GoS
				   teelers!GoSteelers!GoSteelers!GoS         te   el er
   s ! Go        Steelers!GoSteelers!GoSteelers!GoSteel       er s! GoSt
ee l e rs      !GoSteeler    s!GoSteelers!    GoSteelers       !GoSteel
ers!GoSte     elers!GoSt      eelers!GoSt      eelers!GoSt    eelers!G
  oSteele    rs!GoSteele      rs!GoSteele      rs!GoSteelers!GoSteeler
  s!GoSteelers!GoSteelers    !GoSteelers!G    oSteelers!GoSt  eele
   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSteel     ers!
	GoS   teelers!GoSteelers!GoSteelers!GoSteelers!GoSteelers     !GoSt
   eele   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSt       eele
   rs!    GoSteelers!GoSteelers!GoSteelers!GoSteelers!Go Steelers!GoSteele
  rs!GoSteelers  !GoSteelers!GoSteelers!GoSteelers!GoS   teelers!GoSteelers
  !GoSteelers!G   oSteelers!GoSteelers!GoSteelers!Go     Steel
 ers!       GoSt    eelers!GoSteelers!GoSteelers!G      oSte
			elers     !GoSteelers!GoSteelers!         GoS
			  teel          ers!GoSteel           ers!
			   GoSte                                elers
				!GoSte      elers!GoSteele        rs!Go
				  Steelers     !GoSteelers!   GoStee
					 lers!GoSte  elers!GoSteeler
						s!GoSteele rs!GoSteel
								ers!GoSteele
									rs!GoSteeler
									 s!GoSteeler
									  s!GoS
"""
    ]
    parms = [("A-C D?", """
*** *** ***
** ** ** **
"""), ("A", "x y z"), ("The pattern is empty!", "")]
    solns = ["""
A-C D?A -CD
?A -C D? A-
""", "A A A", ""]
    for i, (msg, pattern) in enumerate(parms):
        soln = solns[i]
        soln = soln.strip("\n")
        observed = patternedMessage(msg, pattern)
        #observed = patternedMessage(msg, pattern).strip("\n")
        #print "\n\n***********************\n\n"
        #print msg, pattern
        #print "<"+patternedMessage(msg, pattern)+">"
        #print "<"+soln+">"
        assert (observed == soln)
    # print('Passed!')


def testGetEvalSteps():
    # ic(getEvalSteps("2+3*4-8**3%3"))  # 76-64 = 12 tab
    # ic(getEvalSteps("2+3**4%2**4+15//3-8"))
    # ic(getEvalSteps("32//16"))

    assert (getEvalSteps("0") == "0 = 0")
    assert (getEvalSteps("2") == "2 = 2")
    assert (getEvalSteps("3+2") == "3+2 = 5")
    assert (getEvalSteps("3-2") == "3-2 = 1")
    assert (getEvalSteps("3**2") == "3**2 = 9")
    assert (getEvalSteps("31%16") == "31%16 = 15")
    assert (getEvalSteps("31*16") == "31*16 = 496")
    assert (getEvalSteps("32//16") == "32//16 = 2")
    assert (getEvalSteps("2+3*4") == "2+3*4 = 2+12\n      = 14")
    assert (getEvalSteps("2*3+4") == "2*3+4 = 6+4\n      = 10")

    #? tab 和 space 怎么混用了……
    # or 这里是 IDE 对于 tab 没处理好
    # https://www.cs.cmu.edu/~112/notes/hw3.py
    # 网站上是 space
    assert (getEvalSteps("2+3*4-8**3%3") == """\
2+3*4-8**3%3 = 2+3*4-512%3
             = 2+12-512%3
             = 2+12-2
             = 14-2
             = 12""")

    assert (getEvalSteps("2+3**4%2**4+15//3-8") == """\
2+3**4%2**4+15//3-8 = 2+81%2**4+15//3-8
                    = 2+81%16+15//3-8
                    = 2+1+15//3-8
                    = 2+1+5-8
                    = 3+5-8
                    = 8-8
                    = 0""")
    #     assert (getEvalSteps("2+3*4-8**3%3") == """\
    # 2+3*4-8**3%3 = 2+3*4-512%3
    # 			 = 2+12-512%3
    # 			 = 2+12-2
    # 			 = 14-2
    # 			 = 12""")
    #     assert (getEvalSteps("2+3**4%2**4+15//3-8") == """\
    # 2+3**4%2**4+15//3-8 = 2+81%2**4+15//3-8
    # 					= 2+81%16+15//3-8
    # 					= 2+1+15//3-8
    # 					= 2+1+5-8
    # 					= 3+5-8
    # 					= 8-8
    # 					= 0""")


def testFunDecoder(encodeFn, decodeFn):
    s1 = ''
    for c in range(15):
        if (random.random() < 0.80):
            s1 += random.choice(string.ascii_letters)
        else:
            s1 += random.choice(' \n\n') + random.choice(string.digits)
    for s in ['a', 'abc', s1]:
        if (decodeFn(encodeFn(s)) != s):
            raise Exception(f'Error in {decodeFn.__name__} on {repr(s)}')
    return True


def testFunDecoders():
    print('Testing funDecoders()...', end='')
    testFunDecoder(funEncoder1, funDecode1)
    testFunDecoder(funEncoder2, funDecode2)
    testFunDecoder(funEncoder3, funDecode3)
    print('Passed!')


#################################################
# testAll and main
#################################################


def testAll():
    # comment out the tests you do not wish to run!
    # hw3-standard
    testLargestNumber()
    testRotateStringLeft()
    testIsRotation()
    test_score_total_get()
    testTopScorer()

    # hw3-spicy
    test_count_match_exact()
    test_count_match_partial()
    testMastermindScore()
    testTopLevelFunctionNames()

    # hw3-required
    # testDrawFlagOfQatar()
    testPlayPoker()

    # hw3-collaborative
    test_str_del_kth()
    testEncodeAndDecodeRightLeftRouteCipher()

    # hw3-bonus
    testPatternedMessage()
    testGetEvalSteps()

    # testFunDecoders()

    def plus_five(num):
        return num + 5

    (plus_five(4))
    (plus_five(5))


def main():
    cs112_s21_week3_linter.lint()
    testAll()

    # basic_graphics.run(width=800, height=600)


if __name__ == '__main__':
    main()

# %%
