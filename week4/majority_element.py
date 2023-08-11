def majority_element_naive(elements):
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0

def majority_element(elements):
    elements = sorted(elements)

    low = 0
    high = len(elements)-1
    mid = (low+high)//2
    item = elements[mid]
    left = left_boundary_index(elements, low, mid, item)
    right = right_boundary_index(elements, mid, high, item)
    occurences = right - left + 1
    
    if occurences > len(elements)/2 : # TODO use round?
        return 1
    return 0

def left_boundary_index(keys,low, high, item, last_found=-1):
    if low > high:
        return last_found
    
    mid = (high-low)//2 + low

    if keys[mid] == item:
        last_found = mid
        return left_boundary_index(keys, low, mid-1, item, last_found)
    elif item < keys[mid]:
        return left_boundary_index(keys, low, mid-1, item, last_found)
    elif item > keys[mid]:
        return left_boundary_index(keys, mid+1, high, item, last_found)


def right_boundary_index(keys,low, high, item, last_found=-1):
    if low > high:
        return last_found
    
    mid = (high-low)//2 + low

    if keys[mid] == item:
        last_found = mid
        return right_boundary_index(keys, mid+1, high, item, last_found)
    elif item < keys[mid]:
        return right_boundary_index(keys, low, mid-1, item, last_found)
    elif item > keys[mid]:
        return right_boundary_index(keys, mid+1, high, item, last_found)


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
