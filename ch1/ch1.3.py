# URLify: Write a method that will replace all spaces in a string with '%20'
# There is enough space at the end of the string to hold additional
# characters and you are given the 'true' length of the string


"""
Example:

    Input: "Mr John Smith", 13
    Output: "Mr%20John%20Smith"
"""

"""
Approaches:
1) For loop
    -For each character in the string check if it's equal to space.
        >If so replace with %20
    -Return string
    
2) replace()
    -Just run the replace function
"""


<<<<<<< HEAD

def own_replace(string):
    for i in string:
        if i == " ":
            i = '%20'
    return string
=======
def replace(string):
    for index, strl in enumerate(string):
        if strl == " ":
            string[index] = '%20'
    return string


>>>>>>> a02cde34b96f1c301af8db3c89f4bdf7b58f689f


test = 'ab cd'

print(own_replace(test))
# print(test.replace(' ', '%20'))
