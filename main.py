def readFile(filename, array):
    file = open("./KnapsackTestData/" + filename, "r")
    temp = []
    for line in file:
        temp.append(line)
    for x in temp:
        array.append(int(x.strip().replace("\n", '')))

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
for i in range(1, len(oneBTable)):
    for j in range(1, len(oneAtable[0])):
        oneBTable[i][j] = -1







def knapsack(values, weights, ksTable):
    # fill table
    for i in range(1, len(values)):
        for j in range(1, len(ksTable[i])):
            if j - weights[i] < 0:
                ksTable[i][j] = ksTable[i - 1][j]
            else:
                ksTable[i][j] = max(ksTable[i - 1][j], values[i] + ksTable[i - 1][j - weights[i]])
    for i in ksTable:
        print(i)
    # back trace
    i = len(values) - 1
    j = len(ksTable[0]) - 1
    answer = []
    while i != 0:
        if ksTable[i - 1][j] < ksTable[i][j]:
            answer.append(i)
            j = j - weights[i]
            i -= 1
        else:
            i -= 1
    result = answer[::-1]
    return result

def MFKnapsack(i,j):
    return 1

print(knapsack(values, weights, oneAtable))

