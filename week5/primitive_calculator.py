def compute_operations(n):
    current_number = 1
    num_of_operations = 0
    intermediate = []
    intermediate.append(current_number)

    while current_number < n:
        if current_number <= n/3:
            current_number = current_number*3
        elif current_number <= n/2:
            current_number = current_number*2
        else:
            current_number += 1
        intermediate.append(current_number)
        num_of_operations += 1
    return num_of_operations, intermediate


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
