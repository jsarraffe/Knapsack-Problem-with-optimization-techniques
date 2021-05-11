import matplotlib.pyplot as plt

import time
from HashTable import HshTable
from Greedy import SackNode
from HashTable import Node
import sys
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


x = int(sys.argv[1])


def readAndPopulateGlobalVariablesu():
    readFile('p' + '%0.2d' % int(sys.argv[1]) + '_c.txt', capacity)
    readFile('p' + '%0.2d' % int(sys.argv[1]) + '_v.txt', values)
    readFile('p' + '%0.2d' % int(sys.argv[1]) + '_w.txt', weights)
# ---------------------------------------------------------------------------------------

readAndPopulateGlobalVariablesu()
oneAtable = [[0 for j in range(capacity[0] + 1)] for i in range(1, len(values) + 1)]
oneBTable = [[0 for j in range(capacity[0] + 1)] for i in range(1, len(values) + 1)]

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
    basicOperation1b += 1
    if oneBTable[i][j] < 0:
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

for j in range(capacity[0]):
    hash.insert(Node(0,j,0))
for i in range(len(values)):
    hash.insert(Node(i,0,0))

def MFKnapsackHASH(i, j):
    global basicOperation1c
    global hash
    global spaceTaken

    basicOperation1c += 1
    tmp = hash.find(i,j)
    if tmp == None:
        if j < weights[i]:
            value = MFKnapsackHASH(i - 1, j)
        else:
            value = max(MFKnapsackHASH(i - 1, j),values[i] + MFKnapsackHASH(i - 1, j - weights[i]))
        hash.insert(Node(i, j, value))
        spaceTaken += 1
    return hash.find(i, j)
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
        if hash.find(i - 1, j) < hash.find(i, j):
            knapVal += values[i]
            answer.append(i)
            j = j - weights[i]
            i -= 1
        else:
            i -= 1
    result = answer[::-1]

    nonUsedNodes = 0
    return result, knapVal, basicOperation1c + hash.basicOperation, spaceTaken


# Paremeter gnskVals : greetyKnapSackValues
def mergesort(gnskVals):
    global basicOp2A

    basicOp2A += 1
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
        basicOp2A += 1
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
basicOp2A = 0
# --------------------------------------------------------
def grdyNAPSK():
    #for heap based
    global sackValues
    global basicOp2A

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
        basicOp2A += 1
        if currCapcity + greedyKnapSackValues[i].weight < capacity[0]:
            answer.append(greedyKnapSackValues[i].itemNum)
            currCapcity += greedyKnapSackValues[i].weight
            knapVal += greedyKnapSackValues[i].value
        else:
            answer.sort()
            break
    return answer, knapVal, basicOp2A



def printContributers(twoA):
    ans = ""
    for i in range(len(twoA)):
        if (i < len(twoA) - 1):
            ans += str(twoA[i]) + ", "
        else:
            ans += str(twoA[i]) + ""
    return " {" + ans + "}"





#------------------global values ----------------------------
    basicOp2B = 0
def greedKnapsackMaxheap():
    global basicOp2B
    global sackValues
    greedNodes = sackValues.copy()
    answer = []
    mH = MaxHeap(greedNodes, len(greedNodes))
    mH.heapification()
    currCap = 0
    knapVal = 0
    for i in range(1, len(greedNodes)):
        if currCap +  mH.H[1].weight < capacity[0]:
            answer.append(mH.H[1].itemNum)
            currCap += mH.H[1].weight
            knapVal += mH.H[1].value
            mH.deleteMax()

    answer.sort()
    return answer, knapVal + mH.basicOperation










def main():
    print(sys.argv[1])

    oneC, oneCVal, basicOp1C, oneCSpace = oneCKnapSack()
    startA = time.time()
    oneA, oneAVal, basicOp1A = knapsack()
    startB = time.time()
    oneB, oneBVal, basicOp1B = oneBKnapSack()

    print("Knapsack Capcity = " + str(capacity[0]) + ". Total number of items = " + str(len(values) - 1))
    print("")

    # print("TIME TO COMPILE  A: " + str(endA - startA) + ' SECONDS')
    # print("---------------------------------------------------------------------")
    print("")
    print(" (1a) Traditional Dynamic Programming Optimal value: " + str(oneAVal))
    print(" (1a) Traditional Dynamic Programming Optimal subset: {" + str(oneA)[1:-1] + "}")
    print(" (1a) Traditional Dynamic Programming Total Basic Ops: " + str(basicOp1A))

    # print("")
    #
    # print("TIME TO COMPILE  B: " + str(endB - startB)+ ' SECONDS')
    print("")
    print(" (1b) Memory-function Dynamic Programming Optimal value: " + str(oneBVal))
    print(" (1b) Memory-function Dynamic Programming Optimal subset: {" + str(oneB)[1:-1] + "}")
    print(" (1b) Memory-function Dynamic Programming Total Basic Ops: " + str(basicOp1B))

    # print("")
    # print("TIME TO COMPILE  C: " + str(endC - startC)+ ' SECONDS')
    print("")
    print(" (1c) Traditional Dynamic Programming Optimal value: " + str(oneCVal))
    print(" (1c) Traditional Dynamic Programming Optimal subset: {" + str(oneC)[1:-1] + "}")
    print(" (1c) Traditional Dynamic Programming Total Basic Ops: " + str(basicOp1C))
    print(" (1c) Space-efficient Dynamic Programming Space Taken: " + str(oneCSpace) + "  keys ")

    print("")

    twoA, knapVal2A, basicOp2A = grdyNAPSK()
    twoB, knapVal2B = greedKnapsackMaxheap()

    print(" (2a) Greedy Approach Optimal value: " + str(knapVal2A))
    print(" (2a) Greedy Approach Optimal value:" + printContributers(twoA))
    print(" (2a) Greedy Approach Total Basic Ops: " + str(basicOp2A))

    print(" ")

    print(" (2b) Heap-based Greedy Approach Optimal value: " + str(knapVal2A))
    print(" (2b) Heap-based Greedy Approach Optimal subset:" + printContributers(twoB))
    print(" (2b) Heap-based Greedy Approach Total Basic Ops: " + str(knapVal2B))


if __name__ == "__main__":
    main()

