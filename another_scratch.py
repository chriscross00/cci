def binary_search(list, val):
    lo, hi = 0, len(list)-1

    while lo <= hi:
        mid = (lo+hi)//2

        if list[mid] < val:
            lo = mid+1
        elif val < list[mid]:
            hi = mid-1
        else:
            return mid
    return False


test1 = [1, 4, 7, 9, 10, 21, 90]

# print(binary_search(test1, 90))


def bubble_sort(list):
    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

    return list


test2 = [90, 24, 16, 25, 95, 2, 24, 59]

# print(bubble_sort(test2))



b = [1,2,3,4,5,6,7]

def test(list):
    for i in range(-1,2):
        print(i)


test(b)
