# 프로그래머스 
# [1차] 다트 게임 https://programmers.co.kr/learn/courses/30/lessons/17682

# *은 전 점수와 해당 점수 2배
# '#'은 해당 점수 마이너스
def solution(dartResult):
    # 1,2,3차 점수 저장할 리스트
    answer = ['','','']

    # 분류한 문자열을 저장할 리스트
    temp = []
    s = ""
    sdt = ['S','D','T']
    bonus = ['*','#']


    # 숫자+문자 or '*' or '#' 으로 저장
    for i in dartResult:
        s+=i
        # '*' 이나 '#'일 경우 
        if i in bonus:
            temp.append(s)
            s = ''
        elif i in sdt:
            temp.append(s)
            s= ''

    # *, # 을 직전의 값과 합친 뒤 제거
    for j in range(len(temp)):
        if temp[j] in bonus:
            temp[j-1] = temp[j-1]+temp[j]
    for k in temp:
        if k in bonus:
            temp.remove(k)


    for i in range(len(temp)):
        for j in temp[i]:
            text = j
            # 숫자일 경우
            if text.isdigit():
                answer[i] += str(text)
            #  s,d,t일 경우
            elif text in sdt:
                answer[i] = int(answer[i])
                if text == 'D':
                    answer[i] = answer[i]**2
                elif text == 'T':
                    answer[i] = answer[i]**3
            # '*', '#'일 경우
            elif text in bonus:
                if text == '*':
                    # 첫번째 값이 아니면 i-1번째도 2배
                    if i!=0:
                        answer[i]*=2
                        answer[i-1]*=2
                    else:
                        answer[i]*=2
                elif text == '#':
                    answer[i]*=(-1)

    return sum(answer)


print(solution('1S2D*3T'))      # 37
print(solution('1D2S#10S'))     # 9
print(solution('1D2S0T'))       # 3
print(solution('1S*2T*3S'))     # 23
