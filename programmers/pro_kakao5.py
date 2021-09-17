# 프로그래머스 2020카카오 인턴십
# 키패드 누르기
# https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    numbers = list(map(str,numbers))
    # 가운데 있는 버튼(2,5,8,0) 별로 다른 버튼과의 거리를 딕셔너리에 저장
    dic ={"2":{"1":1,"3":1,"4":2,"6":2,"7":3,"9":3,"*":4,"#":4,"2":0,"5":1,"8":2,"0":3},
          "5":{"1":2,"3":2,"4":1,"6":1,"7":2,"9":2,"*":3,"#":3,"2":1,"5":0,"8":1,"0":2},
          "8":{"1":3,"3":3,"4":2,"6":2,"7":1,"9":1,"*":2,"#":2,"2":2,"5":1,"8":0,"0":1},
          "0":{"1":4,"3":4,"4":3,"6":3,"7":2,"9":2,"*":1,"#":1,"2":3,"5":2,"8":1,"0":0}}
    # 왼손으로만 누를 수 있는 번호 리스트
    left_list=["1","4","7","*"]
    # 오른손으로만 누를 수 있는 번호 리스트
    right_list=["3","6","9","#"]
    answer = ''
    # 왼손의 위치(최초 위치는 *)
    l_h = "*"
    # 오른손의 위치(최초 위치는 #)
    r_h = "#"
    for i in range(len(numbers)):
        # 눌러야 할 번호가 왼손 리스트에 있을 경우
        if numbers[i] in left_list:
            answer+="L"
            l_h = numbers[i]
        # 오른손 리스트에 있을 경우
        elif numbers[i] in right_list:
            answer+="R"
            r_h = numbers[i]
        else:
            # 누를 번호와 왼손 사이의 거리 < 번호와 오른손 사이의 거리
            # => 왼손이 더 가까울 경우
            if dic[numbers[i]][l_h]<dic[numbers[i]][r_h]:
                answer+="L"
                l_h = numbers[i]
            # 오른손이 더 가까울 경우
            elif dic[numbers[i]][l_h]>dic[numbers[i]][r_h]:
                answer+="R"
                r_h = numbers[i]
            # 거리가 같을 경우 주로 사용하는 손 사용
            else:
                if hand == "right":
                    answer+="R"
                    r_h = numbers[i]
                else:
                    answer+="L"
                    l_h = numbers[i]
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],"right"))