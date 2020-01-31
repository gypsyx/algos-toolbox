import lcm_4 as lcm, sys
import fibonacci as fib
import fibonacci_last_digit_2 as fibld
import fibonacci_huge_5 as fibh
import fibonacci_sum_last_digit_6 as fibsumlast
import fibonacci_partial_sum_7 as fibpartial
import fibonacci_sum_squares_8 as fibsquares
import random


def stress_test_lcm():
    a = 0
    b = 0
    res1 = 0
    res2 = 0
    while True:
        a = random.randint(1, 10000)
        b = random.randint(1, 10000)
        res1 = lcm.lcm_naive(a, b)
        res2 = lcm.lcm_fast(a, b)
        print("a: ", a,  " b: ", b)
        if res1 == res2:
            print("OK")
        else:
            print("WRONG lcm_naive: {}, lcm_fast:{}".format(res1, res2))
            break
        print()

def stress_test_fib():
    res1 = 0
    res2 = 0
    while True:
        a = random.randint(1, 100)
        # b = random.randint(1, 10)
        res1 = fib.calc_fib(a)
        res2 = fib.fib_fast(a)
        print("a: ", a)
        if res1 == res2:
            print("OK")
        else:
            print("WRONG calc_fib: {}, fib_fast:{}".format(res1, res2))
            break
        print()

def stress_test_fib_last():
    res1 = 0
    res2 = 0
    while True:
        a = random.randint(1, 1000000)
        # b = random.randint(1, 10)
        
        res2 = fibld.fib_last_fast(a)
        print("a: ", a, " res2: ",res2, end=' ')
        sys.stdout.flush()
        res1 = fibld.get_fibonacci_last_digit_naive(a)
        print( "res1: ",res1)

        if res1 == res2:
            print("OK")
        else:
            print("WRONG fib_last_naive: {}, fib_last_fast:{}".format(res1, res2))
            break
        print()

def stress_test_fib_huge_mod():
    res1 = 0
    res2 = 0
    while True:
        n = random.randint(1, 1000000)
        m = random.randint(2, 1000)
        
        res2 = fibh.fib_mod_fast(n, m)
        print("n: ", n, " m: ",m, " res2: ",res2, end=' ')
        sys.stdout.flush()
        res1 = fibh.get_fibonacci_huge_naive(n, m)
        print( "res1: ",res1)

        if res1 == res2:
            print("OK")
        else:
            print("WRONG fib_last_naive: {}, fib_last_fast:{}".format(res1, res2))
            break
        print()


def stress_test_fib_sum_last():
    res1 = 0
    res2 = 0
    while True:
        n = random.randint(0, 100000)
        # m = random.randint(2, 1000)
        
        res2 = fibsumlast.fib_sum_fast(n)
        print("n: ", n, " res2: ",res2, end=' ')
        sys.stdout.flush()
        res1 = fibsumlast.fibonacci_sum_naive(n)
        print( "res1: ",res1)

        if res1 == res2:
            print("OK")
        else:
            print("WRONG fib_sum_naive: {}, fib_sum_fast:{}".format(res1, res2))
            break
        print()

def stress_test_fib_partial_last():
    res1 = 0
    res2 = 0
    while True:
        m = random.randint(0, 100)
        n = random.randint(0, 100) + m
        
        res2 = fibpartial.fib_partial_fast(m, n)
        print("m:", m, "n:", n, " res2:",res2, end=' ')
        sys.stdout.flush()

        res1 = fibpartial.fibonacci_partial_sum_naive(m, n)
        print( "res1:",res1)

        if res1 == res2:
            print("OK")
        else:
            print("WRONG partial_naive: {}, partial_fast:{}".format(res1, res2))
            break
        print()

def stress_test_fib_sum_squares():
    res1 = 0
    res2 = 0
    while True:
        # m = random.randint(0, 100)
        n = random.randint(0, 100000)
        
        res2 = fibsquares.fib_sum_squares_fast(n)
        print("n:", n, " res2:",res2, end=' ')
        sys.stdout.flush()

        res1 = fibsquares.fibonacci_sum_squares_naive(n)
        print( "res1:",res1)

        if res1 == res2:
            print("OK")
        else:
            print("WRONG naive: {}, fast:{}".format(res1, res2))
            break
        print()

if __name__ == '__main__':
    stress_test_fib_sum_squares()
