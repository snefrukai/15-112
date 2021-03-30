import time
import math


def digit_count(n, digit):  # digit_count(123423526, 2) returns 3
    n = abs(n)
    count = 0
    if n == 0 and digit == 0:
        count == 1
    while n > 0:
        if digit == n % 10:
            count += 1
        n //= 10
    print(count)
    return count


# assert digit_count(123423526, 2) == 3
# digit_count(224, 2) #2
# digit_count(224, 0)  # 0
# digit_count(2, 2)  # 1
# digit_count(-2, 2)  # 1
# digit_count(100, 0)  # 2
# digit_count(0, 0)  # 1

# %%


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
            else:
                val = digit
        digit += 1
    return (run, val)


assert mostFrequentDigit(11) == (2, 1)
assert mostFrequentDigit(111) == (3, 1)
assert mostFrequentDigit(101) == (2, 1)
assert mostFrequentDigit(100) == (2, 0)
assert mostFrequentDigit(9898) == (2, 9)
# print(mostFrequentDigit(9898))

# %%
# current_time_str = input("What is the current time (in hours 0-23)?")
# wait_time_str = input("How many hours do you want to wait")

# current_time_int = int(current_time_str)
# wait_time_int = int(wait_time_str)

# final_time_int = current_time_int + wait_time_int
# print(final_time_int)
