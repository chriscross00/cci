# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use any additional data structures.

"""
Implementation:

Create a hash table that stores each character. If I come across a character
that I already have in my hash table then break out of loop and return False.
"""


def unique_char(string):
    letters = {}
    for i in string:
        if i in letters.keys():
            print('Not unique')
            break
        else:
            letters[i] = 1




test = 'abcddd'

unique_char(test)


# Without any additional data structures
# Sort the string and compare to neighbors
