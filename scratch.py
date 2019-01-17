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