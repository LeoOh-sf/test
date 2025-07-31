#list comprehension
#- 리스트와 관련된 여러 줄의 코드를 한 줄로 줄이자
# - 남용하면 가독성이 똥이다
# 간단한 반복 + 조건문만 활용하는게 좋다
# 알고리즘 -> 사용자 입력 구현 시 엄청 많이 활용

# 구조
# li = [표현식 for 변수 in 반복객체]

#1부터 10까지 숫자 리스트
result1 = [num for num in range(1,10)]
print(result1)

result2 = [num for num in range (1,11) if num % 2 == 0]
print(result2)

result4 = [list(map(int, input().split())) for _ in range (3)]
print(result4)