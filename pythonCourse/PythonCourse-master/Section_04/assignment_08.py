# Assignment 8

"""

Return the sum of the numbers in the list, except ignore sections of
numbers starting with a 7 and extending to the next 8
(every 7 will be followed by at least one 8).
Return 0 for no numbers.

EXAMPLE:
sum78([1, 2, 2]) → 5
sum78([1, 2, 2, 7, 99, 99, 8]) → 5
sum78([1, 1, 7, 8, 2]) → 4

"""


def sum_of_numbers(numbers):
    sum = 0
    in_range = False

    for i in range(len(numbers)):
        # if number at the index is equal to 7 loop will stop
        if numbers[i] == 7:
            in_range = True

        if not in_range:
            sum += numbers[i]

        if numbers[i] == 8:
            in_range = False

    return sum


print(sum_of_numbers([1, 2, 2]))
print(sum_of_numbers([1, 2, 2, 7, 99, 99, 8]))
print(sum_of_numbers([1, 1, 7, 8, 2]))
