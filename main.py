import matplotlib.pyplot as plt
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
    c = 'p' + '%0.2d' % int(sys.argv[1]) + '_c.txt'
    v = 'p' + '%0.2d' % int(sys.argv[1]) + '_v.txt'
    w = 'p' + '%0.2d' % int(sys.argv[1]) + '_w.txt'

    readFile(c, capacity)
    readFile(v, values)
    readFile(w, weights)

    print("File containing the capacity, weights, and values are: " + c + ", " + w + ", and " + v)
    print("")
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
    # tmp = hash.find(i,j)
    if hash.find(i,j) == None:
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
    return result, knapVal, basicOperation1c + hash.basicOperation, (spaceTaken, hash.freespace)


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
    #MERGE
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

def greedKnapsackMaxheap():
    basicOp2B = 0
    global sackValues
    greedNodes = sackValues.copy()
    answer = []
    mH = MaxHeap(greedNodes, len(greedNodes))
    mH.heapification()
    currCap = 0
    knapVal = 0
    for i in range(1, len(greedNodes)):
        basicOp2B += 1
        if currCap +  mH.H[1].weight < capacity[0]:
            answer.append(mH.H[1].itemNum)
            currCap += mH.H[1].weight
            knapVal += mH.H[1].value
            mH.deleteMax()

    answer.sort()
    mH.basicOperation += basicOp2B
    return answer, knapVal, mH.basicOperation + basicOp2B


def graphs():
    caseID = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    report1A = [24, 1660, 135, 1146, 357, 840, 1197, 11265, 153700344]
    report1B = [26, 310, 49, 89, 168, 281, 147, 6130, 13029236]
    report1C = [140, 1681, 632,1080, 950, 1453, 1476, 34228, 64534672]

    report1BSpaceTaken = [25,1815,156, 1330,400,936,1360,12000, 160104500]
    space1C = [13,994,100, 714,216,507,783,7596,98502025]
    report2A = [15, 43, 20, 23, 27, 30, 29, 76, 146]
    report2B = [15, 39, 16, 21, 23, 28, 25, 64, 122]


    fig1A = plt.figure()
    superscript = str.maketrans("2", "²")


    fig1A .suptitle('(Traditional) vs (Memory-function)', fontsize=15)


    plt.scatter(caseID, report1A, s=80)
    # plt.scatter(caseID, report1A, s=112, alpha = 0)
    plt.plot(caseID, report1B, "ro")
    plt.xlabel('CaseID', fontsize=18)
    plt.ylabel('# of basic operations', fontsize=16)
    plt.legend(["Task 1B: Memory-function", "Task 1A: Traditional"])
    plt.xlabel('CaseID', fontsize=18)

    plt.show()



    fig1CExtraCredit = plt.figure()
    plt.plot(space1C, report1C, "ro")
    plt.scatter(report1BSpaceTaken, report1B, s=70)
    fig1CExtraCredit.suptitle('(Space-efficient) vs (Memory-function)', fontsize=12)
    plt.xlabel('space', fontsize=18)
    plt.ylabel('# of basic operations', fontsize=16)
    plt.legend([ "Task1C: Space-efficient", "Task1B: Memory-function"])

    plt.show()


    fig2A = plt.figure()
    plt.scatter(caseID, report2B, s=50)
    plt.plot(caseID, report2A, "ro")
    fig2A.suptitle('Greedy approach (Sorting) vs (Max-heap)', fontsize=15)
    plt.xlabel('CaseID', fontsize=18)
    plt.ylabel('# of basic operations', fontsize=16)
    plt.legend(["Task 2A: Sorting", "Task 2B: Max-heap"])
    plt.show()









def main():


    # graphs()


    oneC, oneCVal, basicOp1C, oneCSpace = oneCKnapSack()
    oneA, oneAVal, basicOp1A = knapsack()
    oneB, oneBVal, basicOp1B = oneBKnapSack()

    print("Knapsack Capcity = " + str(capacity[0]) + ". Total number of items = " + str(len(values) - 1))

    #
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

    # # print("TIME TO COMPILE  C: " + str(endC - startC)+ ' SECONDS')
    print("")
    print(" (1c) Space-efficient Dynamic Programming Optimal value:  " + str(oneCVal))
    print(" (1c) Space-efficient Dynamic Programming Optimal subset: {" + str(oneC)[1:-1] + "}")
    print(" (1c) Space-efficient Dynamic Programming Total Basic Ops: " + str(basicOp1C))
    print(" (1c) Space-efficient Dynamic Programming Space Taken: " + str(oneCSpace[0]) + "  keys " + str(oneCSpace[1]) + " free spaces in hash array")

    print("")

    #TO SEE TOTAL SAPCE TAKEN UP
    # print("")
    # print("Total Space taken by the Task1B: " + str(len(values) * capacity[0]))
    # print(" A total of " + " 1Cspace taken: " + str(oneCSpace[0] + oneCSpace[1]))
    # print("")



    twoA, knapVal2A, basicOp2A = grdyNAPSK()
    twoB, knapVal2B, bo2B  = greedKnapsackMaxheap()

    print(" (2a) Greedy Approach Optimal value: " + str(knapVal2A))
    print(" (2a) Greedy Approach Optimal subset: " + printContributers(twoA))
    print(" (2a) Greedy Approach Total Basic Ops: " + str(basicOp2A))

    print(" ")

    print(" (2b) Heap-based Greedy Approach Optimal value: " + str(knapVal2B))
    print(" (2b) Heap-based Greedy Approach Optimal subset:" + printContributers(twoB))
    print(" (2b) Heap-based Greedy Approach Total Basic Ops: " + str(bo2B))


if __name__ == "__main__":
    main()

