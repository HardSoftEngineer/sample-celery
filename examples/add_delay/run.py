import time

from add_delay.tasks import add
from add_delay.tasks import add_slow_task


# 
print(f"{time.time()} add start")
res = add.delay(10, 20)
value = res.get()
print(f"{time.time()} add value: {value}")

# 
print(f"{time.time()} add start")
res = add_slow_task.delay(10, 20)
value = res.get()
print(f"{time.time()} add (slow) value: {value}")
