# 아래 함수를 수정하시오.

def sort_tuple(new_tuple, reverse=False):
    return tuple(sorted(new_tuple, reverse = reverse))
     

result = sort_tuple((5, 2, 8, 1, 3))
print(result)
