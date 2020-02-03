from car_fueling_3 import *

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