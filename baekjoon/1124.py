import sys
from math import sqrt
a,b=map(int,sys.stdin.readline().rstrip().split())
answer = 0

def factorization(x):
    d = 2 
    count = 0
    while d <= x: 
        if x % d == 0: 
            count += 1 
            x = x / d 
        else:
            d = d + 1
    return count

def prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
        

    for i in range(3, int(sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True

for x in range(a,b+1):
    if prime(factorization(x)):
        answer +=1

dp = [0 for _ in range(100001)]
print(len(dp))
    
