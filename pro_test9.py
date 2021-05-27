# 프로그래머스 
# N개의 최소공배수 https://programmers.co.kr/learn/courses/30/lessons/12953

# 최소 공배수 반환하는 함수
def a(a,b):
    A,B = a,b
    while B!=0:
        A%=B
        A,B=B,A
    return a*b//A

def solution(arr):
    # 첫번째 두번째 원소의 최소공배수 저장
    answer = a(arr[0],arr[1])
    # 세번째 원소부터 => 원소와 직전 최소공배수의 최소 공배수 구하기
    for i in range(2,len(arr)):
        answer = a(arr[i],answer)
    return answer

print(solution([2,6,8,14]))
print(solution([1,2,3]))

