def LRU(pages, fault, capacity):

    fault_pages = []

    for i in pages:
        print("Page", i, "has been requested")
        if(i in fault_pages):
            print("Page", i, " exist in Main memory, HIT")
            print("Page", i, "become recently use in Main memory")
            fault_pages.remove(i)
            fault_pages.append(i)
            print("Main memory:", fault_pages)

        else:
            print("Page", i, " is not exist in Main memory, PAGE FAULT OCCUR")
            if(len(fault_pages) == capacity):
                print("Main memory already full in capacity")
                value = fault_pages.pop(0)
                print("Removing the least used page :",
                      value, " ,from Main memory")
                print("Inserting new page :", i,
                      " from secondary memory to Main memory")
                fault_pages.append(i)
                fault += 1
                print("Main memory:", fault_pages)

            else:
                print("Main memory not full yet")
                print("Inserting new page :", i,
                      " from secondary memory to Main memory")
                fault_pages.append(i)
                fault += 1
                print("Main memory:", fault_pages)
        print()
    return fault


# pages = [7, 0, 1, 2, 0, 3, 0,
#          4, 2, 3, 0, 3, 2]

pages = [1, 2, 3, 4, 1]

fault = 0
capacity = 4


print("Fault for LRU : " + str(LRU(pages, fault, capacity)))
