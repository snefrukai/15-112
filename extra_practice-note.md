# extra_practice

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
- getKthDigit
  - bool
- bool

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

## [extra_practice2.py](https://www.cs.cmu.edu/~112/notes/extra-practice2.html)

- digitCount
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

- digitCount
