def bestFit(block, job_size, x, y):

    index = [-1] * y

    for i in range(y):
        bestIndex = -1
        for j in range(x):

            if(block[j] >= job_size[i]):
                if(bestIndex == -1):
                    bestIndex = j
                elif(block[bestIndex] > block[j]):
                    bestIndex = j

        if(bestIndex != -1):
            index[i] = bestIndex
            block[bestIndex] *= -1  # busy
            # block[bestIndex] -= job_size[i]

    print("Jobnumb\t" + "Job size\t" + " block allocated(index)")

    for i in range(y):
        if(index[i] != -1):
            print(str(i+1) + "\t" +
                  str(job_size[i]) + "\t\t\t" + str(index[i]))
        else:
            print(str(i+1) + "\t" +
                  str(job_size[i]) + "\t\t\t" + "not allocated")


block = [300, 500, 400, 563, 433]
job_size = [320, 150, 650, 127, 520]

x = len(block)
y = len(job_size)

bestFit(block, job_size, x, y)
