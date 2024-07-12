from week5.change_dp import change
from week5.primitive_calculator import compute_operations

def test_change():
    assert change(0) == 0
    assert change(3) == 1
    assert change(34) == 9
    assert change(20) == 5
    assert change(1000) == 250

def test_compute_operations():
    # test 1
    ops, _list = compute_operations(1)
    assert ops == 0
    assert _list == [1]

    #test 2
    ops, _list = compute_operations(96234)
    assert ops == 14