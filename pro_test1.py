# 소수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12977
def isPrime(n):
    temp = 1
    for i in range(2,n):
        if n%i == 0:
            temp = 0
    return temp
def solution(nums):
    answer = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                answer+=isPrime(nums[i]+nums[j]+nums[k])
    return answer
