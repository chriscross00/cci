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



def bs(list, val):

    lo, hi = 0, len(list)-1

    while lo <= hi:
        mid = (lo+hi)//2
        if list[mid] < val:
            lo = mid + 1
        elif val < list[mid]:
            hi = mid -1
        else:
            return True
    return False


class Stack():

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size (self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

kol = Stack()

kol.push('fire')
kol.push('small')

print(kol.peek())
print(kol.is_empty())

