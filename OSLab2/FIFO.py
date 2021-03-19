from queue import Queue


def fifo(pages, fault):
    s = set()
    q = Queue()

    for i in pages:

        if(len(s) < capacity):

            if(i not in s):
                s.add(i)
                q.put(i)
                fault += 1
        else:

            if(i not in s):
                value = q.queue[0]
                q.get(value)
                s.remove(value)

                s.add(i)
                q.put(i)
                fault += 1

    return fault


pages = [7, 0, 1, 2, 0, 3, 0,
         4, 2, 3, 0, 3, 2]
# pages = [7, 5, 0, 1, 2, 4, 0, 3, 0, 2, 1]

fault = 0
capacity = 4

print("Page fault for FIFO : " + str(fifo(pages, fault)))
