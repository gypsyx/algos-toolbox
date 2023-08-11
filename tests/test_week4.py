from week4.binary_search import (
    binary_search, 
    binary_search_single_item
)
from week4 import binary_search_duplicates as bsd
from week4 import majority_element as me

class TestBinarySearch:
    def test_binary_search_single_item(self):
        items = [1, 2,3,4,5,6,7,8,9,10]
        low = 0
        high = len(items)-1

        assert binary_search_single_item(items, low, high, 0) == -1
        assert binary_search_single_item(items, low, high, 11) == -1
        assert binary_search_single_item(items, low, high, 10) == 9
        assert binary_search_single_item(items, low, high, 5) == 4
        assert binary_search_single_item(items, low, high, 1) == 0


    def test_binary_search_single_item_large_input(self):
        keys = []
        for i in range(1, 30000+1):
            keys.append(i)
        
        low = 0; high = 29999
        assert binary_search_single_item(keys,low, high, 30001) == -1
        assert binary_search_single_item(keys,low,high, 0) == -1
        assert binary_search_single_item(keys,low,high, 30000) == len(keys)-1


    def test_basic(self):
        items = [1, 2,3,4,5,6,7,8,9,10]

        assert binary_search(items, 2) == 1
        assert binary_search(items, 10) == 9

    def test_failed_test(self):
        input = "1 5 8 12 13"
        keys  = list(map(int, input.split(" ")))

        query = "8 1 23 1 11"
        query = list(map(int, query.split(" ")))

        expected = [2, 0, -1, 0, -1]

        for q, e in zip(query, expected):
            print( q, e)
            assert binary_search(keys, q) == e
        

    def test_large_input(self, benchmark):
        keys = []
        for i in range(1, 30000+1):
            keys.append(i)
        
        search_items = [i for i in keys]
        expected = [i-1 for i in keys]
        for i, j in zip(search_items, expected):
            assert binary_search(keys, i) == j


class TestBinarySearchDuplicates:
    def test_basic(self):
        items = [1, 2,3,4,5,6,7,8,9,10]
        low = 0
        high = len(items)-1

        assert bsd.binary_search_single_item(items, low, high, 0) == -1
        assert bsd.binary_search_single_item(items, low, high, 11) == -1
        assert bsd.binary_search_single_item(items, low, high, 10) == 9
        assert bsd.binary_search_single_item(items, low, high, 5) == 4
        # import pdb;pdb.set_trace()
        assert bsd.binary_search_single_item(items, low, high, 1) == 0


    def test_large_input(self):
        keys = []
        for i in range(1, 30000+1):
            keys.append(i)
        
        low = 0; high = 29999
        assert bsd.binary_search_single_item(keys,low, high, 30001) == -1
        assert bsd.binary_search_single_item(keys,low,high, 0) == -1
        assert bsd.binary_search_single_item(keys,low,high, 30000) == len(keys)-1

    def test_min_index(self):
        keys = [1, 2, 3, 3, 3, 3, 4, 5, 7]
        assert bsd.min_index(keys, 3, 3) == 2

        keys = [1, 2, 3, 3, 3, 3, 4, 5, 7]
        assert bsd.min_index(keys, 5, 3) == 2

        keys = [1, 2, 3, 3, 3, 3, 4, 5, 7]
        assert bsd.min_index(keys, 3, 3) == 2

        keys = [1, 2, 3, 4, 5, 7]
        assert bsd.min_index(keys, 2, 3) == 2

    def test_duplicates(self):
        items = [1, 2,3,4,5,5,5,6,7,8,9,10]

        assert bsd.binary_search(items, 5) == 4
        assert bsd.binary_search([1,2,2,2,2,2,5], 2) == 1
        assert bsd.binary_search([2,2,2,2,2,2,2], 2) == 0
        assert bsd.binary_search([1,2,2,2,2,2,5], 5) == 6
        assert bsd.binary_search([1], 2) == -1

    def test_duplicates_large_input_fast(self, benchmark):
        keys = [10**9]*15001
        for i in range(1,15001):
            keys.append(10**9 + i)
        
        print("\n", " len(keys) ", len(keys))
        print(keys[len(keys)//2])

        assert benchmark(bsd.binary_search, keys, 10**9) == 0

    def test_duplicates_large_input_slow(self, benchmark):
        keys = [10**9]*15001
        for i in range(1,15001):
            keys.append(10**9 + i)
        
        print("\n", " len(keys) ", len(keys))
        print(keys[len(keys)//2])

        assert benchmark(bsd.binary_search_old, keys, 10**9) == 0

class TestMajorityElement:
    def test_left_boundary(self):
        keys = [1,5,5,5,6]
        assert me.left_boundary_index(keys, 0, 2, 5) == 1

        keys = [1,5,5,5,6,7]
        assert me.left_boundary_index(keys, 0, 2, 5) == 1

        keys = [5,5,5,6,7]
        assert me.left_boundary_index(keys, 0, 2, 5) == 0

    def test_right_boundary(self):
        keys = [1,5,5,5,6]
        assert me.right_boundary_index(keys, 2, 4, 5) == 3

        keys = [1,5,5,5,6,7]
        assert me.right_boundary_index(keys, 2, 5, 5) == 3

        keys = [1,2,5,5,5,]
        assert me.right_boundary_index(keys, 2, 4, 5) == 4

    def test_majority(self):
        keys = [1,5,5,5,6]
        assert me.majority_element(keys) == 1

        keys = [5,5,5,5,5]
        assert me.majority_element(keys) == 1

        keys = [1,5,5,5,6,7]
        assert me.majority_element(keys) == 0

        keys = [1,2,3,6]
        assert me.majority_element(keys) == 0

    def test_large_input_fast(self, benchmark):
        # NOTE: although this is slower than the test with majority_element_naive for this use case
        # coursera seems to accept this solution as 'fast' so it must be fast enough!
        # TODO - try using a mergesort and counting while sorting and see how this performs
        keys = [10**9]*100000
        assert benchmark(me.majority_element, keys) == 1
    
    def test_large_input_naive(self, benchmark):
        keys = [10**9]*100000
        assert benchmark(me.majority_element_naive, keys) == 1


    def test_large_input_not_found(self, benchmark):
        # all unique elements
        keys = []
        for i in (0, 100.000):
            keys.append(i)
        
        assert benchmark(me.majority_element, keys) == 0

    
    def test_large_input_not_found_naive(self, benchmark):
        # all unique elements
        keys = []
        for i in (0, 100.000):
            keys.append(i)
        
        assert benchmark(me.majority_element_naive, keys) == 0

