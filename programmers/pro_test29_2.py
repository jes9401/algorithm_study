# 6주차_복서 정렬하기
# https://programmers.co.kr/learn/courses/30/lessons/85002


def solution(weights, head2head):
    answer = []
    for i in range(len(weights)):
        win = 0
        heavy_win = 0
        game = 0
        weight = weights[i]
        for x in range(len(head2head[i])):
            if head2head[i][x] == "W":
                win+=1
                if weights[x]>weight:
                    heavy_win+=1
            if head2head[i][x] != "N":
                game+=1
        if game == 0:
            answer.append({'win':0, "heavy_win":heavy_win, "weight": weight, "index":i+1})
        else:
            answer.append({'win':win/game, "heavy_win":heavy_win, "weight": weight, "index":i+1})
    answer = sorted(answer, key=lambda k: (k['win'], k['heavy_win'], k['weight']), reverse=True)
    answer = [x['index'] for x in answer]
    return answer

print(solution([50,82,75,120], ["NLWL","WNLL","LWNW","WWLN"]))      # [3, 4, 1, 2]
# print(solution([145,92,86], ["NLW","WNL","LWN"]))                   # [2 3 1]
# print(solution([60,70,60], ["NNN","NNN","NNN"]))                    # [2 1 3]