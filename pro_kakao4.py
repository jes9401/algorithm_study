# 프로그래머스 코딩테스트 연습
# 신규 아이디 추천
# https://programmers.co.kr/learn/courses/30/lessons/72410

import re

def solution(new_id):
    answer = list(new_id)
    for i in range(len(answer)):
        if answer[i].isalpha() and answer[i].isupper():
            answer[i] = answer[i].lower()
    
    answer = re.sub('[=+,#/\?:^$@*\"※~&%ㆍ!』\\‘|\{\}(\)\[\]\<\>`\'…》]+','',"".join(answer))
    answer = re.sub(r"\s+", "", answer)
    temp = []
    text = ""
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
    for z in range(len(temp)):
        if "." in temp[z]:
            temp[z] = '.'
    while '' in temp:
        temp.remove('')
   # temp = sorted(temp,key=len)
    answer = "".join(temp)
    if len(answer)>=2:
        if answer[0]=='.':
            answer = answer[1:]
        if answer[-1]=='.':
            answer = answer[:-1]
    else:
        if len(answer)==1:
            if answer=='.':
                answer=''
    if len(answer) == 0:
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]
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
