# Uses python3
import sys

def get_change(m):
    #write your code here
    count = 0
    options = [10, 5, 1]
    out = []

    while m > 0:
        for item in options:
            if item > m:
                continue
            else:
                m = m - item
                out.append(item)
                count += 1
                break
    # print(out, count)
    return count

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
