# 프로그래머스 카카오 블라인드
# 비밀지도 https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        temp=""
        # bin 함수를 통해 i번째 원소를 이진수로 변환
        # zfill 함수를 통해 n만큼 자릿수를 맞춰줌(왼쪽에 0 추가)
        num1 = bin(arr1[i])[2:].zfill(n)
        num2 = bin(arr2[i])[2:].zfill(n)
        
        for j in range(len(num1)):
            # 둘 다 0일 경우 공백 추가
            if num1[j] == "0" and num2[j]=="0":
                temp+=" "
            # 하나라도 1일 경우 # 추가
            elif num1[j]=="1" or num2[j]=="1":
                temp+="#"
        answer.append(temp)
    return answer

print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))
print(solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))
