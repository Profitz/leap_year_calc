"""
Simple leap year calculator which returns the total days in a month by year
"""


def is_leap(evaluate_year):
    if evaluate_year % 4 == 0:
        if evaluate_year % 100 == 0:
            if evaluate_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(input_year, input_month):
    # list to have total days in each month based upon a non-leap year
    # Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    is_leap_year = is_leap(input_year)
    if is_leap_year:
        if input_month == 2:
            # leap year so February has 29 days
            return 29
        else:
            evaluated_days = month_days[input_month - 1]
            return evaluated_days
    else:
        evaluated_days = month_days[input_month - 1]
        return evaluated_days


print("Welcome to the Leap Year Calculator!")
print("Returning the total days of a month by a year you enter.\n")

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)

if days == 29:
    print(f"Leap Year!  There are {days} days in {month}/{year}.")
else:
    print(f"Non-Leap Year.  There are {days} days in {month}/{year}.")
