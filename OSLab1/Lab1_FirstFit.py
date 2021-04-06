def firstFit(block, job_size, x, y):

    index = [-1] * y

    for i in range(y):
        for j in range(x):

            if(block[j] >= job_size[i]):
                index[i] = j
                block[j] *= -1
                break

    print("Jobnumb\t" + "Job size\t" + " block allocated(index)")

    for i in range(y):
        if(index[i] != -1):
            print(str(i+1) + "\t" +
                  str(job_size[i]) + "\t\t\t" + str(index[i]))
        else:
            print(str(i+1) + "\t" +
                  str(job_size[i]) + "\t\t\t" + "not allocated")


block = [300, 500, 400, 563, 433]  # kotak
job_size = [320, 150, 650, 127, 520]  # bola
# block = [222, 100, 400, 700]
# job_size = [60, 75, 175, 275]

x = len(block)
y = len(job_size)

firstFit(block, job_size, x, y)
