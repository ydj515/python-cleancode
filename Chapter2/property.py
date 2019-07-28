#-*- coding: utf-8 -*-

"""
 _ : private용으로 사용 하지만 외부에서 접근 가능
 __ : 외부에서 접근 불가능 -> setter 메소드로 접근해야함 -> 파이썬에서는 property 사용
"""

class Movie:
    def __init__(self, movie_name):
        self.__movie_name = movie_name # 외부에서 접근 불가
 
    @property
    def movie_name(self): # 이때 메서드 이름은 변수(속성)의 이름과 동일하게 하는 것이 좋다
        return self.__movie_name
 
    @movie_name.setter
    def movie_name(self, new_movie_name): # 이때 메서드 이름은 변수(속성)의 이름과 동일하게 하는 것이 좋다
        """ 영화를 변경하는 setter 메서드"""
        self.__movie_name = new_movie_name
        print("============ setter를 통해 영화를 변경합니다============")
        print('변경 후 영화이름 : {} '.format(self.movie_name))


def main():
    movie = Movie('총알 탄 사나이')
    print(movie.movie_name)
    movie.movie_name = '히든 피겨스' # 객체의 속성값에 직접 접근하는듯이 사용하지만 
                                    # 실제로는 메서드 호출을 통해 변수에 접근한다. 
    print(movie.movie_name)


if __name__ == "__main__":
    main()