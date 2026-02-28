# to subtract five days from current date.
import datetime
current_date = datetime.datetime.now()
new_date = current_date - datetime.timedelta(days=5)
print("Current date:", current_date)
print("Date before 5 days:", new_date)

# to print yesterday, today, tomorrow.
import datetime
today = datetime.datetime.now().date()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#to drop microseconds from datetime
import datetime
current_datetime = datetime.datetime.now()
without_microseconds = current_datetime.replace(microsecond=0)
print("Original:", current_datetime)
print("Without microseconds:", without_microseconds)

#to calculate two date difference in seconds.
import datetime
date1 = datetime.datetime(2025, 2, 20, 12, 0, 0)
date2 = datetime.datetime(2025, 2, 28, 12, 0, 0)
difference = date2 - date1
seconds = difference.total_seconds()
print("Difference in seconds:", seconds)