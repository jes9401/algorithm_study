# 프로그래머스 
# 피보나치 수 https://programmers.co.kr/learn/courses/30/lessons/12945
# 시간복잡도 고려해서 일반적인 피보나치 수열로 해결
def solution(n):
    if n<2:
        return n
    else:
        a = 1
        b = 1
        temp = 0
        for i in range(2, n+1):
            b = a;
            a += temp;
            temp = b;
        return a%1234567

print(solution(3))
print(solution(5))