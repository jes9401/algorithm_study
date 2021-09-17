# 프로그래머스
# [카카오 인턴] 보석 쇼핑
# https://programmers.co.kr/learn/courses/30/lessons/67258
# 시간초과
def solution(gems):
    answer = []
    answer2 = []
    result = []
    gems_set = list(set(gems))
    for i in range(len(gems)):
        temp= gems[i:]
        count = 0
        temp2 = []
        for k in range(len(temp)):
            if temp[k] in gems_set:
                if temp[k] not in temp2:
                    temp2.append(temp[k])
                    count+=1
            if count == len(gems_set):
                break
        answer.append([[i+1,i+k+1],temp2])
    for x in range(len(answer)):
        if len(answer[x][1])!=len(gems_set):
            pass
        else:
            answer2.append(answer[x])
    short = len(gems)+1
    for a in range(len(answer2)):
        if abs(answer2[a][0][0]-answer2[a][0][1])<short:
            short = abs(answer2[a][0][0]-answer2[a][0][1])
            result = answer2[a][0]

    return result

# print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# print(solution(["AA", "AB", "AC", "AA", "AC"]))
# print(solution(["XYZ", "XYZ", "XYZ"]))
# print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))