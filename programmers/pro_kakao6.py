# 프로그래머스
# 2019 KAKAO BLIND RECRUITMENT
# 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889
# 시간초과 해결
def solution(N, stages):
    answer = []
    for i in range(1,N+1):
        # total_count = 스테이지에 도달한 플레이어 수
        total_count = 0
        # fail_count = 도달했지만 클리어 못한 플레이어 수
        fail_count = 0
        for j in range(len(stages)):
            # i가 1부터 N+1 스테이지까지 있을 때
            # 스테이지에 도달한 플레이어 수 = i보다 크거나 같을 경우
            # 도달했지만 클리어 못한 플레이어 수 = i와 같을 경우
            if stages[j]>i:
                total_count+=1
            elif stages[j] == i:
                total_count+=1
                fail_count += 1
        # 도달한 유저 없는 경우 실패율은 0으로 정의
        if total_count == 0:
            temp = 0
        else:
            temp = fail_count/total_count
        answer.append(temp)
    # 결과 반환 위한 리스트
    result = [0 for i in range(len(answer))]
    # answer를 역순 정렬
    answer2 = sorted(answer,reverse=True)
    print(answer,answer2)
    # 실패율이 높은 순으로 결과 반환
    for i in range(len(answer)):
        # answer2는 실패율이 높은 순으로 정렬되어 있기 때문에
        # answer2의 i번째 원소를 answer에서 찾은 뒤 +1 반환
        # => 0등이 아니라 1등 부터 시작
        result[i] = answer.index(answer2[i])+1
        # 중복을 처리하기 위해서 사용한 원소는 None으로 변경
        answer[answer.index(answer2[i])]=None

    return result

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4,[4,4,4,4,4]))
print(solution(8,[1,2,3,4,5,6,7]))
