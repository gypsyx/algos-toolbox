# Uses python3
# Compute the last digit of f0^2 + f1^2 +...+ fn^2 .

from sys import stdin

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
            break
        period.append(cmod)
    
    plen = len(period)
    k = n % plen
    return period[k]

# Solution: Last digit of sum of squares is equal to last digit of 
# product of last digits of n and n+1

def fib_sum_squares_fast(n):
    if n <= 2:
        return n
    
    nth = fib_mod_fast(n, 10)
    next = fib_mod_fast(n+1, 10)
    return (nth*next) % 10


def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fib_sum_squares_fast(n))
