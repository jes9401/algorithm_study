# https://programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    answer = 1
    for i in range(1, n):
        if n % i == 1:
            answer = i
            break
    return answer


print(solution(10))
print(solution(12))
