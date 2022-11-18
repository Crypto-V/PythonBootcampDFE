# Exercise 1.Write a function that returns the lesser of two
# given numbers if both numbers are even, but returns the greater if one or both numbers are odd
# def lesser_of_two_evens(a, b):
#     if a % 2 == 0 and b % 2 == 0:
#         return min(a, b)
#     else:
#         return max(a, b)
#
# print(lesser_of_two_evens(2,4))
# print(lesser_of_two_evens(2,5))

# Exercise 2: Write a function takes a two-word string and returns True if both words begin with same letter
# def animal_crackers(text):
#     wordlist = text.lower().split()
#     return wordlist[0][0] == wordlist[1][0]
#
#
# print(animal_crackers("Levelheaded Llama"))
# print(animal_crackers('Crazy Kangaroo'))

# Exercise 3 :Given two integers, return True if the sum of the integers is 20
# or if one of the integers is 20. If not, return False

# def makes_twenty(n1, n2):
#
#     return (n1+n2) == 20 or n1 == 20 or n2 == 20
#
# print(makes_twenty(12,8))
# print(makes_twenty(20,8))

# Exercise 4: Write a function that capitalizes the first and fourth letters of a name

# def old_mcdonald(name):
#     first_half = name[:3]
#     second_part = name[3:]
#     return first_half.capitalize() + second_part.capitalize()
#
# print(old_mcdonald("macdonald"))

# Exercise 5:

# def reverse_the_words(string):
#     splitedString = string.split()
#     reversed_word_list = splitedString[::-1]
#     return ' '.join(reversed_word_list)
#
# print(reverse_the_words("i am v"))

# Exercise 5:
# def almost_there(n):
#     return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)
#
# print(almost_there(114))
# print(almost_there(104))

# Exercise 6:

def find_three(nums):
    for num in range(0, len(nums) - 1):
        if nums[num:num + 2] == [3, 3]:
            return True
    return False


print(find_three([1, 2, 3]))
print(find_three([1, 2, 3, 3, 5]))
