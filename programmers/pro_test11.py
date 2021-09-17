# 프로그래머스 
# 약수의 개수와 덧셈  https://programmers.co.kr/learn/courses/30/lessons/77884

def yaksu(num):
    result = 1
    for i in range(1,num):
        if num%i==0:
            result+=1
    return result

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if yaksu(i)%2==0:
            answer+=i
        else:
            answer-=i
    return answer
