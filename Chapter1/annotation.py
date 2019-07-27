#-*- coding: utf-8 -*-

"""
annotation을 통해 문서생성, 유효성 검증 타입체크 가능
예상되는 타입을 알수 있지만 강제는 아님

<사용법>
>>> locate.__annotations__
{'latitude': float, 'longitude': float, 'return': __main__.Point}
"""

class Point:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long
    
def locate(latitude: float, longitude: float) -> Point:
    """
    맵에서 좌표에 해당하는 객체를 검색
    """