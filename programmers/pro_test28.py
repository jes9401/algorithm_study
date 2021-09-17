# 프로그래머스
# JadenCase 문자열 만들기 https://programmers.co.kr/learn/courses/30/lessons/12951


def up(s):
    return s.upper()
def solution(s):
    # 우선 전체적으로 소문자로 변경 
    s = s.lower()
    s = list(s)
    # 맨 처음 글자는 무조건 대문자로 변경
    s[0] = up(s[0])
    for i in range(len(s)):
        # 공백이 아니고 이전의 문자열이 공백이면 단어의 첫 글자로 인식
        if s[i] != " ":
            if i != 0 and s[i-1] == " ":
                s[i] = up(s[i])
    return "".join(s)



print(solution("33people   unFollowmeed              me"))
print(solution(" for the las t w3eek"))

