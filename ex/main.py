#기능 분리
# 1. 함수로 기능 별로 분리
# 2. 파일로 분리

# 다른 파일 코드 가져오는 방법
# 1. import를 통해

# 2. 필요한 기능만 가져오자
# as를 통해 별명 지어주기

from first import func as first_func

def func ():
    print("main의 호출됨")
first_func()
func()

# 프로그램의 패러다임(방법론)
# 어떻게하면 프로그램을 좀 더 쉽게 설계하고 구현할 수 있을까
# 절차지향
# 절차에 따라 순서대로 구현하자 C언어

# 객체지향
# 객체를 기준으로 분리 개발 자바, 파이썬
# 팀 별 파트를 맡아서 개발
# 각 팀의 결과를 가정하고 더미 데이터 기반 개발 진행
# 객체란 현실의 사물이나 개념을 코드로 표현

class Smartphone:
    def __init__(self, model, price):
        self.model = model
        self.price = price

giryunPhone = Smartphone("wide5", "0won")
beomseokPhone = Smartphone("galaxy21", "1milwon")

print(giryunPhone.model, giryunPhone.price)
print(beomseokPhone.model, beomseokPhone.price)
