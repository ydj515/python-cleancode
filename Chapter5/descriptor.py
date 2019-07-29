#-*- coding: utf-8 -*-

import logging

"""
데이터 디스크립터 : __set__이나 __delete__ 메소드를 구현
비데이터 디스크립터 : __get__ 만 메소드 구현
@property, @classmethod, @staticmethd데코레이터도 디스크립터임!!
디스크립터는 비지니스 로직의 구현보다는 라이브러리, 프레임워크, 내부 API를 정의하는데 적합
"""
class DescriptorClass:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        logging.info("call: %s.__get__(%r, %r)", self.__class__.__name__, instance, owner)

        return instance


class ClientClasS:
    descriptor = DescriptorClass()

    
def main():
    client = ClientClasS()
    client.descriptor # __get__ 메소드를 호출
    client.descriptor is client # client 자체를 반환 하므로 true

if __name__ == "__main__":
    main()