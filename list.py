#array left rotation

#I'm thinking we append the left-most element to the end and append the
# element. I'll need a temp variable to store the left-most element.



a = [1,2,3,4,5]
d = 4

def left_rotate(array, rotations):
    i = 0
    while i != rotations:
        temp = array.pop(0)
        array = array.append(temp)
        i += 1

left_rotate(a, d)


a = [1,2,3]
d =

def test(a, k):
    return a[k:] + a[:k]

test(a,d)