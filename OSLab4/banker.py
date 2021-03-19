def findneeded(processIndex, maximum, allocation, needed):
    k = len(maximum[processIndex])
    for i in range(0, k):
        value = maximum[processIndex][i] - allocation[processIndex][i]
        needed[processIndex][i] = value


def compare(available, needed, allocation, index):
    for i in range(len(allocation[index])):
        if(needed[index][i] > available[i]):
            return False
    return True


def addAvailable(available, allocation, index):
    for i in range(len(available)):
        available[i] += allocation[index][i]


def banker(maximum, allocation, needed, available):
    index = 0
    process = []
    while(len(process) < len(maximum)):
        if(index >= len(maximum)):
            index = 0
            while(index in process):
                index += 1
        if(compare(available, needed, allocation, index)):
            addAvailable(available, allocation, index)
            process.append(index)
        index += 1
    print("The safe sequence is :")
    for i in range(len(process)):
        print("P" + str(process[i]), end=" --> ")


maximum = [[0, 0, 1, 2], [1, 7, 5, 0], [2, 3, 5, 6],
           [0, 6, 5, 2], [0, 6, 5, 6]]

allocation = [[0, 0, 1, 2], [1, 0, 0, 0], [1, 3, 5, 4],
              [0, 6, 3, 2], [0, 0, 1, 4]]

#needed = max - allocation
needed = [[0]*len(maximum[0]) for i in range(len(maximum))]

# if needed <= available then available + allocation = new available
available = [1, 5, 2, 0]

for i in range(0, len(allocation)):
    findneeded(i, maximum, allocation, needed)

banker(maximum, allocation, needed, available)
