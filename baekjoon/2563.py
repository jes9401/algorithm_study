n = int(input())
temp = []
result = []
for i in range(n):
    temp.append(list(map(int,input().split())))
for j in temp:
    num1 = j.copy()
    for x in range(num1[0],num1[0]+10):
        for y in range(num1[1],num1[1]+10):
            n = [x,y]
            if n not in result:
                result.append(n)
print(len(result))
