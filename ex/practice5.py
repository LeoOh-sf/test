# 아래 함수를 수정하시오.

ini_lst = [1, 2, 2, 3, 4, 4, 5]

def remove_duplicates(lst):
    new_lst = []
    for item in lst:
        if item not in new_lst:
            new_lst.append(item)
    return new_lst

result = remove_duplicates(ini_lst)
print(result)
