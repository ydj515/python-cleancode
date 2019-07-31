#-*- coding: utf-8 -*-

import datetime

"""
decorator 함수를 재사용 함으로써, main 함수에 대한 가독성과 직관성이 훨씬 좋아짐
대상 함수의 수행 중간에 끼어드는 구문은 할 수 없음
decorator는 원래 작업의 앞 뒤에 추가적인 작업을 손쉽게 사용 가능하도록 도와주는 역할을 함

"""
def datetime_decorator(func):
        def decorated():
                print(datetime.datetime.now())
                func()
                print(datetime.datetime.now())

        return decorated


@datetime_decorator # datetime_decorator() 함수 이름과 동일하게 작성
def main_function_1():
        print("MAIN FUNCTION 1 START")


@datetime_decorator
def main_function_2():
        print("MAIN FUNCTION 2 START")


@datetime_decorator
def main_function_3():
        print("MAIN FUNCTION 3 START")


def main():
    # 원래는 이렇게 작성해야 되는 것을 데코레이터를 쓰면 밑의 코드로 가능
    # print datetime.datetime.now()
    # print "MAIN FUNCTION START"
    # print datetime.datetime.now()

    datetime_decorator(main_function_1())
    print("====================================")
    datetime_decorator(main_function_2())
    print("====================================")
    datetime_decorator(main_function_2())

if __name__ == '__main__':
    main()