# 6주차_복서 정렬하기
# https://programmers.co.kr/learn/courses/30/lessons/85002

def get_data(weights, head2head):
    temp = []
    for i in range(len(head2head)):
        win = 0
        heavy_win = 0
        game = 0
        weight = weights[i]
        for j in range(len(head2head[i])):
            if i == j:
                pass
            else:
                if head2head[i][j] != 'N':
                    game += 1
                if head2head[i][j] == "W":
                    win += 1
                    if weight<weights[j]:
                        heavy_win+=1
        if game == 0:
            temp.append({"win":0, "heavy_win":heavy_win, "weight": weight, "index": i+1})
        else:
            temp.append({"win":(win/game)*100, "heavy_win":heavy_win, "weight": weight, "index": i+1})
    return temp

def solution(weights, head2head):
    import copy
    answer = []
    temp = get_data(weights, head2head)
    temp2 = copy.deepcopy(temp)
    temp2 = sorted(temp, key=lambda k: (k['win'], k['heavy_win'], k['weight']), reverse=True)
    for i in temp2:
        answer.append(i['index'])

    return answer

# print(solution([50,82,75,120], ["NLWL","WNLL","LWNW","WWLN"]))      # [3, 4, 1, 2]
# print(solution([145,92,86], ["NLW","WNL","LWN"]))                   # [2 3 1]
print(solution([60,70,60], ["NNN","NNN","NNN"]))                    # [2 1 3]