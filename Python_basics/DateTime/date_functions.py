from datetime import date, timedelta
from datetime import datetime

cur_date=date.today()
print('Current date: ',cur_date)

cur_time=datetime.now()
print('current date and time: ',cur_time)

format_date=cur_time.strftime("%Y-%m-%d")
print(format_date)

cur_date=date.today()

a=cur_date+timedelta(days=1)
b=cur_date-timedelta(days=2)
print("Increment date by 1:", a)
print("Decrement date by 2:", b)
