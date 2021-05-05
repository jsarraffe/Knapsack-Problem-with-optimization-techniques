import matplotlib.pyplot as plt

import time

from HashTable import HshTable

from Greedy import SackNode
from HashTable import Node

from Heap import MaxHeap


# plt.plot([1,2,3,4])
# plt.ylabel('some numbers')
# plt.show()

def readFile(filename, array):
    file = open("./KnapsackTestData/" + filename, "r")
    temp = []
    for line in file:
        temp.append(line)
    for x in temp:
        array.append(int(x.strip().replace("\n", '')))


# ------------------------------------GLOBAL VARIABLES----------------------------------
capacity = []
values = [0]
weights = [0]

readFile('p00_c.txt', capacity)
readFile('p00_v.txt', values)
readFile('p00_w.txt', weights)

oneAtable = [[0 for j in range(capacity[0] + 1)] for i in range(1, len(values) + 1)]
oneBTable = [[0 for j in range(capacity[0] + 1)] for i in range(1, len(values) + 1)]
# ---------------------------------------------------------------------------------------

# initilize table, except row 0, column 0
for i in range(1, len(oneBTable)):
    for j in range(1, len(oneAtable[0])):
        oneBTable[i][j] = -1


def knapsack():
    # fill table
    global values
    global oneAtable
    global capacity
    basicOperation1A = 0
    for i in range(1, len(values)):
        for j in range(1, capacity[0] + 1):
            basicOperation1A += 1
            if j - weights[i] < 0:
                oneAtable[i][j] = oneAtable[i - 1][j]
            else:
                oneAtable[i][j] = max(oneAtable[i - 1][j], values[i] + oneAtable[i - 1][j - weights[i]])
    # back trace
    i = len(values) - 1
    j = len(oneAtable[0]) - 1
    knapVal = 0
    answer = []
    while i > 0:
        basicOperation1A += 1
        if oneAtable[i - 1][j] < oneAtable[i][j]:
            knapVal += values[i]
            answer.append(i)
            j = j - weights[i]
            i -= 1
        else:
            i -= 1
    result = answer[::-1]
    return result, knapVal, basicOperation1A


# ------------------------------------GLOBAL VARIABLES----------------------------------

basicOperation1b = 0


# --------------------------------------------------------------------------------------
def MFKnapsack(i, j):
    global basicOperation1b
    global oneBTable

    if oneBTable[i][j] < 0:
        basicOperation1b += 1
        if j < weights[i]:
            value = MFKnapsack(i - 1, j)
        else:
            value = max(MFKnapsack(i - 1, j), values[i] + MFKnapsack(i - 1, j - weights[i]))
        oneBTable[i][j] = value
    return oneBTable[i][j]


def oneBKnapSack():
    global basicOperation1b

    i = len(values) - 1
    j = capacity[0]
    # memory function
    MFKnapsack(i, j)
    # back trace
    i = len(values) - 1
    j = len(oneBTable[0]) - 1
    knapVal = 0
    answer = []

    # Back Trace
    while i != 0:
        basicOperation1b += 1
        if oneBTable[i - 1][j] < oneBTable[i][j]:
            knapVal += values[i]
            answer.append(i)
            j = j - weights[i]
            i -= 1
        else:
            i -= 1
    result = answer[::-1]
    return result, knapVal, basicOperation1b


# -------------------------------------Global Variables --------------------------------------

basicOperation1c = 1
spaceTaken = 0
hash = HshTable(len(values) - 1, capacity[0])
val = 0


# --------------------------------------------------------------------------------------------

def MFKnapsackHASH(i, j):
    global basicOperation1c
    global hash
    global spaceTaken
    if i > 0:
        basicOperation1c += 1
        if j < weights[i]:
            value = MFKnapsackHASH(i - 1, j)
        else:
            top = MFKnapsackHASH(i - 1, j)
            inclusive = values[i] + MFKnapsackHASH(i - 1, j - weights[i])
            value = max(top, inclusive)
        hash.insert(Node(i, j, value))
    return hash.find(i, j).v


#


def oneCKnapSack():
    global basicOperation1c
    global hash
    global spaceTaken

    i = len(values) - 1
    j = capacity[0]
    # memory function
    MFKnapsackHASH(i, j)
    # back trace
    knapVal = 0
    answer = []

    # Back Trace
    while i > 0:
        basicOperation1c += 1
        if hash.find(i - 1, j).v < hash.find(i, j).v:
            spaceTaken += 1
            knapVal += values[i]
            answer.append(i)
            j = j - weights[i]
            i -= 1
        else:
            i -= 1
    result = answer[::-1]

    nonUsedNodes = 0
    return result, knapVal, basicOperation1c, (spaceTaken, nonUsedNodes)


startC = time.time()
oneC, oneCVal, basicOp1C, oneCSpace = oneCKnapSack()
endC = time.time()

startA = time.time()
oneA, oneAVal, basicOp1A = knapsack()
endA = time.time()

startB = time.time()
oneB, oneBVal, basicOp1B = oneBKnapSack()
endB = time.time()

print("Knapsack Capcity = " + str(capacity[0]) + ". Total number of items = " + str(len(values) - 1))
print("")

print("TIME TO COMPILE  A: " + str(endA - startA))

print("(1a) Traditional Dynamic Programming Optimal value: " + str(oneAVal))
print("(1a) Traditional Dynamic Programming Optimal subset: {" + str(oneA)[1:-1] + "}")
print("(1a) Traditional Dynamic Programming Total Basic Ops: " + str(basicOp1A))

print("")

print("TIME TO COMPILE  B: " + str(endB - startB))
print("(1b) Traditional Dynamic Programming Optimal value: " + str(oneBVal))
print("(1b) Traditional Dynamic Programming Optimal subset: {" + str(oneB)[1:-1] + "}")
print("(1b) Traditional Dynamic Programming Total Basic Ops: " + str(basicOp1B))

print("")
print("TIME TO COMPILE  C: " + str(endC - startC))
print("(1c) Traditional Dynamic Programming Optimal value: " + str(oneCVal))
print("(1c) Traditional Dynamic Programming Optimal subset: {" + str(oneC)[1:-1] + "}")
print("(1c) Traditional Dynamic Programming Total Basic Ops: " + str(basicOp1C))
print("(1c) Space-efficient Dynamic Programming Space Taken: " + str(oneCSpace[0]) + "  keys and "
      + str(oneCSpace[1]) + " open spaces in hash table")


# Paremeter gnskVals : greetyKnapSackValues
def mergesort(gnskVals):
    if len(gnskVals) < 2:
        return
    mid = len(gnskVals) // 2
    left = gnskVals[:mid]
    right = gnskVals[mid:]
    mergesort(left)
    mergesort(right)
    lSize = len(left)
    rSize = len(right)
    i = 0
    t = 0
    j = 0
    while i < lSize and t < rSize:
        if left[i].bangForBuckRatio <= right[t].bangForBuckRatio:
            gnskVals[j] = left[i]
            i += 1
        else:
            gnskVals[j] = right[t]
            t += 1
        j += 1
    # add rest of array
    while (i < lSize):
        gnskVals[j] = left[i]
        i += 1
        j += 1
    while (t < rSize):
        gnskVals[j] = right[t]
        t += 1
        j += 1


# -------------Greedy Algorithms---------------------------------

sackValues = []


# --------------------------------------------------------
def grdyNAPSK():
    global sackValues
    greedyKnapSackValues = []
    for i in range(1, len(weights)):
        newNode = SackNode(values[i], weights[i], i, values[i] / weights[i])
        greedyKnapSackValues.append(newNode)

    # save for heep based
    sackValues = greedyKnapSackValues.copy()
    mergesort(greedyKnapSackValues)
    greedyKnapSackValues = greedyKnapSackValues[::-1]

    answer = []
    currCapcity = 0
    knapVal = 0
    for i in range(len(greedyKnapSackValues)):
        if currCapcity + greedyKnapSackValues[i].weight < capacity[0]:
            answer.append(greedyKnapSackValues[i].itemNum)
            currCapcity += greedyKnapSackValues[i].weight
            knapVal += greedyKnapSackValues[i].value
        else:
            answer.sort()
            break
    return answer, knapVal


twoA, knapVal2A = grdyNAPSK()


def print2AContributers():
    global twoA
    ans = ""
    for i in range(len(twoA)):
        if (i < len(twoA) - 1):
            ans += str(twoA[i]) + ", "
        else:
            ans += str(twoA[i]) + ""
    return " {" + ans + "}"


def sift(sackNode):
    print("sackNOde")


def heapify(sackValues):
    print("arsehole")


def greedyHeap():
    global sackValues

    '''

       1: heapify
       2: delete max, the sift down,  switch with the last node in array, then delete last node, then sift

    '''


print(" ")

greedyHeap()
print("(2a) Greedy Approach Optimal value: " + str(knapVal2A))
print("(2a) Greedy Approach Optimal value:" + print2AContributers())

print('')

# array = [7.0, 3.0, 9.0, 12.0, 6.0, 31.0, 2.0]


nodesToDeleteFrom = {}
heap = []
for i in sackValues:
    heap.append(round((i.bangForBuckRatio),2))
    n = {i.bangForBuckRatio : i}
    nodesToDeleteFrom.update(n)

print(heap)
array = heap

greedNodes = sackValues.copy()

mH = MaxHeap(array, len(array))
mH.heapification()


print(array)


#
# print(array)
