import string
import time

from termcolor import colored

# Exersise 1
# Bring a number to a power
print("\nWhat is " + colored('7', 'red') + ' to the power of ' + colored('4', 'blue') + "?")
a = 7
b = 4

# use two stars [ ** ] as the 'power to' operand
print("\n   = " + colored(str(a ** b), 'green'))
time.sleep(0.6)

# Exercise End

# Exercise 2
# Split a string into a list

# String to be used:
s = "Hi there Sam!"

print("\nSplit this string: " + colored(s, 'red') + " into a list:" "\n")

# Make [li] list and use .split to input the "s" string
li = list(s.split(" "))

print('   = ' + colored(li, 'green'))
time.sleep(0.6)

# Exercise End

# Exercise 3
# Use .format() to print two variables into a string
print(
    "\nGiven the variables below, Use.format() to print the following string: \nThe Diameter of Earth is 12742 kilometers.'\n" + 'planet' + "   = " + colored(
        '\"Earth\"', 'blue') + "\n" + 'diameter' + " = " + colored('\"12742\"', 'red'))
planet = 'Earth'
diameter = '12742'
print('\n   = ' + colored('The diameter of {one} is {two} kilometers'.format(one=planet, two=diameter), 'green'))
time.sleep(0.6)

# Exercise End

# Exercise 4
# Given this nested list, use indexing to grab the word "hello"
# A nested list is created by placing a comma-separated sequence of sub-lists.
# A list can contain any sort object, even another list (sublist), which in
# turn can contain sub-lists themselves, and so on. This is known as nested list.
#
# Example for understanding
# lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
# print(lst[3])        # [5, [100, 200, ['hello']], 23, 11]
# print(lst[3][1])     # [100, 200, ['hello']]
# print(lst[3][1][2])         # 'hello'
#
lst = [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
print("\nGiven this nested list, use indexing to grab the word \"hello\"")
print(colored(lst, 'red'))
print('\n   = ' + colored(lst[3][1][2], 'green'))
time.sleep(0.6)

# Exercise End

# Exercise 5
# Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky
#
# Example for understanding
# Creating a Nested Dictionary
# Dict = { 'Dict1': {1: 'G', 2: 'F', 3: 'G'},
#          'Dict2': {'Name': 'Geeks', 1: [1, 2]} }
# Prints value corresponding to key 'name' in Dict1
# print(Dict['Dict2']['Name'])
#
d = {'k1': [1, 2, 3, {'tricky': ['oh', 'man', 'inception', {'target': [1, 2, 3, 'hello']}]}]}
print("\nGiven this nested dictionary grab the word \"hello\". Be prepared, this will be annoying/tricky\n" + colored(
    "d = " + str(d), 'red'))
print('\n   = ' + colored(d['k1'][3]['tricky'][3]['target'][3], 'green'))
time.sleep(0.6)

# Exercise End

# Exercise 6
# Create a function that grabs the email website domain from a string in the form:
# user@domain.com
# So for example, passing "user@domain.com" would return: domain.com
print('\nCreate a function that grabs the email website domain from a string in the form: ' + colored('user@domain.com',
                                                                                                      'red'))
email = "user@domain.com"
#
# Example for understanding
# the split() method splits a string into a list
# Syntax = string.split(separator, maxsplit)
# reminder [-1] when negative it counts from the right most, unlike positive first number is 1
x = email.split("@")[-1]
print('\n   = ' + colored(x, 'green'))
time.sleep(0.6)

# Exercise End

# Exercise 7
# Create a basic function that returns True if the word 'dog' is contained in the input string.
# Don't worry about edge cases like a punctuation being attached to the word dog, but do account
# for capitalization.
print(
    "\nCreate a basic function that returns True if the word 'dog' is contained in the input string. \nFix punctuation being attached to the word dog, and account for capitalization.")


def find_dog(st):
    print('\n   = ' + colored('dog' in st.lower().split(), 'green'))


# asking for input, and converting input to a lowercase list
s = input('\nEnter a phrase that includes (or not) the word \'dog\':\n')
out = s.translate(str.maketrans('', '', string.punctuation))
find_dog(out)
time.sleep(0.6)

# Exercise End

# Exercise 7
# Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases.
print(
    "\nCreate a function that counts the number of times the word \"dog\" occurs in a string. Again ignore edge cases.")


def count_dog(st):
    count = st.count('dog')
    if count == 1:
        print('\n   = ' + 'There was ' + colored(count, 'green') + ' dog in that phrase.')
    else:
        print('\n   = ' + 'There were ' + colored(count, 'green') + ' dogs in that phrase.')


# asking for input, and converting input to a lowercase list
s = input('\nEnter a phrase that includes (or not) the word \'dog\':\n')
out = s.translate(str.maketrans('', '', string.punctuation))
count_dog(out)
time.sleep(0.6)

# Exercise End

# Exercise 8
# Use lambda expressions and the filter() function to filter out words
# from a list that don't start with the letter 's'. For example:
#
#     seq = ['soup','dog','salad','cat','great']
#
# should be filtered down to:
#
#     ['soup','salad']
print(
    "\nUse lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. \nFor example:\n" + colored(
        "seq = ['soup','dog','salad','cat','great']", 'red') + "\nshould be filtered down to:\n" + colored(
        "['soup','salad']", 'blue'))
# initializing list
seq = ['soup', 'dog', 'salad', 'cat', 'great']

# initializing start Prefix
start_letter = 's'

# using filter() + startswith() + lambda
# Prefix Separation
with_s = list(filter(lambda z: z.startswith(start_letter), seq))

# print result
print("\n   = " + colored("The list with prefix s : ", 'green') + colored(str(with_s), 'green'))
time.sleep(0.6)

# Exercise End

# Final Exercise
# You are driving a little too fast, and a police officer stops you. Write a function
#  to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket".
#  If your speed is 60 or less, the result is "No Ticket". If speed is between 61
#  and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the
#  result is "Big    Ticket". Unless it is your birthday (encoded as a boolean
#  value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all
#  cases.

print(
    '\nYou are driving a little too fast, and a police officer stops you. Write a function\nto return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". \nIf your speed is 60 or less, the result is "No Ticket". If speed is between 61 \nand 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result \nis "Big Ticket". Unless it is your birthday (encoded as a boolean value in the \nparameters of the function) -- on your birthday, your speed can be 5 higher in all \ncases.\n')


def ticket(speed, is_bday):
    if is_bday:
        speeding = speed - 5
    else:
        speeding = speed

    if speeding > 80:
        print("   = " + colored("Big Ticket", "green"))
    elif speeding > 60:
        print("   = " + colored("Small Ticket", "green"))
    else:
        print("   = " + colored("No Ticket", "green"))


ticket(81, True)
ticket(81, False)
time.sleep(0.6)

print(colored('\n\n*Pat* *Pat* *Pat*', 'red') + ' you finished your first Python Tutorial!')
