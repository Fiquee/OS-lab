'''
Write a program to simulate the Dining Philosophers Problem.
'''
import threading
import random
import time


class Philosopher(threading.Thread):
    # Shared by all instances of the class
    running = True

    def __init__(self, index, forkLeft, forkRight):
        threading.Thread.__init__(self)
        self.index = index
        self.forkLeft = forkLeft
        self.forkRight = forkRight

    def run(self):
        while self.running:
            time.sleep(1)
            print(f'Philosopher {self.index + 1} is hungry')
            self.dine()

    def dine(self):
        print(f'Philosopher {self.index+1} is trying to eat')
        fork1, fork2 = self.forkLeft, self.forkRight
        while self.running:
            # Acquire fork 1
            fork1.acquire()
            # False argument means that the semaphore is not blocked
            locked = fork2.acquire(False)
            # If true, the philosopher "obtains" the fork and locks the resource, enabling them to "eat"
            if locked:
                break

            # Prevents deadlock
            fork1.release()

            print(f"Philosopher {self.index+1} is swapping forks.")
            fork1, fork2 = fork2, fork1

        else:
            return

        # Philosopher is eating
        print(f"Philosopher {self.index + 1} starts eating")
        time.sleep(1)
        print(
            f"Philosopher {self.index + 1} finishes eating and leaves to think")

        # Release both fork
        fork2.release()
        fork1.release()


forks = [threading.Semaphore() for i in range(5)]
philosophers = [Philosopher(i, forks[i % 5], forks[(i+1) % 5])
                for i in range(5)]

for philosopher in philosophers:
    philosopher.start()

time.sleep(10)

Philosopher.running = False
print("Now we're finishing")
