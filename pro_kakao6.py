# 프로그래머스
# 2019 KAKAO BLIND RECRUITMENT
# 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889
# 시간초과 해결
def solution(N, stages):
    answer = []
    for i in range(1,N+1):
        total_count = 0
        fail_count = 0
        for j in range(len(stages)):
            if stages[j]>i:
                total_count+=1
            elif stages[j] == i:
                total_count+=1
                fail_count += 1
        if total_count == 0:
            temp = 0
        else:
            temp = fail_count/total_count
        answer.append(temp)
    result = [0 for i in range(len(answer))]
    answer2 = sorted(answer,reverse=True)
    for i in range(len(answer)):
        result[i] = answer.index(answer2[i])+1
        answer[answer.index(answer2[i])]=None

    return result

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4,[4,4,4,4,4]))
print(solution(8,[1,2,3,4,5,6,7]))
