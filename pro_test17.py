# 프로그래머스 
# 조이스틱 https://programmers.co.kr/learn/courses/30/lessons/42860?language=python3
# 해결



def solution(name):
    answer = 0
    print(name)
    temp = [ord(x) for x in name]
    move = [min([ord(y)-65, 90-ord(y)+1]) for y in name]
    return move
# sum(move)+len(name)-1
# A => 65
# Z => 90
# 조작 횟수의 최소값 return
# name은 알파벳 대문자만
# 1~20
# 위 - 다음 알파벳
# 아래 - 이전 알파벳(A에서 아래쪽으로 이동하면 Z)
# 왼쪽 - 커서 왼쪽 이동
# 오른 - 커서 오른쪽 이동
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

# 왼쪽 오른쪽 어느쪽으로 가는게 좋을지 판별해야될듯?

print(solution("JEROEN"))
print(solution("JAN"))
