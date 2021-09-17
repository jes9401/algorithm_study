import math

result=[]
def jes(num):
    if num==1:return False
    n=int(math.sqrt(num))

    for i in range(2,n+1):
        if num%i==0:return False
    return True

while True:
    M=int(input())
    N=int(input())
    if M<=N and M<=10000 and N<=10000:
        break
for i in range(M,N+1):
    if jes(i)==True:result.append(i)

if len(result)>=1:
    print(sum(result))
    print(min(result))
else:
    print("-1")
