import math
from decimal import Decimal
class HshTable:
    def __init__(self, n, W):
        self.n = n
        self.W = W
        self.k = int((((self.W + 1)/2) * n/2))
        self.table = [None] * int(self.k)


#2021626
    def hash(self, i, j):
        Ri = '1' + format(i, "b").zfill(int(math.log2(self.n + 1)))
        Rj = format(j, "b").zfill(int(math.log2(self.W + 1)))
        hashIndex = int(Ri + Rj) % self.k
        return hashIndex

    def insert(self, Node):
        index = int(self.hash(Node.i, Node.j))
        node = self.table[index]
        if node == None:
            self.table[index] = Node
            return
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node

    def find(self, i, j):
        index = int(self.hash(i, j))



        node = self.table[index]
        while node is not None and (node.i != i or node.j != j):
            node = node.next
        if node is None:
            return Node(0,0,0)
        else:
            return node

class Node:
    def __init__(self, i, j, v):
        self.i = i
        self.j = j
        self.v = v
        self.next = None
        self.isIn = False

