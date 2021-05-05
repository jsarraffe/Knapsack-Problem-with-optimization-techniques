class MaxHeap:
    def __init__(self, heap, n):
        self.H = heap

        self.n = n
        #how man elements after deleting
        # self.n = self.n

    def deleteMax(self):
        self.H[1] = self.H[self.n]
        self.H[self.n] = -1
        self.n -= 1
        k = 1
        v = self.H[k]
        heap = False
        while heap != True and 2 * k <= self.n:
            j = 2 * k
            #siftdown
            if j < self.n:
                if self.H[j] < self.H[j + 1]:
                    j = j + 1
            if v >= self.H[j]:
                heap = True
            else:
                self.H[k] = self.H[j]
                k = j
        self.H[k] = v

    def heapification(self):
        self.H.insert(0,0)
        for i in range(int(self.n/2), 0, -1):
            k = i
            v = self.H[k]
            heap = False
            while heap != True and 2 * k <= self.n:
                j = 2 * k
                # siftdown
                if j < self.n:
                    if self.H[j] < self.H[j+1]:
                        j = j + 1
                if v >= self.H[j]:
                        heap = True
                else:
                    self.H[k] = self.H[j]
                    k = j
            self.H[k] = v