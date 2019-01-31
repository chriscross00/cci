# String Compression:

# Need to finish
"""
Approaches:
1) For loop
    -Loop until the second to last element
    -Check if i is equal to i+1
        >If so iterate the counter
        >Else:
            -Add in string[i] to results
            -Add counts after
    -return results
"""


def compress(string):

    results = ''
    count = 1

    for i in range(len(string)-1):
        if string[i] == string[i+1] and i+1 < len(string):
            count += 1
        else:
            results += string[i]
            results += str(count)
            count = 1

    return results


test1 = 'aabcc'

print(compress(test1))
