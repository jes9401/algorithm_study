# 프로그래머스 
# 조이스틱 https://programmers.co.kr/learn/courses/30/lessons/42860?language=python3
# 미해결



def solution(name):
    answer= 0
    temp = [ord(x) for x in name]
    move = [min([ord(y)-65, 90-ord(y)+1]) for y in name]
    num = 0 
    
    while True:
        answer += move[num]
        move[num] = 0
        if sum(move) == 0:
            return answer

        left, right = 1, 1
        
        while move[num - left] == 0:
            left += 1
        while move[num + right] == 0:
            right += 1
            
        if left<right:
            answer+=left
            num-=left
        else:
            answer+=right
            num+=right
    
# A => 65
# Z => 90
# 조작 횟수의 최소값 return
# name은 알파벳 대문자만
# 위 - 다음 알파벳
# 아래 - 이전 알파벳(A에서 아래쪽으로 이동하면 Z)
# 왼쪽 - 커서 왼쪽 이동
# 오른 - 커서 오른쪽 이동



print(solution("JEROEN"))
print(solution("JAN"))
