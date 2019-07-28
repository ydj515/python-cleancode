#-*- coding: utf-8 -*-

"""
시퀀스나 이터러블 객체를 만들지 않고 키로 객체의 특정 요소를 가져오는 방법
"""
class Items:
    def __init__(self, *values):
        self._valuses = list(values)

    def __len__(self):
        return len(self._valuses)

    def __getitem__(self, item):
        return self._valuses.__getitem__(item)