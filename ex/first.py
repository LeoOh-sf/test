# 십진수 -> 이진수 (재귀호출)
arr =  [2, 4, 6, 8, 10]

def func(idx):
    if idx == len(arr) - 1:
        # 종료 조건이 만족했을 때, 수행되어야 할 로직
        print(arr[idx], end=' ')    
        return
    
    print(arr[idx], end=' ')  # 다음 재귀 호출 전에 뭘 하고 싶은가 ?

    func(idx + 1)  # 다음 재귀 호출에는 어떤 값을 전달해주어야 하는가 ?

    print(arr[idx], end=' ')  # 돌아오면서는 어떤 로직을 수행하고 싶은가 ?
    
func(0)