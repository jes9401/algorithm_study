# 프로그래머스 
# 멀쩡한 사각형  https://programmers.co.kr/learn/courses/30/lessons/62048

def solution(w,h):
    w1=w 
    h1=h
    while h1!=0:
        w1%=h1
        w1,h1 = h1,w1
    return (w*h)-(w+h-w1) # 전체 사각형 크기에서 (w+h-최대공약수)만큼 빼면 됨

print(solution(8,12))

