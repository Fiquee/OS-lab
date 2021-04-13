'''
Shortest Job First
Your program receives as input the number of jobs waiting in queue
and the time required to execute each job. 
Display the outcome of each scheduling algorithm.
INDEXES
0 - Job number
1 - Burst time
2 - Arrival time
3 - Completion Time
4 - Waiting time = Turnaround time - Burst time
5 - Turnaround time = Completion time - Arrival time 
'''


def print_times(job_list):
    print("JN      BT      AT      CT      WT      TAT")
    for i in range(len(job_list[0])):
        for j in range(0, 6):
            print(job_list[j][i], end="\t")
        print()
    print()


def swap(job_list, i, j):
    
    for idx in range(0, 6):
        job_list[idx][i], job_list[idx][j] = job_list[idx][j], job_list[idx][i]
        print("Swap",job_list[idx][i],"with",job_list[idx][j])


def sort_times(job_list):
    for i in range(len(job_list[0])):
        for j in range(i):
            if job_list[1][i] < job_list[1][j]:
                swap(job_list, i, j)
    print("Ordered According to Burst Times")            
    print_times(job_list)
    for i in range(len(job_list[0])):
        for j in range(i):
            if job_list[2][i] < job_list[2][j]:
                swap(job_list, i, j)
    print("Ordered According to Arrival Times")            
    print_times(job_list)
    


def calculate_times(job_list):
    temp_job = -1
    # Calculate for first job
    # Completion Time = Arrival Time + Burst Time
    job_list[3][0] = job_list[2][0] + job_list[1][0]
    # Turnaround Time = Completion Time - Arrival Time
    job_list[5][0] = job_list[3][0] - job_list[2][0]
    # Waiting Time = Turnaround Time - Burst Time
    job_list[4][0] = job_list[5][0] - job_list[1][0]
    
    print("First CT:",job_list[3][0],"First TAT:",job_list[5][0],"First WT",job_list[4][0])
    
    for i in range(1, len(job_list[0])):
        previous_completion_time = job_list[3][i-1]
        current_shortest_burst = job_list[1][i]

        for j in range(i, len(job_list[0])):
            if previous_completion_time >= job_list[2][j] and job_list[1][j] <= current_shortest_burst:
                current_shortest_burst = job_list[1][j]
                temp_job = j

        # Completion Time = Arrival Time + Burst Time
        job_list[3][temp_job] = previous_completion_time + job_list[1][temp_job]
        # Turnaround Time = Completion Time - Arrival Time
        job_list[5][temp_job] = job_list[3][temp_job] - job_list[2][temp_job]
        # Waiting Time = Turnaround Time - Burst Time
        job_list[4][temp_job] = job_list[5][temp_job] - job_list[1][temp_job]
        
        print(temp_job,"|CT:",job_list[3][temp_job],"TAT:",job_list[5][temp_job],"WT",job_list[4][temp_job])
        # Swap in case the job has arrived and has a shorter burst time
        swap(job_list, temp_job, i)


def shortest_job_first(job_list):
    sort_times(job_list)
    calculate_times(job_list)



job_number = 4
job_list = [[0 for j in range(job_number)] #Create array of [[],[],[],[]]
            for i in range(6)]                 
job_list[0] = [i for i in range(1, job_number + 1)] #job number

job_list[1] = [9, 5, 3, 5] #Burst time

job_list[2] = [2,2,0,6] #Arrival time
print("Original Input")
print_times(job_list)

shortest_job_first(job_list)

print("Final Result")
print_times(job_list)
print("Average Turnaround Time:",sum(job_list[5])/job_number,end="s\n")
print("Average Waiting Time:",sum(job_list[4])/job_number,end="s")