def restructure_word(word, arr):
    for char in word:
        if char.isdecimal():
            for _ in range(int(char)):
                if arr:
                    arr.pop()
        else:
            if char in arr:
                arr.remove(char)
    return arr

original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []
arr.extend(original_word)

print(arr)
result = restructure_word(word, arr)
end = ''.join(result)


print(result)
print(end)
