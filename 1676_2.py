def fac(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n*fac(n-1)

n=int(input())
num=fac(n)
check=1
count=0
while check:
    if num%10==0:
        count+=1
        num//=10
    else:
        check=0
print(count)
