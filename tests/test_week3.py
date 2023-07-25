from week3.change_1 import get_change
from week3.car_fueling_3 import *
from week3.dot_product import max_dot_product, max_dot_product_naive
from time import time

def test_get_change():
    count = get_change(35)
    assert count is 4


def test_compute_min_refills():
    stops = [200, 375, 550, 750]
    assert compute_min_refills(950, 400, stops) == 2

    stops = [1, 2, 5, 9]
    assert compute_min_refills(10, 3, stops) == -1

    stops = [100, 150]
    assert compute_min_refills(200, 250, stops) == 0

    stops = [100, 200, 300, 400]
    assert compute_min_refills(500, 200, stops) == 2

    stops = [100, 200, 300, 400]
    assert compute_min_refills(700, 200, stops) == -1


def test_max_dot_product():
    first_sequence = [10, 1, 2, 3]
    second_sequence = [100, 10000, 1000, 1]

    assert max_dot_product(first_sequence, second_sequence) == 103201
    assert max_dot_product_naive(first_sequence, second_sequence) == 103201

# slow test
def test_max_dot_product_naive_large():
    fs = [1, 2, 3, 4]
    ss = [x for x in range(1, 11)]
    max_dot_product_naive(fs, ss)

def test_max_dot_product_large():
    fs = [1, 2, 3, 4]
    ss = [x for x in range(1, 11)]
    max_dot_product(fs, ss)
