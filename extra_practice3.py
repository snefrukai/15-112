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
    vowel = 'aeiouAEIOU'
    count = 0
    for i in range(len(s)):
        if s[i] in vowel:
            count += 1
    return count


def interleave(s1, s2):
    s_new = ''
    len_min = min(len(s1), len(s2))

    for i in range(len_min):
        s_new += s1[i] + s2[i]

    if len_min < len(s1):
        s_new += s1[len_min:]
    elif len_min < len(s2):
        s_new += s2[len_min:]
    return s_new


def caesar_cipher_digit(s, shift):
    foo = string.digits + string.ascii_letters
    i = foo.find(s)
    # abs postison = relative postion + distance
    if s.isdigit(): i = (i + shift) % 10
    elif s.islower(): i = (i - 10 + shift) % 26 + 10
    elif s.isupper(): i = (i - 10 + shift) % 26 + 10 + 26
    s = foo[i]
    return s


def applyCaesarCipher(message, shift):
    message_new = ''
    for i in range(len(message)):
        s = message[i]
        if s != ' ': s = caesar_cipher_digit(s, shift)
        message_new += s

        # ic(i, message[:i], message[i:], s)
    return message_new


def anagrams_count(s):
    return 42


def areAnagrams(s1, s2):
    if len(s1) != len(s2): return False
    while s1 != '':
        l, u = s1[0].lower(), s1[0].upper()
        count1 = s1.count(l) + s1.count(u)
        count2 = s2.count(l) + s2.count(u)
        # ic(l, u, s1, count1, s2, count2)
        if count1 != count2: return False
        s1 = s1.replace(l, '')
        s1 = s1.replace(u, '')
    return True


def sameChars(s1, s2):
    if type(s1) != str or type(s2) != str: return False
    if s1 == '' and s2 == '': return True

    while s1 != '':
        foo = s1[0]
        find = s2.find(foo)
        s1 = s1.replace(foo, '')
        s2 = s2.replace(foo, '')
        # ic(s1, s2, foo, find)
    if s2 != '': return False
    return True


def hasBalancedParentheses(s):
    if s.find(")") < s.find("("): return False

    while s.count("(") != 0:
        if s.count(")") == 0: return False
        s = s.replace("(", '', 1)
        s = s.replace(")", '', 1)
    if s.count(")") != 0: return False
    return True


def order_bubble(s):
    foo = string.ascii_letters + string.digits
    for i in range(len(s) - 1):
        s_old = s
        for i in range(len(s) - 1):
            if foo.find(s[i]) > foo.find(s[i + 1]):
                s = s[:i] + (s[i + 1] + s[i]) + s[i + 2:]
        if s == s_old: return s
    return s


def leastFrequentLetters(s):
    if s == '': return ''
    result = ''
    count_min, k = 0, 0
    while s != '':
        if s[0].isalpha():
            s_lower = s[0].lower()
            s_upper = s[0].upper()
            count_new = s.count(s_lower) + s.count(s_upper)
            if k == 0 or count_new < count_min:
                count_min = count_new
                result = s_lower
            elif count_new == count_min:
                result += s_lower
            k = 1
            s = s.replace(s_lower, '')
            s = s.replace(s_upper, '')
        else:
            s = s.replace(s[0], '')
    result = order_bubble(result)
    return result


def is_included(s, check):
    if s.find(check) == -1: return False
    elif s.find(check) >= 0: return True


def longestCommonSubstring(s1, s2):
    if s1 == '' or s2 == '': return ''
    i = 0
    result, s_temp, result_new = '', '', ''

    for i in range(len(s1)):
        if is_included(s2, s1[i]):
            result_new = s1[i]
        # last char, or no further match
        while i < len(s1) - 1 and is_included(s2, result_new + s1[i + 1]):
            result_new += s1[i + 1]
            i += 1
            # ic(i, len(s1), result_new)
        if len(result_new) > len(result) or (len(result_new) == len(result)
                                             and result_new < result):
            result = result_new
        # ic(i, result_new)
    return result


def is_palindro(s):
    for i in range(int(len(s) / 2)):
        if s[i] != s[-1 - i]: return False
    return True


def longestSubpalindrome(s):
    result, s_temp, result_new = '', '', ''

    for i in range(len(s)):
        result_new = s[i:]
        while result_new != '' and not is_palindro(result_new):
            result_new = result_new[:-1]
        if len(result_new) > len(result) or (len(result_new) == len(result)
                                             and result_new > result):
            result = result_new
        # ic(i, result_new)
    return result


def replace(s, c_old, c_new):
    if s.find(c_old) == -1: return s
    s_new = ''
    dist = len(c_old)
    count = s.count(c_old)

    for i in range(count):
        posn = s.find(c_old)
        s_new += s[:posn] + c_new
        # ic(count, s, posn, s_new)
        s = s[posn + dist:]
    s = s_new + s
    return s


def collapseWhitespace(s):
    char_prev_space = False
    s_new = ''

    for c in s:
        if not c.isspace():
            s_new += c
            char_prev_space = False
        elif c.isspace() and not char_prev_space:  # prev is char
            s_new += ' '
            char_prev_space = True
        # ic(c, char_prev_space, s_new)

    # s = replace(s, '\n', ' ')
    # s = replace(s, '\t', ' ')
    # while s.find('  ') != -1:
    #     s = replace(s, '  ', ' ')
    return s_new


def wordWrap(text, width):
    return 42


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
    # testWordWrap()


def main():
    cs112_s21_week3_linter.lint()
    testAll()


if __name__ == '__main__':
    main()