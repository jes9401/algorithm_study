def solution(code, day, data):
    answer = []
    result = []
    data_list = []
    for i in data:
        data_list.append(i.split(" "))
    for j in data_list:
        if j[1][-6:] ==code and j[2][5:13] == day:
            answer.append([int(j[2].split("=")[1]),j[0].split("=")[1],])
    answer.sort()
    for k in answer:
        result.append(int(k[1]))
    return result

print(solution("012345","20190620",["price=80 code=987654 time=2019062113","price=90 code=012345 time=2019062014","price=120 code=987654 time=2019062010","price=110 code=012345 time=2019062009","price=95 code=012345 time=2019062111"]))
