# 프로그래머스 
# 두 정수 사이의 합  https://programmers.co.kr/learn/courses/30/lessons/12912



def solution(a, b):
    return sum([i for i in range(a,b+1)]) if a<b else sum([i for i in range(b,a+1)]) if a>b else a
