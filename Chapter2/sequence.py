#-*- coding: utf-8 -*-

from datetime import datetime, timedelta, date

"""
시퀀스로 구현하면 더 많은 메모리가 사용되지만(모든 것을 한번에 보관해야 하므로)
특정 요소를 가져오기 위한 인덱싱의 시간복잡도는 O(1)로 상수에 가능하다
"""

class DataRangeSequence:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._range = self._create_range()

    def _create_range(self):
        days = []
        current_day = self.start_date

        while current_day < self.end_date:
            days.append(current_day)
            current_day += timedelta(days=1)

        return days
    
    def __getitem__(self, day_no):
        return self._range[day_no]

    def __len__(self):
        return len(self._range)


def main():
    s1 = DataRangeSequence(date(2019, 1, 1), date(2019, 1, 5))
    for day in s1:
        print(day)
    
    s1[0]
    s1[-1]


if __name__ == "__main__":
    main()