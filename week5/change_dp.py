def change(money):
    # write your code here
    min_coins = {0:0}

    for m in range(1, money+1):
        min_coins[m] = 10**9
        for i in [1,3,4]:
            if m >= i:
                num_coins = min_coins[m-i] + 1
                if num_coins < min_coins[m]:
                    min_coins[m] = num_coins
    return min_coins[money]


if __name__ == '__main__':
    m = int(input())
    print(change(m))
