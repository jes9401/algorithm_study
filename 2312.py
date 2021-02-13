T= int(input())

for i in range(T):
    N=int(input())
    for i in range(2, N+1):
        count=0
        if N%i==0:
            while N%i==0:
                N=N//i
                count+=1
            print("%d %d" %(i,count))
        elif N==1:
            break

