from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest

def largest_number_optimal(numbers):
    numbers = sorted(numbers, reverse=True)
    salary = ''

    while numbers:
        last = numbers.pop()
        salary = build_large_combo(str(last), salary)
    return int(salary)

def build_large_combo(a, b):
    if int(a+b) > int(b+a):
        return a+b
    return b+a

if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_optimal(input_numbers))
