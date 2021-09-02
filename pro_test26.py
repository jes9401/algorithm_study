# 프로그래머스 
# 순위 검색 https://programmers.co.kr/learn/courses/30/lessons/72412
# 효율성 미통과

def solution(info, query):
    answer = []
    info = list(map(lambda x: x.split(" "), info))
    query = list(map(lambda x: x.replace("and", " "), query))
    query = list(map(lambda x: ' '.join(x.split()), query))
    query = list(map(lambda x: x.split(" "), query))
    
    for x in range(len(query)):
        count = 0
        for y in range(len(info)):
            if info[y][0] != query[x][0] and query[x][0] != "-":
                continue
            else:
                if info[y][1] != query[x][1] and query[x][1] != "-":
                    continue
                else:
                    if info[y][2] != query[x][2] and query[x][2] != "-":
                        continue
                    else:
                        if info[y][3] != query[x][3] and query[x][3] != "-":
                            continue
                        else:
                            if int(info[y][4]) >= int(query[x][4]):
                                count+=1
        answer.append(count)
    return answer
# [1,1,1,1,2,4]
print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
, ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))

