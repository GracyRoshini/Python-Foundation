import time

print(time.time())

print()

print('local time:', time.localtime())

print()

print(time.localtime(time.time()))

print()

format_time=time.asctime(time.localtime(time.time()))
print("format time: ", format_time)

print()

import calendar
print(calendar.month(2025,5))
