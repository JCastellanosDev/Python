import datetime #importing datetime module
from bday_messages import message as bday_messages
today = datetime.date.today()
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))
next_bday = datetime.date(year, month, day)

days_aways = (next_bday - today)

if today == next_bday:
    print(bday_messages)
else:
    print(f"Your birthday is in {days_aways.days} days!")