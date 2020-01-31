#Uses python3
# compute Fibonacci(n) modulo m, where n may be really huge: up to 10^14 .
import sys, math

# this slows significantly at 10^6
def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

# this computes for 10^18 in heartbeat.
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
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(fib_mod_fast(n, m))
