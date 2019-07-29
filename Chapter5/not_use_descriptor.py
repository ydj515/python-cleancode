#-*- coding: utf-8 -*-

"""
속성을 가진 이란적인 클래스인데 속성의 값이 달라질 때마다 추적
속성의 setter 메소드에서 값이 변경될 때 검사하여 리스트와 같은 내부 변수에 값을 저장
"""

class Travller:
    def __init__(self, name, current_city):
        self.name = name
        self._current_city = current_city
        self._cities_visited = [current_city]
    
    @property
    def current_city(self):
        return self._current_city
    
    @current_city.setter
    def current_city(self, new_city):
        if new_city != self._current_city:
            self._cities_visited.append(new_city)
            self._current_city = new_city

    @property
    def cities_visited(self):
        return self._cities_visited


def main():
    alice = Travller("Alice", "Barcelona")
    alice.current_city = "Paris"
    alice.current_city = "Brussels"
    alice.current_city = "Amsterdam"
    print(alice.cities_visited)


if __name__ == "__main__":
    main()