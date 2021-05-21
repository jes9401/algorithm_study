# 프로그래머스 2016
# https://programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    from datetime import datetime, timedelta
    answer = {1:"SAT",2:"SUN",3:"MON",4:"TUE",5:"WED",6:"THU",0:"FRI"}
    time1 = datetime(2016,1,1)
    time2 = datetime(2016,a,b)
    day = (time2-time1).days
    
    return answer[day%7]


print(solution(5,24))
print(solution(1,8))

