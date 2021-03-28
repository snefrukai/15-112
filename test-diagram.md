
# 1.2 nthCircularxx

mermaid

```mermaid
graph TD
    start
    --> int{check int}
        --F--> 91["not int"]
        int--T
    --> digitCircular{check digit}
        -- n dont have ... digit 
        -- if digits have ... : F
        -- rtn T F  
        -- 0 5
        -- 2n
        --> 92["not circ"]
        digitCircular--T
    --> isPrime{check prime}
        --F--> 92
        isPrime--T
    --> digitRotate{check rotate}
        --F--> 92
        digitRotate--T
    --> 90[n]
```

---
PlantUML
nthCircularPrime

- 3个条件依次判断
- rev
  - 思路没问题
  - 卡在细节

```puml
start
- check int
    if (is int) then (F)
        ->
        - rtn: not int
        stop
    else (T)
    - rtn n
    endif
- check digit
    note right
        check 0 5
        * 59
        * 509
        check 2n: 2 4 6 8
        * 29
        * 69
    end note
    if (dont have) then (F)
        - rtn: not circ
        stop
    else (T)
    endif
- check prime
    if (is prime) then (F)
        - rtn: not circ
        stop
    else (T)
- check rotate 
    if (not rotate) then (F)
        - rtn: not circ
        stop
    else (T)
    endif
- rtn n
stop
```

```puml

rectangle start

rectangle B
rectangle C
rectangle D

start -r-> [check int]
[check int] -> F
[check int] --> [check prime] 
[check prime] --> [checkDigit]

```

---
flowchart.js

```flow
st=>start: start
e=>end: end

op1=>operation: digitCircular
op2=>operation: isPrime
op3=>operation: digitRotate

cond=>condition: digitCircular
cond2=>condition: isPrime
para=>parallel: parallel tasks

st->op1->cond
cond(yes)->cond2(yes)->e
cond(no)->op1
```

语法很严格
    判断必须要拼 yes
    需要很多的声明
