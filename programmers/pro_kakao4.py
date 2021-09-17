# 프로그래머스 코딩테스트 연습
# 신규 아이디 추천
# https://programmers.co.kr/learn/courses/30/lessons/72410

import re

def solution(new_id):
    answer = list(new_id)
    # 1단계 - 소문자 대문자로 변경
    for i in range(len(answer)):
        if answer[i].isalpha() and answer[i].isupper():
            answer[i] = answer[i].lower()
    # 2단계 - 소문자, 숫자, (- _ . ) 빼고 제거
    answer = re.sub('[=+,#/\?:^$@*\"※~&%ㆍ!』\\‘|\{\}(\)\[\]\<\>`\'…》]+','',"".join(answer))
    answer = re.sub(r"\s+", "", answer)

    # 3단계 - 마침표가 2번 이상일 경우 하나로 치환
    
    temp = []
    text = ""
    # temp => 문자,숫자, 마침표로 구분하는 리스트 => 마침표가 연속된 경우 하나의 원소로 취급
    for j in range(len(answer)):
        if answer[j]=='.':
            if j == len(answer)-1:
                text+='.'
                temp.append(text)
            else:
                text+='.'
        else:
            temp.append(text)
            temp.append(answer[j])
            text=''

    # temp의 원소중 '.'가 하나라도 포함된 원소를 '.'로 변경 
    for z in range(len(temp)):
        if "." in temp[z]:
            temp[z] = '.'
    # 공백 제거
    while '' in temp:
        temp.remove('')
    answer = "".join(temp)

    # 4단계 - 처음이나 끝에 마침표가 있으면 제거 
    if len(answer)>=2:
        if answer[0]=='.':
            answer = answer[1:]
        if answer[-1]=='.':
            answer = answer[:-1]
    # 크기가 1 이하일 경우
    else:
        # 크기가 1이면 마침표를 제거해서 빈 문자열이 됨
        if len(answer)==1:
            if answer=='.':
                answer=''
    # 5단계 - 빈 문자열이면 a를 대입
    if len(answer) == 0:
        answer = 'a'

    # 6단계 - 16자 이상이면 첫 15개 문자 외에는 제거
    # 제거 후 마지막이 마침표면 제거
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]
    # 7단계 - 길이가 2자 이하면 마지막 문자를 계속 추가 (길이가 3이 될때까지)
    while len(answer)<=2:
        answer = answer+answer[-1]
        
    return answer
print(solution("...!@BaT#*..y.abcdefghijklm"))
#print(solution("z-+.^."))
#print(solution("=.="))
#print(solution("123_.def"))
#rint(solution("abcdefghijklmn.p"))
#print(solution('~!@#$%&*()=+[{]}:?,<>/" === "aaa'))
#print(solution('.1." == "111'))
