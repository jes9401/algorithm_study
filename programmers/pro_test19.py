# 프로그래머스 
# 상호 평가 https://programmers.co.kr/learn/courses/30/lessons/83201

def solution(scores):
    answer = ''
    new_list = list(map(list, zip(*scores)))
    for i in range(len(new_list)):
        s = 0
        if new_list[i][i] == max(new_list[i]) and new_list[i].count(max(new_list[i]))==1:
            s = (sum(new_list[i]) - new_list[i][i]) / (len(new_list[i])-1)
        elif new_list[i][i] == min(new_list[i]) and new_list[i].count(min(new_list[i]))==1:
            s = (sum(new_list[i]) - new_list[i][i]) / (len(new_list[i])-1)
        else:
            s = sum(new_list[i])/len(new_list[i])
        
        if s >=90:
            answer+="A"
        elif s>=80:
            answer+="B"
        elif s>=70:
            answer+="C"
        elif s>=50:
            answer+="D"
        else:
            answer+="F"
    return answer
