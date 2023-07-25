# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10

def fib_partial_fast(start, end):

    a = 0
    b = fib_sum_fast(end)
    if start > 0:
        a = fib_sum_fast(start - 1)

    if b == 0:
        b = 10
    return (b - a)



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
            break
        period.append(cmod)
    
    plen = len(period)
    k = n % plen
    return period[k]

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))