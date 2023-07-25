# Uses python3
# find the last digit of n-th Fibonacci number
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def fib_last_fast(n):
    if n == 0: return 0
    if n == 1: return 1

    prev = 0
    cur = 1
    i = 2
    while i <= n:
        prev, cur = cur, (prev + cur) % 10
        i += 1
    
    return cur




if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fib_last_fast(n))
