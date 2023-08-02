def optimal_summands(n):
    summands = []
    # write your code here
    sum = 0
    for i in range(1, n+1):
        sum += i
        if (n - sum) <= i:
            summands.append(n-(sum-i))
            break
        summands.append(i)
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
