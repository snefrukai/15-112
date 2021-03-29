# Quiz

## Quiz 1

- review
  - 错的地方都是不仔细导致的“误入 if 歧途”或者计算出错

### Code Tracing

- 1
  - ~~15~~, 2, 2.5, 8
    - 21-12 = 9
    - ~~1+20-36~~, 2, 2.5, 2*2*2
    - 1+2*10-3*3*3*3, 10//4, 10/4, (10%4)\*\*3
  - 28
    - return 28
      - 10\*2+8
    - x = 2
      - 12%10
      - (10+2)%10
    - y = 8
      - 8%10
      - ct1(10)
      - print(ct1(10))
- 2
  - 5.0, ~~512~~, True, Flase
    - 125
      - pow(5, 3)
      - pow(min(5.6, int(5.6)), abs(5-8))
    - 5.0, 64\*8, bool(1.608), bool(0)
    - 5.0, pow(8, 3), bool(8.04/5), bool(1//5)
    - float(y), pow(min(x, int(x)), abs(y-8)), bool(x/y), bool(1//y)
    - y = 5
    - x =8.04
      - 5.6+2.44
      - 2.8\*2.8
      - x*=2 -> x=x*2
      - ~~x\*\*2~~
  - None
    - ct2(2.8, 5)
    - print(ct2(2.8, 5))
- 3
  - ~~54.64~~ 52.64
    - 54 + 64/100
    - ~~y = 54 ~~52
      - 10\*5+ ~~4 ~~ 2
      - 10\*h(5,10)+h(3,5)
        - h(5,10) return 5
          - x = 5
          - y = 10
        - h(3,5) ~~4~~ 2
          - x = 3
          - y = 5
    - z =64
      - 10\*6+4
      - 10\*h(5, 5)+h(5, 6)
        - h(5, 5) 6
        - h(5, 6) 4
    - x = 5
    - ct3(5)
    - print(ct3(5))

### 2. True/False [10 points; 2 points each]

- A. True
- B. False
  - ZeroDivisionError: division by zero
- C. True
- D. True
- E. True

### 3. Free Response: integerSquareRoot

- while

### 4. Free Response: alternatesEvenOdd

- // %
- bool

### Bonus Code Tracing

#### print(bonusCt1(15)) "0 ,16"

- return (h(h(h(h(h(h(h(h(h(h(15)))))))))) ,
- h(h(h(h(h(h(h(h(h(h(16)))))))))))
  - (h(h(h(h(h(h(h(h(h(h(15)))))))))) return 0
    - 0//2 = 0
    - 1//2 = 0
    - 3//2 = 1
    - 7//2 = 3
    - 15//2 = 7
    -
    - f(15\*\*0.5) F
      - return float(3.8) == int(3.8)
    - g(15,1/2) F
      - return f(15\*\*0.5)
    - h(15) 15//2 = 7
      - return 15 if g(15,1/2) else 15//2
  - h(h(h(h(h(h(h(h(h(h(16))))))))))) return 16
    - f(4) T
    - g() T
    - h() 16

#### print(bonusCt2(123, 45))

- return z(x,y,0)+z(x,y,1)+z(x,y,2) 11
  - 5+6+0
  - z(45,123,0) 5
    - 5\*10\*\*0
    - a =5
      - 45//1%10
      - 45//10\*\*0%10
    - b = 3
      - 123//1%10
    - c = 5
      - 125%10
      - 5\*\*3%10
  - z(45,123,1) 6
    - 6\*\*2%10
    - a = 4
      - 45//10%10
    - b = 2
      - 12%10
      - 123//10%10
    - c = 6
      - 4\*\*2%10
  - z(45,123,2) 0
    - 0\*10\*\*2
    - a = 0
      - 45//100%10
    - b = 1
      - 1%10
      - 123//100%10
    - c = 0
      - 0\*\*1%10
