import sys
def fibo(n):
    a,b=0,1
    for i in range(n):
        a,b=b%1000000,(b+a)%1000000
    return a

num = int(sys.stdin.readline())
print(fibo(num%(15*(10**5))))
