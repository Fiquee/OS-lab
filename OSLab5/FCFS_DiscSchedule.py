import random
import time

# test
tracks_size = 200
head = random.randint(0, tracks_size)
travel = 0
path = [93, 176, 42, 148, 27, 14, 180]
print()
starttime = time.time()
print("head start at", head)
for i in path:
    print("from head", head, "to track", i)
    print("head traveled", abs(i-head), "tracks")
    travel += abs(i-head)
    head = i
    print()

print()
endtime = time.time()
totaltime = round((endtime-starttime)*1000, 4)
print("time taken:", totaltime, "ms")
print("avg time:", round((totaltime/len(path)), 4), "ms")
print("total travel:", travel)
