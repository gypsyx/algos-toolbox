# Uses python3
import sys, random

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            current_gcd = d

    return current_gcd

def gcd_fast(a, b):
    if b == 0 :
        return a
    aprime = a % b
    return gcd_fast(b, aprime)

def stress_test():
    a = 0
    b = 0
    res1 = 0
    res2 = 0
    while True:
        a = random.randint(1, 100000)
        b = random.randint(1, 100000)
        res1 = gcd_naive(a, b)
        res2 = gcd_fast(a, b)
        print("a: ", a,  " b: ", b)
        if res1 == res2:
            print("OK")
        else:
            print("WRONG gcd_naive: {}, gcd_fast:{}".format(res1, res2))
            break


if __name__ == "__main__":
    input = input()
    a, b = map(int, input.split())
    # print(gcd_fast(a, b))
    # stress_test()
    print(gcd_naive(a, b))
