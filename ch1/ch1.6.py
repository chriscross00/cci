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
    count = 0

    for i in range(len(string)):
        count += 1
        if i+1 >= len(string) or string[i] != string[i+1]:
            results += string[i]
            results += str(count)
            count = 0

    return results


test1 = 'aabcccd'

print(compress(test1))

