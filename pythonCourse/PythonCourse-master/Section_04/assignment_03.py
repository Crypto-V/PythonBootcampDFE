# Assignment 3

"""
Given a list of ints, return True if the sequence of numbers 1, 2, 3
appears in the list anywhere, false otherwise.

sequence([1, 1, 2, 3, 1]) → True
sequence([1, 1, 2, 4, 1]) → False
sequence([1, 1, 2, 1, 2, 3]) → True
sequence([1, 2]) → False
sequence([]) → False
"""

def sequence(list_of_ints):
    for i in range(len(list_of_ints)-2):
        if list_of_ints[i] == 1 and list_of_ints[i + 1] == 2 and list_of_ints[i + 2] == 3:
            return True

    return False
print(sequence([1,2,1,2,3]))



