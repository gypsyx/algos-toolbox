from week2.max_pairwise_product import *

import random
import math, time
import pytest

@pytest.mark.skip(reason="max_product_fast function missing implementation")
def test_pairwise_prods():
    c = 1
    while True:
        n = math.floor(random.random() * 1000 + 2)
        numbers = [random.randint(1, 1000) for x in range(n)]
        
        start = time.perf_counter()
        prod_naive = max_pairwise_product(numbers)
        end = time.perf_counter()
        naive_time = (end - start)*1000

        start = time.perf_counter()
        prod_fast = max_product_fast(numbers)
        end = time.perf_counter()
        fast_time = (end - start)*1000

        if prod_naive != prod_fast:
            print("WRONG: prod_naive {}, prod_fast {}".format(prod_naive, prod_fast))
            print(n, numbers)
        else:
            print("OK {} naive_speed: {}  fast_speed: {}".format(c, naive_time, fast_time))
        c += 1