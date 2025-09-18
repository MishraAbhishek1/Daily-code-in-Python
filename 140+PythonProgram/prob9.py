# Write a Python program to display calendar.
# here we  import in python calendar
import calendar

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))

cal = calendar.month(year, month)
print(cal)