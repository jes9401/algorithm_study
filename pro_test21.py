# toss 1¹ø
def solution(name_list):
    temp = {}
    num = 65
    for i in range(len(name_list)):

        if name_list[i] not in temp:
            temp[name_list[i]] = 0
            name_list[i] += chr(num)
        else:
            temp[name_list[i]] = temp[name_list[i]] + 1
            name_list[i] += chr(temp[name_list[i]] + num)

    return name_list