# https://programmers.co.kr/learn/courses/30/lessons/86051?language=python3

def solution(numbers):
    temp = [x for x in range(10)]
    answer = sum([x for x in temp if x not in numbers])
    return answer


print(solution([1, 2, 3, 4, 6, 7, 8, 0]))
print(solution([5, 8, 4, 0, 6, 7, 9]))
