# One Away: Types of inserts: insert a char, remove a char, or replace a char.
# Given 2 strings write a function to check if they are one or zero edits
# away.

"""
Approaches:
1) Brute force
    -Difference counter = 0
    -Check every element in a against element in b
        >If i of a not in b: difference counter += 1
    -If difference counter <= 1: return true
        >Else: return false
    -Time: O(a*b)
    -Space: 1

2) Dictionaries
    -Diff counter = 0
    -Store all letter, counts for a & b in dict
    -If a.key in b.key:
        >If a.values == b.values:
            pass
        >else:
            difference counter += abs(a.value - b.value)
    -If a.key not in b.key:
        >difference counter += b.value(i)
    -If b.key not in a.key:
        >difference counter += a.value(i)

    -If difference counter <= 1: return true
        >else: return false
    -Time: O(a+b)
    -Space: (a+b)

    -To make it slightly more efficient I could wrap the entire thing in a
    while loop. while diff < 2...
    This would stop me from doing extra work.


Hmmm, i had it right in the first place, I should have just used 3
functions. okay, i'll implement it.
"""


def one_away(a, b):
    if len(a) == len(b):
        return replace(a, b)
    elif len(a) + 1 == len(b):
        return edit(a, b)
    elif len(a) - 1 == len(b):
        return edit(b, a)
    else:
        return False


def replace(a, b):
    diff = False
    for i, j in zip(a, b):
        if i != j:
            if diff:
                return False
            diff = True
    return True


def edit(a, b):
    diff = False
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] != b[j]:
            if diff:
                return False
            diff = True
            j += 1
        else:
            i += 1
            j += 1
    return True


s1 = 'pale'
s2 = 'palo'

print(one_away(s1, s2))

"""
def one_away(a, b):

    if len(a) == len(b) + 2:
        return False
    if len(a) == len(b) - 2:
        return False

    diff = 0
    a_dict = {}
    b_dict = {}

    for i in a:
        if i in a_dict.keys():
            a_dict[i] += 1
        else:
            a_dict[i] = 1
    for i in b:
        if b in b_dict.keys():
            b_dict[i] += 1
        else:
            b_dict[i] = 1

    for i in a_dict.keys():
        if a_dict[i] in b_dict:
            if a_dict[i] == b_dict[i]:
                pass
            else:
                diff += abs(a_dict[i] - b_dict[i])
        if a_dict[i] not in b_dict:
            diff += b_dict[i]
    for in
"""














