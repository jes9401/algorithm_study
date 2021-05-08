# 프로그래머스
# [카카오 인턴] 수식 최대화
# https://programmers.co.kr/learn/courses/30/lessons/67257

# 숫자2개, 기호 입력 받아서 결과 리턴하는 함수
def cal(num1, num2, string):
    if string == "+":
        return int(num1)+int(num2)
    elif string == "*":
        return int(num1)*int(num2)
    elif string == "-":
        return int(num1)-int(num2)


def solution(expression):
    temp = [] # 숫자, 기호로 구분해서 저장할 리스트
    num = "" # 숫자 판별 변수
    temp2 = [] # 기호만 저장할 리스트
    temp3 = [] # 기호 개수에 따른 모든 경우의 수 저장할 리스트
    for i in range(len(expression)):
        if expression[i].isdigit():
            num += expression[i]
        else:
            temp.append(num)
            num = ""
            temp.append(expression[i])
            if expression[i] not in temp2:
                temp2.append(expression[i])
        if i == len(expression) - 1:
            temp.append(num)
    if len(temp2) == 2: # 기호가 2개일 경우
        temp3.append(temp2)
        temp3.append(temp2[::-1])
    elif len(temp2) == 3: # 기호가 3개일 경우
        temp3.append(temp2)
        temp3.append([temp2[0], temp2[2], temp2[1]])
        temp3.append([temp2[1], temp2[2], temp2[0]])
        temp3.append([temp2[1], temp2[0], temp2[2]])
        temp3.append([temp2[2], temp2[0], temp2[1]])
        temp3.append(temp2[::-1])
    else: # 기호가 1개일 경우
        temp3 = temp2
    max_num = 0 # 최대값 저장 변수
    for x in temp3:
        temp_ga = temp.copy() # 리스트 형태로 계산하기 위해서 copy
        for y in x:
            while y in temp_ga:
                index=temp_ga.index(y)
                result = cal(temp_ga[index-1], temp_ga[index+1], temp_ga[index])
                temp_ga.pop(index)
                temp_ga.pop(index)
                temp_ga.pop(index-1)
                temp_ga.insert(index-1, result)
        if result < 0: # abs 안 쓴 이유 => 테스트 실패뜨는 게 있음
            result *= -1
        if result > max_num:
            max_num = result
    return max_num


# print(solution("100-200*300-500+20"))
# print(solution("50*6-3*2"))
# print(solution("200-300-500-600*40+500+500"))
# print(solution("177-661*999*99-133+221+334+555-166-144-551-166*166-166*166-133*88*55-11*4+55*888*454*12+11-66+444*99"))
# print(solution("2-990-5+2"))