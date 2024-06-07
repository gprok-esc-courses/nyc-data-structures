import random
import time

prob_control = 50
prob_takeoff = 72
prob_land = 94
prob_emergency = 100


for i in range(20):
    r = random.randint(1, 100)
    if r <= prob_control:
        print("Control")
    elif r <= prob_takeoff:
        print("Take Off")
    elif r <= prob_land:
        print("Land")
    else:
        print("Emergency")
    time.sleep(random.randint(2, 5))
    
