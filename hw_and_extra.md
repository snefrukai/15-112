# homework and extra practice

## hw1

## [extra_practice1](https://www.cs.cmu.edu/~112/notes/extra-practice1.html)

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

## [extra-practice1-ct-and-roc](https://www.cs.cmu.edu/~112/notes/extra-practice1-ct-and-roc.html)

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

## [extra_practice2.py](https://www.cs.cmu.edu/~112/notes/extra-practice2.html)

- digit_count
  - loop
    - //
- gcd
  - var
- nthLeftTruncatablePrime
  - n//10% != 0
  - isPrime
  - leftTruncatablePrime
    - isPrime

### nthPowerfulNumber

- [无脑：i 遍历 n](https://cutt.ly/Lx2L9Tx)
  - n%i == 0 and prime
    - n%i\*\*2 == 0
  - i 的次数 ≈n
  - 随着 n 的增大会计算许多不必要的 i
- [高手：一边 i 遍历一边 divide n](https://www.geeksforgeeks.org/powerful-number/)
  - for every prime factor, find the highest power of it that divides n
    - if pow1 or pow2 > 1
    - m = a**pow1 \* b**pow2
  - 这时需要计算的 i 也变小了
  - 再用新的(3, nNew\*\*0.5+1, 2)算一遍
  - 先把一个除干净了，剩下的就是另一个了
  - check prime
  - m = a**2 \* b**3
    - if a = b, m = a\*\*5
    - if
      - m = p**2 \* p1**3
      - m = p1**2 \* p**3
    - if pow1 = even and > 2
      - m = (a**pow1/2)**2 \* b\*\*3
    - if pow1 = odd and > 2
      - m = (a**(pow1-3)\*a**3) \* b\*\*3
        - =(a**x)**2\* ab\*\*3
    - 同理可将 pow2 != 3 时归于 a\*2
    - 2 3 5 7
    - a\*a
    - b*b * b
    - so p**2 means at least a**2
- 差别 f(25), 88-22 steps
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

### [12F](https://www.kosbie.net/cmu/fall-12/15-112/handouts/notes-practice-thru-week3.html)

- digit_count

## [hw3](https://www.cs.cmu.edu/~112/notes/hw3.html)

Do not use lists, list indexing, or recursion this week.

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
- 'a' 'd'
  - 2 exact match
- 'b'
  - 1 partial match

#### step

- `count_match_exact(s, s1)` # abab, afaf
  - ~~replace when match~~
    - for i in [0, len(s)-1]
      - if s[k] == s1[k]
    - i = 0, k = 0
      - bab, faf
      - s = s[k+1:]
    - i = 1, k =1
      - bab, faf
      - s = s[:k] + s[k+1:]
    - replace 需精确到个位
    - i 会因为 replace 导致 out range
  - **replace after match**
    - loop str, save count and match
      - for i
        - i[0, len(s)]
    - loop match and replace
  - all match
    - count == len(s)
    - s == ""
- `count_match_partial(s, s1)` # bc, ab
  - loop str, save count and match
    - for i
      - i[0, len(s)]
      - should only count once
        - if match: break?
      - 0 aaffzx, yyazb - a, 1
      - 1 aaffzx, yyzb - 1
      - 4 aaffzx, yyzb - z, 2
      - 5 aaffzx, yyb - x, 2
  - no match
    - count == 0

#### rev

### 6. topLevelFunctionNames(code)

#### def

- multi-line string of Python code
- string with the names of the top-level functions

### 9. encodeRightLeftRouteCipher(s, n)

def

- 3WEATTACKATDAWN, 3 # 3-WTCTW-NDKTE-AAAAz
  - W T C T W
  - E T K D N
  - A A A A z

step

- get col
  - col = round up len(s)/rows # 5
    - 14/3 = 4.6
- fill missing grid
  - get difference
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

step

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

rev

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

## [extra-practice3](https://www.cs.cmu.edu/~112/notes/extra-practice3.html)

## [extra-practice3-ct-and-roc](https://www.cs.cmu.edu/~112/notes/extra-practice3-ct-and-roc.html)
