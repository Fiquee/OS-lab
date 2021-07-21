'''
Write a program to simulate the Banker’s algorithm for the purpose of deadlock avoidance.
Your program receives as input the number of processes in the systems and how many devices each job requires to complete execution.
Your program shows how devices are allocated to each process as it executes and if the system is currently in a safe or unsafe state.
'''


def calculate_needed(n, m, max_resources, allocated_resources):
    needed_resources = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            needed_resources[i][j] = max_resources[i][j] - \
                allocated_resources[i][j]

    return needed_resources


def print_needed(n, m, needed_resources):
    print("Needed Resources")
    A = 65
    for i in range(m):
        print("\t{char}".format(char=chr(A)), end="")
        A += 1
    print()
    for i in range(n):
        print("P{i}".format(i=i), end="\t")
        for j in range(m):
            print(needed_resources[i][j], end='\t')
        print()
    print()


def banker(n, m, max_resources, allocated_resources):
    needed_resources = calculate_needed(
        n, m, max_resources, allocated_resources)

    print_needed(n, m, needed_resources)

    # Available Resources for Unsafe Data
    # available = [0, 0, 2]

    # Available Resources for Safe Data
    available = [1, 5, 2, 0]
    safe_sequence = []

    A = 65
    header = '\t'.join([chr(i) for i in range(A, A+m)])

    flag = [0]*n
    for i in range(n):
        for j in range(n):
            if flag[j] == 0:
                curr_flag = True
                for k in range(m):
                    if needed_resources[j][k] > available[k]:
                        curr_flag = False
                        print(
                            "Process {j} is skipped. Available resources is not enough.".format(j=j))
                        break

                if curr_flag:
                    for k in range(m):
                        available[k] += allocated_resources[j][k]
                    print(
                        "Process {j} is completed. Allocated resources become available.".format(j=j))
                    print("Currently Available Resources:")
                    print(header)
                    print("\t".join(str(i) for i in available))
                    flag[j] = 1
                    safe_sequence.append(j)

    print()
    print("Available Resources After Completion")
    print(header)
    print("\t".join(str(i) for i in available))
    print()

    if sum(flag) == len(flag):
        print("Safe State")
        print("Safe Sequence:")
        for i in safe_sequence:
            print("P{i}".format(i=i), "->", end=" ")
    else:
        print("Unsafe State")
        for i in range(0, len(flag)):
            if flag[i] == 1:
                print("P{i}".format(i=i), "is complete")
            else:
                print("P{i}".format(i=i), "is incomplete")


# Safe Data Test
num_processes = 5
num_devices = 4
max_resources = [[0, 0, 1, 2], [1, 7, 5, 0],
                 [2, 3, 5, 6], [0, 6, 5, 2], [0, 6, 5, 6]]
allocated_resources = [[0, 0, 1, 2], [1, 0, 0, 0],
                       [1, 3, 5, 4], [0, 6, 3, 2], [0, 0, 1, 4]]

# Self-Reminder: Change available array when changing from safe and unsafe data.

# Unsafe Data Test
# num_processes = 3
# num_devices = 3
# max_resources = [[2, 2, 4], [2, 1, 3],
#                  [3, 4, 1]]
# allocated_resources = [[1, 2, 1], [2, 0, 1],
#                        [2, 3, 1]]


banker(num_processes, num_devices, max_resources, allocated_resources)
