#################################################
# hw3.py
# name:
# andrew id:
#################################################
import cs112_s21_week3_linter
import math, string, random, basic_graphics

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
# hw3-standard-functions
#################################################

# def largestNumber(s):
#     n = 0
#     n_new = ""
#     for i in range(len(s) - 1):
#         if s[i].isdigit():
#             n_new += s[i]
#             if not s[i + 1].isdigit():  # digits end, 78a
#                 n = max(int(n_new), n)
#                 n_new = ""
#             if i + 2 == len(s):  # end with digit, a7
#                 n_new += s[i + 1]  # "" + "7"
#                 n = max(int(n_new), n)
#     # print(n, n_new)
#     if n == 0: return None
#     return n


def largestNumber(s):
    n = 0
    n_new = ""
    for i in range(len(s)):
        if s[i].isdigit():
            n_new += s[i]
            n = max(int(n_new), n)
            # print(n, n_new)
        else:  # if digits end
            n_new = ""
    # print(n, n_new)
    if n == 0: return None
    return n


def rotateStringLeft(s, n):
    n = n % len(s)
    if n == 0: return s
    return s[n:] + s[:n]


def isRotation(s, t):
    if s == t: return False
    if len(s) != len(t): return False

    for i in range(1, len(s)):
        s = rotateStringLeft(s, i)
        # print(s, t)
        if s == t: return True
    return False


def score_total_get(data):
    name = ""
    score_total = 0
    for val in data.split(","):
        val = val.strip()
        # print(val, val.isalpha())
        if val.isalpha(): name = val.strip()
        if val.isdigit(): score_total += int(val)
    return name, score_total


def topScorer(data):
    winner = ""
    score_max = 0
    if data == "": return None

    for line in data.splitlines():
        name, score_total = score_total_get(line)
        if score_total > score_max:  # save max
            winner = name
            score_max = score_total
        elif score_total == score_max:
            winner += "," + name
        # print(line)
        # print(name, score_total)
    return winner


#################################################
# hw3-spicy-functions
# you can do these instead of the hw3-standard
# functions if you prefer.  Otherwise, you can
# skip the hw3-spicy functions.  Either way,
# you should continue on to the hw3-required
# functions below.
#################################################


def count_match_exact(s, s1):
    count = 0
    len_s = len(s)
    match_exact = ""
    text = " exact match"

    for i in range(len(s)):
        if s[i] == s1[i]:
            count += 1
            if not s[i] in match_exact:
                match_exact += s[i]
        # print(i, count, match_exact)
    for c in match_exact:
        s = s.replace(c, "")
        s1 = s1.replace(c, "")

    if count == len_s: result_exact = 'You win!!!'
    elif count == 0: result_exact = "none"
    else:
        if count > 1: text += "es"
        result_exact = str(count) + text
    return s, s1, result_exact


def count_match_partial(s, s1):
    count = 0
    text = " partial match"

    for c in s:
        k = s1.find(c)
        if k >= 0:
            count += 1
            s1 = str_del_kth(s1, k)
            # print(count, k, s1)

    if count == 0: result_partial = 'No matches'
    else:
        if count > 1: text += "es"
        result_partial = str(count) + text
    return s, s1, result_partial


def str_del_kth(s, k):
    # print(s, k, len(s))
    if k > len(s) - 1: return "out of range"
    elif k == len(s) - 1: s = s[:k]
    elif k == 0: s = s[k + 1:]
    else: s = s[:k] + s[k + 1:]
    # print(s[:k], s[k + 1:])
    return s


def mastermindScore(s, s1):
    result = "sth bug"
    # print(s, s1)
    s, s1, result_exact = count_match_exact(s, s1)
    # print(s, s1, result_exact)
    s, s1, result_partial = count_match_partial(s, s1)
    # print(s, s1, result_partial)
    if result_exact == "none":
        result = result_partial
    elif result_partial == "No matches":
        result = result_exact
    else:
        result = result_exact + ", " + result_partial
    return result


def topLevelFunctionNames(code):
    return 42


#################################################
# hw3-required-functions
#################################################


def drawFlagOfQatar(canvas, x0, y0, x1, y1):
    # Replace all of this with your drawing of the flag of Qatar
    # Also: remember to add the title "Qatar" centered above the flag!
    canvas.create_rectangle(x0, y0, x1, y1, fill='orange')
    font = 'Arial 20 bold' if (x1 - x0 > 150) else 'Arial 12 bold'
    canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2,
                       text='Draw the flag\nof Qatar here!',
                       font=font)
    if (x1 - x0 > 100):
        canvas.create_text((x0 + x1) / 2,
                           y1 - 10,
                           text='Remember to add the title!',
                           font='Arial 12 bold')


def playPoker(deck, players):
    return 42


#################################################
# hw3-collaborative-functions
#
# Important note: for only these functions, you
# may work collaboratively with your cohort parters,
# as assigned by your cohort TA.  See the hw writeup
# for details.  In any case, this is ONLY FOR THIS SECTION.
# All other parts of this hw are entirely SOLO as usual!!!
#################################################


def cipher_reindex(text, groups, step):
    text_new = ""
    for k in range(groups):
        part = ""
        for i in range(step):
            index = i * groups + k
            part += text[index]
        # print(k, part)
        text_new += part
    return text_new


def cipher_rotate(text, groups, step):
    text_new = ""
    for i in range(groups):
        part = ""
        part += text[i * step:(i + 1) * step]
        if i % 2 != 0: part = part[::-1]
        # print(part)
        text_new += part
    return text_new


def encodeRightLeftRouteCipher(text, rows):
    col = math.ceil(len(text) / rows)
    fill = col * rows - len(text)

    endcode = text + string.ascii_lowercase[-fill:][::-1]
    endcode = cipher_reindex(endcode, rows, col)
    endcode = cipher_rotate(endcode, rows, col)
    endcode = str(rows) + endcode

    return endcode


def decodeRightLeftRouteCipher(text):
    rows = int(text[0])
    col = int(len(text) / rows)

    decode = text.replace(text[0], "")
    # print(rows, col, decode)
    decode = cipher_rotate(decode, rows, col)
    decode = cipher_reindex(decode, col, rows)
    while decode[-1] in string.ascii_lowercase:
        decode = decode.replace(decode[-1], "")

    return decode


#################################################
# hw3-bonus-functions
# these are optional
#################################################


def trailing_remove(text, s):
    while text[-1] in s:
        text = text[:-1]
    while text[0] in s:
        text = text[1:]
    return text


def patternedMessage(msg, pattern):
    if pattern == "": return ""
    msg = msg.replace(" ", "")

    k = 0
    pattern_new = ""
    for line in pattern.splitlines():
        line_new = ""
        for i in range(len(line)):
            if line[i] != " ":
                k = k % len(msg)
                foo = msg[k]
                k += 1
                # print(foo, ",", end="")
            else:
                foo = " "
            line_new += foo
        # print(line_new)
        pattern_new += "\n" + line_new
    pattern_new = trailing_remove(pattern_new, "\n")

    return pattern_new


def getEvalSteps(expr):
    return 42


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
    # assert (largestNumber("I saw 3") == 3)
    assert (largestNumber("3 I saw!") == 3)
    assert (largestNumber("I saw 3 dogs, 17 cats, and 14 cows!") == 17)
    assert (largestNumber("I saw 3 dogs, 1700 cats, and 14 cows!") == 1700)
    assert (largestNumber("One person ate two hot dogs!") == None)
    assert (largestNumber("42!!!!") == 42)
    assert (largestNumber("12+3==15") == 15)
    assert (largestNumber("12dogs345cats67owls") == 345)
    print("Passed!")


def testRotateStringLeft():
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


def testTopScorer():
    print('Testing topScorer()...', end='')
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


def testMastermindScore():
    print("Testing mastermindScore()...", end="")
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

    # comment character (#) in quotes
    code = """\
def f(): return '#' + '''
def g(): pass # '''
def h(): return "#" + '''
def i(): pass # '''
def j(): return '''#''' + '''
def k(): pass # '''
"""
    assert (topLevelFunctionNames(code) == "f.h.j")
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


def testPlayPoker():
    print('Testing playPoker()...', end='')
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
    print('Passed!')


def testEncodeRightLeftRouteCipher():
    print('Testing encodeRightLeftRouteCipher()...', end='')
    assert (encodeRightLeftRouteCipher("WEATTACKATDAWN",
                                       4) == "4WTAWNTAEACDzyAKT")
    assert (encodeRightLeftRouteCipher("WEATTACKATDAWN",
                                       3) == "3WTCTWNDKTEAAAAz")
    assert (encodeRightLeftRouteCipher("WEATTACKATDAWN",
                                       5) == "5WADACEAKWNATTTz")
    print('Passed!')


def testDecodeRightLeftRouteCipher():
    print('Testing decodeRightLeftRouteCipher()...', end='')
    assert (
        decodeRightLeftRouteCipher("4WTAWNTAEACDzyAKT") == "WEATTACKATDAWN")
    assert (decodeRightLeftRouteCipher("3WTCTWNDKTEAAAAz") == "WEATTACKATDAWN")
    assert (decodeRightLeftRouteCipher("5WADACEAKWNATTTz") == "WEATTACKATDAWN")
    text = "WEATTACKATDAWN"
    cipher = encodeRightLeftRouteCipher(text, 6)
    plaintext = decodeRightLeftRouteCipher(cipher)
    assert (plaintext == text)
    print('Passed!')


def testEncodeAndDecodeRightLeftRouteCipher():
    testEncodeRightLeftRouteCipher()
    testDecodeRightLeftRouteCipher()


def testPatternedMessage():
    print('Testing patternedMessage()...', end='')
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
    print('Passed!')


def testGetEvalSteps():
    print("Testing getEvalSteps()...", end="")
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
    print("Passed!")


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
    testTopScorer()

    # hw3-spicy
    testMastermindScore()
    # testTopLevelFunctionNames()

    # hw3-required
    # testDrawFlagOfQatar()
    # testPlayPoker()

    # hw3-collaborative
    testEncodeAndDecodeRightLeftRouteCipher()

    # hw3-bonus
    testPatternedMessage()
    # testGetEvalSteps()
    # testFunDecoders()


def main():
    cs112_s21_week3_linter.lint()
    testAll()
    # print(rotateStringLeft("abcde", 2))
    # print(rotateStringLeft("abcde", -2))
    # print(isRotation("ab", "ba"))
    # data = '''\
    # Fred,10,20,30,40
    # Wilma,10,20,30, 40
    # '''
    # print(topScorer(data))
    # print(count_match_exact('abcd', 'afff'))  # 1
    # print(count_match_exact('abay', 'afaz'))  # 2
    # print(count_match_exact('afay', 'afaz'))  # 3
    # print(count_match_exact('abcd', 'abcd'))  # win
    # print(count_match_partial('ooffzx', 'yyazb'))  # z, 1
    # print(count_match_partial('aaffzx', 'yyazb'))  # az, 2
    # print(count_match_partial('aaffzx', 'ooo'))  # none
    # print(mastermindScore('abcd', 'aabd'))
    # print(mastermindScore('efgh', 'abef'))
    # print(mastermindScore('efgh', 'efef'))
    # print(mastermindScore('ijkl', 'mnop'))
    # print(mastermindScore('abcd', 'aabd'))
    # print(mastermindScore('abcd', 'aabd'))

    # print(str_del_kth("123", 3))
    # print(str_del_kth("123", 0))
    # print(str_del_kth("123", 2))
    # print(str_del_kth("123", 1))

    # print(encode_fill("WN", 1))
    # print(encode_fill("WN", 2))
    # print(encode_row_get("WEATTACKATDAWN", 3, 5, 0))
    # print(encode_row_get("WEATTACKATDAWNz", 3, 5, 1))
    # print(encode_row_get("WEATTACKATDAWNz", 3, 5, 2))
    # print(encode_row_get("WEATTACKATDAWN", 3, 5, 2))
    # print(encodeRightLeftRouteCipher("WEATTACKATDAWN", 3))  # 3WTCTWNDKTEAAAAz
    # print(encodeRightLeftRouteCipher("WEATTACKATDAWN", 5))  # 5WADACEAKWNATTTz

    # print(decodeRightLeftRouteCipher("3WTCTWNDKTEAAAAz"))
    # print(decodeRightLeftRouteCipher("4WTAWNTAEACDzyAKT"))
    # print(patternedMessage("1 23", "******   ******"))


#     print(
#         patternedMessage(
#             "Three Diamonds!", """
#     *     *     *
#    ***   ***   ***
#   ***** ***** *****
#    ***   ***   ***
#     *     *     *
# """))

#     patternedMessage(
#         "Three Diamonds!", """
# """)

if __name__ == '__main__':
    main()
