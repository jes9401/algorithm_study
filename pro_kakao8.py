# 프로그래머스 카카오
# 오픈채팅방 https://programmers.co.kr/learn/courses/30/lessons/42888
# 미해결

def solution(record):
    answer = []
    dic = {}
    for i in record:
        temp = i.split()
        if temp[0] == "Enter":
            answer.append("%s %s 님이 들어왔습니다." %(temp[1],temp[2]))
            dic[temp[1]] = temp[2]
        elif temp[0] == "Leave":
            answer.append("%s %s 님이 나갔습니다." %(temp[1],dic[temp[1]]))
        elif temp[0] == "Change":
            dic[temp[1]] = temp[2]
    answer2 = answer.copy()
    for j in range(len(answer)):
        s0 = answer[j].split()[0] # 아이디
        s1 = answer[j].split()[1] # 이름
        if  s1 == dic[s0]:
            answer[j] = answer[j].replace(s0,"")
            answer[j] = answer[j].lstrip()
            answer[j] = answer[j].replace(answer[j][len(s1)],'')
        else:
            answer[j] = answer[j].replace(s0,"")
            answer[j] = answer[j].lstrip()
            answer[j] = answer[j].replace(s1, dic[s0])
            answer[j] = answer[j].replace(answer[j][len(dic[s0])],'')
        if "님이 " not in answer[j]:
            answer[j] = answer[j].replace("님이","님이 ")
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
