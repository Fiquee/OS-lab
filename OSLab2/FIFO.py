from queue import Queue


def fifo(pages, capacity):
    fault = 0
    q = Queue()

    for i in pages:
        print("Page", i, "has been requested")
        if(q.qsize() < capacity):
            print("Main memory not full yet")
            if(i not in q.queue):
                print("Page", i, "not exist in main memory, PAGE FAULT OCCUR")
                q.put(i)
                fault += 1
                print("Page", i, "received from secondary memory")
                print("Main memory", list(q.queue))
            else:
                print("Page", i, " exist in Main memory, HIT")
                print("Main memory", list(q.queue))
        else:
            print("Main memory already full in capacity")
            if(i not in q.queue):
                value = q.get()
                print("Removing page", value, "from Main memory")

                print("Page", i, "not exist in main memory, PAGE FAULT OCCUR")
                print("Insert page", i, "into Main memory")
                q.put(i)
                print("Page", i, "received from secondary memory")
                print("Main memory", list(q.queue))
                fault += 1
            else:
                print("Page", i, " exist in Main memory, HIT")
                print("Main memory", list(q.queue))
        print()

    return fault


# pages = [7, 0, 1, 2, 0, 3, 0,
#          4, 2, 3, 0, 3, 2]

pages = [1, 2, 3, 4, 1]

capacity = 3

print("Page fault for FIFO : " + str(fifo(pages, capacity)))
