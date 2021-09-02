# 프로그래머스
# JadenCase 문자열 만들기 https://programmers.co.kr/learn/courses/30/lessons/12951


# def solution(s):
#     word_list = s.split()
#     for i in range(len(word_list)):
#         word_list[i] = word_list[i].lower()
#         if word_list[i][0].isalpha():
#             word_list[i] = list(word_list[i])
#             word_list[i][0] = word_list[i][0].upper()
#             word_list[i] = "".join(word_list[i])
#     answer = " ".join(word_list)
#     return answer



def solution(s):
    word_list = s.split()
    for i in range(len(word_list)):
        word_list[i] = word_list[i].lower()
        word_list[i] = list(word_list[i])
        word_list[i][0] = word_list[i][0].upper()
        word_list[i] = "".join(word_list[i])
    answer = " ".join(word_list)
    return answer

print(solution("33people   unFollowed              me"))
print(solution("for the las t w3eek"))

