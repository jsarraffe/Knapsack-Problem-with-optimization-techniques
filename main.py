import matplotlib.pyplot as plt
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
for i in range(1, len(oneBTable)):
    for j in range(1, len(oneAtable[0])):
        oneBTable[i][j] = -1


def knapsack(values, weights):
    # fill table
    for i in range(1, len(values)):
        for j in range(1, len(oneAtable[i])):
            if j - weights[i] < 0:
                oneAtable[i][j] = oneAtable[i - 1][j]
            else:
                oneAtable[i][j] = max(oneAtable[i - 1][j], values[i] + oneAtable[i - 1][j - weights[i]])

    # for i in ksTable:
    #     print(i)
    # back trace
    i = len(values) - 1
    j = len(oneAtable[0]) - 1
    answer = []
    while i != 0:
        if oneAtable[i - 1][j] < oneAtable[i][j]:
            answer.append(i)
            j = j - weights[i]
            i -= 1
        else:
            i -= 1
    result = answer[::-1]
    return result


def MFKnapsack(i, j):
    if oneBTable[i][j] < 0:
        if j < weights[i]:
            value = MFKnapsack(i - 1, j)
        else:
            value = max(MFKnapsack(i - 1, j), values[i] + MFKnapsack(i - 1, j - weights[i]))
        oneBTable[i][j] = value
    return oneBTable[i][j]


# ------------------------------------GLOBAL VARIABLES----------------------------------
value = 0


# --------------------------------------------------------------------------------------

def oneBKnapSack():
    i = len(values) - 1
    j = capacity[0]

    # memory function
    MFKnapsack(i, j)


    #
    # for i in oneBTable:
    #     print(i)



    # back trace
    i = len(values) - 1
    j = len(oneBTable[0]) - 1
    answer = []
    while i != 0:
        if oneBTable[i - 1][j] < oneBTable[i][j]:
            answer.append(i)
            j = j - weights[i]
            i -= 1
        else:
            i -= 1
    result = answer[::-1]
    return result


# print(knapsack(values, weights, oneAtable))


oneA = knapsack(values, weights)
oneB = oneBKnapSack()

print("Solution to 1A")
print(oneA)

print("Solution to 1B")
print(oneB)
