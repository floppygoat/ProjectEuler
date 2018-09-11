from datetime import date

MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6

JANUARY = 1
FEBRUARY = 2
MARCH = 3
APRIL = 4
MAY = 5
JUNE = 6
JULY = 7
AUGUST = 8
SEPTEMBER = 9
OCTOBER = 10
NOVEMBER = 11
DECEMBER = 12


def get_answer(start_year=1901, end_year=2001, start_day=SUNDAY):
    """
    Using python's library date, gets the day of the week of the first day of <start_year>.
    It then calculates the first day of the month of all consecutive days.
    :return:
    """
    count = 0
    start_day_of_month = date(start_year, JANUARY, 1).weekday()
    for year in range(start_year, end_year):
        for month in range(JANUARY, DECEMBER + 1):
            if start_day_of_month == start_day:
                count += 1
            if month in {JANUARY, MARCH, MAY, JULY, AUGUST, OCTOBER, DECEMBER}:
                start_day_of_month = (start_day_of_month + 31) % 7
            elif month in {APRIL, JUNE, SEPTEMBER, NOVEMBER}:
                start_day_of_month = (start_day_of_month + 30) % 7
            elif (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                start_day_of_month = (start_day_of_month + 29) % 7
    return count
