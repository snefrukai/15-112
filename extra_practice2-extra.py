import math

def digitCount(n, digit):  # digitCount(123423526, 2) returns 3
    n =abs(n)
    count = 0
    if n ==0 and digit == 0: count == 1
    while n > 0:
        if digit == n%10:
            count += 1
        n //= 10
    #print(count)
    return count

assert digitCount(123423526, 2) == 3
'''digitCount(224, 2) #2
digitCount(224, 0) #0
digitCount(2, 2) #1
digitCount(-2, 2) #1
digitCount(100, 0) #2
digitCount(0, 0) #1
'''


def mostFrequentDigit(n):
    run = 0
    val = 0
    n = abs(n)
    for digit in range(10):
        foo = 0
        bar = n
        while bar > 0:
            if digit == bar % 10:
                foo += 1
            bar //= 10
        if foo >= run:  # most freq
            run = foo
            if foo == run: 
                val = max(val, digit)
            else: val = digit
        digit += 1
    return(run, val)


assert mostFrequentDigit(11) == (2,1)
assert mostFrequentDigit(111) == (3,1)
assert mostFrequentDigit(101) == (2,1)
assert mostFrequentDigit(100) == (2,0)
assert mostFrequentDigit(9898) == (2,9)        

###########################

def digitCompare(n):
    n = abs(n)
    numbCompare = False
    count = 0
    if n < 10:
        return 1, True
    #if n < 10: count = 1
    while n > 0:
        n = n//10
        foo =  (n%10%2 == 0 or n%10%5 == 0)
        #print(n % 10%2)
        if foo: 
            numbCompare = False
        count += 1
        #print("n:", n, count, numbCompare)
    #print(numbCompare)
    return count, numbCompare

#print(digitCompare(3))
#print(digitCompare(0))
#print(digitCompare(5))
#print(digitCompare(25))
#print(digitCompare(53))
print(digitCompare(67))
#print(digitCompare(119))
#print(digitCompare(317))

def isPrime2(n):
    if (n % 2 == 0 or n % 5 == 0):
        return False
    print("primer2: ",n)
    maxFactor = int(n**0.5)
    for factor in range(3, maxFactor+1, 2):
        if (n % factor == 0):
            return False
    return True
    

#print("prim:", isPrime(731))
#print("prim:", isPrime(119))

def rotatePrime(n):
    n = abs(n)
    if (n < 11): return True
    rotate = False
    count, numbCompare = digitCompare(n)
    #if not numbCompare: return False
    #print("left:",a)
    for m in range(1, count+1):
        while (n >= 10):
            a = n
            a = a//10
        print("n:",n, end="-")
        foo = (n-a*10**(count-1))*10+a
        n = foo
        print("rotate:", a, count-1, foo, m)
        if isPrime2(n): rotate = True
        else: rotate = False
    if rotate < m: rotate = False
    # all True = m
    # False = 0, True = 1
    return rotate

#print("rota: ",rotatePrime(3))
#print("rota: ",rotatePrime(5))
#print("rota: ",rotatePrime(11))
#print("rota: ",rotatePrime(14))
#print("rota: ", rotatePrime(19)) 
#print("rota: ", rotatePrime(23))
#print("rota: ", rotatePrime(119))
#print("rota: ", rotatePrime(173))
#print("rota: ", rotatePrime(191))


def isPrime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = round(n**0.5)
    for factor in range(3, maxFactor+1, 2):
        if (n % factor == 0):
            return False

        elif not rotatePrime(n):
            return False
    return True 

#print("prime:",isPrime(3))
#print("prime:",isPrime(11))
#print("prime:",isPrime(83))
#print("prime:",isPrime(119))
#print("prime:",isPrime(191))
#print("prime:",isPrime(14964321))
#print("prime:",isPrime(149345643266432421))

def nthCircularPrime(nth):
    found = 0
    guess = 0
    while (found <= nth):
        guess += 1
        #count, numbCompare = digitCompare(guess)
        #print(count, numbCompare)
        #cond = numbCompare and isPrime(guess)  # and rotatePrime(guess)
        #cond = isPrime(guess)
        cond = rotatePrime(guess)
        if cond:
            found += 1
    return guess

print()
'''print(nthCircularPrime(0), end="?2 ")
print(nthCircularPrime(1), end="?3 ")
print(nthCircularPrime(2), end="?5 ")
print(nthCircularPrime(3), end="?7 ")'''
#print(nthCircularPrime(4), end="?11 ")
#print(nthCircularPrime(5), end="?13 ")
#print(nthCircularPrime(6), end="?17 ")
#print(nthCircularPrime(7), end="?31 ") #91
#print(nthCircularPrime(9), end="?71 ")
#print(nthCircularPrime(10), end="?73 ")
#print(nthCircularPrime(14), end=" ")
#print(nthCircularPrime(15), end="?197 ")
#print(nthCircularPrime(16), end=" ")
#print(nthCircularPrime(20), end="?719 ")
#print(nthCircularPrime(25), end="?1193 ")
'''assert(nthCircularPrime(0) == 2)
assert(nthCircularPrime(5) == 13)
assert(nthCircularPrime(10) == 73)
assert(nthCircularPrime(15) == 197)
assert(nthCircularPrime(20) == 719)
assert(nthCircularPrime(25) == 1193)'''
