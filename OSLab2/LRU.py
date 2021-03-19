def LRU(pages, fault, capacity):

    fault_pages = []

    for i in pages:

        if(i in fault_pages):
            fault_pages.remove(i)
            fault_pages.append(i)

        else:

            if(len(fault_pages) == capacity):
                fault_pages.pop(0)
                fault_pages.append(i)
                fault += 1

            else:
                fault_pages.append(i)
                fault += 1

    return fault


pages = [7, 0, 1, 2, 0, 3, 0,
         4, 2, 3, 0, 3, 2]

fault = 0
capacity = 2

print("Fault for LRU : " + str(LRU(pages, fault, capacity)))
