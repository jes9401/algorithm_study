import sys
a,b=map(int,sys.stdin.readline().rstrip().split())


result=0
for i in range(a,b+1):
    N=i
    num=2
    temp=0
    while num<=N:
        if N%num==0:
            temp+=1
            N//=num
        else:
            num+=1
    count=0
    for j in range(2,temp):
        if temp%j==0:
            count=1
    if count!=1:
        result+=1
print(result)
