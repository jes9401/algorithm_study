N,L = map(int,input().split(" "))


temp=0
x=-1
iter = 0
for i in range(L, 101):
    temp = (i * i - i) / 2
    if (N- temp) % i == 0 and (N - temp) // i >= 0:
        x = (N- temp) // i
        iter = i
        break
if x == -1:
    print(-1)
else:
    for i in range(iter):
        print(int(x + i))
