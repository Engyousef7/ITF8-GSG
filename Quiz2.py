def find_smallest_largest(numbers):
    numbers.sort()
    smallest = numbers[0]
    largest = numbers[-1]
    return smallest, largest
input_list = [18, 2, 20, 100, 90, 81]
smallest_num, largest_num = find_smallest_largest(input_list)
print(f"The smallest number is: {smallest_num}")
print(f"The largest number is: {largest_num}")