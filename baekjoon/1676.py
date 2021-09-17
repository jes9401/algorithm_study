def fac(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return n*fac(n-1)

n=str(fac(int(input())))[::-1]
count=0
i=0
while True:
    if int(n[i])!=0:
        break
    count+=1
    i+=1    
print(count)

