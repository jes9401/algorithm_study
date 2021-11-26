# https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    user_num = 1
    turn = 1
    used_words = [words[0]]
    last_alphabet = words[0][-1]
    for i in range(len(words)):
        if i != 0:
            first_alphabet = words[i][0]
            if last_alphabet != first_alphabet:
                return [user_num, turn]
            if words[i] not in used_words:
                used_words.append(words[i])
                last_alphabet = words[i][-1]
            else:
                return [user_num, turn]
        if n == user_num:
            user_num = 1
            turn += 1
        else:
            user_num += 1
    return [0, 0]

# 3,3 [번호, 차례]
print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
# 0,0
# print(solution(5,
#                ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang",
#                 "gather",
#                 "refer", "reference", "estimate", "executive"]))
# 1,3
# print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
