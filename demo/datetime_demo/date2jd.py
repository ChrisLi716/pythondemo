import math
from datetime import datetime


def julian_day(now):
    """
    1. Get current values for year, month, and day
    2. Same for time and make it a day fraction
    3. Calculate the julian day number via   https://en.wikipedia.org/wiki/Julian_day
    4. Add the day fraction to the julian day number

    """
    year = now.year
    month = now.month
    day = now.day
    day_fraction = now.hour + now.minute / 60.0 + now.second / 3600.0 / 24.0

    # The value 'march_on' will be 1 for January and February, and 0 for other months.
    march_on = math.floor((14 - month) / 12)
    year = year + 4800 - march_on
    # And 'month' will be 0 for March and 11 for February. 0 - 11 months
    month = month + 12 * march_on - 3

    y_quarter = math.floor(year / 4)
    jdn = day + math.floor((month * 153 + 2) / 5) + 365 * year + y_quarter

    julian = year < 1582 or year == (1582 and month < 10) or (month == 10 and day < 15)
    if julian:
        reform = 32083  # might need adjusting so needs a test
    else:
        reform = math.floor(year / 100) + math.floor(year / 400) + 32030.1875  # fudged this

    return jdn - reform + day_fraction


if __name__ == '__main__':
    now_str = datetime.now().strftime("%Y%m%d%H%M%S")
    dateTime_p = datetime.strptime(now_str, '%Y%m%d%H%M%S')
    print(dateTime_p)
    print(julian_day(dateTime_p))
