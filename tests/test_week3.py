from week3.change_1 import get_change
from week3.car_fueling_3 import *
from week3.dot_product import max_dot_product, max_dot_product_naive
from week3.covering_segments import Segment, optimal_points

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
    # for i, seg in enumerate(segments):
    #     print(i, " ", seg.start, "  ", seg.end)
    
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




    
