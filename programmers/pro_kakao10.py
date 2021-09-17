# 프로그래머스 
# 2019카카오 튜플   https://programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    import re
    answer = []
    # 제일 처음과 마지막의 { } 제거
    s=s[1:-1]
    # {} 쌍으로 구분해서 리스트에 저장
    temp = re.findall('\{[^}]+}', s)
    
    # 반복문 돌면서 각 원소의 { }를 제거하고
    # 각 원소를 , 단위로 잘라서 리스트화 한 뒤 int형으로 변경
    for i in range(len(temp)):
        temp[i] = temp[i].replace('{','').replace('}','')
        temp[i] = temp[i].split(',')
        temp[i] = list(map(int,temp[i]))
    # 원소의 크기순으로 정렬
    temp = sorted(temp,key=len)
    
    for i in range(len(temp)):
        # 제일 처음일 경우 바로 answer에 추가
        if i == 0:
            answer.append(temp[i][0])
        # 아닐 경우 temp[i] 리스트를 temp2라는 변수에 복사한 뒤
        # answer에 있는 값을 모두 remove 함수를 이용해 제거
        # 제일 마지막에 남은 값을 answer에 추가
        else:
            temp2 = temp[i].copy()
            for i in answer:
                temp2.remove(i)
            answer.append(temp2[0])
    return answer

print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
