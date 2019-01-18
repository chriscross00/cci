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
b = 'cap'

print(perm(a, b))

def test(s1, s2):
    done = len(s1) == len(s2) and sorted(s1) == sorted(s2)
    return done


