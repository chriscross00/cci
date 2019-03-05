# https://interactivepython.org/courselib/static/pythonds/Trees/BinaryHeapImplementation.html#fig-percdown
class bin_heap:

    def __init__(self):
        self.heap = [0]
        self.size = 0

    def bubble_up(self, i):
        while i//2 > 0:
            if self.heap[i] < self.heap[i//2]:
                self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i//2

    def insert(self, k):
        self.heap.append(k)
        self.size += 1
        self.bubble_up(self.size)

    def bubble_down(self, i):
        while (i * 2) <= self.size:
            mc = self.min_child(i)
            # Compares current node to min child node
            if self.heap[i] > self.heap[mc]:
                self.heap[i], self.heap[mc] = self.heap[mc], self.heap[i]
            i = mc
    # Because the children unordered we have to determine the smallest child
    #  for each node.
    def min_child(self, i):
        # Keeps the pointers within the bounds of the tree
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            # If left < right
            if self.heap[i*2] < self.heap[i*2+1]:
                return i * 2
            # If left > right
            else:
                return i * 2 + 1

    def del_min(self):
        # Sets up the value we want returned
        min = self.heap[1]
        # Changes the pointer of position 1 to the last element of the heap
        self.heap[1] = self.heap[self.size]
        # Decreases the size of the heap, removing the pointer to the last
        # element
        self.size -= 1
        # removes the min element of the heap
        self.heap.pop()
        # Moves the first element down to its proper position
        self.bubble_down(1)
        return min

    def build_heap(self, list):
        i = len(list)//2
        self.size = len(list)
        self.heap = [0] + list[:]
        while (i>0):
            self.bubble_down(i)
            i -= 1


test = [9, 5, 6, 2, 3]

bh = bin_heap()
bh.build_heap(test)

print(bh.del_min())
print(bh.del_min())
print(bh.del_min())
print(bh.del_min())
print(bh.del_min())