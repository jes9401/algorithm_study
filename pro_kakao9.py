# 프로그래머스 카카오 BLIND RECRUITMENT
# 문자열 압축 https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    # 반복문 돌리기 위한 변수
    size = len(s)
    # 문자열 길이 비교를 위한 변수, 최초 값 = 원래 문자열 길이
    result = size

    # 1부터 (문자열 길이-1) 만큼 반복 
    for i in range(1, size):
        temp = []
        answer = ""

        # i개의 문자열씩 끊어서 temp 리스트에 저장
        for j in range(0,size,i):
            temp.append(s[j:j+i])

        # 자릿수 변수
        x = 1
        # 반복 값 변수
        count = 1
        # temp 리스트에 원소가 하나라도 있으면 반복
        while temp:
            # 크기가 1일 경우, 원소를 answer에 추가하고 종료
            if len(temp) < 2:
                answer+=temp[0]
                break
            else:
                # 남은 원소 모두가 같은 문자열일 경우
                if len(temp) == count:
                    # 반복된 횟수+문자열 더해줌
                    answer = answer+str(count)+temp[0]
                    # 더해준 만큼 temp에서 제거
                    for x in range(count):
                        temp.pop()
                    break
                # 맨 처음 원소와 x번째 원소가 같을 경우
                if temp[0] == temp[x]:
                    # 남은 원소가 2개일 경우 
                    if len(temp) == 2:
                        # 2+문자열 추가해주고 count 횟수 만큼 문자열을 temp에서 제거
                        answer = answer+"2"+temp[0]
                        temp.pop(0)
                        temp.pop(0)
                        break
                    # 원소가 3개 이상일 경우 x, count 증가
                    else:
                        x+=1
                        count += 1
                # 맨 처음 원소와 그 다음 원소가 다를 경우
                else:
                    # count가 1이면 중복된 문자열이 없다는 뜻
                    if count == 1:
                        # 첫번째 원소를 answer에 더하고 temp에서 제거
                        answer+=temp[0]
                        temp.pop(0)
                        x = 1
                    # 이전까지 중복된 문자열이 있던 경우
                    else:
                        # 횟수+문자열을 answer에 추가
                        answer = answer+str(count)+temp[0]
                        # 추가한만큼 temp에서 제거
                        for x in range(count):
                            temp.pop(0)
                        count = 1
                        x = 1
        # 위의 while문을 통해 생성된 answer의 길이가 result보다 작으면 값 대입
        if len(answer)<result:
            result = len(answer)
        
    return result

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
print(solution("xxxxxxxxxxyyy"))
