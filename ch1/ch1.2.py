# Check Permutation:  Given two strings, write a method to decide if one is
# a permutation of the other.

"""
Approaches:
1) Brute Force
    - Take every combination of the string X. See if string Y in those
    combinations.
    - Time complexity: O(n!) Really bad
    - Space complexity: O(n!)

2) Sort strings and check if order is the same
    - If the lengths aren't the same length return False
    - Sort the 2 strings
    - Compare the ith element in both strings
    - Time complexity: O(nLogn)

3) Count the number of each character in each string
    - For character in string store in dict
    - Compare key, values in dict1 to dict2
    - Time complexity: O(n)
"""


def perm(s1, s2):

    if len(s1) != len(s2):
        return False

    else:
        s1 = ''.join(sorted(s1))
        s2 = ''.join(sorted(s2))

        for key, val in enumerate(s1):
            if s1[key] != s2[key]:
                return False
        else:
            return True


a = 'pop'
b = 'pop'

# print(perm(a, b))

# This is a shorter version of above found on SO.


def test(s1, s2):
    done = len(s1) == len(s2) and sorted(s1) == sorted(s2)
    return done


# Counting

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


print(perm_count(a, b))
