def binary_search(keys, query):
    # write your code here
    index_dict = {}

    if query in index_dict:
        return index_dict.get(query)
    index = binary_search_single_item(keys, 0, len(keys)-1, query)
    return index

def binary_search_single_item(sorted_keys,low, high, item):
    if item < sorted_keys[low] or item > sorted_keys[high]:
        return -1
    
    mid = (high-low)//2 + low

    if sorted_keys[mid] == item:
        return mid
    elif item < sorted_keys[mid]:
        return binary_search_single_item(sorted_keys, low, mid-1, item)
    elif item > sorted_keys[mid]:
        return binary_search_single_item(sorted_keys, mid+1, high, item)
    else:
        raise Exception("shouldn't be here") 



if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
