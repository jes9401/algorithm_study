# 프로그래머스 카카오 BLIND RECRUITMENT
# 문자열 압축 https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    size = len(s)
    short_size = size+1
    result = size
    for i in range(1, size):
        temp = []
        answer = ""
        for j in range(0,size,i):
            temp.append(s[j:j+i])
        x = 1
        count = 1
        while temp:
            if len(temp) < 2:
                answer+=temp[0]
                break
            else:
                if len(temp) == count:
                    answer = answer+str(count)+temp[0]
                    for x in range(count):
                        temp.pop()
                    count = 1
                    break
                if temp[0] == temp[x]:
                    if len(temp) == 2:
                        answer = answer+"2"+temp[0]
                        temp.pop(0)
                        temp.pop(0)
                        break
                    else:
                        x+=1
                        count += 1
                else:
                    if count == 1:
                        answer+=temp[0]
                        temp.pop(0)
                        x = 1
                    else:
                        answer = answer+str(count)+temp[0]
                        for x in range(count):
                            temp.pop(0)
                        count = 1
                        x = 1
        if len(answer)<result:
            result = len(answer)
        
    return result

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
print(solution("xxxxxxxxxxyyy"))
