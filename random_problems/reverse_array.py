# Reverse an array in place.
# https://www.youtube.com/watch?v=p0VD9Fdlx5A&index=57&list=WL


"""
Approaches:
1) Iterative:
    -Start a at front and back of arr
    -Swap front and back
    -Stop before front > back
    -Return arr

Notes:
    -Slicing does not work because it is ot in place. Instead it creates a
    copy of the array and returns that.
        >Runtime: O(n)
        >Space: n

"""


def reverse(arr):

    if not arr:
        return None
    front, back = 0, len(arr)-1
    while front < back:
        arr[front], arr[back] = arr[back], arr[front]
        front += 1
        back -= 1

    return arr


test1 = [1,2,3,4,5]
test2 = []
test3 = [7,9,11,13]
test4 = [0,1]

print(reverse(test4))
