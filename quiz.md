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

## Quiz 2

### PART 1 (10 min.)

#### CT1

- print √
  - 0
    - i=0, j=0
      - T
  - 3
    - i=0, j=1
    - i=0, j=3
  - 112
  - 2
    - i=1, j=2
    - i=1, j=4
  - 112
  - (break)
  - 1
    - i=2, j=1
  - 4
    - i=2, j=4
- for i in range(3)
  - for j in range(i, 5)
    - if (i+j) % 3 == 0
      - print(j)
  - if i < 2
    - print(112)
    - if (i+j > 4)
      - break
- ct1(3, 5)

#### CT2

- print √
  - 0
    - n=2
    - n=20
    - a=10
    - b=2
    - c=7
  - 20
    - n=27
    - n=270
    - b=7
    - c=2
  - 270
    - n=272
    - n=2720
  - 2720
- ct2(10,7,2)

#### RC1 (10 pts)

def

- x is int
- x[1000, 5000]

rev

- 算到晕了
- 原来是被 % 和 // 迷惑了啊
  - 看来是数学没学好的缘故

step

- while x > 0
  - t = t\*100
  - a = x%10
  - b = (x%100) - x%10
    - 后两位的运算
  - x = x//100
    - i = 2
  - t += 10\*(x%10) + (x%100 - x%10)//10
- v3
  - x = _qwer_
  - a = r
  - b = e0
    - = er-r
  - x = qw
  - so, 1202
    - t2 = re00 + wq = 2021 = rewq
    - t1 = re
      - r0 + e
      - 10r + e0//10
- arch
  - x%10 = 200
  - x%100 = 230y
    - (x%100 - 200)//10 = 210
    - (x%100 - x%10)//10 = 210
  - = t*100 + 10*x%10 + (x%100 - x%10)//10
  - v2
  - a = 2
  - b//10 = 2001 ? ((x % 100) - 2)//10
  - a = 200 ? x%10
  - b = 21y ? (x%100) - 200

### PART 2 (10 min.)

#### nthSnarfPrime

rev

- 26min

## [Quiz 3](https://www.cs.cmu.edu/~112/notes/quiz3a.html)

- MAY NOT use VS Code or any other editor or resource for this quiz.
- may not use LISTS (except implicitly in loops), LIST INDEXING, SETS, DICTIONARIES, or RECURSION either.
- 15 min

Fill-in-the-Blank: averageGrade(gradebook) [50 points]

- rounded average quiz score
  - or None
  - not take a quiz
    - score will be '--' and will not count in average

```python
def averageGrade(student, gradebook):
    student = student.lower()
    gradebook = gradebook.lower()
    for line in gradebook.splitlines():
        name = None
        score = count = 0
        for entry in line.split(','):
            if (name == None):
                name = entry
            elif name != None:
                score += int(entry)
                count += 1
        if (name == student):
            if (count == 0):
              return None
            else:
              return score
    return None
```

CT1

- s = 'a'
- t = 'A'
- s = s + 'z' = 'az'
- t = t \* len('az'+'A')
  - = 'A' \* 3
  - = 'AAA'

print

- f's+t{s+t}'
- ~~'az' + t{'azAAA'}~~
- 's+t' + 'azAAA'
- = st+azAAA

CT2

- r = 'amazing'
- s = 'zambia'
- t = ''
- len(r) = 7
- i =
  - 0
    - 'zambia'.find(r[0])
    - a
    - t += 1
  - 2
    - a
    - 1 += 1
  - 4
    - i
    - 2 += 4
  - 6
    - g
    - 6 += -1
  - t = 7
  - 7 == eval(7)

print

- ~~False~~
- f'{t}=={eval(t)}'
- '114-1==113'
- '114-1==' + '113'
- t = '114-1'
  - '1' + '1' + '4' + '-1'

RC1
def

- c = 4
- chr(n) = 'B'

step

- xxxx
  - c from 0 to 4
- (B+4)(B+3)(B+2)(B+1)
  - n -=1 -> B
  - ord(s[0]) == n
- 'FEDC'

rev

- 17min
  - not RC1
  - not bonus

## [Quiz5 Version A](https://www.cs.cmu.edu/~112/notes/quiz5a.html)

info

- 20min
- may not use LISTS (except implicitly in loops), LIST INDEXING, SETS, DICTIONARIES, or RECURSION

Free Response: Animation [100 points]

- canvas is square, so app.width == app.height
- red dot of radius 50
- moves back-and-forth diagonal
  - from the top-left to the bottom-right
  - constant speed, by 5 at each step
  - start in the middle of the screen, moving towards the bottom-right
  - change direction each time its center moves off the canvas
- p
  - pause
- s
  - increase speed by 2
- click
  - inside
    - halved
  - outside
    - end

## [Midterm #1](https://www.cs.cmu.edu/~112/notes/midterm1.html)

[info](https://www.cs.cmu.edu/~112/notes/midterm1-frontmatter.html)

- **80 minutes** TOTAL
  - recommend <= 30 minutes on part 1
  - once in part 2, may not return to part 1

### [Version A](https://www.cs.cmu.edu/~112/notes/midterm1a.html)

#### p1

CT1

- idk ord
- so ord('A') == 65
- s = 'about baccarat wins!'
- r, n = '', 0
- for t in s.upper().split(' ') #
  - 'ABOUT'
    - n = 0+1 =1
    - c = char(65+1) = 'B'
    - r = ''+'B1' = 'B1'
  - 'BACCARAT'
    - n = 1+1 =2
    - c = 'C'
    - r = 'B1'+'C2'
  - 'WINS!'
    - n = 3
    - c = 'D'
    - r = 'B1C2'+'D0'

print

- 'B1C2D0'

CT2

- L = [2,3,3,2,5,3]
  - len = 6
- M = []
- i, j
  - ~~0, 0
    - L[0] == L[0]
    - M = [0]~~
  - 1, 0
    - L[1] != L[0]
  - ~~1, 1
    - L[1] = L[1]
    - apend 10\*1+1
    - M = [0,11]~~
  - 2, 0
    - L[2] != L[0]
  - 2, 1
    - L[2] == L[1]
    - apend 10\*2+1
    - M = [21]
  - ~~2, 2
    - L[2] == L[2]
    - apend 10\*2+2
    - M = [0,11,21,22]~~
  - 3, 0
    - L[3] == L[0]
    - _ap 10\*3+0_
    - M = [2,31]
  - 3, 2
    - l[3] != L[2]
  - 4, 0
    - L4 != L0
  - 4, 1
  - ...
  - L[4] != any
  - 5, 1
  - l5 == l1
    - _ap 10\*5+1_
  - l5 == l2
    - _ap 10\*5+2_
- M = [21,30,51,52]
- return [30,51,52,21]

CT3

- L = [3,1,2]
- M = sorted(L) = [1,2,3] # nondes
- N = L # alias
- M.append(L.pop(0))
  - L = [1,2]
  - N = [1,2]
  - M = ~~[1,2,3,1,2]~~ [1,2,3,3] # 加一位的运算怎么都错了
- N.append(M.pop(0))
  - M = ~~[2,3,1,2]~~ [2,3,3]
  - N = L = ~~[1,2,2,3,1,2] ~~ [1,2,1]
  - N = N[:2] = [1,2]

print

- ~~[1,2,2,3,1,2]~~ [1,2,1]
- ~~[2,3,1,2]~~ [2,3,3]
- [1,2]

CT4

- b = A(x=0, s='')
- for a in M
  - A(x=3,s='a')
    - b.x = 0+3 = 3
  - A(x=1,s='bc')
    - b.s = ''+'bc'[0] = 'b'
  - A(x=4,s='de')
    - b.x = 3+4 = 7
  - A(x=2,s='f')
  - b.s = 'b'+'d' = 'bf'

print

- [b.x, b.s]
- [7,'bf']

SA1

- M = L

SA2

- L.append adds one value and L.extend adds a list of values

SA3

- M is equal to L, only with the value 5 nondestructively inserted at index 3 (so L is unchanged).
- len(L)>3
- M = ~~L[:].insert(3, 5)~~
  - rtn None
- M = L[:3] + [5] + L[3:]

SA4

- refers to a singleton (length 1) tuple containing just the value 42
- T = (42,)
- or T = 42,

SA5

- contains the list of the squares of the values in L, which you may assume is a list of integers
- M = [i**2 for i in L]

SA6
indicate if they are part of the Model, the View, or a Controller

- timerFired(app)
  - C
- takeStep(app)
  - C
- drawGameOver(app)
  - V
- app.foodPosition
  - M
- placeFood(app)
  - C

#### p2

Free Response: nthSortOfSquarish(n)

def

- cannot use strings
- lists are ok
- isPerfectSquare(n), isSortOfSquarish(n), and nthSortOfSquarish(n)
  - isSortOfSquarish(n) you might want to make a list containing the individual digits in n

#### p3

BonusCT1

- eval(str(list(range(n)))[1:-1].replace(', ' , '-(')+(n-1)\*')')
- WTF...

#### rev

- 80min at FR2, w/o line func
  - which takes 17 more mins
- 薄弱点
  - CT's tracing
  - FR's complicated trigger
