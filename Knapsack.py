

class KnapSack:
    def __init__(self, capacity, values):
        self.capacity = capacity
        self.values = values

        self.basicOperation1A = 0
        self.basicOperation1B = 0

        self.oneAtable = [[0 for j in range(capacity[0] + 1)] for i in range(1, len(values) + 1)]
        self.oneBTable = [[0 for j in range(capacity[0] + 1)] for i in range(1, len(values) + 1)]
        for i in range(1, len(self.oneBTable)):
            for j in range(1, len(self.oneAtable[0])):
                self.oneBTable[i][j] = -1
