""" Q. The Dining Philosopher Problem – The Dining Philosopher Problem states that K
philosophers seated around a circular table with one chopstick between each pair of
philosophers. There is one chopstick between each philosopher. A philosopher may eat if he
can pickup the two chopsticks adjacent to him. One chopstick may be picked up by any one
of its adjacent followers but not both.
There are three states of philosopher : THINKING, HUNGRY and EATING. Here there
are two semaphores : Mutex and a semaphore array for the philosophers. Mutex is used such that no two philosophers may access the pickup or putdown at the same time. The array is used to control the behavior of each philosopher. But, semaphores can result in deadlock due to programming errors.
"""
import threading
import random
import time

#inheriting threading class in Thread module
class Philosopher_331(threading.Thread):
    running = True  #used to check if everyone is finished eating

 #Since the subclass overrides the constructor, it must make sure to invoke the base class constructor 
    #(Thread.__init__()) before doing anything else to the thread.
    def __init__(self, index, forkOnLeft, forkOnRight):
        threading.Thread.__init__(self)
        self.index = index
        self.forkOnLeft = forkOnLeft
        self.forkOnRight = forkOnRight

    def run(self):
        while(self.running):
            # Philosopher is thinking (but really is sleeping).
            time.sleep(30)
            print ('Philosopher %s is hungry.' % self.index)
            self.dine_331()

    def dine_331(self):
        # if both the semaphores(forks) are free, then philosopher will eat
        fork1, fork2 = self.forkOnLeft, self.forkOnRight
        while self.running:
            fork1.acquire() # wait operation on left fork
            locked = fork2.acquire(False) 
            if locked: break #if right fork is not available leave left fork
            fork1.release()
            print ('Philosopher %s swaps forks.' % self.index)
            fork1, fork2 = fork2, fork1
        else:
            return
        self.dining_331()
        #release both the fork after dining
        fork2.release()
        fork1.release()
 
    def dining_331(self):			
        print ('Philosopher %s starts eating. '% self.index)
        time.sleep(30)
        print ('Philosopher %s finishes eating and leaves to think.' % self.index)

def main():
    forks = [threading.Semaphore() for n in range(5)] #initialising array of semaphore i.e forks

    #here (i+1)%5 is used to get right and left forks circularly between 1-5
    philosophers= [Philosopher_331(i, forks[i%5], forks[(i+1)%5])
            for i in range(5)]

    Philosopher_331.running = True
    for p in philosophers: p.start()
    time.sleep(100)
    Philosopher_331.running = False
    print ("Now we're finishing.")
 

if __name__ == "__main__":
    main()
