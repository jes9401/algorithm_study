# 프로그래머스 
# 순위 검색 https://programmers.co.kr/learn/courses/30/lessons/72412
# 효율성 미통과

def solution1(info, query):
    answer = []
    info = list(map(lambda x: x.split(" "), info))
    query = list(map(lambda x: x.replace("and", " "), query))
    query = list(map(lambda x: ' '.join(x.split()), query))
    query = list(map(lambda x: x.split(" "), query))
    for x in range(len(query)):
        count = 0
        for y in range(len(info)):
            if (info[y][0] == query[x][0] or query[x][0] == "-") and (info[y][1] == query[x][1] or query[x][1] == "-") and (info[y][2] == query[x][2] or query[x][2] == "-") and (info[y][3] == query[x][3] or query[x][3] == "-") and (int(info[y][4]) >= int(query[x][4])):
                count+=1
        answer.append(count)
    return answer

def solution2(info, query):
    answer = []
    info_list = []
    for i in info:
        temp = i.split(" ")
        score = ","+temp[-1]
        m = ["".join(temp[:-1])+score, "----"+score]
        for j in range(4):
            temp2 = temp.copy()
            temp2[j] = "-"
            m.append("".join(temp2[:-1])+score)
            for k in range(j+1, 4):
                k_word = "".join(temp2[:-1]).replace(temp2[k], "-")
                m.append(k_word+score)
                for x in range(k+1, 4):
                    x_word = "".join(temp2[:-1]).replace(temp2[x], "-")
                    m.append(x_word+score)
                    m.append(k_word.replace(temp2[x],"-")+score)
        info_list.extend(list(set(m)))
    info_list.sort()
    query = list(map(lambda x: x.replace("and", ""), query))
    query = list(map(lambda x: ' '.join(x.split()).split(" "), query))
    query = list(map(lambda x: ["".join(x[:-1]),x[-1]], query))
  
    for i in range(len(query)):
        a = list(filter(lambda x: query[i][0] in x and int(query[i][1])<=int(x.split(",")[1]), info_list))
        answer.append(len(a))
    return answer


def solution(info, query):
    answer = []
    info_list = []
    for i in range(len(info)):
        score = ","+info[i].split()[-1]
        temp = info[i].split()[:-1]
        temp1 = [temp[0], "-"]
        temp2 = [temp[1], "-"]
        temp3 = [temp[2], "-"]
        temp4 = [temp[3], "-"]
        info_list.extend([a+b+c+d+score for a in temp1 for b in temp2 for c in temp3 for d in temp4])
    query = map(lambda x: x.replace("and", ""), query)
    query = list(map(lambda x: ["".join(x.split(" ")[:-1]),x.split(" ")[-1]], query))

    for i in range(len(query)):
        a = list(filter(lambda x: query[i][0] in x and int(query[i][1])<=int(x.split(",")[1]), info_list))
        answer.append(len(a))
    return answer

# [1,1,1,1,2,4]
print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
, ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))

