# 프로그래머스 Dev-Matching(백엔드)
# 로또의 최고 순위와 최저 순위
# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    dic = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    zero_count = lottos.count(0)
    count = 0
    for i in range(len(lottos)):
        for j in range(len(lottos)):
            if (lottos[i] == win_nums[j]) and lottos[i]!=0:
                count+=1
    min_grade = dic[count]
    max_grade = dic[count+zero_count]
    result = [max_grade,min_grade]
    return result