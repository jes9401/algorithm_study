n = int(input())

result = []
# n개의 나이, 이름 값 추가
for i in range(n):
    temp = input().split()
    temp[0] = int(temp[0])
    result.append(temp)

# 나이를 기준으로 정렬    
result.sort(key = lambda x : x[0])

# 결과 출력
for j in result:
    print(j[0],j[1])
