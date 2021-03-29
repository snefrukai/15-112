# hw

## hw2

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

1. check digit
   - if digit % x != 0
2. check prime
   - helper func
3. circular_p_rotate # if rotate are prime
   - rotate(n) -> [bac, cba]
     - delete left1 digit # 097 970
       - foo = bc\*10 + a
       - 无法到达 970
     - delete right1 digit # 970
       - 可以更快地把 0 放到个位
     - geek 的做法
       - rotate 绕场一周，n_new == n
       - 如果已经判断过 prim
         - not then F 效率更高？
     - return - **卡在这里**
       - 自己复杂化了，用了 bool 代表的二进制
         - if rotate < m: return False
         - False = 0, True = 1
         - all True = m = count
       - 用 not: return F 做排除即可
         - FT - F
         - TT - T
   - is_prime(rotate) == T
4. nthCircularPrime
   - if 1 and 2 and 3
     - found += 1

- rev
  - 3 个条件依次判断
    - 思路没问题
    - 卡在细节
  - ref
    - [geek](https://www.geeksforgeeks.org/check-whether-number-circular-prime-not/)

### nthPalindromicPrime

- ~~digit_equal_first_last(n) # abcd..z 12321~~
  - get a, z
  - if a == z
    - return bcd
- palindromic_digit # a..z 12321
  - ~~v1 check and remove digit~~
    - while n > 1 digit # TTT, TTF
      - n = digit_equal_first_last(n)
  - v2 check each digit with i # abc...xyz, 12345
    - a = n // 10\*\*(5-1-0) # 1
    - b = n // 10\*\*(5-1-1) % 10 # 2
    - y = n//10\*\*1 % 10 # 4
    - z = n//10\*\*0 % 10 # 5
  - list
    - 1..1
    - 2..2
    - 3
- isPrime
- rev
  - 去头去尾
  - abcd: 1231
    - a, d: 1, 1
      - n%10 # d
    - b, c: 2..3
      - bcd = abcd - a\*10\*\*(count-1)
      - bc = bcd//10
  - 121: 2
  - 1021: (0, 2)

### digitEqual

- rev
  - loop，取 nth 的新方法
    - loop time = %10 time, count

### carrylessAdd

- 7285+76
- loop min(x,y), %10 add
  - +1
    - 5+6 = 1
    - +5\*10
    - 8+7 = 5
- // \* 10\*\*count-2
  - add back to the left
  - +7200

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
