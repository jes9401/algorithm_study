n= int(input())

for i in range(n):
    temp = list(map(int,input().split()))
    temp = list(set(temp))
    temp.sort()
    print(temp[-3])