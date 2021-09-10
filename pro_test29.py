def solution(s):
    import re
    answer = True
    temp = re.findall('\(([^)]+)',  s)
    print(temp)

    return answer


# print(solution("()()"))   
# print(solution("(())()"))   
# print(solution(")()("))   
# print(solution("(()("))        