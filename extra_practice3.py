#################################################
# extra-practice3.py
#################################################

import cs112_s21_week3_linter
import math, string, random, basic_graphics
from icecream import ic
from hw3 import str_del_kth

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
# ep3-functions
#################################################


def vowelCount(s):
    vowels = 'aeiou'
    vowels += vowels.upper()
    count = 0
    for c in s:
        if c in vowels: count += 1
    return count


# ============================================================================ #
#


def interleave(s1, s2):
    s = ''
    len_min = min(len(s1), len(s2))

    for i in range(len_min):
        s += s1[i] + s2[i]
    s += s1[len_min:] if len_min < len(s1) else s2[len_min:]
    return s


# ============================================================================ #
#


def caesar_cipher_digit(s, shift):
    # s_target = string.digits + string.ascii_letters
    # i = s_target.find(s)  # abs postison = relative postion + distance
    # if s.isdigit(): i = (i + shift) % 10
    # elif s.islower(): i = (i - 10 + shift) % 26 + 10
    # elif s.isupper(): i = (i - 10 + shift) % 26 + 10 + 26
    # return s_target[i]

    if s.isdigit():
        chars = string.digits
        step = 10
    elif s.isalpha():
        chars = string.ascii_lowercase if s.islower(
        ) else string.ascii_uppercase
        step = 26
    i = chars.find(s)
    return chars[(i + shift) % step]


def applyCaesarCipher(message, shift):
    s = ''
    for c in message:
        s += caesar_cipher_digit(c, shift) if c != ' ' else c
    return s


# ============================================================================ #
#


def areAnagrams(s1, s2):
    if len(s1) != len(s2): return False

    while s1 != '':
        count1, count2 = 0, 0
        chars = s1[0].lower() + s1[0].upper()
        for c in chars:
            count1 += s1.count(c)
            count2 += s2.count(c)
            s1 = s1.replace(c, '')
        if count1 != count2:
            return False
    return True


# ============================================================================ #
#


def sameChars(s1, s2):
    if not (type(s1) == str and type(s2) == str): return False
    elif s1 == s2 == '': return True

    while s1 != '':  # old way
        c = s1[0]
        if s2.find(c) == -1: return False
        s1 = s1.replace(c, '')
        s2 = s2.replace(c, '')
    return s2 == ''

    # s_temp = '' # list of unique c in s1
    # for c in s1:
    #     if c not in s_temp:
    #         s_temp += c
    #         if s2.find(c) == -1: return False
    #         s2 = s2.replace(c, '')
    # return s2 == ''


# ============================================================================ #
#


def hasBalancedParentheses(s):
    if s.find(")") < s.find("("): return False  # ')('

    while s.count("(") != 0:
        if s.count(")") == 0: return False  # '('
        for c in '()':
            s = s.replace(c, '', 1)
    return s.count(")") == 0


# ============================================================================ #
#


def order_bubble(s):
    chars = string.ascii_letters + string.digits
    for i in range(len(s) - 1):
        s_origin = s
        for i in range(len(s) - 1):
            if chars.find(s[i]) > chars.find(s[i + 1]):
                s = s[:i] + (s[i + 1] + s[i]) + s[i + 2:]
        if s == s_origin: return s  # no change
    return s


def leastFrequentLetters(s):
    if s == '': return ''

    result = ''
    count = 0
    while s != '':
        c = s[0]
        if c.isalpha():
            letters = c.lower() + c.upper()
            count_new = 0
            for c in letters:
                count_new += s.count(c)
            if count == 0 or count_new < count:  # fisrt and smaller
                count = count_new
                result = letters[0]  # replace with smaller
            elif count_new == count:
                result += letters[0]  # add if count is equal
            for c in letters:
                s = s.replace(c, '')
        else:
            s = s.replace(c, '')
    return order_bubble(result)


# ============================================================================ #
#


def is_included(s, s_test):
    return s.find(s_test) >= 0


def longestCommonSubstring(s1, s2):
    if s1 == '' or s2 == '': return ''
    s = ''

    for i in range(len(s1)):
        s_temp = ''
        for k in range(i, len(s1)):  # last char, or no further match
            if is_included(s2, s_temp + s1[k]):
                s_temp += s1[k]
            else:
                break
        if len(s_temp) > len(s) or (len(s_temp) == len(s) and s_temp < s):
            s = s_temp
    return s


# ============================================================================ #
#


def is_palindro(s):
    for i in range(int(len(s) / 2)):
        if s[i] != s[-1 - i]: return False
    return True


def longestSubpalindrome(str):
    s, s_temp = '', ''

    for i in range(len(str)):
        s_temp = str[i:]
        while s_temp != '' and not is_palindro(s_temp):
            s_temp = s_temp[:-1]
        if s == '':
            s = s_temp
        elif len(s_temp) > len(s) or (len(s_temp) == len(s) and s_temp > s):
            s = s_temp
    return s


# ============================================================================ #
#


def replace(s, target, val):
    if s.find(target) == -1: return s

    s_new = ''
    for i in range(s.count(target)):
        posn = s.find(target)
        s_new += s[:posn] + val  # left part
        # ic(count, s, posn, s_new)
        s = s[posn + len(target):]  # right part
    return s_new + s  # rem part (no hit)


# ============================================================================ #
#


def collapseWhitespace(s):
    s_new = ''

    prev_space = False  #* check last char
    for c in s:
        if not c.isspace():
            s_new += c
            prev_space = False
        elif c.isspace() and not prev_space:  # prev is char
            s_new += ' '
            prev_space = True

    # i = 0 #* skip next few ' '
    # while i < len(s):
    #     if not s[i].isspace():
    #         s_new += s[i]
    #         i += 1
    #     elif s[i].isspace():
    #         s_new += ' '
    #         i += 1
    #         while i < len(s) and s[i].isspace():
    #             i += 1

    return s_new


# ============================================================================ #
#


def wordWrap(s, n):
    s_temp = ''
    for i in range(math.ceil(len(s) / n)):  # 7/4 + 1 = 2
        chars = s[:n]
        chars = chars.strip()
        chars = chars.replace(' ', '-')
        s_temp += '\n' + chars if i != 0 else chars
        s = s[n:]
    return s_temp

    # s = s_new  #* course method
    # while s.count(' ') != 0:
    #     posn = s.find(' ')
    #     if s[posn - 1].isalpha() and s[posn + 1] != '\n':
    #         s = s.replace(' ', '-', 1)
    #     else:
    #         s = s.replace(' ', '', 1)
    # return s_new


#################################################
# Test Functions
#################################################


def testVowelCount():
    print('Testing vowelCount()...', end='')
    assert (vowelCount('abcdefg') == 2)
    assert (vowelCount('ABCDEFG') == 2)
    assert (vowelCount('') == 0)
    assert (vowelCount('This is a test.  12345.') == 4)
    assert (vowelCount(string.ascii_lowercase) == 5)
    assert (vowelCount(string.ascii_lowercase * 100) == 500)
    assert (vowelCount(string.ascii_uppercase) == 5)
    assert (vowelCount(string.punctuation) == 0)
    assert (vowelCount(string.whitespace) == 0)
    print('Passed!')


def testInterleave():
    print("Testing interleave()...", end="")
    # ic(interleave("aaa", "bbbyyy"))
    assert (interleave("abcdefg", "abcdefg") == "aabbccddeeffgg")
    assert (interleave("abcde", "abcdefgh") == "aabbccddeefgh")
    assert (interleave("abcdefgh", "abcde") == "aabbccddeefgh")
    assert (interleave("Smlksgeneg n a!",
                       "a ie re gsadhm") == "Sam likes green eggs and ham!")
    assert (interleave("", "") == "")
    print("Passed!")


def test_caesar_cipher_digit():
    ic(caesar_cipher_digit("a", 2))
    ic(caesar_cipher_digit("z", 1))
    ic(caesar_cipher_digit("A", 2))
    ic(caesar_cipher_digit("Z", 1))


def testApplyCaesarCipher():
    print("Testing applyCaesarCipher()...", end="")
    # test_caesar_cipher_digit()
    # ic(applyCaesarCipher("abc 123 ABC", 1))
    assert (applyCaesarCipher("abcdefghijklmnopqrstuvwxyz",
                              3) == "defghijklmnopqrstuvwxyzabc")
    assert (applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
    # assert (applyCaesarCipher("1234", 6) == "1234")
    assert (applyCaesarCipher("12 34", 6) == "78 90")
    assert (applyCaesarCipher("abcdefghijklmnopqrstuvwxyz",
                              25) == "zabcdefghijklmnopqrstuvwxy")
    assert (applyCaesarCipher("We Attack At Dawn", 2) == "Yg Cvvcem Cv Fcyp")
    assert (applyCaesarCipher("We Attack At Dawn", 4) == "Ai Exxego Ex Hear")
    assert (applyCaesarCipher("We Attack At Dawn", -1) == "Vd Zsszbj Zs Czvm")
    # And now, the whole point...
    assert (applyCaesarCipher(applyCaesarCipher('This is Great', 25),
                              -25) == 'This is Great')
    print("Passed.")


def testAreAnagrams():
    print("Testing areAnagrams()...", end="")
    # ic(areAnagrams("aaAAyyYY", "aayBBBaa"))
    assert (areAnagrams("", "") == True)
    assert (areAnagrams("", "a") == False)  # self
    assert (areAnagrams("abCdabCd", "abcdabcd") == True)
    assert (areAnagrams("abcdaBcD", "AAbbcddc") == True)
    assert (areAnagrams("abcdaabcd", "aabbcddcb") == False)
    print("Passed!")


def testSameChars():
    print("Testing sameChars()...", end="")
    # ic(sameChars("aabbcc", "abcbcyyzz"))
    assert (sameChars("abcabcabc", "cba") == True)
    assert (sameChars("abcabcabc", "cbad") == False)
    assert (sameChars("abcabcabc", "cBa") == False)
    assert (sameChars(42, "The other parameter is not a string") == False)
    assert (sameChars("", "") == True)
    print("Passed!")


def testHasBalancedParentheses():
    print("Testing hasBalancedParentheses()...", end="")
    # ic(hasBalancedParentheses("()aa)("))
    assert (hasBalancedParentheses("()") == True)
    assert (hasBalancedParentheses("") == True)
    assert (hasBalancedParentheses("())") == False)
    assert (hasBalancedParentheses("()(") == False)
    assert (hasBalancedParentheses(")(") == False)
    assert (hasBalancedParentheses("(()())") == True)
    assert (hasBalancedParentheses("((()())(()(()())))") == True)
    assert (hasBalancedParentheses("((()())(()((()())))") == False)
    assert (hasBalancedParentheses("((()())(((()())))") == False)
    print("Passed!")


def test_order_bubble():
    ic(order_bubble('654321'))
    ic(order_bubble('123645'))
    ic(order_bubble('cba'))


def testLeastFrequentLetters():
    print("Testing leastFrequentLetters()...", end="")
    # test_order_bubble()
    # ic(leastFrequentLetters("bac ABC Cxy'xy!!!"))
    assert (leastFrequentLetters("abc def! GFE'cag!!!") == "bd")
    assert (leastFrequentLetters("abc def! GFE'cag!!!".lower()) == "bd")
    assert (leastFrequentLetters("abc def! GFE'cag!!!".upper()) == "bd")
    assert (leastFrequentLetters("") == "")
    assert (leastFrequentLetters(string.punctuation) == "")
    assert (leastFrequentLetters(string.whitespace) == "")
    assert (leastFrequentLetters(
        string.ascii_lowercase) == string.ascii_lowercase)
    assert (leastFrequentLetters(
        string.ascii_uppercase) == string.ascii_lowercase)
    noq = string.ascii_lowercase.replace('q', '')
    nor = string.ascii_lowercase.replace('r', '')
    nos = string.ascii_lowercase.replace('s', '')
    assert (leastFrequentLetters(string.ascii_lowercase + noq) == "q")
    assert (leastFrequentLetters(nor + string.ascii_lowercase) == "r")
    assert (leastFrequentLetters(nos + nor + " aaa " +
                                 5 * string.ascii_lowercase) == "rs")
    print("Passed!")


def test_is_included():
    ic(is_included('abc', 'a'))


def testLongestCommonSubstring():
    # test_is_included()
    print("Testing longestCommonSubstring()...", end="")
    # ic(longestCommonSubstring("abcdef", "ghi"))
    # ic(longestCommonSubstring("abcbcy", "abc"))  # abc
    # ic(longestCommonSubstring("abxAB", "abyAB"))  # ab, AB
    # ic(longestCommonSubstring("00yy111", "00yy-yy111"))  #
    assert (longestCommonSubstring("abcdef", "abqrcdest") == "cde")
    assert (longestCommonSubstring("abcdef", "ghi") == "")
    assert (longestCommonSubstring("", "abqrcdest") == "")
    assert (longestCommonSubstring("abcdef", "") == "")
    assert (longestCommonSubstring("abcABC", "zzabZZAB") == "AB")
    print("Passed!")


def test_is_palindro():
    ic(is_palindro('a'))
    ic(is_palindro('aba'))
    ic(is_palindro('abca'))
    ic(is_palindro('abccba'))


def testLongestSubpalindrome():
    print("Testing longestSubpalindrome()...", end="")
    # test_is_palindro()
    # ic(longestSubpalindrome("abcbcy"))
    assert (longestSubpalindrome("ab-4-be!!!") == "b-4-b")
    assert (longestSubpalindrome("abcbce") == "cbc")
    assert (longestSubpalindrome("aba") == "aba")
    assert (longestSubpalindrome("a") == "a")
    print("Passed!")


def testReplace():
    print('Testing replace()...', end='')
    # ic(replace('abcd', 'bc', 'x'))
    # ic(replace('abcd', 'x', 'y'))
    # ic(replace('abc abc', 'b', 'y'))
    # ic(replace('abc abc', 'ab', 'abd'))
    assert (replace('abc', 'd', 'e') == 'abc'.replace('d', 'e'))
    assert (replace('abc', 'b', 'e') == 'abc'.replace('b', 'e'))
    assert (replace('abcb abc', 'b', 'e') == 'abcb abc'.replace('b', 'e'))
    assert (replace('abcb abc', 'ab',
                    'abd') == 'abcb abc'.replace('ab', 'abd'))
    print('Passed!')


def testCollapseWhitespace():
    print("Testing collapseWhitespace()...", end="")
    # ic(collapseWhitespace(" A B "))
    # ic(collapseWhitespace(" A  \n\n  \t\t\t z  \t\t "))  # " A z "

    assert (collapseWhitespace("a\nb") == "a b")
    assert (collapseWhitespace("a\n   \t    b") == "a b")
    assert (collapseWhitespace("a\n   \t    b  \n\n  \t\t\t c   ") == "a b c ")
    assert (collapseWhitespace("abc") == "abc")
    assert (collapseWhitespace("   \n\n  \t\t\t  ") == " ")
    assert (collapseWhitespace(" A  \n\n  \t\t\t z  \t\t ") == " A z ")
    print("Passed!")


def testWordWrap():
    print('Testing wordWrap()...', end='')
    # ic(wordWrap("abc", 3))
    # ic(wordWrap(" a c yz", 3))
    # ic(wordWrap("abcdefghij", 4))
    # ic(wordWrap("a b c de f ", 4))

    assert (wordWrap("abc", 3) == "abc")
    assert (wordWrap("abc", 2) == "ab\nc")
    assert (wordWrap("abcdefghij", 4) == """\
abcd
efgh
ij""")
    assert (wordWrap("a b c de fg", 4) == """\
a-b
c-de
fg""")
    print('Passed!')


#################################################
# testAll and main
#################################################


def testAll():
    # comment out the tests you do not wish to run!
    testVowelCount()
    testInterleave()
    testApplyCaesarCipher()
    testAreAnagrams()
    testSameChars()
    testHasBalancedParentheses()
    testLeastFrequentLetters()
    testLongestCommonSubstring()
    testLongestSubpalindrome()
    testReplace()
    testCollapseWhitespace()
    testWordWrap()


def main():
    cs112_s21_week3_linter.lint()
    testAll()


if __name__ == '__main__':
    main()
