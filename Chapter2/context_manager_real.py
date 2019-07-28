#-*- coding: utf-8 -*-

import contextlib

"""
컨텍스트 관리자 제대로 구현
"""

def stop_database():
    print("stop db")

def start_database():
    print("start db")

def db_backup():
    print("pg_dump database")

@contextlib.contextmanager
def db_handler():
    stop_database()
    yield
    start_database()

with db_handler():
    db_backup()


class dbhandler_decorator(contextlib.ContextDecorator):
    def __enter__(self):
        stop_database()

    def __exit__(self, exc_type, ex_value, ex_traceback):
        start_database()


@dbhandler_decorator
def offline_backup():
    print("offline backup")