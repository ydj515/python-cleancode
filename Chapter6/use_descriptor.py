#-*- coding: utf-8 -*-

"""
디스크립터 코드가 복잡해 졋지만, 클라이언트 클래스 코드는 간결해 졌다.
디스크립터 안에서 어떠한 비지니스 로직도 포함되어 있지 않아서 완전히 다른 클래스를 적용해도 같은 효과 발생할 수 있다.
최종적으로, 디스크립터는 비지니스 로직의 구현보다는 라이브러리, 프레임워크, 내부 API를 정의하는데 적합
"""

class HistoryTraceAttribute:
    def __init__(self, trace_attribute_name) -> None:
        self.trace_attribute_name = trace_attribute_name
        self._name = None

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        self._track_change_in_value_for_instance(instance, value)
        instance.__dict__[self._name] = value

    def _track_change_in_value_for_instance(self, instance, value):
        self._set_default(instance)
        if self._needs_to_track_change(instance, value):
            instance.__dict__[self.trace_attribute_name].append(value)

    def _needs_to_track_change(self, instance, value) -> bool:
        try:
            current_value = instance.__dict__[self._name]
        except KeyError:
            return True
        
        return value != current_value
    
    def _set_default(self, instance):
        instance.__dict__.setdefault(self.trace_attribute_name, [])

class Travller:

    current_city = HistoryTraceAttribute("cities_visited")

    def __init__(self, name, current_city):
        self.name = name
        self.current_city = current_city

    
def main():
    pass


if __name__ == "__main__":
    main()