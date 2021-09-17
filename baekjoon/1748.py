import sys

n = int(sys.stdin.readline())
result=0
temp = [int("9"+"0"*i) for i in range(0,len(str(n)))]
for i,s in enumerate(temp):
    if s==temp[-1]:
        result+=len(str(n))*(n-sum(temp[:-1]))
    else:
        i+=1
        result+=i*s
print(result)