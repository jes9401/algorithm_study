# 최소직사각형
# https://programmers.co.kr/learn/courses/30/lessons/86491
def solution(sizes):
    size_list = [sorted(x, reverse=True) for x in sizes]
    max_one = [x[0] for x in size_list]
    max_two = [x[1] for x in size_list]
    answer = max(max_one) * max(max_two)
    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))   #4000     80  50
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])) #120   8 15
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])) #133    19  7