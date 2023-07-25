# Uses python3
# find the last digit of a sum of the first n Fibonacci numbers.

import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current
    return sum
    # return sum % 10

# Property : last digit of the sum of n fibonnacci numbers is equal to 
# last digit of (n+2) fibonacci number - 1 for n >= 2.
# so --> Last_digit(F(n+2)) - 1
def fib_sum_fast(n):
    if n < 2: 
        return n
    
    s = fib_mod_fast(n+2, 10)
    if s  == 0: # Wouldn't have found this if not for stress testing
        return 9
    return s-1

def fib_mod_fast(n, m):
    period = [0, 1]

    if n <=1: return period[n]

    prev = 0
    cur = 1
    pmod = 0
    cmod = 1

    for i in range(2, n+1):
        prev, cur = cur, (prev+cur)
        pmod, cmod = cmod, (cur % m)

        if i > 2 and pmod == 0 and cmod == 1:
            a = period.pop() # this should be  a 0
            # print("period.pop() ", a, " i ", i)
            break
        period.append(cmod)
    
    # print(period)
    plen = len(period)
    # print("len(period) ", plen)
    k = n % plen
    # print("remainder: n%plen ", k)
    return period[k]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fib_sum_fast(n))
