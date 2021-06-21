"""
The main date and time module in python is called `datetime`,
and confusingly enough the main class in that module is also called `datetime`.

"""

from datetime import datetime

print(datetime.now())


#  Coordinated Universal Time ‎(UTC)‎

from datetime import timezone

print(datetime.now(timezone.utc))

"""

When a user gives you a time, convert it to UTC.

When you show the user a time, convert it to their timezone.

That way, you only have to deal with timezones when you show a time to a user; 
and you don’t have to work with timezones at any other point in your system.

"""



# Add or Subtract Time

from datetime import timezone, timedelta

today = datetime.now(timezone.utc)
print(today)
tomorrow = today + timedelta(days=1)  # We can also do weeks= ,hours= ,minutes=, seconds= ,microseconds= .
print(tomorrow)

# Formatting time to show them to user

print(today.strftime('%Y-%m-%d'))   # 2020-08-06
print(today.strftime('%d-%m-%y'))   # 06-08-20
print(today.strftime('%d/%m/%Y %H:%M'))  # 06/08/2020 09:10


# We can also take a string and covert into time format

user_input = input("Enter The Date in YYYY-mm-dd Format:- ")

user_date = datetime.strptime(user_input, '%Y-%m-%d')

print(user_date)