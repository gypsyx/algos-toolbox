from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def largest_number_optimal(numbers):
    numbers = sorted(numbers, reverse=True)
    i = 0
    
    while i < len(numbers):
        outer = numbers[i]
        swap = False

        for j in range(i+1, len(numbers)):
            inner = numbers[j]
            if not is_better(str(outer), str(inner)):
                swap = True
                break
        
        if swap:
            numbers[i], numbers[j] = numbers[j], numbers[i]
        else:
            i += 1
    numbers = list(map(str, numbers))
    salary = "".join(numbers)
    return int(salary)

def is_better(a, b):
    if int(a+b) >= int(b+a):
        return True
    return False


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_optimal(input_numbers))
