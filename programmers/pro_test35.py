# https://programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    s = s.lower()
    answer = True if s.count('p') == s.count('y') else False
    return answer


print(solution("pPoooyY"))
print(solution("Pyy"))
