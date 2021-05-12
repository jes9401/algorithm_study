# 프로그래머스, 2019 카카오, 크레인 인형뽑기
# https://programmers.co.kr/learn/courses/30/lessons/64061
# 처음에 문제를 board[i] 원소가 세로로 한 줄이라고 이해함
# 그래서 통과 못하다가 8~10 라인 추가해서 원하는 형식의 리스트로 바꾸고 해결
# 쓸데 없이 어렵게 생각해서 코드가 길어짐 => 시간 나면 다시 풀기
def solution(board, moves):
    temp = []
    answer = 0
    
    # 이중 리스트의 행렬 변환
    board = list(map(list, zip(*board)))
    # 각 원소를 뒤집기
    for aa in range(len(board)):
        board[aa] = board[aa][::-1]

    # 맨 위에 있는 값이 0(빈 칸)일 경우 제거
    for x in board:
        isZero = 0
        for y in range(len(x) - 1, -1, -1):
            if x[y] == 0:
                x.pop(y)
            else:
                isZero = 1
            if isZero:
                break
    # moves 배열 원소를 이용해서 인형 뽑기 진행
    for i in range(len(moves)):
        # 각 세로 줄에 인형이 1개라도 있을 경우
        if board[moves[i]-1]:
            # 맨 위에 있는 인형을 temp 리스트에 추가
            temp.append(board[moves[i]-1][-1])
            # 추가한 값을 board에서는 제거
            board[moves[i]-1].pop(-1)
        # temp 안에 인형이 2개 이상 있을 경우에만 반복
        while len(temp)>1:
            # 위의 동작을 수행하고 난 후 맨 위가 빈 칸(0)인 경우 제거
            for x in board:
                isZero = 0
                for y in range(len(x) - 1, -1, -1):
                    if x[y] == 0:
                        x.pop(y)
                    else:
                        isZero = 1
                    if isZero:
                        break
            # 제일 마지막에 추가된 값과 그 전 값이 같을 경우
            if temp[-1] == temp[-2]:
                # temp 리스트에서 둘 다 제거하고 answer 값 +1
                temp.pop(-1)
                temp.pop(-1)
                answer+=1
            # 인형을 제거하고 난 뒤 인형이 1개 이하일 경우 반복 종료
            if len(temp)<2:
                break
            # 제거하고 난 뒤 맨 위 인형과 그 밑 인형이 다를 경우도 종료
            elif temp[-1] != temp[-2]:
                break
    # 한 번 수행될 때 인형이 2개씩 사라지기 때문에 answer*2 반환
    return answer*2 

# print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))

