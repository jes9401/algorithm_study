import math

def jes(num):
    if num==1: return False
    n=int(math.sqrt(num))

    for i in range(2,n+1):
        if num%i==0:return False
    return True

while True:
    M,N=list(map(int,input().split(" ")))
    if 1<=M<=N<=1000000:
        break

for i in range(M,N+1):
    if jes(i)==True:print(i)
