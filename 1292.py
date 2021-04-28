A, B = list(map(int, input().split()))
temp = []
num = 1
result = 0
while len(temp)<=B:
    for i in range(num):
        temp.append(num)
    num+=1
for i in range(A-1,B):
    result += temp[i]
print(result)