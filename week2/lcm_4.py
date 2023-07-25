# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def lcm_fast(a, b):
    if a == 0 or b ==0 :return 0
    return int((a*b) / gcd_fast(a, b))

def gcd_fast(a, b):
    if b == 0 :
        return a
    aprime = a % b
    return gcd_fast(b, aprime)
        


if __name__ == '__main__':
    input = input()
    a, b = map(int, input.split())
    print(lcm_fast(a, b))

