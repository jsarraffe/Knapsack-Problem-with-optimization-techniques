import matplotlib.pyplot as plt

from HashTable import HshTable

from HashTable import Node
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
# print(weights)
# print("\n")
# print(values)
# print("\n")
# print(capacity)
oneAtable = [[0 for j in range(capacity[0] + 1)] for i in range(1, len(values) + 1)]
oneBTable = [[0 for j in range(capacity[0] + 1)] for i in range(1, len(values) + 1)]
# ---------------------------------------------------------------------------------------

# initilize table, except row 0, column 0
for i in range(1, len(oneBTable)):
    for j in range(1, len(oneAtable[0])):
        oneBTable[i][j] = -1


def knapsack(values, weights):
    # fill table
    basicOperation1A = 0
    for i in range(1, len(values)):
        for j in range(1, len(oneAtable[i])):
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
    while i != 0:
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

basicOperation1c = 0
hash = HshTable(len(values)-1, capacity[0])
val = 0
# --------------------------------------------------------------------------------------------

def MFKnapsackHASH(i, j):
    global basicOperation1c
    global hash

    if  i  > 0:
        if j < weights[i]:
            val = MFKnapsackHASH(i - 1, j)
        else:
            val = max(MFKnapsackHASH(i - 1, j), values[i] + MFKnapsackHASH(i - 1, j - weights[i]))
        hash.insert(Node(i, j, val))
    return hash.find(i, j)



i = len(values) - 1
j = capacity[0]
# memory function
MFKnapsackHASH(i, j)

print(hash.find(4,5))

print("asshole")












oneA, oneAVal, basicOp1A = knapsack(values, weights)
oneB, oneBVal, basicOp1B = oneBKnapSack()

print("Knapsack Capcity = " + str(capacity[0]) + ". Total number of items = " + str(len(values) - 1))

print("(1a) Traditional Dynamic Programming Optimal value: " + str(oneAVal))
print("(1a) Traditional Dynamic Programming Optimal subset: {" + str(oneA)[1:-1] + "}")
print("(1a) Traditional Dynamic Programming Total Basic Ops: " + str(basicOp1A))

print("")

print("(1b) Traditional Dynamic Programming Optimal value: " + str(oneBVal))
print("(1b) Traditional Dynamic Programming Optimal subset: {" + str(oneB)[1:-1] + "}")
print("(1b) Traditional Dynamic Programming Total Basic Ops: " + str(basicOp1B))





print("you made it here you are safe")