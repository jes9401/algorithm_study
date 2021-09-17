# 프로그래머스 
# 소수 찾기 https://programmers.co.kr/learn/courses/30/lessons/42839


# 리스트의 원소 중 소수를 카운트하는 함수
def prime(lst):
    count = 0
    for i in lst:
        if i<=1:
            continue
        elif i==2 or i==3:
            count+=1
        else:
            isPrime = 0
            for j in range(2,i):
                if i%j==0:
                    isPrime = 0
                    break
                else:
                    isPrime = 1
            if isPrime:
                count+=1
    return count

def solution(numbers):
    # 리스트의 모든 조합을 구하기 위한 라이브러리
    from itertools import chain,combinations,permutations
    answer = []
    numbers=list(numbers)
    total_num = []
    
    # 입력받은 문자열의 크기와 같은 크기의 모든 경우의 수 반환
    # ex) "17" 입력 받았을 경우 2자리 수 반환 17,71
    numbers2 = list(permutations(numbers,len(numbers)))
    
    for x in range(len(numbers2)):
        # 1~문자열크기 만큼의 모든 경우의 수를 temp 리스트에 저장
        temp = sum([list(map(list, combinations(numbers2[x], i))) for i in range(len(numbers2[x]) + 1)], [])
        # total_num 리스트에 temp 리스트 추가
        total_num.extend(temp)

    # 0과 중복을 제거하기 위한 반복문
    for i in range(len(total_num)):
        if len(total_num[i]) == 0:
            continue
        else:
            n= int("".join(total_num[i]))
            if (n not in answer):
                answer.append(n)
    result = prime(answer)
    return result

print(solution("17"))
print(solution("011"))
print(solution("7843"))
