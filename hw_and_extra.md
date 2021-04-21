# homework and extra practice

info

- hw: homework
- ep: extra practice
  - optional
  - help you prepare for the upcoming quizzes, midterms, and final exam
- ct: code tracing
  - What will each of these print?
- roc: reasoning over code
  - Find values for the parameters so the functons return True

## hw1

### colorBlender(rgb1, rgb2, midpoints, nth)

def

- takes
  - a non-negative integer number of midpoints
  - a non-negative integer n
- returns the nth color in the palette
  - that creates with midpoints
  - None If n is out of range (too small or too large)
  - represent these RGB values as a single integer
    - first 3 digits
    - 220-020-060
      - color0: rgb(220, 20, 60)
    - RGB values must be ints, not floats
- use roundHalfUp(n) instead of round(n)

## [ep1](https://www.cs.cmu.edu/~112/notes/ep1.html)

- Previous Quizzes
  - splitPower(x,n) # S20
    - int
      - n > 0
    - removes the n rightmost digits of x
      - leaving 0 or more leftmost digits
      - (-902,2)
      - -9
    - returns
      - leftmost digits raised to the power of the rightmost digits
      - (-9)\*\*2
  - largestPerfectSquare
    - non-negative int n
    - returns the largest perfect square
      - that is no larger than n
- dist
  - ez
- dist
  - ez
- range n bool
  - ez
- rem or divination
  - ez
- rem n bool
- rem n bool
  - ez
- max n bool
- max n bool
- rem
  - ez
- bool
  - ez

### golden ratio + bool

- [Binet = (Phi**n-(-Phi)**-n)/math.sqrt(5)](https://mathworld.wolfram.com/BinetsFibonacciNumberFormula.html)
- Phi = (1+math.sqrt(5))/2
- x = (1+√(1+4))/2
  - a = 1, b = -1, c = -1
  - ax² + bx + c = 0
  - [B² – B – 1 = 0](https://www.goldennumber.net/math/)
-
- ![See the source image](https://th.bing.com/th/id/Re37cd0d244c412549f0c1fb46153c3bf?rik=f29JBR2Mt5IweQ&pid=ImgRaw)
- rem n bool
- nearestOdd
  - even down
    - 12-1
  - 11.9, 12.1
    - floor%2
    - ceil%2

### getKthDigit

- move loop to 10\*\*kth
- loop kth times
  - rem = n%10
  - n //= 10

### bool

### rev

- 0321

  - getKthDigit 不用 index 怎么做？！
    - 全部罗列？

### [ep1-ct-and-roc](https://www.cs.cmu.edu/~112/notes/ep1-ct-and-roc.html)

### rev

- 跟做简单数学一样，更多的是细致的

### 1

- x = 6 ; return 6
- f(g(f(5))) + 5
- -
- x = 4 ; return 6
- x = 0 ; return f(3)
- f(g(6)) + 5
- -
- x = 7 ; return 9
- f(6) + 5
- -
- return 14
- ans
  - f5
  - g6
  - f6
- rev
  - white space in print('g', x)

### 2

- ans
  - 3
    - 2+4-3
  - 2.6
    - 1.6+11//10
    - 2+
  - ~~5~~ 6
    - ~~2~~ 3
    - 2.6, 3
- 3
  - C
  - D
    - a = 1%10 = 1
    - b = 2%10 = 2
    - a-b < 2
- 1
  - cond
    - x, y != 0
  - list
    - **6, 4**
    - 7, 3
    - 8, 2
    - 9, 1
  - print(rc1(6,4))
- 2
  - cond
    - int
    - sqrt is int
      - int(round(x\*\*0.5)) == sqrt(x)
    - range
      - x//10 > 2 -> x > 20
      - max(x%10) <=9 -> x <= 119
      - (x//10 == x%10 + 2))
  - list
    - 25, 7
    - 36, 8
    - 49,11
    - **64,6**
    - 81,3
    - 100, 2
- 3
  - cond
    - int in 0, 100
    - (y+9) % 10 == y//10
  - list x%10 == (x-9)//10
    - 9, 99
    - 8, 98
    - 7, 87
    - 76, 65, 54, 43, 32, 21, 10
  - list (y+9) % 10 == y//10
    - ~~9, 90~~
    - 8, 89
    - 7, 78
    - ...67, 56,  45, 34, 23, 12
  - print(rc3(98, 89))
  - print(rc3(87, 78))
  - print(rc3(76, 67))
  - print(rc3(65, 56))
  - print(rc3(54, 45))
  - print(rc3(43, 34))
  - print(rc3(32, 23))
  - print(rc3(21, 12))

## [hw2](https://www.cs.cmu.edu/~112/notes/hw2.html)

### **question**s

- how to test different func in a string
  - for y in x[x1, x2, x3]

### longestDigitRun

- compare left digit
  - if n%10 == n//10 % 10
- compare each digit
  - count_new == count = 1
  - while n >= 10 # 2 digits
    - if compare_left_digit
      - count += 1
    - if not compare_left_digit  # compare
      - if count_new > count  # save max
      - if count_new == count  # get lower tie
- rev
  - 117773732
    - 777, (3, 7)
    - 11, (2, 1)
  - 连续次数 m，max(m)
  - not very robust?

### nthCircularPrime(n)

#### def

- the number generated at each intermediate step when cyclically permuting its digits will be prime
- e.g.
  - 1193 is a prime
  - 1931, 9311 and 3119 all are also prime
  - -> 1193 is a circular prime
- -> dont have digits in [0, 5, 2, 4, 6, 8]
  - 509 -> 950, 95
  - 429 -> 942, 294

#### step

1. check digit
   - if mode [0, 5, 2n] -> F
     - [2, 4, 6, 8] -> 2n
2. check prime
3. - if not prime -> F
4. check rotates
   - if not prime -> F
   - for i
     - abc -> bca, cab
     - i[max] = 2 = count - 1
     - i[min] = 1
   - delete right1 digit # 709 -> 970
     - cab = ab + c\*10\*\*2
     - 可以更快地把 0 推到个位
   - ~~delete left1 digit # 709, 097, 970~~
     - bca = (n - a*10\*\*2)*10 + a
     - leading 0 导致位数变化，无法到达 970（？
5. check cond
   - if TTT -> T

```python
# to check if n is circular prime
isPrime(n) # return if n is prime
count = digit_count(n) # count n's digits

if digits{n} % x{0, 5, 2n} == 0
  return False
if not isPrime(n)
  return False
for i in (1, count) # rotate count-1 times
    n = n//10 + n%10 * 10**(count-1)
    if not isPrime(n) # rorates are not prime
      return False
if all are True
  return True
```

```puml
start
- input nth

repeat
    repeat
        repeat
            repeat
              - n = n + 1
            repeatwhile (circular_p_digit) is (F)
        repeatwhile (isPrime) is (F)
    repeatwhile (circular_p_rotate(n)) is (F)
repeatwhile (nth circular prime) is (F)

- return n
stop
```

ref

- [geek](https://www.geeksforgeeks.org/check-whether-number-circular-prime-not/)
  - rotate 绕场一周，n_new == n
  - 如果已经判断过 prim，not: F 效率更高？

#### rev

- 3 个条件依次判断
  - 思路没问题
  - 卡在细节
- 卡点 1：return
  - 自己复杂化了，用了 bool 代表的二进制
    - if rotate < m: return False
    - False = 0, True = 1
    - all True = m = count
  - 用 not 做排除即可
    - FT - F
    - TT - T

### nthPalindromicPrime(n)

def

- abc...xyz

#### step

- input n # abc...xyz
- for i, check digits
  - `getKthDigit(n, k)`
    - `foo = n // 10**k % 10`
    - a -> k = count - 1 - i
    - z -> k = 0 + i
    - 算法是一样的
  - string
    - a = n[0]
    - b = n[1] -> i
    - y = n[-2] -> -1-i
    - z = n[-1] -> -1-i
  - i
    - 12321
      - i = 5/2 = 2.5
    - 1221
      - i = 4/2 = 2
    - i in [1, int(count/2)]
- `isPrime(n)`
- return n

```python
for i in (0, int(count/2))
  z = getKthDigit(n, i)
  a = getKthDigit(n, count-1-i)
```

#### rev

- check and remove digit
  - digit_equal_first_last(n) # abcd..z 12321
    - a = n//10//10....
    - z = n%10
    - if a == z
  - while n > 1 digit # TTT, TTF
    - n = digit_equal_first_last(n)
    - bcd = abcd - a\*10\*\*(count-1)
    - bc = bcd//10

### digitEqual

- rev
  - loop，取 nth 的新方法
    - loop time = %10 time, count

### carrylessAdd(x1, x2)

- 8+7
  - 5 (ignore the carry)
- 18+27
  - 35 (still ignore the carry)

#### algorithm

- 7285 + 76
- get the minimum counts of two digits
  - 2
- for i in count_min
  - add each digit, save the reminder
    - 5 + 6 -> 1
    - 8 + 7 -> 5
    - k(0, count)
  - add each reminder
    - 5\*10 + 1 = 51
    - `5*10**i + 1*10**i`
- add back to the left part of the larger number
  - 7200 + 51

```python
count_min = min(count(x1), count(x2))
for i in count_min
  rem = (x1%10 + x2%10) % 10
  x1 //= 10
  x2 //= 10
  n += rem * 10**i # adjust digits
```

### findZeroWithBisection

- x\*x-2=?
  - x\*x=2
- x\*\*2 - (x + 1)
- x**5 - 2**x
- test

### nthKaprekarNumber

def

- Kaprekar number is a positive integer

  - the representation of whose square
    - two possibly-different-length parts
    - right part is not zero
    - add up to the original number again
  - 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,...

- rev
  - mid break
    - 88209
      - 297
    - if one True: FT TF
      - 88+209
      - 882+09

### **play112**

- rev
  - 542123121
    - 2 1 1 2 -
    - 1x5
    - (4, 2)
  - val(posi, numb)
    - [1, 9], [1, 2]
  - v1
    - board
    - r1
      - chk offboard
      - chk occupied
      - chk numb
      - chk winner
        - 11288118
        - check player
    - r2
      - ...
      - chk finished

% \f is defined as #1f(#2) using the macro
\f\relax{x} = \int\_{-\infty}^\infty
\f\hat\xi\,e^{2 \pi i \xi x}
\,d\xi

You want to make sure the Markdown render will not touch your special characters

- e.g., $x_{i} + y_{i}$
- $y_{i}$
- should not be rendered as $x<em>{i} + y</em>{i}$ (i.e., a pair of underscores should not mean italics).

```

```

### carrylessMultiply (x,y)

def

- carrylessMultiply(643, 59)
  - returns 417
    - 005- = 643\*5
    - -467 = 643\*9
    - 417

step

- for i
  - i = 0
    - rightmost digit
    - \*10\*\*0
  - i = 1
    - rightmost 2nd digit
    - \*10\*\*1

### nearestKaprekarNumber(n)

def

- that takes an int or float value n
  - returns the Kaprekar number closest to n
    - ties going to smaller value
- check from n

### Integer Data Structures

def

- include multiple integers in a single integer
- [sign-digit] [count-count] [count] [number]
- to encode -1234512345
  - sign-digit is 2 (negative)
  - count is 10
  - so count-count is 2
  - entire encoding is 22101234512345

step

- lengthEncode(n)
  - takes a possibly-negative integer
  - intCat(n, m)
- lengthDecode(n)
- lengthDecodeLeftmostValue(n) # _highly reccomend completing this function BEFORE lengthDecode_
  - takes a number with one-or-possibly-more encoded values
  - return
    - leftmost decoded value, rest of the encoded values
  - 1112113789
    - 2 as 1112
    - 789 as 113789
    - return (2, 113789)
  - for i # in 4 part
    - 0, sigg
      - max of 1 digit
    - 1, count_count
      - max of 1 digit
      - in [1,9]
    - 2, count
      - max of 9 digits
      - abs < 999,999,999
    - 3, number
- Lists
  - [9, 8888]
    - len of 2
    - 2,9,888
    - 1112,1119,1148888
    - 111211191148888
  - []
    - len of 0
    - 0
    - 110

**not done**

- Finite State Machines (FSM's)

## [ep2](https://www.cs.cmu.edu/~112/notes/ep2.html)

- not use string indexing, lists, list indexing, or recursion in this unit

### digit_count

def

- loop
  - //

### gcd

def

- var

### nthLeftTruncatablePrime

def

- in a given base, contains no 0
- if the leading ("left") digit is successively removed
  - all resulting numbers are prime
- https://en.wikipedia.org/wiki/Truncatable_prime

step

- isTrunc
  - check digit no 0
    - n//10% != 0
  - check rem number is prime
- leftTruncatablePrime
  - isTrunc

### nthPowerfulNumber

def

- a positive integer m
- for every prime number p dividing m
  - `p**2` also divides m
- Equivalently, product of a square and a cube
  - m = `a**2 * b**3`
    - if a = b
      - m = `a**5`
    - if
      - m = p**2 \* p1**3
      - m = p1**2 \* p**3
    - if pow1 = even and > 2
      - m = `(a**(pow1/2))**2 * b**3`
    - if pow1 = odd and > 2
      - m = `(a**(pow1-3) * a**3) * b**3`
        - = `(a**x)**2 * (a*b)**3`
    - 同理可将 pow2 != 3 时归于 a\*2
    - 2 3 5 7
    - `a*a`
    - `b*b * b`
    - so `p**2` means at least a\*\*2
- **prime numbers are not powerful**
- list
  - 1
  - 4
    - 2**2 \* 1**3
      - 2,1
  - 8
    - 1**2 \* 2**3
      - **1,2**
  - 9
    - 3**2 \* 1**3
      - 3,1
    - ! 1**1 \* 3**3
  - 16
    - 4**2 \* 1**3
      - 4,1
    - ! 1**1 \* 3**3
  - 25
    - 5**2 \* 1**3
      - 5,1
  - 27
    - 1**2 \* 3**3
      - **1,3**
  - 32
    - 2**2 \* 2**3
    - 2, 2
  - 36

step

- [无脑：i 遍历 n](https://cutt.ly/Lx2L9Tx)
  - n%i == 0 and prime
    - n%i\*\*2 == 0
  - i 的次数 ≈n
  - 随着 n 的增大会计算许多不必要的 i
- [高手：一边 i 遍历一边 divide n](https://www.geeksforgeeks.org/powerful-number/)
  - for every prime factor, find the highest power of it that divides n
    - If highest dividing power of all prime factors are more than 1
  - 这时需要计算的 factor 也变小了
    - 再用新的 range `(3, nNew**0.5+1, 2)`算一遍
  - 先把一个除干净了，剩下的就是另一个了
  - check prime
- step 差别
  - f(25), 88-22 steps
  - 自己更新后的做法
    - f(243), 39-51 step
      - 超过了 geek 上的
      - 虽然大的逻辑是一样，只是在 factor 的处理上优化了

### nthWithProperty309(n)

def

- its 5th power contains every digit (from 0 to 9) at least once
- `309**5 = 2817036000549`
- too cheaty to use 'char in str'

step

- for i in range (10)
  - count i in n
  - if count == 0: F

### integral(f, a, b, N)

def

- takes
  - a Python function f
    - (that itself takes one value x, a float, and returns a float),
  - two floats a and b
    - where a<=b
  - a positive int N
- return the approximate area under the curve of f(x)
  - uses the trapezoidal rule with N trapezoids to
  - where a <= x <= b
- 微积分的面积
  - 多个小梯形 trapezoid 的面积和
  - 梯形面积
    - `(b-a) * (f(a)+f(b))/2`
    - `width*(h1+h2)/2`
      - width times the average height

step

- loop N
  - from a to b
    - cal step of N
    - 复杂点：怎样将 f(a)和 f(b)纳入范围
  - get area
    - width = (b-a)/N
    - h1 = f(i)
    - h2 = f(i+1)
  - sum area

### longestIncreasingRun(n)

def

- takes in a positive int value n and
- returns the _longest increasing run_ of digits
  - tie in run length, return larger
- 123345
  - 345
- 27648923679 # 27-6-489-23679
  - 23679

### nthSmithNumber

def

- a composite
  - (non-prime)
  - sum of whose digits
    - == sum of the digits of its **prime factors** (excluding 1)
  - if a prime number divides the Smith number multiple times
    - its digit sum is counted that many times
- 4
  - the prime factor 2 is counted twice
  - 4 = (2\*2)
- 22
  - 2, 11
  - 2 + 2 = 2 + (1+1)
- 58
  - 2, 29
  - 5 + 8 = 2 + (2+9)

step

- get prime factor
  - get digit sum
- get digit sum
- check

### Counting Primes

def

- between the sum of the reciprocals of the integers (1/1 + 1/2 + ...) and the number of prime numbers.
  - there is some kind of very deep relationship
  - This has been explored in great detail by many mathematicians over the past few hundred years,
  - with some of the most important results in modern mathematics relating to it

### [12F](https://www.kosbie.net/cmu/fall-12/15-112/handouts/notes-practice-thru-week3.html)

- digit_count

## [hw3](https://www.cs.cmu.edu/~112/notes/hw3.html)

- Do not use lists, list indexing, or recursion this week.

### rev

- count_match_exact 的 replace 比较有意思
- min, 1234567890
  - len of 10
  - \*\*0.2 = 65.8

### 1. largestNumber(s)

#### def

- n >= 0
- consecutive digits
- int(max)
  - "I saw 3 dogs, 17 cats, and 14 cows!"
  - 17
- None
  - "One person ate two hot dogs!"

#### step

- get digits
  - str stack
    - 1
    - 17
    - 170
  - n = int(n)
- save n[max]
  - bubbling

```python
# "I saw 3 dogs, 1700 cats, and 14 cows!"
for i in len(s)
  if s[i] is digit
    n_new += s[i]
    n = max(int(n_new), n)
  else # if digits end
    clear n_new
if n == 0: return None
return n
```

```puml
start
- digit
  repeat
      repeat
      - stack str
      - save n[max]
      repeatwhile (is digit) is (F)
    - next char
  repeatwhile (last char) is (F)

stop
```

#### rev

- **冒泡和判断大小在之前哪里用过**？
- 注意 clear n_new 的步骤位置
- 注意 save max 的步骤位置
  - bubble 要先存了才能继续
  - 同样是一个操作，判断出赋值更好吗？
    - 最少减少了 print
- 用 i+1 判断，step 只相差 2
- psuedo 已经几乎等于最后的代码了

### 2. rotateStringLeft(s, n)

#### def

- no loop
- list
  - 1, bcde + a
    - s[n] at the end
  - 2, cde + ab
  - 5, abcde
  - -1, e + abcd
    - s[n] at the start
  - -25, abcde

#### step

- mode n # abcde, 5
  - by len(s)
- get 1st 2nd part
  - 3, de + abc
    - s[3:] + s[:3]
  - -2, de + abc
    - s[-2:] + s[:-2]
- adjust sequence
  - s[n:] + s[:n]

```python
n = n % len(s)
if n == 0
  return s
return s[n:] + s[:n]
```

#### rev

- psuedo 已经几乎等于最后的代码了

### 3. isRotation(s, t)

#### def

- assert (isRotation('abcd', 'abcd') == False)
- assert (isRotation('abcd', 'bcd') == False)
- assert (isRotation('abcd', 'cdab') == True)
  assert (isRotation('abcd', 'bcda') == True)

#### step

- check equal
  - if euqal -> F
- check length
  - if not euqal -> F
- check rotate
  - if rotate(s) == t -> T
  - for i
    - i[1, len(s)-1]
    - `rotateStringLeft(s, n)`

```python

```

### 4. topScorer(data)

#### def

- multi-line string
- comma-separated values
  - name, score[1], score[2], ..., score[n]
- tie
  - return name with ","

#### step

- `score_total_get`
  - split
    - a 10 10 10
    - b 20 20 20
  - save name
  - add and save score
  - return name, score_total_get
    - a 30
    - b 60
- split lines
- compare total score
  - for i
    - `score_total_get(line[i])`
    - if score_total_get[i] > max
      - winner = name
    - if score_total_get[i] = max
      - winner += name
- return winner

### 5. mastermindScore

#### def

- 'abcd', 'aabd'
  - 'a' 'd', 2 exact match
  - 'b', 1 partial match

#### step

- str_del_kth
  - s = aaa-i-bbb
  - s = s[:i-1] + s[i+1:]
- `count_match_exact(s, s1)` # abab, afaf
  - if all match
    - s = s1
    - count == len(s)
    - s = ""
  - loop and replace when match
    - for i
      - i = 4 ?
      - replace 需精确到个位
      - i 会因为 replace 导致 out range
    - while i
      - i = 0
      - k = len-1 = 3
      - i[0] # afcd, abcd
        - k -= 1 # 3
        - count += 1
      - i[0] # fcd, bcd
        - i += 1
      - i[1] # fcd, bcd
        - k -= 1 # 2
        - count += 1
      - i[1] # fd, bd
      - i = 2 = k, stop
    - _cant use replace at 1st_
  - ~~loop andreplace after match~~
    - for i in len
      - if s[i] == s1[i]
        - save i to match
        - [1, 9, 11]
        - "1911"
        - 但里要存成 list
    - for val in mactch
      - use helper to delete
        - 不能直接用用 replace
  - result fromcount
    - no match
    - multi match
- `count_match_partial(s, s1)` # bc, ab
  - loop str
    - for i
      - i[0, len(s)]
      - 0 aaffzx, yyazb - a, 1
      - 1 aaffzx, yyzb - 1
      - 4 aaffzx, yyzb - z, 2
      - 5 aaffzx, yyb - x, 2
    - should only count once
      - if match: break?
    - _could use replace at 1st_
  - calculate result groups
    - win
    - no
    - one or multi
    - single or dual

#### rev

### 6. topLevelFunctionNames(code)

#### def

- multi-line string of Python code
- string with the names of the top-level functions

### 7. drawFlagOfQatar(canvas, x0, y0, x1, y1)

def

- border
  - 1px, black
- name
  - 'Qatar', center
- color
  - #FFFFFF, #B31722

step

- 1/3 white
- 2/3 red
- repeat white triangles \*9
  - for i
    - y = y + (y1-y0)/9

### 8. playPoker(deck, players)

#### def

- 'AS-2D-3S-4C-5H-6D-7S-8D', 4
- players take turns to get cards
  - start from player[1]
- max 2 cards
- order of score
  - straight flush
  - flush
  - straight
  - pair
  - high card
- tie
  - flush
    - highest card in hand
    - 8D-5D, 6H-9H
    - 9H > 8D
  - ties in individual cards
    - by rank
    - then by suit
    - 7C-2D, 7H-5S
    - 7H > 7C
- meta
  - sub
    - get h
- no "actual tie" cuz card is unique of 1

#### step

- check length
  - min =
    - player, group, len
    - 1, 2, 5
    - 2, 4, 11
- get score of hand1 # _'AS-2D-3S-4C-5H-6D-7S-8D'_
  - get hand
    - for
      - 'AS-2D-3S-4C-5H-6D-7S-8D', 1
        - 01-34
      - 'AS-2D-3S-4C-5H-6D-7S-8D', 2
        - 01-67 # 1 grp
        - 34-910
      - 'AS-2D-3S-4C-5H-6D-7S-8D', 3
        - 01-910 # 2 grp
        - 34-1213
        - 67-1516
      - i = i\*3
      - step = 3\*player
        - len(grp) of 'ab-' = 3
    - **hand**
      - ('AS-5H')
        - ('AS-2D-3S-4C-5H-6D-7S-8D', 1, 4)
  - change to index # - _'A23456789TJQK', 'CDHS'_
    - **index in number**
      - (0, 3)
      - (4, 2)
        - 'AS-5H'
  - get category and result
    - category
      - 5 straight and flush
      - 4 flush
      - 3 straight
      - 2 pair
      - 1 high card
      - split then compare each card
        - 'AH', '5H'
      - compare each card in a string that rep hand
        - 'AS-5H'
      - **category, highest**
        - (1, '5H')
          - 'AS-5H'
          - '2C-3C' # s flush
          - '2D-6D' # flush
          - 'QD-KC' # straight
          - '2D-2H' # pair
          - '2C-2S'
          - '2D-5H' # high card
    - score
      - category \* 1000 + rank \* 10 + suit
      - max = 5123 # flush KS
        - min = 1000 # high card AC
      - **score, highest**
        - (1042, '5H')
        - 'AS-5H'
          - 1000*1 + 10*4 + 2
  - evaluate hand[n]'s score and result str
    - **score, highest**
      - (1042, 'a high card of 5H')
      - 'AS-5H'
- get score of next hand and compare
  - if max
    - save player ID
      - 'player 1'
    - save result str
      - 'a high card of 5H'

#### rev

- 用赋值 score 判断结果的确比 if 嵌套更清晰
  - if meta1
    - check sub
  - elif meta2
- to improve
  - 如果 card 的数量不确定
    - 如何比较和求出 card 的种类
    - 如何求出 card_highest
    - v1
      - split，根据 rank 排序
        - 'AS-2D-2S-4C-5D'
          - '5D-2D-AS-2S-4C'
      - if flush
        - 'AS-2S'
        - '2D-5D'
        - if straight
          - 'AS-2S'
        - if not straight
          - get highest
            - '5D'
            - 'AS-4S'
            - '2D-5D'
      - elif straight
        - get highest
          - '3C'
            - 'AS-2H'
            - '2D-3C'

### 9. encodeRightLeftRouteCipher(s, n)

def

- 3WEATTACKATDAWN, 3 # 3-WTCTW-NDKTE-AAAAz
  - W T C T W
  - E T K D N
  - A A A A z

#### step

- get col
  - col = round up len(s)/rows # 5
    - 14/3 = 4.6
- fill missing grid
  - get difference
    - 15%3, 0
    - 16%3, 1
      - fill = 3-1
    - 17%3, 2
      - fill = 3-2
    - 18%3, 0
  - fill from ascii_lowercase
- get code parts by rows
  - row1 = _WTCTW_ # WEA-TTA-CKA-TDA-WNz
    - col1[0] + col2[0] +...+ col[nth][0]
    - s[0] + s[3] + s[6] + s[9] + s[12]
    - s[0*3] + s[1*3] +...+ s[4*3]
  - [nth]
  - for i in col
    - step = 1
- attach code parts
  - row2 = s[0+1] + s[1*3+1] +...+ s[4*3+1]
  - row[nth] = s[i[0]*rows+k] +...+ s[i[nth]*rows+k]
  - [nth] = rows
  - for k
    - rotate if k is odd
      - row2 ETKDN -> _NDKTE_
- format
  - str(rows) + ...

decode

- 3WTCTWNDKTEAAAAz

#### step

- get rows, col, new cipher
  - delete 1st digit
- rotate even part # WTCTW-NDKTE-AAAAz
  - get 1st part
  - get 2nd part
    - rotate
    - attach to 1st part
  - get [nth] part
  - [nth] = col
  - for i
    - part = cipher[i*col : (i+1)*col]
    - step 5 的等差数列
- get decode
  - for k in col
    - for i in rows
      - i\*col + k
  - k = 0
    - s[0] = s[0]
    - s[1] = s[5]
    - s[2] = s[10]
  - k = 1
    - s[3] = s[1]
    - s[4] = s[6]
    - s[5] = s[11]
- delete fill

#### rev

- 起初没看 hint 直接上的
- course 上的解法推了半天，发现和自己的逻辑是一样的
  - 课程的解法是罗列 row 和 col 组合，然后找表达式
  - 自己的解法是把每 row 的表达式带入到整体
    - 没意识到已经把 text 的 index 表达出来了
- ~~split s by col # WEA, TTA, CKA, TDA, WNz~~
  - 因为不能用 list，最后出来的还是 str
  - for i in [1, col]
  - col1 = s[0:3]
  - col2 = s[3:6]
  - col[i]
- reduce parameter(step)

### 10. patternedMessage

def

- white space
  - skip msg
  - persevere pattern

step

- remove white space in msg
- get each character in pattern
  - if white_space_check: skip
  - if not white_space_check
    - mode [i]
    - replace with message[i]
      - 123
      - 0 1 2
      - 3 4 5
        - 0+3, 1+3, 2+3
      - 6 7 8
        - 0+3*2, 1+3*2, 2+3\*2
      - 0+len*n, 1+len*n, 2+len\*n
      - mode
    - i += 1
  - check next
- remove trailing lines in pattern

## [ep3](https://www.cs.cmu.edu/~112/notes/ep3.html)

### 1. vowelCount(s)

def

- str
- 'aeiouAEIOU'

step

- check each digit
  - for i - if s[i] in vowel - count += 1
    rev
- 这也太简单了吧

### 2. interleave(s1, s2)

def

- ('pto', 'yhn')
  - "python"
- ('a#', 'cD!f2')
  - "ac#D!f2"

step

- get min len
- for i
  - get each digit
  - add each digit
- add rest str

### 3. applyCaesarCipher(message, shift)

def

- shift in step
  - between -25 and 25
- skip non-letter
- ascii_lowercase
  - 'abcdefghijklmnopqrstuvwxyz'
  - 25
- ascii_uppercase
  - 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

step

- get each char
- check index
  - check case
- get new index
  - add step
  - deal with extreme
    - mode
- get new char

### 4. areAnagrams(s1, s2)

def

- "Aba" and "BAA" are anagrams
- may not use sort() or sorted() or any other list-based

step

- get digit
- count as lower or upper
  - replace
- change to upper or lower, count
  - replace
- get next digit

### 5. areAnagrams

def

- case sensi
- ("abcabcabc", "cba") == True

step

- get s1[0]
- check with s2
  - if find
- replace to ''
- repeat
- check if all are ''

### 6. hasBalancedParentheses(s)

def

- ignoring all non-parentheses
- right match left
- no left parentheses are left unclosed

step

- check order
  - `)(`
  - right before left
- get 1st left parentheses
  - check if light exsist
- replace 1st left and right
- repeat until no left
  - if right: F

### 7. leastFrequentLetters(s)

def

- case insensi
- return str of lowercase
  - in alpha order

step

- get 1st digit
  - if alpha
    - if count == min
      - add to result
    - replace
  - if not alpha
    - replace
- repeat until s is''
- order result
  - bubble
    - for i in len
      - if s[i] ? s[i+1]
        - 4332
        - 34-32
    - 4321
      - 34-21
      - 324-1
      - 3214
    - 23-14
      - 213-4
      - 2134
    - 12-34
      - 123-4
      - 1234

### 8. longestCommonSubstring(s1, s2)

def

- longest string that occurs in both strings
- list
  - abcyy, abc
    - a, a
    - ab, ab
    - abc, abc
    - abcy, none
-

step

- start from s1[0]
  - while temp is inclu in s2 # get new str
    - += s1[0+1]
    - break
      - if last char
      - if += next not inclu
    - repeat
  - save result
- start from s1[1]
- repeat

rev

- 重新检验被互相包含的
  - 00y[y]y111
    - 00yy111
  - 00[yy]111
    - 00yy-yy111
  - i 需重置到 i+1 ？
  - 既然要逐个检查，那就还是用 for 好了
- while
  - break 的一些条件可以放到 while 那儿去

### 9. longestSubpalindrome(s)

def

- consecutive char
- case insensi
- cant skip char in case of multual include
  - ab[c]bce
  - bcb, cbc
- helper palindro
  - for i
    - abc, 1
    - abcd, 2

step

- start from s[0] # 0123
  - while temp is not palindro # get new str
    - abc...xyz
    - abc...xy
  - save result
- start from s[1] # 123
  - remove left chars
  - compare results
    - len
    - lexi
- repeat

### 10. replace(s,c_old, c_new)

def

- no .replace
- hypo
  - abc...mn...xyz
    - find
  - abc... + mn + ...xyz
    - contact
- cant use while
  - need to ignore the newly added chars

step

- if cant find c_old: return s
- get 1st part that has c_old
  - form s_new
  - s_new = abc + mn
    - abcyy
  - del s after c_old
- get 2nd part that has c_old
  - form s_new
    - s_new += efg + mn
- repeat
  - for i in count
- add whats left in s

### 11. collapseWhitespace(s)

def

- multi space into one

step

- change format with 10.
  - to ' '
  - \n
  - \t
- change white space
  - ' ' to ' '
    - 2 to 1
  - repeat
    - until cant find

### 12. wordWrap(s, n)

def

step

- form lines
  - add \n by n
    - "ababab", 2
      - ab
- remove trailing white
  - 'a b c de f '
    - 'a b '
    - 'c de'
    - ' f '
  - loop line
  - loop c
    - len = 5\*3 = 14
    - i
      - 0, 3
      - 5, 8
      - 10, ~~12~~
- replace white
  - '-'

### [ep3-ct-and-roc](https://www.cs.cmu.edu/~112/notes/ep3-ct-and-roc.html)

### Code Tracing (CT)

#### 1

step

- print(ct1("net", "two"))
  - for c in 'net' # n e t
    - if (c.upper() not in "NO!!!"): # N E T
      - i = 'two'.find(c)
        - e, -1
        - t, 0
      - if (result != ""): result += ":"
      - result += "%d%s%s%s" % (i, c, s[i], t[i])
        - += "%d%s%s%s" % (-1, 'e', 'net'[-1], 'two'[-1])
        - += "%d%s%s%s" % (0, 't', 'net'[0], 'two'[0])

print
-'-1eto:0tnt'

#### 2

step
print

### Reasoning Over Code (ROC)

Find values for the parameters so the functons return True:

#### 1 rc1(nn)

def

- n is int
- s is str of n
- 2000 > n > 1000

step

- `n == int( s[0] * len(s) )`
  - len(s) = 4 # repeat 4 time
  - s[0] = 1
- 1111

## [hw4](https://www.cs.cmu.edu/~112/notes/hw4.html)

def

- not use lists, list indexing, or recursion
- one feature at a time
  - draw the title
  - choose a random word and draw the underlines in place of the letters of the word
  - actually draw the word instead of the underscores when the user presses the mouse (and hide it again if they press the mouse again)
- **structure**
  - title
    - 'Word Guessing Game'
    - cap first letter
  - target world
    - len = 7
    - shown as alpha or underscore
  - list of alpha
    - A to Z
    - upper
    - 2 lines, 13 char each
  - info
    - guess count
      - start 0
      - count same key pressed
    - time count
      - count each sec
    - feedback copy
  - p.s.
    - 4 areas have equal height
    - responsive

step

- 1 title
  - resize
- 2 dispaly
  - distance box
    - start from left
    - or start from mid
  - underline
    - len of word
    - 20px of each char
    - for i in len=4
      - draw 4 times
      - full width = 20px \* 4 = 80px
      - starting from - 40px
      - step is i\*20px
- 3 choices
  - trigger and reaction
    - 1 string
      - add space better chars
      - if hit
        - replace s[i] with char
    - 2 strings
      - 1 is random word
        - CERTAIN
      - 1 is guess w \_
        - `_ _ _ T A _ _`
      - when adding char to `'_ _ _'`
      - margin and position problem
    - check input
      - check c in word, lock prev inputs
      - if not letter
      - elif c not in choices_temp
        - 'You already guessed ' c '. Guess again.'
        - count += 1
      - elif c in new guess str
        - fill 'green'
        - replace c in choices
        - 'Good job! Keep guessing...'
      - elif c not in
        - fill 'red'
        - replace c in choices
        - 'Sorry... Guess again.'
      - final
        - 'You got it! (press the mouse to restart)'
    -
- 4 info
  - 'Guesses: 0'
  - 'Time: 0s'
  - 'Guess a letter...'
- basic
  - line
    - draw sections - 1 times
  - reset
    - F5
    - game round += 1
  - stop when

rev

- how to place underscore directly under chars?

## ep4

we encourage you to write short animations that use the mouse, keyboard, and timer. Here are some ideas to get you started:

- Write an app where a dot is centered in the screen, and it keeps growing larger until it fills the canvas, then it keeps growing smaller until it is its original size, then it stops changing.
- Write an app with a red dot and a green dot. The red dot moves in some interesting way, say sweeping across the canvas left-to-right or top-to-bottom. The green dot moves in response to the arrow keys. The goal is to make the dots touch, at which point 'You Win!' is drawn.
- Write an app where the user presses the mouse 3 times to enter 3 points, then the triangle formed by connecting those 3 points is drawn, then you display the length (to the nearest integer) of each side, and then using threeLinesArea from week1 you display the area of the triangle.
- You get the idea. Short apps that use some combination of mouse, keyboard, and timer. Invent your own. Have fun!!!!

## [week 5: Worked Examples](https://www.cs.cmu.edu/~112/notes/notes-1d-lists-examples.html)

### 1 Locker Problem

def

- all close
- 1st open all
- 2nd close all even
- start from 3rd
  - change state

step

- prepare the list
  - close = F
  - open = T
- loop
  - for i in [3, n]
  - toggle

adv: mathematical solution

- ref
- https://proofwiki.org/wiki/Locker_Problem
- https://tasks.illustrativemathematics.org/content-standards/tasks/938

### 2 sieve prime

def

- https://en.wikipedia.org/wiki/Wheel_factorization

  - factor is coprime with basis in prime{2,3,5,7}

rev

- why edit list is faster than create new list?
- **过于沉浸于自己的方法里了**

step

- destructive
  - get list
    - remove by basis[2,3,5]
  - check item
    - remove not prime
- non-destructive
  - get list of bool
    - set F by basis [2,3,5]
  - check item
    - if prime
      - add to new list
      - check list by Eratos, set F

## [ep5](https://www.cs.cmu.edu/~112/notes/ep5.html)

info

- not use 2d lists, sets, dicts, or recursion this week.

### 2 Short Answer Practice Problems

1. D
   - M = L is alias
2. A
   - destructive func is more likely not to return value
3. ~~C~~ B
   - str dont have .index() ?
   - list dont have .find, only .index
4. ~~D~~ B
   1. extend adds a list of values
5. M = L[:3] + ~~5~~ [5] + L[3:]
6. B
   1. use while if edit the val of list when looping
7. B
   1. .sort() is destructive
8. C
   1. tuples immutable
9. len 1 tuple
   1. ~~(42)~~ (42,)
10. square
    1. M = [i**2 for i in L]

### 3 alternatingSum(a)

def

- l1-l2 + l3-l4 ...
- empty -> 0

step

- check L[0] with 0
- assign sign
  - for i
    - i = 1
    - i = 2
    - (-1)\*\*0 = -1

### 4 median(a)

def

- non-destructive
- middle or average of middle 2
- empty -> None

step

- get new list
  - order
- get middle
  - if len % 2 == 0

### 5 isSorted(a)

def

- list of numbers
- either smallest-first or largest-first
- function must only consider each value in the list once
  - may not sort the list
- list
  - 5,4,4,4
  - 3,4,4,4
  - 3,4,6,5
  - 1,2,3,3,2,1

step

- l[0] and l[len]
  - ...+...+ ? l[1]+l[len-1]
  - has max and min?
  - slice
- repaet

ref

- https://docs.python.org/3/howto/sorting.html
- https://www.programiz.com/python-programming/methods/list/sort

### 6 smallestDifference

def

- integers
- smallest absolute difference between any two
  - assert(smallestDifference([19,2,83,6,27]) == 4)

step

- sort
- get difference
  - change to abs
  - add to new list
- get min of new list

### 7 lookAndSay

def

- return [(count, number),...]
  - lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]

step

- if l[i] == l[i+1] == l[i+n]
  - count += n
  - remove l[i] to l[i+n]

### 9 nondestructiveRemoveRepeats

def

- nondestructively

step

- check if l[i] in l_new
  - if not: +=

### 11 isPalindromicList

def

- takes a list

step

- check 1st and last item
  - if not: F
  - list
    - l[i] == l[-1+i]
    - len, i[max]
    - 3, 1, a-b-c
    - 2, 1, a-b
    - 4, 2, ab-cd
    - 5, 2, ab-cde

### 12 reverse

step

- for i in len(l)
  - insert l[-1] at l[i]
  - pop l[-1]

### 13 vectorSum

def

- two same-length lists of numbers
- ([2,4],[20,30])
  - returns new list [22, 34]

step

- l_new += [l1[0] + l2[0]]

### 14 dotProduct

def

- the sum of the products of the corresponding terms
  - [1,2,3] and [4,5,6] is (1*4)+(2*5)+(3\*6), or 4+10+18, or 32
- non-destructively
- ignore the extra elements in the longer list

step

- use func 13
- change lambda expression

### 15 moveToBack

def

- two list
- destructively modify a
- without creating another list of length len(a).
- ([2, 3, 3, 4, 1, 5], [3, 2])
  - [4, 1, 5, 3, 3, 2]
- ([2, 3, 3, 4, 1, 5, 3, 2], [3, 2])
  - [4, 1, 5, 3, 3, 3, 2, 2]

step

- v2 edit the hit list
  - create hit list
    - with count = 0
    - indexing with l2
    - [3,2]
    - [0,0]
- v1 create new hit list # hard to deal w non-consecutive a[i] in b
  - create hit list
    - while a[i] in b
      - l_hit = [(count, number),(...)...]
      - pop a[i]
      - [4, 1, 5]
      - [2, 3]
- add count to l_hit
- add d in l_hit to a
  - d\*hit
    - for b in l_hit
    - [3, 2]

### 16 binaryListToDecimal

def

- reading the list from left to right as a single binary number
- list of 1s and 0s,
- binaryListToDecmial([1, 0]) -> 2
  - `2**1 + 0`
- binaryListToDecmial([1, 0, 1, 1]) ->11
  - `2**3 + 0 + 2**1 + 2**0`
- binaryListToDecmial([1, 1, 0, 1]) ->13
  - `2**3 + 2**2 + 0 + 2**0`

step

- if l[i] == 0
  - += 0
- elif l[i] == 1
  - += 2\*\*(len-1-i)

### 17 split(s, delimiter)

def

- split("ab,cd,efg", ",")
  - returns ["ab", "cd", "efg"].
- "ab,cd,efg", ","
  - 0
    - 'ab,cd,efg'
    - []
  - 1
    - 'cd,efd'
    - ['ab']
  - 2 - 'efg' - ['ab','cd']
    step
- find index in s
  - l += s[:i]
  - slice s
- check deli posn
  - if not last: += s

### 18 join(l, delimiter)

def

- join(["ab", "cd", "efg"], ",")
  - returns "ab,cd,efg".

step

- s += delimiter + l[i]

### 19 repeatingPattern

def

- takes a list a and
  - returns True if a == b\*k for some list b
- a == b\*k
- k is int, k > 1
- if len is odd
  - b is odd

step

- for k in (2, len+1)
  - if l[:x] \* n == l: T
    - abcd, l[1]
    - abcde, l[2]
    - min = 2
    - max = int(len/2)

### 20 mostAnagrams(wordList)

def

- possibly-unsorted list of words (all lowercase)
- first word alphabetically in the list that contains the most anagrams of itself in the list
  - If there are ties, still return just the first word alphabetically.

step

- help_count_anag(word, list)
  - return n

with var count_max

- check 1st item
  - count anag and replace
    - del itself, count = 1
    - rotate chars
    - if new word in list
      - del
      - count += 1
  - compare with max
    - only save if count_new > count_max
- repeat untill list == []

with list

- l_anag
  - [('act',1),('bay',2),('cat',2)]
  - could use lookAndSay(l)
  - or
    - l_anag = []
    - while l != []
      - if l[0] not in l_anag
        - l_anag += [l[0], l.count(l[0])]
        - while l[0] in l
          - l.remove(l[0])
- l_anag_max
  - get count_max in l_anag
  - create new list with count_max
  - ['bay','cat']
- if l[i] in l_anag_max
  - return

### 21 map(f, a)

def

- map(plus3, [2,4,7])
  - returns [5,7,10]

### 22 firstNEvenFibonacciNumbers(n)

def

- takes a non-negative number n
- returns a list of the first n even Fibonacci numbers in increasing order
  - (4) returns [2, 8, 34, 144]
- must run reasonably quickly (in O(n) time
  - cannot repeatedly call nthEvenFibonacciNumber

step

-

### 23 mostCommonName

def

- case sensitively, so 'jane' and 'Jane' are different names
- in order sorted() uses

### 24 histogram(a)

def

- histogram([73, 62, 91, 74, 100, 77])

```
    60-69: *
    70-79: ***
    80-89:
    90++ : **
```

step

v2

- change format
  - ['70-79', '60-69']
- count
  - sort
  - use helper func lookAndSay
- draw

v1

- set list of range
  - [(0,'60-69')]
- loop with counter
  - if in range: count += 1
- draw
  - if count == 0: skip
  - if item >= 90 or <= 10: format

#### rev

- [97, 5] 的范围时会出现奇怪的 string symbol

```
s = '10-- : *
            '
             '10-19:
            '
             '20-29:
            '
             '30-39:
            '
             '40-49:
            '
             '50-59:
            '
             '60-69:
            '
             '70-79:
            '
             '80-89: *
            '
             '90++ : *'
```

- 干，以为的 symbol bug 只是自己忘了改 test case

### 25 nearestWords(wordList, word)

def

- only contain lowercase letters
- If the word is in the wordlist, return that word.
- Otherwise, returns a list of all the words (in order) in the wordlist
  - that can be obtained by making _a single small edit_ on the given word
    - either by adding a letter
      - ['cat', 'hat'], 'at'
        - ['cat', 'hat']
        - m2
      - ['cat', 'hat'], 'ct'
        - ['cat']
        - m2
    - changing a letter
      - ['cat', 'hat'], 'bat'
        - m2
        - ['cat', 'hat']
      - (['cat', 'hat'], 'cab')
        - m2
        - ['cat']
    - deleting a letter
      - ['cat', 'hat'], 'htat'
        - ['hat']
        - match 3
      - ['cat', 'hat'], 'hcat'
        - ['cat','hat']
        - match 3
    - -> only 1 mismactch
- If no such words exist, returns None.

step

- scenario: add
  - if s1 in s
  - if c of s not in s1
    - pop
    - rest equal
- scenario: change
  - len == len1
  - count_mismatch == 1
- scenario: del
  - len == len1 - 1
  - if slice out the mismatch
    - the leftover parts all in s

### 26 bowlingScore(pinsPerThrowList)

def

- 10 frame
  - 2 throw
  - base score
    - the sum of all the pins knocked down
    - max 10
  - additional score
    - strike
      - knocks down all 10 pins on the first throw of a frame
      - the number of pins knocked down in the _next 2 throws_ are added to the score of that frame
    - spare
      - knocks down the rest of the 10 pins on the second throw in a frame
      - the number of pins knocked down in the _next 1 throw_ are added to the score of that frame
    - 10 + 10
      - strike + strike\*2
    - 10 + 9
      - strike + strike + x
    - 9 + (10-9)
      - strike + spare
  - if there is a spare or strike in the final frame
    - the bowler gets one extra throw in that frame
- takes a list of the number of pins knocked down on each throw and returns the score
  - _throws skipped due to strikes_ are not listed
  - best possible result is a list of 12 10's (all strikes)
    - score 300 points
    - 1 (10+10+10)
    - 2 (10+10+10)
    - ...
    - 10 (10+10+10)
- list
  - [10,10,9,1,6,3,7,3]
    - (10 + 10+9) + (10 + 9+1) + (9+1 + 6) + (6+3)
  - the last frame
    - [10,10,10]
    - [10,9,1]
    - [9,1,9]
  - [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

step

- frame[1]
  - score = based + additional
  - if strike
    - f[i] == 10
    - add 2 more
  - elif spare
    - f[i]+f[i+1] == 10
    - add 1 more
  - else
    - f[i]+f[i+1] < 10
- add sum

rev

- 看起来很复杂，写出来很简单
  - 糊里糊涂就 pass test 了……
- 要注意的是 index
  - 一个 i 计数 index
  - 一个 k 计数 frame

ref

- https://www.bowlinggenius.com/
- https://www.wikihow.com/Score-Bowling

27 polynomialToString(p)

def

- returns a string representation of that polynomial
  - Include a space before/after each "+" or "-" sign
  - Do not include 0 coefficients (unless the entire polynomial equals 0)
- [2,-3,0,4]
  - "2n^3 - 3n^2 + 4"
    - 2,3
    - -3,2
    - 0,1
    - 4,0
  - l[i]n^(len-1-i)

### [ep5-ct-and-roc](https://www.cs.cmu.edu/~112/notes/ep5-ct-and-roc.html)

#### CT

1

- step
  - ct1([2,1,0])
    - for i in range(3)
      - l[0] = 2+3+2 = [7,1,0]
      - l[1] = 1+8+7 = [7,16,0]
      - l[2] = 0+23+16 = [7,16,39]
    - sort n%10
      - [7,6,9]
  - a
    - ~~[5,6,7]~~
- print
  - [16,7,39]
    - ~~[5,6,7]~~
  - [7,16,39]
    - ~~[2,1,0]~~

2

- ct2([4], [2,3])
  - a = [4]+[3] = [4,3]
  - a(local) = [4,3] + [4] = [4,3,4]
  - for c in [4,3]
    - for i in range(0,2)
      - c = 4, i = 0
        - b[0] = 2, not in a
        - b[0] += 4 = 6
        - b = [6,3]
        - 'A'
      - c = 4, i = 1
        - b[1] = 3, in a, b[-1] = 3 != c
        - b(local) = [6,3] + ~~[c]~~ 4 = [6,3,4]
        - 'C'
      - ~~c = 3, i = 0
        - b[0] = 6, not in a
        - b[0] += 3 = 9 [9,3,c]
    - for i in (0,3)
      - c = 3, i = 1
        - b[1] = 3, in a, b[-1] = c == c, 3%2 ==1
      - c = 4, i = 0
        - b[0] = 9 not in a
      - c = 4, i = 1
        - b[1] = 3~~
      - c = 3, i = 0
        - b[0] = 6 not in a
        - b[local] = [9,3,4]
      - c = 3, i = 1
        - b[1] = 3
        - b[local] += [3] = [9,3,4,3]
      - ~~c = 4, i = 1
        - b[0] = 9 not in a
        - b[local] += [4] = [9,3,4,3,4]~~
      - c = 3, i = 2
        - b[2] = 4 not in a, 3%2 == 1
        - b[local] += [3] = [9,3,4,3,3]
    - - for i in (0,5)
- print
  - ~~ACAB~~
  - ~~[4,3,4],[9,3]~~
  - [4,3], [6,3]

#### ROC

1

- M is list
- len = 5
- for i in (-1,3)
  - M[-1] = M[-2] + (-1)
  - M[0] = M[-1] + 0
  - M[1] = M[0] + 1
  - M[2] = M[1] + 2
- abcde
  - e = d-1
  - a = e
  - b = a + 1
  - c = b + 2
  - a + (a+1) + (a+1 + 2) + (a+1) + a = 15
    - 5\*a + 5 = 15
    - a = 2
  - [2,3,5,3,2]

2

- list, no None
  - [item1, item2,...]
- L[0] != None
  - j = L[0]
  - L[0] = None
  - i = L[0] = item1
  - a = [None, None]
- [None, item2,....]
- [1, 3, -1, 4, None]
  - [None, None, -1, None, None]
  - i = 0
    - j = L[0] = 1
    - L[0] = None, [None, x, -1, x, x]
    - i = j = 1
  - i = 1
    - j = L[1] = 3
    - L[1] = None, [None, None, -1, x, x]
    - i = j = 3
  - i = 3
    - j = L[3] = 4
    - L[3] = None, [None, None, -1, None, x]
    - i = j = 4
  - i = 4
    - j = L[4] = x
    - L[4] = None, [None, None, -1, None, None]
    - i = j = x = [0,1,3,4]
  - End
- L
  - [1,3,-1,4,0]
  - [1,3,-1,4,1]
  - [1,3,-1,4,3]
  - [1,3,-1,4,4]

## [hw6](https://www.cs.cmu.edu/~112/notes/hw6a.html)

info

- covers week5 material. Still, since it is technically hw6, the linter refers to week6.

### 1 destructiveRemoveEvens

def

- possibly-empty list
  - contains only integers
- destructively removes all the even integers

step

- .remove

rev

- 就这？……
- for d 也不能用，背后是按照 index 来走的

### 2 nondestructiveRemoveEvens

def

- nondestructive
- works the same as the previous function
- need to build up a new list from scratch

step

- if not event
  - add to new list

### 3 areaOfPolygon

def

- in the last term, the expression wraps around back to the first vertex again

step

- for i
  - mode when the last i
  - len-1 and i%i

### 5 multiplyPolynomial

def

- ([2,0,3], [4,5]) represents the problem (2x\*\*2 + 3)(4x + 5)
  - (2x**2 + 3)(4x + 5) = 8x**3 + 10x\*\*2 + 12x + 15
  - returns [8, 10, 12, 15]
- ([2, -4], [3, 5])
  - [2,-4]
  - [3,5]
  - [6, -2, -20]

step

- form new lists
  - [0]\*n
- add lists
  - ([2,0,3], [4,5])
    - [8,0,12,0]
    - [0,10,0,15]
  - ([1,2,3], [1,2,3])
    - [1,2,3,0,0]
    - [0,2,4,6,0]
    - [0,0,3,6,9]
  - l[0] += p2[0] \* p1[0]
  - l[1] += p2[0] \* p1[1]
  - ...
  - l[1] += p2[1] \* p1[0]
  - l[2] += p2[1] \* p1[1]

### 6 solvesCryptarithm(puzzle, solution)

def

- takes two strings, a puzzle (such as "SEND + MORE = MONEY") and a proposed solution (such as "OMY--ENDRS")
  - assign 0 to "O", 1 to "M", 2 to "Y", 5 to "E", 6 to "N", 7 to "D", 8 to "R", and 9 to "S"
  - _9 5 6 7 + 1 0 8 5 = 1 0 6 5 2_
- return True if substituting the digits from the solution back into the puzzle results in a mathematically correct addition problem
- do not have to check whether a letter occurs more than once in the proposed solution
- do have to verify that all the letters in the puzzle occur somewhere in the solution

step

- get each part - change to number - according to index in solution

### 7 bestScrabbleScore(dictionary, letterScores, hand)

def

- takes 3 lists -- dictionary (a list of lowercase words), letterScores (a list of 26 integers), and hand (a list of lowercase characters)
  - finds the highest-scoring word in the dictionary that can be formed by some arrangement of some set of letters in the hand
    - some or all, any order
- try to think of at least two helper functions you could use before writing any code at all
- do not try to generate all the possible ways to arrange the hand
  - takes a word and a hand, and tells whether or not that word could be constructed using that hand
- ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
  - ['xyz', 'zxy', 'yy', 'yx'] # l_hit
  - [10,10,10,9]
  - (['xyz', 'zxy', 'yy'], 10)

step

- get list_anagram of hand
  - check each word in dict with hand, w helper?
- loop list_anagram
  - check score w helper
- result of highest score
  - 1 in tuple
    - (s_word, n_score)
  - multi in tuple
    - ([s_word], n_score)
  - N

### 8 Bonus / Optional: runSimpleProgram(program, args)

def

- write a so-called interpreter
  - keep track of the local variables
  - move line-by-line through the program
  - simulating the execution of the line
- useful to keep track of the current line number
- infinite runs until hit a RTN statement
- may solve this how you wish
  - we used strip, split, and splitlines in sample solution
- build your function incrementally
  - starting with the simplest test cases you can think up
  - add more test cases as you implement more of the language

legal expressions

- [Non-negative Integer]
- A[N]
- L[N]
- [operator] [operand1] [operand2]

legal statements

- ! comment
- L[N] [expr]
- [label]:
- JMP [label]
- JMP+ [expr] [label]
- JMP0 [expr] [label]
- RTN [expr]

helper

- translate
  - str to val in l_arg or l_var
- get type of line

step

- split str
  - sublist in list
  - exclude comment
  - ['c', l1, l2, 'c', l3]
- \*scan max index of l_var
- if local var

### 9 Bonus / Optional: Solving Puzzles with Combinatoric Generatorsd

#### allSublists

def

- example
  - Python must build the whole enormous list before we can use any of it
- generator, yield
  - Python stops running the function at that point,
  - uses the yielded value,
  - never creates the list, it just creates one value of the list at a time
- numb of sublists
  - [], [3], [3, 5], [5]
    - 2 + 2\*1
  - [], [6], [6, 7], [6, 7, 8], [6, 8], [7], [7, 8], [8]
    - 2 + 3*1 + 3*1
- allSublists(L) # [3,5]
  - []
    - k = 0 (0)
  - [5]
    - _[0,5]_
      - how to return len of 2
    - k = 1 (1)
  - [3]
    - [3,0]
    - k = 10 (2)
  - [3,5]
    - k = 11 (3)

step

- for d in k(as binary):
  - if d == 1 - add to l_result

rev

- debug 了半天
  - 大逻辑没错，format 错了
  - l_temp.insert(0, L[-1 - kth])
    - l_temp += L[kth]

#### heapsAlgorithmForPermutations

def

- the iterative (non-recursive) form of [Heap's Algorithm](https://en.wikipedia.org/wiki/Heap%27s_algorithm)
- n = 3
- c = [0,0,0]
- A = [3,1,2]
-
- i = 0
  - c[0] == 0
  - i = 0+1
- i = 1
  - c[1] == 0, < i
    - i is _odd_
    - swap A[c[1]],A[1]
    - _output [1,3,2]_ # round1
    - c[1] = 0+1
    - _c = [0,1,0]_ # pass c[1]
    - i = 0
-
- i = 0
  - c[0] == 0
  - i = 0+1
- i = 1
  - c[1] == 1 # pass
  - c[1] = 0
  - _c = [0,0,0]_
  - i = 1+1
- i = 2
  - c[2] == 0, < i
  - i is _even_
  - swap A[0],A[2]
  - _output [2,3,1]_ # round2
  - c[2] = 0+1
  - _c = [0,0,1]_
  - i = 0
-
- i = 0
  - c[0] == 0
  - i = 0+1
- i = 1
  - c[1] == 0, < i
  - i is _odd_
  - swap A[c[1]],A[1]
  - _output [3,2,1]_ # round2
  - c[1] = 0+1
  - _c = [0,1,1]_
  - i = 0
-
- i = 0
  - c[0] == 0
  - i = 0+1
- i = 1
  - c[1] == 1
  - c[1] = 0
  - _c = [0,0,1]_
  - i = 1+1
- i = 2
  - c[2] == 1, < i
  - i is _even_
  - swap A[0],A[2]
  - _output [1,2,3]_
  - c[2] = 1+1
  - _c = [0,0,2]_
  - i = 0
-
- i = 0
  - c[0] == 0
- i = 1
  - c[1] == 0, < i
  - i is _ood_
  - swap A[c[1]],A[1]
  - _output [2,1,3]_
  - c[1] = 0+1
  - _c = [0,1,2]_
  - i = 0
-
- i = 0
  - c[0] == 0
- i = 1
  - c[1] == 1
  - c[1] = 0
  - _c = [0,0,2]_
- i = 2
  - c[2] == 2
  - c[2] = 0
  - _c = [0,0,0]_
  - i = 2+1
- i = 3, end while

result

```
A = [3,1,2]
ic| c: [0, 0, 0]
ic| A: [1, 3, 2]
ic| c: [0, 1, 0]
ic| c: [0, 1, 0]
ic| c: [0, 0, 0]
ic| A: [2, 3, 1]
ic| c: [0, 0, 1]
ic| c: [0, 0, 1]
ic| A: [3, 2, 1]
ic| c: [0, 1, 1]
ic| c: [0, 1, 1]
ic| c: [0, 0, 1]
ic| A: [1, 2, 3]
ic| c: [0, 0, 2]
ic| c: [0, 0, 2]
ic| A: [2, 1, 3]
ic| c: [0, 1, 2]
ic| c: [0, 1, 2]
ic| c: [0, 0, 2]
ic| c: [0, 0, 0]
```

rev

- well，看懂 pseudo 的逻辑后把它翻译出来倒不难
  - 但还是没清楚原理。超出了目前的理解能力

ref

- http://ruslanledesma.com/2016/06/17/why-does-heap-work.html
- https://www.geeksforgeeks.org/heaps-algorithm-for-generating-permutations/
- https://stackoverflow.com/questions/31425531/heaps-algorithm-for-permutations

#### Solving cryptarithms

def

- find the solution that solves a cryptarithm
  - SEND + MORE = MONEY
- unique letters in the 3 words
  - SENDMORY
- len of 10 with dashes, indexing to [0,9]
  - SENDMORY--
- generate every possible permutation of the string
  - check each one in turn to see if it does in fact solve the puzzle
  - if, rtn it
  - elif none, rtn None

### [hw6b](https://www.cs.cmu.edu/~112/notes/hw6b.html)

info

- collaborative
- encourage you to finish hw6a before starting hw6b

step

- show msg default
- if click is in clickable area
  - if click is at ends
    - if saved index is null
      - skip
    - elif not null
      - if saved index is valid
        - move
        - change msg
        - _check win_
          - if win
            - pause
            - change msg
      - elif not valid
        - show msg
        - change msg
  - elif not at ends
    - get index of click in len of 3
    - show selection bg
    - if indexs includes each ends
      - change msg
      - change selection bg

view

- draw board
- draw selection
- draw player

rev

- 多个 bool 构成的 if
  - 完整写出各个 bool 的情况，避免位置顺序可能的省略？

## [hw8](https://www.cs.cmu.edu/~112/notes/hw8.html)

info

- not use recursion
- 感觉些难度,考虑先做下 ep

### [case study](https://www.cs.cmu.edu/~112/notes/2d-list-case-studies.html)

#### wordSearch1

step

- search word from each position in the board
  - each row
    - each col
  - board[0][0]
- search word from each direction at a position
  - direction 'right'
    - startRow = n, startCol = 0
    - board at [n][0], [n][1], [n][2]
    - i = 0,1,2 in word
    - drow = 0, dcol = 1
  - 'left'
    - board at [n][2], [n][1], [n][0]
    - startRow = n, startCol = 2
    - drow = 0, dcol = -1
  - 'up-left'
    - drow = -1, dcol = -1
    - startRow = n, startCol = 0
    - board at [n][2], [n-1][1], [n-2][0]

#### connect4saasd

step

- basic
  - save move count
  - save player count
- input col numb
  - check input valid
  - check col valid
    - in range
    - not full
- print board
- make move in col
- print board
- check win
  - if True: end
- repeat until
  - no room for new move
  - if win

### 1 isRectangular(L)

def

- takes a possibly-2d (or possibly not) list L
- returns True if the list
  - is in fact 2d
  - and if it is also rectangular
    - so each row has the same number of elements.
- return False otherwise

step

- check len
  - if not > 1
- loop through each val
  - check type
  - if i > 0
    - check length w last val
  - check sub val
- return True

### 2 makeMagicSquare

def

- takes a positive odd integer n
  - return None if not
- returns an nxn magic square by
  - following De La Loubere's [Method](https://en.wikipedia.org/wiki/Siamese_method)

step

- test
  - n = 3
  - row = col = 3
- 1
  - _0,1_
  - 0, 1
- 2
  - _2,2_
  - (-1), 2
- 3
  - _1,0_
  - (-2), 3%3
- 4
  - 0,1
    - (-3), (0+1)
    - encountered
  - _2,0_
- 5
  - _1,1_
  - (-2), (0+1)
- 6
  - _0,2_
  - (-3), (1+1)
- 7
  - 2,0
  - (-1), (2+1)

### 3 [Tetris](https://www.cs.cmu.edu/~112/notes/notes-tetris/index.html)

def

- may not use a different design
- write code according to a specific algorithm
  - rather than writing code to solve a specific problem

ref

- https://inventwithpython.com/pygame/chapter7.html
- game
  - https://tetris.com/play-tetris
  - https://www.lumpty.com/amusements/Games/Tetris/tetris.html

rev

- the goal is to practice knowledge and skills
  - not just to re-create a game
- **有点像 hw2 的 nthCircularPrime**
  - 都是被 func 的嵌套弄得晕头转向
  - 并且急切地想“提高效率以及复用率”

#### 1 Design Overview

- two main elements
  - a falling piece
    - is drawn over the board
    - is a 2-dimensional list of booleans
    - becomes part of the board when it can no longer fall
    - introduced other colors
    - to fill rows entirely with non-empty colors to remove row
  - a board
    - is full of one color(emptyColor)
- hci
  - pause 'p'
  - step 's'
  - reset 'r'
- helper
  - loop_each_cell
    - 因为 parameter 数量的限制，只适合这个项目？

#### 2 Creating and Drawing the board

- basic setup
  - gameDimensions()
    - set default parameters
    - return tuple
  - playTetris()
    - set width and height for app window
    - call app
- draw board
  - appStarted(app)
    - set app parameter from gameDimensions()
    - app.board # 2d list of str[['color names']]
    - app.emptyColor
  - redrawAll(app,canvas)
    - drawBoard() # loop each cell
      - call drawCell()
    - drawCell(app,canvas,row,col)
      - fill = board[row][col]
- test code

#### 3 Creating and Drawing the fallingPiece

- select a random falling piece in a random color
  - set pieces parameter
    - tetrisPieces # list of boolean
      - whether the given cell is painted
    - tetrisPieceColors
  - newFallingPiece(app)
    - randomly choose i from pieces
      - set fallingPiece
      - set fallingPieceColor
    - position in middle of the top row
      - set fallingPieceRow
      - set fallingPieceCol
- draw it over the board
  - drawFallingPiece() # loop each cell in fallingPiece
    - if T: call drawCell()
      - add color parameter
- test code
  - changes the falling piece if key == 'n'

#### 4 Moving the fallingPiece left/right/down

- make move
  - if keys in [directions]
  - moveFallingPiece()
    - save var temp
  - if not legal, undo # the result of the move
    - fallingPieceIsLegal() # loop each cell in fallingPiece
      - on board
      - no collision -> empty color
- when piece reach bottom
  - stay until reset

#### 5 Rotating the fallingPiece

- make change
  - if key == 'Up'
  - rotateFallingPiece() # 90 degrees counterclockwise
    - save var temp
      - [1,2,3]
      - [4,5,6]
      - to
      - [3,6]
      - [2,5]
      - [1,4]
    - col_new = reversed(row)
      - [3,2,1]
    - row_new = col[-1]
      - [3,6]
    - update location
  - if not legal, undo
    - fallingPieceIsLegal()

#### 6 Dropping and Placing the fallingPiece and Handling Game-Over

- piece stops moving
  - timerFired # no user illegal move
    - if not moveFallingPiece() # add return bool
- placeFallingPiece() # fallingPiece'data to board
  - board[x][y] = fallingPieceColor
- newFallingPiece()
- gameover
  - not fallingPieceIsLegal()

#### 7 Removing Full Rows and Keeping Score

- removeFullRows()
  - could be at any row
  - new board to store non empty rows
  - call in placeFallingPiece()
  - update score
- score
  - reward removing multiple lines at once
    - square of total number of full rows
  - dispaly
    - drawScore()
- hard drop
  - if key == 'space'

#### 8 More Ideas

- if user presses 'b', then switches to
- course
  - Dual rotation
  - Levels difficulty
    - dropping faster
    - **more difficult piece types**
      - row from -1 to -n
      - randomly choose colors other than empty
  - More attractive pieces
  - "Splash screens" with help instructions
  - **Piece Preview**
    - app.pieceNext
      - call newPiece earlier and save
  - (Moderate) High scores list # tedious to test
    - if gameover: add score to list
    - sort and display list
  - (Moderate) A Piece editor
    - (so you can create new types of pieces and add them to the game)
  - (Moderate/Hard) Integration with other Tkinter widgets
    - (buttons, menus, etc)
  - hard
    - Music (you can find the Tetris midi here).
    - (Hard) High scores list, but stored on the web and shared across users.
    - (Very Hard) Making this implementation **object-oriented**
      - adding a Piece class with LPiece, SPiece, and so on as subclasses,
      - then actual falling pieces as instances
    - (Very Hard) Network-based multiplayer Tetris.
- self
  - **show destination**
    - on current falling
  - store fallingPiece info as list
    - list works but might not be that efficient like class

## [ep8](https://www.cs.cmu.edu/~112/notes/ep8.html)

info

- not use recursion
- may assume 2d lists are rectangular unless explicitly stated otherwise

### 1 hasNoPrimes(L)

def

- returns True if L does not contain any primes
- refactor old ones
  - 2,3,5,7
  -

step

- loop each val in sublist l[0] and l[1]
- check if val is prime

### 2 hasDuplicates(L)

def

- returns True if L contains any duplicate values
  - (that is, if any two values in L are equal to each other)

step

- loop each val in sublist l[0]
  - check if val is in sublist l[1]

### 3 isLatinSquare(board)

def

- returns True if it is a [Latin square](https://en.wikipedia.org/wiki/Latin_square)
- n × n array filled with n different symbols
  - each occurring exactly _once in each row_ and exactly _once in each column_
  - [A,B,C]
  - [C,A,B]
  - [B,C,A]
  - O(n\*\*2)?
  - 1234
    2143
    3412
    4, can only 4
    4321
  - 1234
    2341
    3412
    4123

step

- const list of col
- compare all sublist
  - sort each, non-destru
    - if l[x] != l[y]: F
    - 2n
      - sort each row - n
      - sort each col - n
  - or sort board?
    - const list
      - add each val\*n in l[0]
    - if != sorted(board)
    - (n+2)
      - sort board - 1
      - sort l[0] - 1
      - loop and edit l[0] - n
      - compare - 1
    - (2+1,n+2)
      - loop and check
      - if val\*n not in board: F
  - or just check board
    - (n)
    - if count(val in l[0]) in board == n
- loop each val in l[n] in rows and cols
  - if count(val) > 1: F

### 4 matrixMultiply(m1, m2)

def

- takes two 2d lists
  - (that we will consider to be matrices)
  - The number of columns of the 1st matrix must equal the number of rows of the 2nd matrix
- returns a new 2d list
  - that is the result of multiplying the two matrices
  - Return None if the two matrices cannot be multiplied for any reason.
- matrix product
  - `m*n * n*p = m*p`
  - has the number of rows of the 1st matrix
  - has the number of columns of the 2nd matrix
- https://www.mathsisfun.com/algebra/matrix-multiplying.html

step

- check n1 == n2
- const list of cols in m2
- loop each row in m1
  - loop each row in l_cols_2
    - get sum of dot multi
      - m1[k] and l_cols_2[i]
    - add to sublist
  - add to 2d list

### 5 isKnightsTour(board)

def

- takes such a 2d list of integers
- returns True if it represents a legal knight's tour and False otherwise
  - all the numbers from 1 to N2 will be included
  - each move from k to (k+1) will be a legal knight's move
- ref
  - https://en.wikipedia.org/wiki/Knight's_tour
  - https://www.geeksforgeeks.org/the-knights-tour-problem-backtracking-1/
  -
  - https://en.wikipedia.org/wiki/Knight_(chess) - forming the shape of an L) - may move two squares vertically and one square horizontally, - or two squares horizontally and one square vertically

step

- check board
  - if not digit in sequence: F
- for i
  - `[0, n**n)`
  - get position of i
  - get position of i+1
  - check if two postion are legal
    - 8 moves in row and col
    - [-2,-1], [-2,1]
    - [2,-1], [2,1]
    - [-1,-2], [1,-2]
    - [-1,2], [1,2]
    - if any(): T
    - abs in [[2,1], [1,2]]

### ct-and-roc

#### CT1

- L = [[1],[2,5]] # p1=[1], p2=[2,5]
- a = L
- b = copy.copy(L) # shallow, copy ref
  - _b = [p1,p2]_
- c = copy.deepcopy(L)
  - _c = [[1],[2,5]]_
- b[1][1] = c[0][0] # 1
  - _p1=[1], p2=[2,1]_
  - b and L=a change
  - _b = [[1],[2,1]]_
  - _a = L = [[1],[2,1]]_
- c[1].append(b[1][0]) # 2
  - _c = [[1],[2,5,2]]_
- a[0] = b[1]
  - change ref
  - _a=[p2,p2]=L=[[2,1],[2,1]]_
  - b's ref not change
  - obj of p not change
  - ~~a = [[2,1],[2,1]] = L = b~~
- a[0][0] += b.pop()[0] # [2,1][0]=2
  - _b=[[1]]_ # p1
  - _a=L=[[4,1],[4,1]]_ # p2 change
- rtn a,b,c

print

- [[4, 1], [4, 1]] # a
  [[1]] # b
  [[1], [2, 5, 2]] # c
  [[4, 1], [4, 1]] # L=a

rev

- if a[0][0] += b.pop()[0] not pop
- a[0][0] += b[0][0]
  - a=[p2,p2]=L=[[2,1],[2,1]]
  - b=[[1],[2,1]]
- then
  - p2=[3,1]
  - a=L=[p2,p2]=[[3,1],[3,1]]
  - b=[p1,p2]=[[1],[3,1]]
