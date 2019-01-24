# Move all zeros present in the array to the end of the array and return the
#  same array.

"""
Approaches:
1) Swap zero for nonzero
    -If arr empty, return none
    -Find zero
        >Find next nonzero
        >Call swap function, swapping zero for nonzero
    -Return array


Notes:
Does not work. It appends the ith element to the back and deletes the former
place. But, it 'skips' the i+1 element. Meaning that for the case
[0,0,1] the first 0 is correctly moved to the back but the second 0 will
move into position 0. Since position 0 has already been iterated through,
it will be skipped and the second 0 will not be moved correctly.
[append the each zero to the end?
    -For each i in arr
        >If i == 0, append it to the arr
    -return list
    -Time= O(n)
    -Space: n]

"""

def findnz(i, arr):
    while i < len(arr) and arr[i] == 0:
        i += 1
    return i

def z_nz(arr):

    if not arr:
        return None
    for i in range(len(arr)):
        if arr[i] == 0:
            j = findnz(i, arr)
            if j < len(arr):
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def zero_push(arr):

    if not arr:
        return None

    for i in range(len(arr)):
        if arr[i] == 0:
            arr.append(arr[i])
            del(arr[i])
    return arr

test1 = [1, 0, 2, 0, 3, 0]
test2 = [0,0,2,2,0,3]
test3 = [0,0,1]

print(z_nz(test3))
