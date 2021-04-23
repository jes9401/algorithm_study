N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A2 = sorted(A, reverse=True)
B2 = sorted(B)
sum_num=0
for i in range(len(A2)):
    sum_num+=(A2[i]*B2[i])
print(sum_num)
