import sys

n = int(sys.stdin.readline())
temp = []
temp2 = []
result= [0 for i in range(n)]
for _ in range(n):
    kg, cm = list(map(int,sys.stdin.readline().rstrip().split()))
    temp.append([kg,cm])

temp2 = sorted(temp)
for i in range(len(temp2)):
    count = 0
    for j in range(i+1,len(temp2)):
        if temp2[i][0]<temp2[j][0] and temp2[i][1]<temp2[j][1]:
            count+=1
    result[temp.index(temp2[i])] = count+1

for j in range(len(result)):
    if j == len(result)-1:
        print(result[j])
    else:
        print(result[j],end = " ")

# 갈을 경우 예외처리 추가해야
