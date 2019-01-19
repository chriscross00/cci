def bs(list):
    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j],list[j + 1] = list[j + 1],list[j]

    return list

a = [87,42,32,52,90,22,74,25,90]


def binarysearch(list, val):
    lo, hi = 0, len(list)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if list[mid]<val:
            lo = mid+1
        elif val<list[mid]:
            hi = mid-1
        else:
            return True

    return False




def bubble(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

    return list

print(bubble(a))

NO_OF_CHARS = 256


# Function to check whether two strings are
# Permutation of each other
def arePermutation(str1):
    # Create two count arrays and initialize
    # all values as 0
    count1 = [0] * NO_OF_CHARS

    # For each character in input strings,
    # increment count in the corresponding
    # count array
    for i in str1:
        count1[ord(i)] += 1

    return count1

top = 'stop'

print(arePermutation(top))

