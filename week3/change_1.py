# Uses python3
import sys

def get_change(money):
    #write your code here
    options = [10, 5, 1]
    out = []

    while money > 0:
        for item in options:
            if item > money:
                continue

            money = money - item
            out.append(item)
            break
    return len(out)

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
