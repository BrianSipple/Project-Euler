"""
You are given the following information, but you may prefer
to do some research for yourself:

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4,
but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
"""

def next_day(dt_tuple):

    if (dt_tuple[2] % 4 == 2) and (dt_tuple[2] % 100 != 0) or (dt_tuple[2] % 400 == 0):
        leap_year = True
        feb_days = 29
    else:
        leap_year = False
        feb_days = 28

    month_days = {
        1: 31,
        2: feb_days,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    if dt_tuple[1] == month_days[dt_tuple[0]]: #If the day equals last day of month, go to first of next month
        if dt_tuple[0] < 12:
            return (dt_tuple[0] + 1, 1, dt_tuple[2], (dt_tuple[3]+1) % 7)
        else:
            return (1, 1, dt_tuple[2]+1, (dt_tuple[3]+1) % 7)

    else:
        return (dt_tuple[0], dt_tuple[1] + 1, dt_tuple[2], (dt_tuple[3]+1) % 7)

dates = []
dt_tuple = (1, 1, 1901, 2)

while (dt_tuple[2] < 2001):
    dates.append(dt_tuple)
    dt_tuple = next_day(dt_tuple)

sundays = [i for i in dates if (i[1] == 1) and i[3] == 0]

print sundays
print(len(sundays))
