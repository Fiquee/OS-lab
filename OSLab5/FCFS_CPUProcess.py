def checkTimeArrival(readyQueue, currentTime, process):
    for j in range(currentTime+1):
        for i in range(len(process[0])):
            if(process[0][i] == j):
                readyQueue.append(i)
                process[0][i] = -1
    print("current ready queue:", readyQueue)


def checkReadyQueue(readyQueue, process):
    smallestArrTime = 99999999999999
    bestIdx = 999999999
    for i in range(len(readyQueue)):
        if(process[0][readyQueue[i]] < smallestArrTime):
            smallestArrTime = process[0][readyQueue[i]]
            bestIdx = readyQueue[i]
            popidx = i

    readyQueue.pop(popidx)
    return bestIdx


process = [[2, 0, 2, 3, 4], [2, 1, 3, 5, 4]]  # arrival time & burst time
readyQueue = []
doneQueue = []


currentTime = 0
while(len(doneQueue) != len(process[0])):

    checkTimeArrival(readyQueue, currentTime, process)

    if(len(readyQueue) != 0):
        index = checkReadyQueue(readyQueue, process)
        print("Process", index, "is done")
        doneQueue.append(index)
        currentTime += process[1][index]

    else:
        print("idle")
        currentTime += 1

    print("current time =", currentTime)

print("Done all process at time", currentTime)
