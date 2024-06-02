from datetime import datetime

# Get current timestamp
now = datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

# Timestamp format 
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
print("Timestamp formateado:", formatted_now)

# Get Unix timestamp
unix_timestamp = int(now.timestamp())
print("Unix timestamp:", unix_timestamp)

year_2024 = datetime(2024, 1, 1)
print_date(year_2024)


# Time Module
from datetime import time
current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

# Date Module
from datetime import date
current_date = date(21, 6, 1)

print(current_date.year)
print(current_date.month)
print(current_date.day)

# Do math operations with dates
from datetime import timedelta

birthday = date(1990,6,9)
print(now.date())
print(birthday)

diff = now.date()-birthday
print(diff)

start_timedelta = timedelta(200, 100, 100)
end_timedelta = timedelta(300, 50, 50)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
