# 예외처리
# try - except - finally

# 첫 번째 규칙: Exception 으로는 예외처리 하지말자
# 두 번째 규칙: try-except 는 성능 상 이슈가 발생할 수 있다.
# - 남용하면 안된다.
# -> 먼저 if 로 예외처리를 고려하고
# --> if 로 잡는 게 어려운 케이스에서는 try-except 를 사용하는 게 좋다.

try:
    num = 12
    target = 0
    result = num / target
except ZeroDivisionError:
    print("미안하다")


num = 12
target = 0
if target == 0:
    print("0으로는 못나눈다")
else:
    result = num / target

