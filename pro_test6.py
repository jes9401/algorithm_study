# 프로그래머스 
# 수박수박수박수박수박수? https://programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    return "수박"*(n//2) if n%2==0 else "수박"*(n//2) + "수박"[0]


print(solution(5))
print(solution(1))
print(solution(0))

