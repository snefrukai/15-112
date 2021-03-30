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


def largestNumber(s):
    n = 0
    n_new = ""
    for i in range(len(s)):
        if s[i].isdigit():
            n_new += s[i]
            n = max(int(n_new), n)
            # print(n, n_new)
        else:  # if find alpha
            n_new = ""
    # print(n, n_new)
    if n == 0: return None
    return n


def rotateStringLeft(s, n):
    return 42


def isRotation(s, t):
    return 42


def topScorer(data):
    return 42


#################################################
# hw3-spicy-functions
# you can do these instead of the hw3-standard
# functions if you prefer.  Otherwise, you can
# skip the hw3-spicy functions.  Either way,
# you should continue on to the hw3-required
# functions below.
#################################################


def mastermindScore(target, guess):
    return 42


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


def encodeRightLeftRouteCipher(text, rows):
    return 42


def decodeRightLeftRouteCipher(cipher):
    return 42


#################################################
# hw3-bonus-functions
# these are optional
#################################################


def patternedMessage(msg, pattern):
    return 42


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
    # testRotateStringLeft()
    # testIsRotation()
    # testTopScorer()

    # hw3-spicy
    # testMastermindScore()
    # testTopLevelFunctionNames()

    # hw3-required
    # testDrawFlagOfQatar()
    # testPlayPoker()

    # hw3-collaborative
    # testEncodeAndDecodeRightLeftRouteCipher()

    # hw3-bonus
    # testPatternedMessage()
    # testGetEvalSteps()
    # testFunDecoders()


def main():
    cs112_s21_week3_linter.lint()
    testAll()


if __name__ == '__main__':
    main()
