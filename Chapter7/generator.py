#-*- coding: utf-8 -*-

# 제너레이터 사용x
def _load_purchases(filename):
    purchases = []

    with open(filename) as f:
        for line in f:
            *_, price_raw = line.partition(",")
            purchases.append(float(price_raw))
    
    return purchases

# 제너레이터 사용o
# 제너레이터는 파일의 전체 내용을 리스트에 담을 필요 x, 그때그때 가져오는 것. return 문도 필요 x
def load_purchases(filename):

    with open(filename) as f:
        for line in f:
            *_, price_raw = line.partition(",")
            yield float(price_raw) # yield 키워드를 붙히면 제너레이터가 됨