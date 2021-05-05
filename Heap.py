class MaxHeap:
    def __init__(self, heap, size, n):
        self.heap = heap
        self.size = size
        self.n = n
        #how man elements after deleting
        # self.n = self.n

    def deleteMax(self):
        self.heap[1] = self.heap[self.n]
        self.heap[self.n] = -1
        self.n -= 1
        k = 1
        v = self.heap[k]
        heap = False
        while heap != True and 2 * k <= self.n:
            j = 2 * k
            if j < self.n:
                if self.heap[j] < self.heap[j + 1]:
                    j = j + 1
            if v >= self.heap[j]:
                self.heap = True
            else:
                self.heap[k] = self.heap[j]
                k = j
        self.heap[j] = v

    def heapification(self):
        self.heap.insert(0,0)
        for i in range(int(self.n/2), 0, -1):
            k = i
            v = self.heap[k]
            heap = False
            while heap != True and 2 * k <= self.n:
                j = 2 * k
                if j < self.n:
                    if self.heap[j] < self.heap[j+1]:
                        j = j + 1
                if v >= self.heap[j]:
                        self.heap = True
                else:
                    self.heap[k] = self.heap[j]
                    k = j
            self.heap[j] = v


