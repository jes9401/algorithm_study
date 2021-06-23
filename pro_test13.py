# 프로그래머스 
# 같은 숫자는 싫어 https://programmers.co.kr/learn/courses/30/lessons/12906
# 시간초과 해결중
def solution(arr):
    from operator import is_not
    from functools import partial
    answer =[]
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                arr[j] = None
            else:
                break
    arr= list(filter(partial(is_not, None), arr))
    return arr




print(solution([1,1,3,3,0,1,1])) # [1,3,0,1]
print(solution([4,4,4,3,3])) # [4,3]
