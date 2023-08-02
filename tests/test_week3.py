from week3.change_1 import get_change
from week3.car_fueling_3 import *
from week3.dot_product import max_dot_product, max_dot_product_naive
from week3.covering_segments import Segment, optimal_points
from week3.different_summands import optimal_summands
from week3.largest_number import largest_number_optimal, build_large_combo

from time import time
import pytest

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

def test_optimal_points_failed_test():
    segments = [
        Segment(1, 3),
        Segment(2, 5),
        Segment(3, 6),
    ]
    points = optimal_points(segments)
    assert points == [3]

def test_optimal_points():
    segments = [
        Segment(6, 8),
        Segment(2, 5),
        Segment(1, 3),
        Segment(10, 11),
        Segment(7, 9),
    ]
    points = optimal_points(segments)
    assert len(points) == 3
    assert points == [2, 7, 10]

    assert optimal_points([]) is None

def test_optimal_points_two_segments():
    segments = [
        Segment(3, 5),
        Segment(1, 2),
    ]
    points = optimal_points(segments)
    assert points == [1, 3]

def test_optimal_points_one_segment():
    segments = [
        Segment(3, 5),
    ]
    points = optimal_points(segments)
    assert points == [3]

def test_optimal_points_large_input_failed_test():
    import os
    dirname = os.path.dirname(os.path.abspath(__file__))
    fname = os.path.join(dirname, 'segment_data')
    segments = []

    with open(fname, 'r') as data_file:
        for line in data_file.readlines():
            start,end = line.rstrip("\n").split(" ")
            segments.append(Segment(int(start), int(end)))
    
    segments = sorted(segments)
    
    points = optimal_points(segments)
    print(len(points))
    print(points)

def test_optimal_points_point_segment():
    segments = [
        Segment(80, 82),
        Segment(81, 81),
        Segment(82, 83)
    ]
    points = optimal_points(segments)
    assert points == [81, 82]

@pytest.mark.parametrize(
        "n, expected", [(8, [1,2,5]), (2, [2]), (1, [1]), (25, [1,2,3,4,5,10])]
)
def test_optimal_summands(n, expected):
    assert optimal_summands(n) == expected


def test_build_large_combo():
    assert build_large_combo('25', '9') == '925'
    assert build_large_combo('25', '35') == '3525'
    assert build_large_combo('', '23') == '23'
    
@pytest.mark.parametrize(
        "numbers, expected", [
            ([21, 2], 221), 
            ([9,4,6,1,9], 99641), 
            ([23,39,92], 923923),
            ([8,9,10], 9810)]
)
def test_largest_number_optimal(numbers, expected):
    assert largest_number_optimal(numbers) == expected


def test_largest_number_optimal_performance(benchmark):
    input = "2 8 2 3 6 4 1 1 10 6 3 3 6 1 3 8 4 6 1 10 8 4 10 4 1 3 2 3 2 6 1 5 2 9 8 5 10 8 7 9 6 4 2 6 3 8 8 9 8 2 9 10 3 10 7 5 7 1 7 5 1 4 7 6 1 10 5 4 8 4 2 7 8 1 1 7 4 1 1 9 8 6 5 9 9 3 7 6 3 10 8 10 7 2 5 1 1 9 9 5"
    input = input.split(" ")
    assert len(input) == 100
    for i in range(0, 100):
        input[i] = int(input[i])
    
    start = time()
    output = largest_number_optimal(input)
    end = time()
    print()
    print(output)
    print(end-start)

    benchmark(largest_number_optimal, input)
    




    
