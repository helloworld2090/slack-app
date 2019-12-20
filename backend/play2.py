from datetime import datetime
import time
print(type(datetime.now()))

now = time.time()
print(now)
future = now + 1
while time.time() < future:
    pass

print("10 seconds has passed")

