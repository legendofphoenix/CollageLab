"""Q. Assume we have a buffer of fixed size. A producer can produce an item and can place in
the buffer. A consumer can pick items and can consume them. We need to ensure that when a
producer is placing an item in the buffer, then at the same time consumer should not consume
any item. In this problem, buffer is the critical section.
To solve this problem, we need two counting semaphores – Full and Empty. “Full” keeps
track of number of items in the buffer at any given time and “Empty” keeps track of number
of unoccupied slots."""
import threading
import random
import time
q_331 = []
empty_331 = threading.Semaphore(1)
full_331 = threading.Semaphore(0)
def producer_331():
nums = range(5)
global q_331
while True:
no_331 =int(randint(1,100))
empty_331.acquire()
q_331.append(no_331)
print("Produced", no_331)
full_331.release()
time.sleep(random.randrange(0, 3))
def consumer_331():
global q_331
while True:
full_331.acquire()
no_331 = q_331.pop(0)
print("Consumed", no_331)
empty_331.release()
time.sleep(random.randrange(0, 3))
producerThread = threading.Thread(target=producer_331)
consumerThread = threading.Thread(target=consumer_331)
producerThread.start()
consumerThread.start()
