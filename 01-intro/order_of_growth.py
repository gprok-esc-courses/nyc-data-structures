import random
from time import time

items = [1000, 10000, 100000, 1000000, 10000000, 10000000000]

for s in range(6):
    size = items[s]

    data = [random.randint(1, 100) for i in range(size)]


    start = time()
    total = 0
    counter = 0
    for i in range(size):
        if data[i] % 2 == 0:
            total += data[i]
            counter += 1
    print(total/counter)
    stop = time()
    print(items[s], "ELAPSED:", stop - start)


