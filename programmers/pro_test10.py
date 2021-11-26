# 프로그래머스 
# 가장 큰 수 https://programmers.co.kr/learn/courses/30/lessons/42746
# 시간초과, 해결방법 모르겠음..

def solution(numbers):
    # 리스트의 모든 조합을 구하기 위한 라이브러리
    from itertools import permutations
    numbers = list(permutations(numbers, len(numbers)))
    #  for i in range(len(numbers)):
    #      numbers[i] = "".join(map(str,numbers[i]))
    answer = '0'
    for i in numbers:
        if answer < "".join(map(str, i)):
            answer = "".join(map(str, i))
    return answer if int(answer) != 0 else "0"

print(solution([6, 10, 2]))
print(solution([3, 303, 34, 5, 9]))
print(solution([0, 5, 10, 15, 20]))
print(solution([1000, 0, 5, 99, 100]))
print(solution([0, 0, 0, 0, 0]))
