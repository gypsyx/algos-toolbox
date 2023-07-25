# Uses python3
# implement an algorithm for the fractional knapsack problem.

import sys

def get_optimal_value(capacity, weights, values):
    # if capacity == 0 : return 0
    value = 0
    items = []
    for w, v in zip(weights, values):
        t = [v/w, w, v]
        items.append(t)

    items = sorted(items, reverse=True)

    # Here the assumption is that between all the items
    # the capacity can be fullfilled. Is this assumption right?
    for item in items:
        # assert capacity >= 0
        if capacity == 0:
            break

        w = item[1]
        if w == 0: continue
        if w <= capacity:
            capacity -= w
            # print("in if, capacity ", capacity)
            item[1] = 0
            value += item[2]
        else:
            value += item[0]*capacity
            item[1] -= capacity
            capacity = 0
        # print(capacity, value, items, "\n")
    # assert capacity == 0
    value = round(value, ndigits=4)
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
