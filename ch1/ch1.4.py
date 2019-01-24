# Palindrome Permutation: Given a string, write a function to check if its a
#  permutation of a palindrome.

"""
Approaches:
1) Brute force
    -Check if permutation
        >Count number of characters
            +If not equal, exit out of loop
    -Check palindrome
        >Create both instances, forward and backwards
        >Reverse backwards, compare each letter against forward

2) check if odd
    -Okay, so it seems that if a I have >1 odd characters than it is False.
    https://stackoverflow.com/questions/35377351/check-string-to-see-if-it-is-a-palindrome-of-any-of-its-permutations
"""

def perm_count(s1, s2):

    if len(s1) != len(s2):
        return False

    count1 = {}
    count2 = {}

    for i in s1:
        if i in count1.keys():
            count1[i] += 1
        else:
            count1[i] = 1

    for i in s2:
        if i in count2.keys():
            count2[i] += 1
        else:
            count2[i] = 1

    for i in count1.keys():
        if count1[i] != count2[i]:
            return False
    else:
        return True

# Creating the palindrome function
def pal(s2):
    s2a = s2.replace(' ', '') # stripping the spaces from s1
    s2b = s2.replace(' ', '')[::-1] # remove the spaces & reversing the order

    for i, j in enumerate(s2a):
        if s2a[i] != s2b[i]:
            return False
    else:
        return True


def perm_pal(s1, s2):
    return perm_count(s1, s2), pal(s2)



test1 = 'tact coa'
test2 = 'taco cat'

print(perm_pal(test1, test2))
