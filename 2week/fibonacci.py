# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def fib_fast(n):
    if n == 0: return 0
    if n == 1: return 1
    n1 = 0
    n2 = 1
    i = 2
    temp = 0
    
    while i <= n:
        temp = n2
        n2 += n1
        n1 = temp
        i += 1
    
    return n2

if __name__ == '__main__':
    n = int(input())
    print(calc_fib(n))
