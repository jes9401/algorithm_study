N=int(input())
i=2
temp=[]
count=None
if N!=1:
    while i<=N:
        if N%i==0:
            temp.append(i)
            N//=i
        else:
            i+=1
for j in temp:
    print(j,end=" ")
