while True:
    T=int(input())
    if T<=100:
        break

for i in range(1,T+1):
    A,B= map(int,input().split(" "))
    print("Case #%s: %s" %(i,A+B))
