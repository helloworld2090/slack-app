import time
from datetime import datetime

def counter(num):
    now = time.time()
    future = now + num
    print(now)
    num = 0
    while time.time() <= future:
        print("YEET")
        num += 1

    print(future)
    print(datetime.now())

