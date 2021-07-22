# 프로그래머스 
# 직사각형 별찍기 https://programmers.co.kr/learn/courses/30/lessons/12969


n, m = map(int, input().strip().split(' '))
print((("*"*n+"\n")*m).rstrip())
