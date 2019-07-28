#-*- coding: utf-8 -*-

"""
제너레이터 표현식은 출력 시퀀스를 메모리에 로딩하지 않는다.
iterator로 한 번에 출력만 만들기 때문
"""

######################################### 기본 예제 
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

######################################### 제너레이터로 만들기 
 
def square_numbers2(nums):
    for i in nums:
        yield i * i


def main():
    my_nums = square_numbers([1,2,3,4,5])
    print(my_nums)
    print(type(my_nums))

    my_nums = square_numbers2(([1,2,3,4,5]))
    print(my_nums)


if __name__ == "__main__":
    main()