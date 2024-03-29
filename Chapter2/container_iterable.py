#-*- coding: utf-8 -*-

from datetime import datetime, timedelta, date

class DateRangeContainerIterable:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
    
    def __iter__(self):
        current_day = self.start_date

        while current_day < self.end_date:
            yield current_day
            current_day += timedelta(days=1)


def main():
    r1 = DateRangeContainerIterable(date(2019, 1, 1), date(2019, 1, 5))
    ", ".join(map(str, r1))
    max(r1)


if __name__ == "__main__":
    main()