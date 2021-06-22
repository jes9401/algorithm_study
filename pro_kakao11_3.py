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


    # 문자열을 돌면서 분류
    for x in range(len(dartResult)):
        char = dartResult[x]
        s+=char
        # 마지막 문자일 경우 s를 그냥 추가
        if x == len(dartResult)-1:
            temp.append(s)
        else:
            next_char = dartResult[x+1]
            # S,D,T이고 다음 문자열이 *,#이 아닌 경우
            if char in sdt and next_char not in bonus:
                temp.append(s)
                s=''
            # *,#인 경우
            elif char in bonus:
                temp.append(s)
                s=''


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
