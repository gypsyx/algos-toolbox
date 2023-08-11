def majority_element_naive(elements):
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0

def majority_element(elements):
    elements = sorted(elements)

def binary_search_single_item(keys,low, high, item, last_found=-1):
    if item < keys[low] or item > keys[high] or low > high:
        return last_found
    
    mid = (high-low)//2 + low

    if keys[mid] == item:
        last_found = mid
        return binary_search_single_item(keys, low, mid-1, item, last_found)
    elif item < keys[mid]:
        return binary_search_single_item(keys, low, mid-1, item, last_found)
    elif item > keys[mid]:
        return binary_search_single_item(keys, mid+1, high, item, last_found)

def right_boundary():
    pass


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))
