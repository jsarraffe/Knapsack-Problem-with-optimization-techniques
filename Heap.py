class MaxHeap:
    def __init__(self, heap, n):
        self.H = heap

        self.n = n
        self.basicOperation = 0


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
            self.basicOperation += 1
            if j < self.n:
                if self.H[j].bangForBuckRatio < self.H[j + 1].bangForBuckRatio:
                    j = j + 1
            if v.bangForBuckRatio >= self.H[j].bangForBuckRatio:
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

            self.basicOperation += 1
            while heap != True and 2 * k <= self.n:
                j = 2 * k
                # siftdown
                self.basicOperation += 1
                if j < self.n:
                    if self.H[j].bangForBuckRatio < self.H[j+1].bangForBuckRatio:
                        j = j + 1
                if v.bangForBuckRatio >= self.H[j].bangForBuckRatio:
                        heap = True
                else:
                    self.H[k] = self.H[j]
                    k = j
            self.H[k] = v