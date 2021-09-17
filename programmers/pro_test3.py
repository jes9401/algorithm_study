# 3진법 뒤집기
# https://programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    answer = []
    temp = 3
    i = 1
    while True:
        if temp >n:
            temp //= 3
            break
        else:
            temp*=3
    temp_list = [0 for x in range(int(temp**(1/3))+1)]
    while n>0:
        answer.append(n//temp)
        n-=(n//temp)*temp
        temp//=3
    while len(temp_list)!=len(answer):
        answer.append(0)

    result = answer.pop(0)
    temp = 3
    for i in range(len(answer)):
        result+=(temp*answer[i])
        temp*=3
    return result

print(solution(45))
print(solution(125))
print(solution(46))
print(solution(47))
print(solution(54))
