# 프로그래머스 카카오
# 오픈채팅방 https://programmers.co.kr/learn/courses/30/lessons/42888
# 해결 완료

def solution(record):
    answer = []
    dic = {}
    for i in record:
        # 명령어, 아이디, 이름으로 구분해서 저장
        temp = i.split()
        # 문자열에 공백 넣은 이유 => 밑에서 split으로 구분할거라서
        if temp[0] == "Enter":
            answer.append("%s 님이 들어왔습니다." %(temp[1]))
            dic[temp[1]] = temp[2]
        elif temp[0] == "Leave":
            answer.append("%s 님이 나갔습니다." %(temp[1]))
        elif temp[0] == "Change":
            dic[temp[1]] = temp[2]
    for j in range(len(answer)):
        s0 = answer[j].split()[0] # 아이디
        # '아이디 ' 인 형식 변경 => dic[아이디] == (이름) 
        answer[j] = answer[j].replace(s0+' ',dic[s0])
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234",
                "Enter uid1234 Prodo","Change uid4567 Ryan"]))
