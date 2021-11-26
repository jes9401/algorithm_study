# https://programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    temp = [arr[0]]
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            temp.append(arr[i+1])
    return temp


print(solution([1, 1, 3, 3, 0, 1, 1]))
print(solution([4, 4, 4, 3, 3]))
