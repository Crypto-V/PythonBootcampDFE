# Exercise number 1. Print words that start with s;
# st = 'Print only the words that start with s in this sentence'
#
# for word in st.split():
#     if word[0].lower() == "s":
#         print(word)
#
# Exercise number 2.Print even number from 0 to 10:
#
# for x in range(0, 10):
#     if x % 2 == 0 and x != 0:
#         print(x)
#
# Exercise number 3.List comprehension
#
# my_range = [x for x in range(1, 51) if x % 3 == 0]
# print(my_range)
#
# Exercise number 4: Print even for every word that have a even size
#
# st = 'Print every word in this sentence that has an even number of letters'
#
# for word in st.split():
#     size = len(word)
#     if size % 2 == 0 and size != 0:
#         print("The word [{}] have the length of [{}] which makes it an even number!".format(word, str(size)))
# else:
#     print("Done!")
#
# Q5.FizzBuzz game
# list_of_numbers = []
# for number in range(1,101):
#     if number % 3 == 0 and number % 5 == 0:
#         number = 'FizzBuzz'
#         list_of_numbers.append(number)
#     elif number % 3 == 0:
#         number = 'Fizz'
#         list_of_numbers.append(number)
#     elif number % 5 == 0:
#         number = 'Buzz'
#         list_of_numbers.append(number)
#     else:
#         list_of_numbers.append(number)
# print(list_of_numbers)
#
# Q6. List comprehension to create a list of first letter of every word in the string below.
#
# st = 'Create a list of the first letters of every word in this string'
# new_st = [str(letter[0].lower()) for letter in st.split()]
# print(new_st)
