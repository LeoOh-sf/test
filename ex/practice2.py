data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
# '''
# 예시코드
# arr = [1, 2, 3, 4, 5]
# for num in arr:
#     print(num, end='')
# 출력결과 : 12345
# '''
# 아래에 코드를 작성하시오.
def uppercase(text):
    uppercase = ""
    for char in text:
        if char.isupper() or char == ' ':
            uppercase += char
    return uppercase
    
result = uppercase(data_1)
print(result)

data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
set1 = ("내", "힘", "들", "다")
arr = []

def tired(text):
    for char in set1:
        index = text.find(char)
        if index != -1:
            arr.append((index))
    return arr

result = tired(data_2)
print((result))
result.sort()
print((result))

index_list = result 
for index, char in enumerate(data_2):
    if index in index_list:
        print(char, end="")

# # 아래에 코드를 작성하시오.

def uppercase(text):
    uppercase = ""
    for char in text:
        if char.isupper():
            uppercase += char
    for char in text:
        if " " in data_1:
            " ".join(uppercase)
            return uppercase
    return uppercase

result = uppercase(data_1)
print(result)