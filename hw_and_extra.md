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

### nthCircularPrime

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
   - [0, 5, 2n]
     - [2, 4, 6, 8] -> 2n
2. check prime
3. check rotates
   - abc -> bca, cab
   - for i
     - i[max] = 2 = count - 1
     - i[min] = 1
   - delete right1 digit # 709 -> 970
     - cab = ab + c\*10\*\*2
     - 可以更快地把 0 推到个位
   - ~~delete left1 digit # 709, 097, 970~~
     - bca = (n - a*10\*\*2)*10 + a
     - leading 0 导致位数变化，无法到达 970（？
4. `nthCircularPrime(nth)`
   - cond = TTT

```python
# to check if n is circular prime
isPrime(n) # return if n is prime
count = digit_count(n) # count n's digits

1. if (digits in n) % {0, 5, 2n} == 0
  return Fals
2. if not isPrime(n)
  return False
3. for i in (1, count) # rotate count-1 times
    n = n//10 + n%10 * 10**(count-1)
    if not isPrime(n) # rorates are not prime
      return False
4. if 1, 2, 3 all are True
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
      - chk result
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
n = 0
n_new = ""
for i in len(s)
  if s[i] is digit
    n_new += s[i] 
    n = max(int(n_new), n) 
  else # if find alpha
    n_new = ""
if n == 0: return None 
return n
```

```python
for i in len(s)-1
  n = s[i]
  m = s[i+1]
```

rev

- clear n_new 的时机需要在顶级

## [extra-practice3](https://www.cs.cmu.edu/~112/notes/extra-practice3.html)

## [extra-practice3-ct-and-roc](https://www.cs.cmu.edu/~112/notes/extra-practice3-ct-and-roc.html)
