import math
from decimal import Decimal
class HshTable:
    def __init__(self, n, W):
        self.n = n
        self.W = W
        self.k = int((((self.W + 1)* n) *0.677))
        self.table = [None] * int(self.k)
        self.basicOperation = 0
        self.freespace = self.k


#2021626
    def hash(self, i, j):
        Ri = '1' + format(i, "b").zfill(int(math.log2(self.n + 1)))
        Rj = format(j, "b").zfill(int(math.log2(self.W + 1)))
        hashIndex = int(Ri + Rj) % self.k
        return hashIndex

    def insert(self, Node):
        index = int(self.hash(Node.i, Node.j))

        node = self.table[index]
        self.basicOperation += 1
        if node == None:
            self.freespace -= 1
            self.table[index] = Node
            return
        prev = node

        self.basicOperation += 1
        while node is not None:
            self.basicOperation += 1
            prev = node
            node = node.next
        prev.next = Node



    def find(self, i, j):


        if i <= 0:
            return 0
        index = int(self.hash(i, j))
        node = self.table[index]

        self.basicOperation += 1
        while node is not None and (node.i != i or node.j != j):
            self.basicOperation += 1
            node = node.next


        self.basicOperation += 1
        if node is None:
            return None
        else:
            return node.v

class Node:
    def __init__(self, i, j, v):
        self.i = i
        self.j = j
        self.v = v
        self.next = None
