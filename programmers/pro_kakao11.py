# 프로그래머스 
# [1차] 다트 게임 https://programmers.co.kr/learn/courses/30/lessons/17682

# *은 전 점수와 해당 점수 2배
# '#'은 해당 점수 마이너스
def solution(dartResult):
    import re
    answer1 = ''
    answer2 = ''
    answer3 = ''
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
        elif i in sdt:
            temp.append(s)
            s= ''
    for j in range(len(temp)):
        if temp[j] in bonus:
            temp[j-1] = temp[j-1]+temp[j]
    for k in temp:
        if k in bonus:
            temp.remove(k)


    for x in range(len(temp)):
        for y in temp[x]:
            if x == 0:
                if y.isdigit():
                    answer1 += y
                elif y in sdt:
                    answer1= int(answer1)
                    if y == 'D':
                        answer1 = answer1**2
                    elif y == 'T':
                        answer1 = answer1**3
                elif y in bonus:
                    if y == '*':
                        answer1*=2
                    elif y == '#':
                        answer1*=(-1)
            elif x == 1:
                if y.isdigit():
                    answer2 += y
                elif y in sdt:
                    answer2= int(answer2)
                    if y == 'D':
                        answer2 = answer2**2
                    elif y == 'T':
                        answer2 = answer2**3
                elif y in bonus:
                    if y == '*':
                        answer2*=2
                        answer1*=2
                    elif y == '#':
                        answer2*=(-1)
            else:
                if y.isdigit():
                    answer3 += y
                elif y in sdt:
                    answer3= int(answer3)
                    if y == 'D':
                        answer3 = answer3**2
                    elif y == 'T':
                        answer3 = answer3**3
                elif y in bonus:
                    if y == '*':
                        answer3*=2
                        answer2*=2
                    elif y == '#':
                        answer3*=(-1)
    return answer1+answer2+answer3


print(solution('1S2D*3T'))      # 37
print(solution('1D2S#10S'))     # 9
print(solution('1D2S0T'))       # 3
print(solution('1S*2T*3S'))     # 23
