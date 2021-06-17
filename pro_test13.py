# 프로그래머스 
# [1차] 다트 게임 https://programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    import re
    answer = 0
    temp = []
    s = ""
    sdt = ['S','D','T']
    bonus = ['*','#']
    for i in dartResult:
        s+=i
        if i in bonus:
            temp.append(s)
            s = ''
        elif i in 
    return answer


print(solution('1S2D*3T'))      # 37
print(solution('1D2S#10S'))     # 9
print(solution('1D2S0T'))       # 3
print(solution('1S*2T*3S'))     # 23
