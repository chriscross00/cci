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



b = [1,2,3,4,5,6]

# stack -LIFO
class Stack():

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items) -1]

    def size(self):
        return len(self.items)


def merge_sort(list):

    if len(list) > 1:
        mid = len(list)//2
        L_list = list[:mid]
        R_list = list[mid:]

        merge_sort(L_list)
        merge_sort(R_list)
        merge(L_list, R_list, list)
    return list


def merge(L_list, R_list, list):

    x = y = z = 0

    while x < len(L_list) and y < len(R_list):
        if L_list[x] < R_list[y]:
            list[z] = L_list[x]
            z += 1
            x += 1
        else:
            list[z] = R_list[y]
            z += 1
            y += 1
    while x < len(L_list):
        list[z] = L_list[x]
        z += 1
        x += 1
    while y < len(R_list):
        list[z] = R_list[y]
        z += 1
        y += 1
    return list

print(merge_sort(test2))
