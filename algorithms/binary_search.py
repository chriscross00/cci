def binary_search(list, val):
    lo, hi = 0, len(list)-1

    while lo <= hi:
        mid = (lo+hi)//2

        if list[mid] < val:
            lo = mid + 1
        elif val < list[mid]:
            hi = mid - 1
        else:
            return mid

    return False

test1 = [2,6,12,19,20,24,26,29,30]

print(binary_search(test1, 20))