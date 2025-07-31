# 1 리스트를 파라미터로 받아, 반복문을 이용해 리스트 내 모든 정수의 합을 반환하는 함수를 작성하시오. (sum() 사용 금지)
my_lst = [4, 13, 2, 3, 24, 5]
my_lst[0] = 2
print(sum(my_lst))


def sum_lst(lst):
    sum1 = 0     # 전체 값 받을 변수
    for i in lst: # 리스트를 순회하면서 인자들을 더할 준비
        sum1 += i
    return sum1 # 하니씩 sum1 변수에 인자 값을 더해서 반환

a = sum_lst(my_lst)
print(a)

# 2 문자열을 입력받아, 문자열이 모두 소문자인지 확인하는 함수를 작성하시오. (islower() 사용 금지)

a = 'OgT08FizzY'
def lower(str):
    return str.lower() == str
print(lower(a))

# 3 0부터 n까지의 정수 중 홀수만 리스트로 반환하는 함수를 작성하시오.

a = [0, 37, 22, 13, 222, 78, 45, 15, 11]

def odd(lst):
    odd_lst = []
    for num in lst:
        if num % 2 == 1:
            odd_lst.append(num)
    return odd_lst

print(odd(a))

# 4 두 개의 정수를 입력받아, 큰 값을 반환하는 함수를 작성하시오. (max() 사용 금지)

a = 3 
b = 5
c = 10 
d = -2

def larger(num1, num2):
    if num1 > num2:
        print(num1)
    elif num1 < num2:
        print(num2)
    else:
        print("equal")

larger(a, b)
larger(c, d)
larger(-5, -10)
larger(100, 100)

# 5 리스트 안에 있는 모든 문자열을 하나의 문자열로 연결하는 함수를 작성하시오. (join() 사용 금지)

a = ["오규태", "정신 좀", "치려리 뭔 자유시간이여"]

def single_line(lst):
    single = ""
    for let in lst:
        single += let 
    return single.rstrip()

print(single_line(a))

# 6 문자열을 입력받아, 알파벳만 대문자로 변환해 반환하는 함수를 작성하시오. (isalpha(), upper() 사용 가능)

a = 'OgT08FizzY'

upper_char = ''.join([ch for ch in a if ch.isupper()])
print(upper_char)

def extrac_upper(s):
    result = ''
    for ch in s:
        if ch.isalpha() and ch == ch.upper():
            result += ch
    return result
print(extrac_upper(a))

# 7 리스트를 입력받아, 가장 작은 값을 반환하는 함수를 작성하시오. (min() 사용 금지)

my_lst = [4, 13, 42, 3, 24, 55]

def num_small(n):
    n = 100
    for num in my_lst:
        if num < n:
            n = num
    return n

print(num_small(my_lst))

# 8 리스트에서 중복을 제거한 후 정렬된 리스트를 반환하는 함수를 작성하시오. (set()과 sort() 사용 가능)

a = (1, 1, 1, 3, 6, 18, 3, 6, 5, 7, 2, 2)

def non_multi(lst):
    return sorted(set(lst))

b = non_multi(a)
print(b)

# 9 주어진 문자열에서 공백을 모두 제거한 문자열을 반환하는 함수를 작성하시오. (replace() 또는 strip() 사용 가능)

a = " leading and trailing "

def sent_nospace(s):
    return s.replace(" ", "")

print(sent_nospace(a))

# 10 딕셔너리의 값을 모두 더해 반환하는 함수를 작성하시오. (딕셔너리의 값은 모두 정수라고 가정)

a = {"apple": 150, "banana": 300, "cherry": 50}

def total_dict(d):
    total = 0
    for value in d:
        total += int(a.get(value))
    return total

print(total_dict(a))

# 11 리스트 안에 있는 튜플의 각 첫 번째 요소들만 모아 새로운 리스트로 반환하는 함수를 작성하시오.

a = [('a', 100), ('b', 200), ('c', 300)]

def new_lst(tup):
    new = []
    for item in tup:
        new.append(item[0])
    return new

print(new_lst(a))

# 12 문자열이 회문(palindrome)인지 판별하는 함수를 작성하시오. (예: "level" → True)

a = 'level'
b = 'watermelon'

def check_panlindrome(s):
    return s == s[::-1]

print(check_panlindrome(a))
print(check_panlindrome(b))
         
# 13 문자열 리스트를 받아, 각 문자열의 길이를 리스트로 반환하는 함수를 작성하시오.

a = 'level'
b = 'watermelon'

def length_str(s):
    return len(s)

print(length_str(a))
print(length_str(b))

# 14 리스트에서 가장 많이 등장한 숫자를 반환하는 함수를 작성하시오. (여러 개면 아무거나 반환)

a = (1, 3, 3, 3, 6, 18, 3, 6, 5, 7, 2, 2)

def mode(lst):
    counts = {}
    for i in lst:
        counts[i] = counts.get(i, 0)+1
    max_num = 0
    mode_val = None
    for x, cnt in counts.items():
        if cnt > max_num:
            max_num = cnt
            mode_val = x
    return mode_val

print(mode(a))

# 15 정수 n을 입력받아, 1부터 n까지의 정수 중 3의 배수만 리스트로 반환하는 함수를 작성하시오.

def multi_tri(n):
    lst = []
    for i in range(1, n+1):
        if i % 3 == 0:
            lst.append(i)
    return lst

print(multi_tri(31))

# 16 리스트를 파라미터로 받아, 짝수만 골라 새로운 리스트로 반환하는 함수를 작성하시오.

a = [0, 37, 22, 13, 222, 78, 45, 15, 11]

def even(lst):
    even_lst = []
    for num in lst:
        if num % 2 == 0:
            even_lst.append(num)
    return even_lst

print(even(a))

# 17 문자열을 받아 단어별로 나누고, 각 단어의 첫 글자만 대문자로 바꾼 문자열을 반환하는 함수를 작성하시오. (title() 사용 금지)

a = 'level is power over whelming'

def first_upper(s):
    return "".join(
    (w[0].upper() + w[1:]) if w else ''
     for w in s.split(' ')
        
    )

print(first_upper(a))

# 18 숫자 리스트를 받아 평균을 계산하고, 평균 이상인 값만 리스트로 반환하는 함수를 작성하시오.

def above_average(numbers):
    if not numbers:
        return []
    avg = sum(numbers) / len(numbers)
    result = []
    for n in numbers:
        if n >= avg:
            result.append(n)
    return result

print(above_average([1, 2, 3, 4, 5]))      
print(above_average([10, 20, 30]))        
print(above_average([-1, -2, -3, 0, 1]))

# 19 리스트 안의 문자열 중 길이가 5 이상인 문자열만 모아 리스트로 반환하는 함수를 작성하시오.

def long_strings(strings):
    result = []
    for s in strings:
        if len(s) >= 5:
            result.append(s)
    return result

# 20 리스트가 주어졌을 때, 해당 리스트를 역순으로 반환하는 함수를 작성하시오. (reverse(), [::-1] 사용 금지)

def reverse_list(lst):
    result = []
    for i in range(len(lst) - 1, -1, -1):
        result.append(lst[i])
    return result

print(reverse_list([1, 2, 3, 4]))