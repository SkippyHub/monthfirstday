# %%
'''
1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine. 
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

How would you solve it for Tuesday?

'''

'''
I've done two solutions for this problem.
The first one is a simple solution using datetime.
The second one is a more complex solution using a dictionary
to store the number of days in each month and a function to determine
if a year is a leap year. The second solution is more complex 
but it is faster than the first solution.
'''


'''
simple trivial solution using datetime
'''
from datetime import datetime
start_date = datetime(1901, 1, 1)
end_date = datetime(2000, 12, 31)

Sunday_count = 0

while start_date <= end_date:
    if start_date.weekday() == 6: # Sunday is 6, change to 1 for tuesday
        Sunday_count += 1
    if start_date.month == 12:
        start_date = start_date.replace(year=start_date.year + 1, month=1)
    else:
        start_date = start_date.replace(month=start_date.month + 1)
print('Sunday_count', Sunday_count)
# %%


'''
Second solution using a dictionary to store the number of days in each month.

'''

dict_months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

# Adjust the starting weekday index based on the known day of the week for January 1, 1900 (Monday)
weekday_index = 1  # Monday

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_days_in_month(month, year):
    return 29 if month == 2 and is_leap_year(year) else dict_months[month]

def get_next_day(day, month, year, weekday_index):
    day += 1
    weekday_index = 1 if weekday_index == 7 else weekday_index + 1
    if day > get_days_in_month(month, year):
        day = 1
        month, year = (1, year + 1) if month == 12 else (month + 1, year)
    return day, month, year, weekday_index

def get_day_on_first_of_month(iday ,start_day, start_month, start_year, end_day, end_month, end_year):
    day, month, year, weekday = start_day, start_month, start_year, weekday_index
    Tuesday_count = 0
    while not (day == end_day and month == end_month and year == end_year):
        if day == 1 and year >= 1901 and year <= 2000 and weekday == iday:
            Tuesday_count += 1
        day, month, year, weekday = get_next_day(day, month, year, weekday)
    return Tuesday_count

sunday_count = get_day_on_first_of_month(7 ,1, 1, 1900, 31, 12, 2000)
print('Sunday_count', sunday_count)

tuesday_count = get_day_on_first_of_month(1 ,1, 1, 1900, 31, 12, 2000)
print('tuesday_count', tuesday_count)

# %%
