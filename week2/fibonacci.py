# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def fib_fast(n):
    
    seq = []
    for i in range(0, n):
        if i == 0:
            seq.append(0)
        elif i == 1:
            seq.append(1)
        else:
            seq.append(seq[i-1] + seq[i-2])
    
    return seq

if __name__ == '__main__':
    n = int(input())
    print(fib_fast(n))
