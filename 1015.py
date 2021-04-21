n= int(input())

A=list(map(int,input().split()))
AA=sorted(A)
p=[]
for i in A:
    p.append(AA.index(i))
    AA[AA.index(i)]= -1

for j in p:
    print(j,end= " ")
