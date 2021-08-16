# 프로그래머스 
# 숫자 문자열과 영단어 https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    dic = {"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
    answer = ""
    str_list = list(dic.keys())
    temp = ""
    for i in s:
        if i.isalpha():
            temp+=i
            if temp in str_list:
                answer+=dic[temp]
                temp=""
        else:
            answer+=str(i)
    return int(answer)