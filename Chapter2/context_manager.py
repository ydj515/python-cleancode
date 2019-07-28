#-*- coding: utf-8 -*-

"""
f1과 f2는 동일한 기능이지만 f2로 쓰는 것이 파이썬스러운 것!
"""
# def f1():
#     fd = open(filename)
#     try:
#         proccess_file(fd)
#     finally:
#         fd.close()

# def f2():
#     with open(filename) as fd:
#         proccess_file(fd)

#################################################

def stop_database():
    print("stop db")

def start_database():
    print("start db")

def db_backup():
    print("pg_dump database")


class DBHandler:
    def __enter__(self):
        stop_database()
        return self # return 값은 필수적이지 않지만 무엇인가를 반환하는 것이 좋다

    def __exit__(self, exc_type, ex_value, ex_traceback):
        start_database()


def main():
    with DBHandler():
        db_backup

if __name__ == "__main__":
    main()