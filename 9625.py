import sys

n = int(sys.stdin.readline())

A=[]
B=[]
for i in range(n+1):
    if i==0:
        A.append(1)
        B.append(0)
    elif i==1:
        A.append(0)
        B.append(1)
    else:
        A.append(A[i-1]+A[i-2])
        B.append(B[i-1]+B[i-2])
print(A[n],B[n])