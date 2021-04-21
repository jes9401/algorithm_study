import sys
def fibo(n):
    a,b=1,1
    if n==1 or n==2:
        return 1
    for i in range(1,n):
        a,b=b,b+a
    return a

print(fibo(int(sys.stdin.readline())))